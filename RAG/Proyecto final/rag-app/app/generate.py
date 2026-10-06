import os
from google import genai

# Connexión a GoogleAPI
# NO OLVIDAR BORRAR EL API KEY ANTES DE SUBIR ☢️☢️☢️☢️
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
# NO OLVIDAR BORRAR EL API KEY ANTES DE SUBIR ☢️☢️☢️☢️


def generar_respuesta(pregunta, documentos, metadatos):
    # Estrategia 1 de abstención - verificar disponibilidad de fuentes
    if not documentos or len(documentos) == 0:
        return "No hay evidencia suficiente para responder a esta pregunta. Intenta subiendo archivos con el tema de interés.", [], True
    
    contexto = ""
    for i, doc in enumerate(documentos):
        # Esto sirve para citar las fuentes (nota: son 7 en mi caso)
        contexto += f"[{i+1}] {doc}\n\n"
        
    prompt = f"""
    Responde a la pregunta del usuario utilizando exclusivamente la información de los siguientes fragmentos. 
    No inventes información. Si la respuesta no está en los fragmentos, di explícitamente "no tengo evidencia suficiente".
    Cita los fragmentos usados con el formato [n]. Responde en español.
    
    Fragmentos:
    {contexto}
    
    Pregunta: {pregunta}
    """
    
    # Genera las respuestas
    # Nota para el profesor: usé otras versiones y esta es la que menos errores devuelve (unavailable)
    response = client.models.generate_content(
        model= 'gemini-3.8-flash',
        contents= prompt
    )
    
    return response.text, metadatos, False