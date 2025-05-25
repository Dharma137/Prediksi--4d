import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.title("Prediksi Angka 4D dengan Random Forest")

# Data hasil keluaran 4D (contoh, bisa kamu ganti)
data_4d = [
    '5849', '2413', '2968', '5314', '0952', '4174', '1921', '9151',
    '8840', '7238', '5924', '4554', '5415', '0071', '1768', '2986',
    '1085', '4791', '9459', '4353', '1317', '6569', '9653'
]

# Ekstrak fitur dan target
X = []
y = {0: [], 1: [], 2: [], 3: []}  # target tiap digit posisi

for i in range(len(data_4d) - 1):
    current_num = data_4d[i]
    next_num = data_4d[i + 1]
    features = [int(d) for d in current_num]
    X.append(features)
    for pos in range(4):
        y[pos].append(int(next_num[pos]))

# Split data dan latih model untuk tiap posisi digit
models = {}
for pos in range(4):
    X_train, X_test, y_train, y_test = train_test_split(X, y[pos], test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    models[pos] = model
    acc = model.score(X_test, y_test)
    st.write(f"Akurasi prediksi digit ke-{pos+1}: {acc:.2f}")

# Prediksi angka 4D berikutnya
last_num = [int(d) for d in data_4d[-1]]
prediksi = [models[pos].predict([last_num])[0] for pos in range(4)]
prediksi_angka = ''.join(str(d) for d in prediksi)

st.subheader("Prediksi Angka 4D Berikutnya:")
st.write(prediksi_angka)
