import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Carga SMARTFENSE", layout="wide")

st.title("🛡️ SMARTFENSE - Carga Masiva de Usuarios")
st.markdown("---")

# Sidebar: Configuración de la sesión
with st.sidebar:
    st.header("Configuración")
    modo = st.radio("Selecciona el modo:", ["Carga Única", "Carga por Tenant"])
    st.info("Nota: Asegúrate de que el Excel no contenga encabezados.")

# Área principal
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("1. Subir Datos")
    archivo = st.file_uploader("Arrastra tu archivo Excel aquí", type=["xlsx"])

with col2:
    st.subheader("2. Selección de Tenant")
    tenant = st.selectbox("Destino del Tenant:", 
                          ["Breca-Corporativo", "Breca-Sub1", "Breca-Sub2", "Breca-Sub3"])

st.markdown("---")

# Previsualización
if archivo:
    st.subheader("👁️ Previsualización de Datos")
    # Simulamos lectura de Excel
    df = pd.read_excel(archivo)
    st.dataframe(df, use_container_width=True)
    
    st.subheader("3. Acción")
    if st.button("🚀 Validar y Procesar Carga"):
        with st.spinner('Procesando datos y validando estructura...'):
            # Aquí irá la lógica de transformación
            st.success("¡Datos validados! Listo para enviar a la API.")
else:
    st.info("Por favor, sube un archivo Excel para comenzar.")

# Pie de página
st.markdown("---")
st.caption("Herramienta interna de carga masiva para SMARTFENSE")
