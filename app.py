import streamlit as st
import pandas as pd
import joblib

# ===== Carregar modelo =====
model = joblib.load("modelo_obesidade.pkl")

st.set_page_config(page_title="Predição de Obesidade", layout="centered")

st.title("🩺 Sistema Preditivo de Obesidade")
st.write("Preencha os dados do paciente para obter a predição.")

# ===== Entradas =====
gender = st.selectbox("Gênero", ["Male", "Female"])
age = st.number_input("Idade", min_value=1, max_value=120, value=30)
height = st.number_input("Altura (m)", min_value=1.0, max_value=2.5, value=1.70)
weight = st.number_input("Peso (kg)", min_value=30, max_value=200, value=70)

family_history = st.selectbox(
    "Histórico familiar de excesso de peso?",
    ["yes", "no"]
)

favc = st.selectbox(
    "Consome alimentos altamente calóricos com frequência?",
    ["yes", "no"]
)

fcvc = st.slider("Consumo de vegetais", 1.0, 3.0, 2.0)
ncp = st.slider("Número de refeições principais", 1.0, 4.0, 3.0)

caec = st.selectbox(
    "Come entre as refeições?",
    ["no", "Sometimes", "Frequently", "Always"]
)

smoke = st.selectbox("Fuma?", ["yes", "no"])
ch2o = st.slider("Consumo diário de água", 1.0, 3.0, 2.0)

scc = st.selectbox("Monitora calorias?", ["yes", "no"])
faf = st.slider("Frequência de atividade física", 0.0, 3.0, 1.0)
tue = st.slider("Tempo em telas (horas)", 0.0, 3.0, 1.0)

calc = st.selectbox(
    "Consumo de álcool",
    ["no", "Sometimes", "Frequently", "Always"]
)

mtrans = st.selectbox(
    "Meio de transporte",
    ["Public_Transportation", "Walking", "Automobile", "Motorbike", "Bike"]
)

# ===== Botão =====
if st.button("🔍 Prever nível de obesidade"):

    input_data = pd.DataFrame([{
        "Gender": gender,
        "Age": age,
        "Height": height,
        "Weight": weight,
        "family_history_with_overweight": family_history,
        "FAVC": favc,
        "FCVC": fcvc,
        "NCP": ncp,
        "CAEC": caec,
        "SMOKE": smoke,
        "CH2O": ch2o,
        "SCC": scc,
        "FAF": faf,
        "TUE": tue,
        "CALC": calc,
        "MTRANS": mtrans
    }])

    prediction = model.predict(input_data)

    st.success(f"📊 Nível de obesidade previsto: **{prediction[0]}**")
