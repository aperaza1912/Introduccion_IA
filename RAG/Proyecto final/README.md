# Proyecto Final — Sistema RAG (Streamlit + FastAPI + ChromaDB + Google AI)

Este repositorio contiene la implementación de un sistema RAG (Generación Aumentada por Recuperación). El sistema permite cargar documentos, indexarlos vectorialmente y realizar consultas en lenguaje natural obteniendo respuestas ancladas estrictamente en los documentos proporcionados, citando las fuentes utilizadas.

## Arquitectura y Stack Tecnológico

* **UI (Cliente):** Streamlit (Puerto 8501)
* **API (Backend):** FastAPI (Puerto 8000)
* **Base de Datos Vectorial:** ChromaDB (Persistencia local)
* **Embeddings y Generación:** Google AI (Gemini / API de Google AI Studio)

## Estructura del Proyecto

```text
RAG/Proyecto final/rag-app/
├── README.md
├── requirements.txt
├── .env.example
├── data/               # Corpus de ejemplo (PDFs, txt, md)
├── chroma/             # Persistencia local de ChromaDB (ignorado en git)
├── app/
│   ├── main.py         # Endpoints de FastAPI: /health, /ingest, /query
│   ├── chunk.py        # Lógica de partición de texto con solapamiento
│   ├── embed.py        # Cliente de embeddings usando Google AI
│   ├── store.py        # Interacción con ChromaDB (alta y consulta top-k)
│   └── generate.py     # Generación de respuestas con Gemini (ancladas y con abstención)
└── ui/
    └── streamlit_app.py # Interfaz de usuario para carga, chat y visualización de citas
```

## Requisitos previos

1. Python 3.8 o superior.
2. Obtener una clave de API de Google AI Studio: [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)

## Instalacion y configuracion

Para iniciar, primero debes clonar el repositorio (o crear la carpeta del proyecto) y establecer un entorno virtual:

1. Abre tu terminal y navega al directorio del proyecto.
2. Crea el entorno virtual:
   ```bash
   python -m venv venv
   ```
3. Activa el entorno virtual:
   * En Windows:
     ```bash
     venv\Scripts\activate
     ```

## Instalacion de dependencias

Con el entorno virtual activado, instala todas las librerias requeridas por el proyecto:

```bash
pip install -r requirements.txt
```

## Configurar variables de entorno

El sistema necesita acceso a la API de Google AI para generar los embeddings y las respuestas. 

1. Abre el archivo `.env` y añade tu clave de API. Puedes conseguirla en el link de arriba:

```env
GOOGLE_API_KEY=tu_clave_de_google_aqui
```

*Nota: Asegúrate de que el archivo `.env` esté incluido en tu `.gitignore` para no subir tus credenciales al repositorio.*

## Ejecución

Para levantar el sistema de forma local, necesitas ejecutar la API y la UI en dos terminales separadas. **Nota**: Ten activado el virtual environment en ambas terminales.

**Terminal 1: Iniciar la API (FastAPI)**
```bash
uvicorn app.main:app --reload --port 8000
```
*Puedes verificar la documentación interactiva de la API en `http://localhost:8000/docs`.*

**Terminal 2: Iniciar la UI (Streamlit)**
```bash
streamlit run ui/streamlit_app.py
```

## Comprobacion de pregunta

Con las dos terminales corriendo:

1. Abre la interfaz en tu navegador accediendo a `http://localhost:8501`.
2. Utiliza la barra lateral o el área designada para cargar tus documentos al sistema (esto consumirá el endpoint `/ingest` de la API).
3. Escribe una pregunta relacionada con el dominio de los documentos en la caja de texto.
4. El sistema devolverá una respuesta generada citando las fuentes `[n]` correspondientes y mostrará los chunks de texto recuperados con sus respectivos puntajes de similitud.
5. **Para probar la abstención:** Realiza una pregunta que no tenga relación alguna con los documentos cargados. El sistema identificará que no hay evidencia suficiente y se abstendrá de responder, indicando claramente la falta de información en lugar de inventarla.

   **IMPORTANTE**: Toma en cuenta que el modelo usado presenta mucha demanda a veces. Esto puede corroborarse leyendo los códigos de error. Si eso sucede, esperar 5 minutos y volver a intentar.

## Autor

Alan Peraza - Maestría en Inteligencia Artificial