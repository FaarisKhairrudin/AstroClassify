import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import plotly.io as pio
import os

def classify_visualize(df_sample, df_user):
    st.header("🪐 Fitur Visualisasi Hasil Klasifikasi")
    st.markdown("Gunakan fitur di bawah untuk menyaring dan memvisualisasikan objek astronomi berdasarkan hasil klasifikasi.")

    # Salinan aman
    df_sample_safe = df_sample.copy()
    df_user_safe = df_user.copy()
    df_sample_safe['class'] = df_sample_safe['class'].astype(str)
    df_user_safe['class'] = df_user_safe['class'].astype(str)

    df = pd.concat([df_sample_safe, df_user_safe], ignore_index=True).drop_duplicates()
    if df.empty or not all(col in df.columns for col in ['alpha', 'delta', 'redshift', 'class']):
        st.error("❌ Data kosong atau kolom wajib tidak lengkap.")
        return

    # Sidebar-like Multiselect
    with st.container():
        st.markdown("### 🔍 Filter Data")
        selected_labels = st.multiselect("🎯 Pilih kelas objek yang ingin divisualisasikan:", df['class'].unique().tolist(), default=df['class'].unique().tolist())

    if not selected_labels:
        st.warning("⚠️ Pilih minimal satu kelas objek.")
        return

    filtered_df = df[df['class'].isin(selected_labels)]

    # Titik pusat
    if 'center_point_data' not in st.session_state:
        if df_user_safe.empty:
            st.error("❌ Data user kosong.")
            return
        selected_center = df_user_safe[['alpha', 'delta', 'redshift', 'class']].sample(n=1).iloc[0]
        match = df[(df['alpha'] == selected_center['alpha']) &
                   (df['delta'] == selected_center['delta']) &
                   (df['redshift'] == selected_center['redshift'])]
        if match.empty:
            st.error("❌ Gagal menemukan titik pusat di data gabungan.")
            return
        st.session_state.center_point_data = match.iloc[0].to_dict()

    center_point = st.session_state.center_point_data

    with st.expander("📌 Titik Pusat Visualisasi", expanded=True):
        st.json(center_point, expanded=False)

    # Hitung jarak angular
    distance = np.sqrt((filtered_df['alpha'] - center_point['alpha'])**2 +
                       (filtered_df['delta'] - center_point['delta'])**2)
    max_distance = float(np.ceil(distance.max() * 10) / 10)
    user_distance = st.slider("📏 Batas Jarak Angular (α & δ)", 0.0, max_distance, min(1.0, max_distance), 0.1)

    plot_df = filtered_df[distance <= user_distance].copy()
    if plot_df.empty:
        st.warning("⚠️ Tidak ada objek dalam jarak yang dipilih.")
        return

    # Tandai titik pusat
    plot_df['highlight'] = (plot_df['alpha'] == center_point['alpha']) & \
                           (plot_df['delta'] == center_point['delta']) & \
                           (plot_df['redshift'] == center_point['redshift']) & \
                           (plot_df['class'] == center_point['class'])

    highlight_point = plot_df[plot_df['highlight']]
    main_points = plot_df[~plot_df['highlight']]

    class_map = {'GALAXY': 0, 'QSO': 1, 'STAR': 2}
    main_points['class_code'] = main_points['class'].map(class_map).astype(int)
    highlight_point['class_code'] = highlight_point['class'].map(class_map).astype(int)

    user_other_points = pd.merge(
        df_user_safe[
            ~(
                (df_user_safe['alpha'] == center_point['alpha']) &
                (df_user_safe['delta'] == center_point['delta']) &
                (df_user_safe['redshift'] == center_point['redshift']) &
                (df_user_safe['class'] == center_point['class'])
            )
        ],
        plot_df,
        on=['alpha', 'delta', 'redshift', 'class'],
        how='inner'
    )
    user_other_points['class_code'] = user_other_points['class'].map(class_map).astype(int)

    with st.expander("🌌 Visualisasi 3D Scatter", expanded=True):
        st.caption(f"Menampilkan objek dalam radius ≤ {user_distance}° dari titik pusat.")

        fig_3d = go.Figure(data=[
            go.Scatter3d(
                x=main_points['alpha'], y=main_points['delta'], z=main_points['redshift'],
                mode='markers',
                marker=dict(size=5, opacity=0.8, color=main_points['class_code'],
                            colorscale='Viridis',
                            colorbar=dict(title='Kelas', tickvals=[0,1,2], ticktext=list(class_map.keys()))),
                text=main_points.apply(lambda row: f"Class: {row['class']}<br>Redshift: {row['redshift']:.3f}<br>α: {row['alpha']:.3f}°<br>δ: {row['delta']:.3f}°", axis=1),
                hoverinfo='text', name='Objek'
            ),
            go.Scatter3d(
                x=user_other_points['alpha'], y=user_other_points['delta'], z=user_other_points['redshift'],
                mode='markers',
                marker=dict(size=7, color='cyan', line=dict(color='blue', width=1.5)),
                text=user_other_points.apply(lambda row: f"User Point<br>Class: {row['class']}<br>Redshift: {row['redshift']:.3f}<br>α: {row['alpha']:.3f}°<br>δ: {row['delta']:.3f}°", axis=1),
                hoverinfo='text', name='Titik dari User'
            ),
            go.Scatter3d(
                x=highlight_point['alpha'], y=highlight_point['delta'], z=highlight_point['redshift'],
                mode='markers',
                marker=dict(size=8, color='red', line=dict(color='white', width=2)),
                text=highlight_point.apply(lambda row: f"Class: {row['class']}<br>Redshift: {row['redshift']:.3f}<br>α: {row['alpha']:.3f}°<br>δ: {row['delta']:.3f}°<br><b>(Titik Pusat)</b>", axis=1),
                hoverinfo='text', name='Titik Pusat'
            )
        ])
        fig_3d.update_layout(
            title='Distribusi 3D Objek Astronomi (α, δ, redshift)',
            scene=dict(xaxis_title='Right Ascension (α)', yaxis_title='Declination (δ)', zaxis_title='Redshift'),
            legend=dict(x=0.01, y=0.99),
            margin=dict(l=0, r=0, b=0, t=40)
        )
        st.plotly_chart(fig_3d, use_container_width=True)

    # Pilih ulang titik pusat
    if st.button("🔄 Pilih Ulang Titik Pusat"):
        st.session_state.pop('center_point_data', None)
        st.rerun()

    st.markdown("---")

    # Histogram
    with st.expander("📊 Visualisasi Histogram Koordinat", expanded=False):
        selected_coord = st.selectbox("📌 Pilih Koordinat untuk Histogram:", ['alpha', 'delta'])
        fig_hist = px.histogram(
            plot_df, x=selected_coord, color='class',
            color_discrete_sequence=px.colors.qualitative.Plotly,
            title=f'Distribusi {selected_coord.capitalize()} Berdasarkan Kelas Objek',
            labels={selected_coord: selected_coord.capitalize(), 'class': 'Kelas Objek'},
            barmode='overlay', opacity=0.7
        )
        fig_hist.update_layout(bargap=0.1)
        st.plotly_chart(fig_hist, use_container_width=True)

    # Tombol simpan
    st.markdown("### 💾 Simpan Gambar Visualisasi")
    st.info("Klik tombol di bawah untuk menyimpan gambar visualisasi 3D dan histogram", icon="💡")
    save_col1, save_col2 = st.columns([1, 6])
    with save_col1:
        save_clicked = st.button("📸 Simpan Gambar", use_container_width=True)
    with save_col2:
        if save_clicked:
            output_dir = "./result_visualization"
            os.makedirs(output_dir, exist_ok=True)
            scatter_path = os.path.join(output_dir, "plot_klasifikasi_3d.png")
            histogram_path = os.path.join(output_dir, "plot_klasifikasi_2d.png")

            pio.write_image(fig_3d, scatter_path, format='png', width=900, height=600, scale=2)
            pio.write_image(fig_hist, histogram_path, format='png', width=900, height=500, scale=2)

            st.session_state['path_scatter_3d'] = scatter_path
            st.session_state['path_histogram_2d'] = histogram_path

            st.success("Gambar berhasil disimpan", icon="✅")

    st.caption("📌 Visualisasi ini menggunakan titik acak dari data user sebagai pusat klasifikasi.")


def show():
    if 'df_sample' not in st.session_state:
        st.session_state.df_sample = pd.read_csv('data/star_classification.csv')

    if 'predicted' in st.session_state:
        st.session_state.df_sample = st.session_state.df_sample[st.session_state.predicted.columns]
        class_name = {0 : 'GALAXY', 1: 'QSO', 2 : 'STAR'}
        st.session_state.predicted['class'] = st.session_state.predicted['class'].apply(lambda x: class_name.get(x, x))
        st.session_state.predicted['class'] = st.session_state.predicted['class'].astype(str)
        classify_visualize(st.session_state.df_sample, st.session_state.predicted)
    else:
        st.warning("Data belum tersedia. Lakukan modeling selection terlebih dahulu.")
