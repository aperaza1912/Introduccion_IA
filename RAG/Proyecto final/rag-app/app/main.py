import os
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import traceback
###########################################################################
from app.chunk import extraer_texto_pdf, crear_chunks
from app.store import guardar_chunks_en_chroma, consultar_chroma
from app.generate import generar_respuesta  # <-- NUEVA IMPORTACIÓN

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "La API funciona exitosamente."}

@app.post("/ingest")
def ingest_document(file: UploadFile = File(...)):
    try:
        #Guardar en buffer
        ruta_temp = os.path.join("data", file.filename)
        with open(ruta_temp, "wb") as buffer:
            buffer.write(file.file.read())
        
        # Creación de los chunks
        texto = extraer_texto_pdf(ruta_temp)
        chunks = crear_chunks(texto, tamano_chunk=300, solape=50)
        
        total_chunks = guardar_chunks_en_chroma(chunks, file.filename)
        
        try:
            os.remove(ruta_temp)
        except PermissionError:
            pass 
        
        return {
            "message": f"Documento {file.filename} indexado exitosamente.", 
            "chunks_indexados": total_chunks
        }
    except Exception as e:
        return {"error_critico": str(e), "detalle": traceback.format_exc()}

class QueryRequest(BaseModel):
    question: str
    top_k: int = 3

@app.post("/query")
def query_documents(request: QueryRequest):
    """Busca fragmentos y le pide a Gemini que responda usaándolos."""
    try:
        # Buscar contexto en Chroma DB
        resultados = consultar_chroma(request.question, top_k=request.top_k)
        
        # Extraer docs
        documentos = resultados.get("documents", [[]])[0] if resultados.get("documents") else []
        metadatos = resultados.get("metadatas", [[]])[0] if resultados.get("metadatas") else []
        
        # Generar texto con Gemini
        respuesta_texto, citas, abstuvo = generar_respuesta(request.question, documentos, metadatos)
        
        # Formato de respuesta: respuesta, citas. Else, abstenerse.
        return {
            "answer": respuesta_texto,
            "citations": citas,
            "abstained": abstuvo
        }
    except Exception as e:
        import traceback
        return {"error_critico": str(e), "detalle": traceback.format_exc()}