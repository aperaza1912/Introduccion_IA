import pypdf

def extraer_texto_pdf(ruta_archivo):
    """Lee un archivo PDF y devuelve todo su texto como un solo string."""
    texto_completo = ""
    with open(ruta_archivo, 'rb') as archivo:
        lector = pypdf.PdfReader(archivo)
        for pagina in lector.pages:
            texto = pagina.extract_text()
            if texto:
                texto_completo += texto + " "
    return texto_completo

def crear_chunks(texto, tamano_chunk=300, solape=50):
    """
    Divide el texto en fragmentos (chunks) de un tamaño de palabras específico.
    Usa un solape para no perder el contexto entre un bloque y otro.
    """
    palabras = texto.split()
    chunks = []
    
    i = 0
    while i < len(palabras):
        # Tomamos una rebanada de palabras según el tamaño del chunk
        chunk = " ".join(palabras[i:i + tamano_chunk])
        chunks.append(chunk)
        # Avanzamos restando el solape para que las últimas palabras se repitan en el siguiente
        i += (tamano_chunk - solape)
        
    return chunks