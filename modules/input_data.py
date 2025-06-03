import streamlit as st
import pandas as pd
import csv

# -------------------- FUNCTIONAL VALIDATORS --------------------

def is_csv(file):
    return file.name.endswith('.csv')

def validate_column_presence(df, required_columns):
    return all(col in df.columns for col in required_columns)

def validate_manual_input(data, min_value=0, max_value=360_000):
    try:
        val = float(data)
        return min_value <= val <= max_value
    except ValueError:
        return False

def has_missing_values(df):
    return df.isnull().any().any()

def safe_read_csv(uploaded_file):
    uploaded_file.seek(0)
    try:
        # Deteksi delimiter secara otomatis
        sample = uploaded_file.read(2048).decode("utf-8")
        dialect = csv.Sniffer().sniff(sample)
        delimiter = dialect.delimiter
    except Exception:
        delimiter = ","  # fallback jika gagal deteksi

    uploaded_file.seek(0)
    try:
        return pd.read_csv(
            uploaded_file,
            sep=delimiter,
            engine="python",
            on_bad_lines="skip",
            dtype=str
        )
    except Exception as e:
        raise e

# -------------------- OBJECT-ORIENTED HANDLER --------------------

class AstroInputHandler:
    def __init__(self, required_columns):
        self.required_columns = required_columns

    def process_file_upload(self, uploaded_file):
        if not is_csv(uploaded_file):
            return None, "File harus berformat CSV."
        try:
            df = safe_read_csv(uploaded_file)  # ← pakai fungsi toleran
        except Exception as e:
            return None, f"Gagal membaca file: {e}"
        
        if df.empty:
            return None, "File kosong."
        
        if not validate_column_presence(df, self.required_columns):
            return None, "File tidak memiliki semua kolom yang dibutuhkan (minimal: alpha, delta, u, g, r, i, z, redshift)."

        if has_missing_values(df):
            return df, "File valid, tetapi terdapat missing values."

        return df, "File berhasil diunggah dan valid."

    def process_manual_input(self, input_values):
        results = []
        for i, val in enumerate(input_values):
            if validate_manual_input(val):
                results.append(float(val))
            else:
                return None, f"Input manual pada kolom {i+1} tidak valid atau di luar rentang (0 - 360.000)."
        return results, "Input manual valid."

# -------------------- STREAMLIT APP --------------------

def main():
    st.title("AstroClassify - Fitur Input Data Astronomi")
    handler = AstroInputHandler(required_columns=["alpha", "delta", "u", "g", "r", "i", "z", "redshift"])

    mode = st.radio("Pilih Metode Input:", ["Upload File CSV", "Input Manual"])

    if mode == "Upload File CSV":
        uploaded_file = st.file_uploader("Unggah file CSV dari SDSS", type="csv")
        if uploaded_file:
            df, msg = handler.process_file_upload(uploaded_file)
            st.info(msg)
            if df is not None:
                st.write("Preview Data:", df.head())

    else:  # Input Manual
        st.write("Masukkan nilai untuk fitur berikut:")
        input_values = [
            st.text_input("Right Ascension (ra) / alpha"),
            st.text_input("Declination (dec) / delta"),
            st.text_input("Filter u"),
            st.text_input("Filter g"),
            st.text_input("Filter r"),
            st.text_input("Filter i"),
            st.text_input("Filter z"),
            st.text_input("Redshift"),
        ]
        if st.button("Submit"):
            result, msg = handler.process_manual_input(input_values)
            st.info(msg)
            if result:
                st.success(f"Data valid: {result}")

if __name__ == "__main__":
    main()