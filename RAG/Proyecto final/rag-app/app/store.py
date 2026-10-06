import chromadb
import os
from app.embed import obtener_embedding

# 1. Configurar el almacenamiento de datos
ruta_chroma = os.path.join(os.path.dirname(os.path.dirname(__file__)), "chroma")
cliente_chroma = chromadb.PersistentClient(path=ruta_chroma)

# Pasar vectores generados por GoogleAI
coleccion = cliente_chroma.get_or_create_collection(name="animales_marinos")

def guardar_chunks_en_chroma(chunks, nombre_archivo):
    # Asistido por IA:
    """Recibe una lista de fragmentos de texto, 
    pide sus vectores a Google y los guarda."""
    if not chunks:
        return 0
        
    ids = []
    embeddings = []
    metadatos = []
    
    for i, chunk in enumerate(chunks):
        # Vectores obtenidos de GoogleAI
        vector = obtener_embedding(chunk)
        
        ids.append(f"{nombre_archivo}_chunk_{i}")
        embeddings.append(vector)
        # Guardar los sources e indexarlos para citarlos.
        metadatos.append({"source": nombre_archivo, "chunk_index": i})
        
    # Guardar textos:
    coleccion.add(
        ids=ids,
        embeddings=embeddings,
        metadatas=metadatos,
        documents=chunks
    )
    return len(chunks)
    # FIN ASISTENCIA DE IA


def consultar_chroma(pregunta, top_k=3):
    vector_pregunta = obtener_embedding(pregunta)
    
    # Chroma usa k-NN por debajo para devolver los más cercanos al vector de la pregunta
    resultados = coleccion.query(
        query_embeddings=[vector_pregunta],
        n_results=top_k
    )
    return resultados