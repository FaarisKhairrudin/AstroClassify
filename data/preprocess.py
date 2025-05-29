import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

df = pd.read_csv('./data/star_classification.csv')

# hilangkan data yang tidak valid
df = df.drop(df[(df['u'] == -9999) | (df['g'] == -9999) | (df['z'] == -9999)].index)

# 1. Hapus kolom tidak relevan
cols_to_drop = ['obj_ID', 'run_ID', 'rerun_ID', 'cam_col', 'field_ID', 'spec_obj_ID','fiber_ID']
df_clean = df.drop(columns=cols_to_drop, errors='ignore')  # `errors='ignore'` untuk kolom yang tidak ada

# 2. Handle missing values (jika ada)
if df_clean.isnull().sum().any():
    df_clean = df_clean.fillna()  # atau imputasi dengan mean/median

# 3. Encode target `class` ke numerik
le = LabelEncoder()
df_clean['class_encoded'] = le.fit_transform(df_clean['class'])  # 0=GALAXY, 1=QSO, 2=STAR

# 4. Pisahkan fitur (X) dan target (y)
X = df_clean.drop(columns=['class', 'class_encoded'])
y = df_clean['class_encoded']

# 5. Normalisasi fitur numerik
scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)

# 6. Bagi data menjadi training dan testing set
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

print("Data setelah preprocessing:")
X_scaled.head()

