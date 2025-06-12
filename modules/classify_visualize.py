import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly.io as pio
import os

def classify_visualize(df_sample, df_user):
    st.header("🪐 Fitur Visualisasi Hasil Klasifikasi")
    # Buat salinan aman dari df_sample dan df_user
    df_sample_safe = df_sample.copy()
    df_user_safe = df_user.copy()
    # Konversi kolom class ke string
    df_sample_safe['class'] = df_sample_safe['class'].astype(str)
    df_user_safe['class'] = df_user_safe['class'].astype(str)

    # Gabungkan data
    df = pd.concat([df_sample_safe, df_user_safe], ignore_index=True).drop_duplicates()

    if df.empty:
        st.error("❌ Data kosong atau gagal dimuat.")
        return

    required_cols = ['alpha', 'delta', 'redshift', 'class']
    if not all(col in df.columns for col in required_cols):
        st.error("❌ Kolom wajib tidak lengkap: alpha, delta, redshift, class")
        return

    unique_labels = df['class'].unique().tolist()
    selected_labels = st.multiselect("🎯 Filter kelas objek", unique_labels, default=unique_labels)

    if not selected_labels:
        st.warning("⚠️ Pilih minimal satu kelas objek.")
        return

    filtered_df = df[df['class'].isin(selected_labels)]

    if 'center_point_data' not in st.session_state:
        if df_user_safe.empty:
            st.error("❌ Data user kosong.")
            return

        # Ambil satu baris sample dari df_user_safe secara aman
        selected_center = df_user_safe[required_cols].sample(n=1).iloc[0]

        match = df[
            (df['alpha'] == selected_center['alpha']) &
            (df['delta'] == selected_center['delta']) &
            (df['redshift'] == selected_center['redshift'])
        ]

        if match.empty:
            st.error("❌ Gagal menemukan titik pusat di data gabungan.")
            return

        st.session_state.center_point_data = match.iloc[0].to_dict()

    center_point = st.session_state.center_point_data

    with st.expander("🎯 Titik pusat visualisasi:", expanded=True):
        st.write({
            'alpha': center_point['alpha'],
            'delta': center_point['delta'],
            'redshift': center_point['redshift'],
            'class': center_point['class']
        })

    distance = np.sqrt(
        (filtered_df['alpha'] - center_point['alpha'])**2 +
        (filtered_df['delta'] - center_point['delta'])**2
    )
    max_possible_distance = float(np.ceil(distance.max() * 10) / 10)
    max_distance = st.slider(
        "📏 Batas jarak angular (α & δ)",
        min_value=0.0,
        max_value=max_possible_distance,
        value=min(1.0, max_possible_distance),
        step=0.1
    )

    plot_df = filtered_df[distance <= max_distance].copy()

    if plot_df.empty:
        st.warning("⚠️ Tidak ada objek dalam jarak yang dipilih.")
        return

    plot_df['highlight'] = (
        (plot_df['alpha'] == center_point['alpha']) &
        (plot_df['delta'] == center_point['delta']) &
        (plot_df['redshift'] == center_point['redshift']) &
        (plot_df['class'] == center_point['class'])
    )
    highlight_point = plot_df[plot_df['highlight']].copy()
    main_points = plot_df[~plot_df['highlight']].copy()

    class_map = {'GALAXY': 0, 'QSO': 1, 'STAR': 2}
    main_points['class_code'] = main_points['class'].apply(lambda x: class_map.get(x, x)).astype(int)
    highlight_point['class_code'] = highlight_point['class'].apply(lambda x: class_map.get(x, x)).astype(int)

    # Ambil hanya titik dari user (selain titik pusat) yang juga ada di plot_df
    user_other_points = df_user_safe[
        ~(
            (df_user_safe['alpha'] == center_point['alpha']) &
            (df_user_safe['delta'] == center_point['delta']) &
            (df_user_safe['redshift'] == center_point['redshift']) &
            (df_user_safe['class'] == center_point['class'])
        )
    ]

    # Hanya ambil yang ada di plot_df (dengan merge antar DataFrame)
    user_other_points = pd.merge(
        user_other_points,
        plot_df,
        on=['alpha', 'delta', 'redshift', 'class'],
        how='inner'
    )

    user_other_points['class_code'] = user_other_points['class'].apply(lambda x: class_map.get(x, x)).astype(int)

    st.markdown("### 🌌 3D Scatter Plot: Distribusi Objek Astronomi")
    st.caption(f"Menampilkan objek dalam jarak ≤ {max_distance}° dari titik pusat.")

    scatter_main = go.Scatter3d(
        x=main_points['alpha'],
        y=main_points['delta'],
        z=main_points['redshift'],
        mode='markers',
        marker=dict(
            size=5,
            opacity=0.8,
            color=main_points['class_code'],
            colorscale='Viridis',
            colorbar=dict(title='Kelas', tickvals=[0, 1, 2], ticktext=['GALAXY', 'QSO', 'STAR'])
        ),
        text=main_points.apply(
            lambda row: f"Class: {row['class']}<br>Redshift: {row['redshift']:.3f}<br>α: {row['alpha']:.3f}°<br>δ: {row['delta']:.3f}°",
            axis=1
        ),
        hoverinfo='text',
        name='Objek'
    )

    scatter_user = go.Scatter3d(
        x=user_other_points['alpha'],
        y=user_other_points['delta'],
        z=user_other_points['redshift'],
        mode='markers',
        marker=dict(
            size=7,
            color='cyan',
            line=dict(color='blue', width=1.5)
        ),
        text=user_other_points.apply(
            lambda row: f"User Point<br>Class: {row['class']}<br>Redshift: {row['redshift']:.3f}<br>α: {row['alpha']:.3f}°<br>δ: {row['delta']:.3f}°",
            axis=1
        ),
        hoverinfo='text',
        name='Titik dari User'
    )

    scatter_center = go.Scatter3d(
        x=highlight_point['alpha'],
        y=highlight_point['delta'],
        z=highlight_point['redshift'],
        mode='markers',
        marker=dict(size=8, color='red', line=dict(color='white', width=2)),
        text=highlight_point.apply(
            lambda row: f"Class: {row['class']}<br>Redshift: {row['redshift']:.3f}<br>α: {row['alpha']:.3f}°<br>δ: {row['delta']:.3f}°<br><b>(Titik Pusat)</b>",
            axis=1
        ),
        hoverinfo='text',
        name='Titik Pusat'
    )

    fig_3d = go.Figure(data=[scatter_main, scatter_user, scatter_center])
    fig_3d.update_layout(
        title='Distribusi 3D Objek Astronomi (α, δ, redshift)',
        scene=dict(
            xaxis_title='Right Ascension (α)',
            yaxis_title='Declination (δ)',
            zaxis_title='Redshift'
        ),
        legend=dict(x=0.01, y=0.99),
        margin=dict(l=0, r=0, b=0, t=40)
    )
    st.plotly_chart(fig_3d, use_container_width=True)

    if st.button("🔄 Pilih Ulang Titik Pusat"):
        st.session_state.pop('center_point_data', None)
        st.rerun()

    # ===============================
    # 🔹 Histogram Interaktif (2D)
    # ===============================
    st.markdown("### 📊 Histogram Berdasarkan Alpha atau Delta")
    selected_coord = st.selectbox("Pilih koordinat untuk histogram:", ['alpha', 'delta'])

    color_sequence = px.colors.qualitative.Plotly  # atau px.colors.qualitative.Set2, dsb.
    fig_hist = px.histogram(
        plot_df,
        x=selected_coord,
        color='class',
        color_discrete_sequence=color_sequence,
        title=f'Distribusi {selected_coord.capitalize()} Berdasarkan Kelas Objek',
        labels={selected_coord: selected_coord.capitalize(), 'class': 'Kelas Objek'},
        barmode='overlay',
        opacity=0.7
    )
    fig_hist.update_layout(bargap=0.1)
    st.plotly_chart(fig_hist, use_container_width=True)

    # ===============================
    # 🔹 Tombol Simpan + Preview Gambar
    # ===============================
    if st.button("💾 Simpan Gambar"):
        # Pastikan folder penyimpanan ada
        output_dir = "./result_visualization"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Path untuk file output
        scatter_path = os.path.join(output_dir, "plot_klasifikasi_3d.png")
        histogram_path = os.path.join(output_dir, "plot_klasifikasi_2d.png")

        # Simpan histogram sebagai gambar
        pio.write_image(fig_hist, histogram_path, format='png', width=900, height=500, scale=2)
        # Simpan gambar
        pio.write_image(fig_3d, scatter_path, format='png', width=900, height=600, scale=2)

        # Simpan path ke session_state jika perlu
        st.session_state['path_histogram_2d'] = histogram_path
        st.session_state['path_scatter_3d'] = scatter_path

        # Tampilkan notifikasi dan preview
        st.success("✅ Histogram & Scatter berhasil disimpan!")

    st.markdown("---")
    st.caption("Data divisualisasikan berdasarkan jarak angular dari titik pusat yang dipilih secara acak dari data user.")

def show():
    if 'df_sample' not in st.session_state:
        st.session_state.df_sample = pd.read_csv('data/star_classification.csv')

    if 'predicted' in st.session_state:
        st.session_state.df_sample = st.session_state.df_sample
        class_name = {0 : 'GALAXY', 1: 'QSO', 2 : 'STAR'}
        st.session_state.predicted['class'] = st.session_state.predicted['class'].apply(lambda x: class_name.get(x, x))
        st.session_state.predicted['class'] = st.session_state.predicted['class'].astype(str)
        classify_visualize(st.session_state.df_sample, st.session_state.predicted)
    else:
        st.warning("Data belum tersedia. Lakukan modeling selection terlebih dahulu.")
