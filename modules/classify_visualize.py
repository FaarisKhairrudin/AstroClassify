import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

def classify_visualize(df_sample, df_user):
    # Gabungkan data
    df = pd.concat([df_sample, df_user], ignore_index=True)

    # Konfigurasi halaman
    st.set_page_config(page_title="AstroClassify", layout="wide")
    st.title("🪐 AstroClassify - Visualisasi Hasil Klasifikasi")
    st.markdown("---")

    # Validasi data
    if df.empty:
        st.error("❌ Maaf, data untuk visualisasi belum tersedia atau gagal dimuat.")
        return

    required_cols = ['obj_ID', 'alpha', 'delta', 'redshift', 'class']
    if not all(col in df.columns for col in required_cols):
        st.error("❌ Data tidak memiliki kolom wajib: obj_ID, alpha, delta, redshift, class")
        return

    # Filter kelas (sekarang di halaman utama, bukan sidebar)
    unique_labels = df['class'].unique().tolist()
    selected_labels = st.multiselect("🎯 Filter kelas objek", unique_labels, default=unique_labels)

    if len(selected_labels) == 0:
        st.warning("⚠️ Tidak ada kelas objek yang dipilih. Silakan pilih minimal satu.")
        return

    filtered_df = df[df['class'].isin(selected_labels)]

    # Pilih titik pusat dari df_user (acak)
    if 'center_point_data' not in st.session_state:
        if df_user.empty:
            st.error("❌ Data user kosong, tidak dapat memilih titik pusat.")
            return
        selected_center = df_user.sample(n=1).iloc[0]
        st.session_state.center_point_data = selected_center.to_dict()

    center_point = st.session_state.center_point_data

    # Tampilkan titik pusat (sekarang di halaman utama)
    with st.expander("🎯 Titik pusat visualisasi (dipilih dari data user):", expanded=True):
        st.write({
            'obj_ID': center_point['obj_ID'],
            'alpha': center_point['alpha'],
            'delta': center_point['delta'],
            'redshift': center_point['redshift'],
            'class': center_point['class']
        })

    # Hitung jarak angular
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

    # Tandai titik pusat
    center_obj_id = center_point['obj_ID']
    plot_df['highlight'] = plot_df['obj_ID'] == center_obj_id
    highlight_point = plot_df[plot_df['highlight']].iloc[[0]]
    main_points = plot_df.drop(index=highlight_point.index)

    # Visualisasi 3D
    st.markdown("### 🌌 3D Scatter Plot: Distribusi Objek Astronomi")
    st.caption(f"Menampilkan objek dalam jarak ≤ {max_distance}° dari titik pusat.")

    class_map = {'GALAXY': 0, 'QSO': 1, 'STAR': 2}
    plot_df['class_numeric'] = plot_df['class'].map(class_map)

    scatter_main = go.Scatter3d(
        x=main_points['alpha'],
        y=main_points['delta'],
        z=main_points['redshift'],
        mode='markers',
        marker=dict(
            size=5,
            opacity=0.8,
            color=main_points['class'].map(class_map),
            colorscale='Viridis',
            colorbar=dict(title='Kelas', tickvals=[0, 1, 2], ticktext=['GALAXY', 'QSO', 'STAR'])
        ),
        text=main_points.apply(
            lambda row: f"ID: {row['obj_ID']}<br>Class: {row['class']}<br>Redshift: {row['redshift']:.3f}",
            axis=1),
        hoverinfo='text',
        name='Objek'
    )

    scatter_center = go.Scatter3d(
        x=highlight_point['alpha'],
        y=highlight_point['delta'],
        z=highlight_point['redshift'],
        mode='markers',
        marker=dict(
            size=8,
            color='red',
            line=dict(color='white', width=2)
        ),
        text=highlight_point.apply(
            lambda row: f"ID: {row['obj_ID']}<br>Class: {row['class']}<br>Redshift: {row['redshift']:.3f}<br><b>(Titik Pusat)</b>",
            axis=1),
        hoverinfo='text',
        name='Titik Pusat'
    )

    fig_3d = go.Figure(data=[scatter_main, scatter_center])
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

    if filtered_df.shape[0] > 0:
        if st.button("🔄 Pilih Ulang Titik Pusat"):
            if 'center_point_data' in st.session_state:
                del st.session_state['center_point_data']
            st.rerun()

    # Histogram
    st.markdown("### 📊 Histogram Berdasarkan Alpha atau Delta")
    selected_coord = st.selectbox("Pilih koordinat untuk histogram:", ['alpha', 'delta'])

    hist_df = plot_df[['class', selected_coord]].copy()
    fig_hist = px.histogram(
        hist_df,
        x=selected_coord,
        color='class',
        title=f'Distribusi {selected_coord.capitalize()} Berdasarkan Kelas Objek',
        labels={selected_coord: selected_coord.capitalize(), 'class': 'Kelas Objek'},
        barmode='overlay',
        opacity=0.7
    )
    fig_hist.update_layout(bargap=0.1)
    st.plotly_chart(fig_hist, use_container_width=True)

    # Download
    if 'prediction' in st.session_state and st.session_state.prediction:
        download_df = pd.DataFrame(st.session_state.prediction)
        csv = download_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Hasil Klasifikasi (CSV)",
            data=csv,
            file_name='hasil_klasifikasi.csv',
            mime='text/csv'
        )

    st.markdown("---")
    st.caption("Data divisualisasikan dalam radius tertentu dari objek pusat yang dipilih dari data user.")


def show():
    # buatkan code untuk membaca data dan menyimpannya di st.session_state.df_sample
    if 'df_sample' not in st.session_state:
        st.session_state.df_sample = pd.read_csv('data/star_classification.csv')  # Inisialisasi jika belum ada
    if 'df_sample' in st.session_state and 'predicted' in st.session_state:
        classify_visualize(st.session_state.df_sample, st.session_state.df_user)
    else:
        st.warning("Data belum tersedia. Lakukan preprocessing terlebih dahulu.")