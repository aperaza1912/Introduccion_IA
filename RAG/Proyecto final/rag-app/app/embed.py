import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
# RECORDAR BORRAR EL API KEY ANTES DE HACER COMMIT
# RECORDAR BORRAR EL API KEY ANTES DE HACER COMMIT
# RECORDAR BORRAR EL API KEY ANTES DE HACER COMMIT
client = genai.Client(api_key=os.environ.get("GOOGLE_API_KEY"))
# RECORDAR BORRAR EL API KEY ANTES DE HACER COMMIT
# RECORDAR BORRAR EL API KEY ANTES DE HACER COMMIT
# RECORDAR BORRAR EL API KEY ANTES DE HACER COMMIT
def obtener_embedding(texto: str) -> list[float]:
    # Vectorizar el texto
    response = client.models.embed_content(
        model='gemini-embedding-001',
        contents=texto
    )
    return response.embeddings[0].values

if __name__ == "__main__":
    print("Conectando a GoogleAI\n")
    
    frase1 = "El tiburón blanco es un gran depredador marino."
    frase2 = "Los escualos cazan focas en el océano."
    frase3 = "El camello almacena agua en su joroba para cruzar el desierto."
    
    vec1 = obtener_embedding(frase1)
    vec2 = obtener_embedding(frase2)
    vec3 = obtener_embedding(frase3)
    
    print(f"Éxito: El vector de la frase 1 tiene {len(vec1)} dimensiones.")
    print("Las frases 1 y 2 deberían ser matemáticamente más cercanas que la 3.")