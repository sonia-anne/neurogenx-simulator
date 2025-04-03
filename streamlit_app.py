import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="NEUROGEN-X Simulator", layout="centered")

st.title("Simulador Interactivo de Eficacia: NEUROGEN-X vs. Terapias Actuales")

st.markdown("""
Este simulador permite comparar la eficacia del tratamiento **NEUROGEN-X** con otras terapias contra la enfermedad de Creutzfeldt-Jakob.  
Ajusta la dosis y observa cómo varía la eficacia del tratamiento en función de parámetros simulados de laboratorio.
""")

dosis = st.slider("Dosis de nanorobots (en millones)", 10, 200, 100)
activacion_ia = st.selectbox("Nivel de optimización con IA", ["Baja", "Media", "Alta"])
combinado_regenerativo = st.checkbox("Activar módulo regenerativo neuronal")

base_eficacia = 60 + (dosis / 4)
if activacion_ia == "Media":
    base_eficacia += 10
elif activacion_ia == "Alta":
    base_eficacia += 20

if combinado_regenerativo:
    base_eficacia += 5

eficacia_neurogenx = min(base_eficacia, 100)
eficacia_actuales = 48

st.subheader("Resultados Simulados")
st.write(f"**Eficacia estimada NEUROGEN-X:** {eficacia_neurogenx:.2f}%")
st.write(f"**Eficacia promedio terapias actuales:** {eficacia_actuales}%")

fig, ax = plt.subplots()
ax.bar(["NEUROGEN-X", "Terapias Actuales"], [eficacia_neurogenx, eficacia_actuales], color=["green", "red"])
ax.set_ylabel("Eficacia (%)")
ax.set_title("Comparación de Eficacia")
st.pyplot(fig)

st.subheader("Comparación Económica")
cost_neurogenx = 8000
cost_actual = 1200000
st.write(f"**Costo por paciente NEUROGEN-X:** ${cost_neurogenx}")
st.write(f"**Costo por paciente terapias actuales:** ${cost_actual:,}")

st.markdown("""
Este simulador demuestra el potencial de NEUROGEN-X como una solución efectiva y accesible para tratar enfermedades priónicas.  
Los parámetros se basan en modelos predictivos y datos experimentales simulados.
""")
