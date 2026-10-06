import streamlit as st
import requests

st.set_page_config(page_title="RAG Animales Marinos", page_icon="🐋")

# URL de tu API local
API_URL = "http://127.0.0.1:8000"

st.title("RAG de Animales Marinos - Alan Peraza")
st.write("Sube archivos de texto, markdown o PDF y haz preguntas con respecto a la evidencia en los archivos.")

# Sección 1: Carga de documentos
st.header("1. Sube tus Documentos")
uploaded_file = st.file_uploader("Sube un archivo PDF", type=["pdf"])

if st.button("Indexar a ChromaDB"):
    if uploaded_file is not None:
        with st.spinner("Extrayendo, fragmentando y vectorizando..."):
            # Streamlit manda el archivo a FastAPI
            files = {"file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")}
            try:
                response = requests.post(f"{API_URL}/ingest", files=files)
                if response.status_code == 200:
                    data = response.json()
                    # Imprime mensaje de success
                    # Revisar esto
                    st.success(f"{data['message']} (Chunks: {data['chunks_indexados']})")
                else:
                    st.error(f"Error de la API: {response.text}")
            except requests.exceptions.ConnectionError:
                st.error("No se pudo conectar con FastAPI. ¿Está corriendo uvicorn?")
    else:
        st.warning("Por favor seleccionar un documento")

st.divider()

# Sección 2: Consultar al modelo
st.header("2. Consulta al Modelo")
pregunta = st.text_input("Haz una pregunta sobre el hábitat, dieta, características o datos de un animal mareino:")

if st.button("Generar Respuesta"):
    if pregunta:
        with st.spinner("Buscando contexto y consultando a Gemini..."):
            try:
                payload = {"question": pregunta, "top_k": 3}
                response = requests.post(f"{API_URL}/query", json=payload)
                
                if response.status_code == 200:
                    data = response.json()
                    
                    
                    if "error_critico" in data:
                        st.error(f"Error interno del servidor: {data['error_critico']}")
                        with st.expander("Ver rastreo técnico"):
                            st.code(data["detalle"])
                    else:
                        st.markdown("### Respuesta")
                        if data.get("abstained"):
                            st.info("El modelo se ha abstenido de responder por falta de evidencia.")
                        
                        st.write(data.get("answer", ""))
                        
                        # Mostrar metadatos como evidencia/citas
                        if data.get("citations"):
                            st.markdown("### Evidencia Recuperada")
                            for i, cita in enumerate(data["citations"]):
                                st.caption(f"**[{i+1}] Fuente:** {cita.get('source', 'Desconocido')}")
                else:
                    st.error(f"Error en la consulta HTTP: {response.text}")
            except requests.exceptions.ConnectionError:
                st.error("No se pudo conectar con FastAPI.")
    else:
        st.warning("Escribe una pregunta para continuar.")