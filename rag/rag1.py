import os
import pdfplumber
import requests
from dotenv import load_dotenv
import chromadb

# Load environment variables from a .env file
load_dotenv()

def embed_text(api_key, text):
    """
    Function to get embeddings for given text using OpenAI API.
    """
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'model': "text-similarity-davinci-001",
        'inputs': text
    }
    try:
        response = requests.post('https://api.openai.com/v1/embeddings', json=data, headers=headers)
        if response.status_code == 200:
            return response.json()['data']
        else:
            print("Failed to retrieve embeddings:", response.status_code, response.text)
            return None
    except requests.RequestException as e:
        print(f"Request failed: {str(e)}")
        return None

def process_pdf_and_embed(file_path, api_key):
    """
    Function to process PDF, extract text, get embeddings, and return them.
    """
    try:
        with pdfplumber.open(file_path) as pdf:
            text_chunks = []
            embeddings = []
            for page in pdf.pages:
                text = page.extract_text() or ''
                chunks = text.split('\n\n')
                text_chunks.extend(chunks)
        
        for chunk in text_chunks:
            embedding = embed_text(api_key, chunk)
            if embedding:
                embeddings.append(embedding)
        return text_chunks, embeddings
    except Exception as e:
        print(f"Failed to open or process PDF {file_path}: {str(e)}")
        return [], []

def store_in_chroma(file_name, chunks, embeddings, db_path="chroma_db"):
    """
    Store chunks and embeddings in ChromaDB.
    """
    try:
        client = chromadb.PersistentClient(path=db_path)
        collection_name = os.path.splitext(os.path.basename(file_name))[0]
        collection = client.get_or_create_collection(collection_name)

        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            collection.add(
                ids=[f"{collection_name}chunk{i}"],
                metadatas=[{"source": file_name}],
                documents=[chunk],
                embeddings=[embedding]
            )
            print(f"Added chunk {i} to collection {collection_name}: {chunk[:50]}...")
    except Exception as e:
        print(f"Error storing chunk {i}: {e}")

def main():
    api_key = os.getenv('OPENAI_API_KEY', 'default_api_key_if_not_found')  # Fetch the API key securely
    pdf_path = 'C:\\Users\\mohan\\OneDrive\\Desktop\\pdfs\\your_pdf_file.pdf'  # Adjust this path
    chunks, embeddings = process_pdf_and_embed(pdf_path, api_key)
    if chunks and embeddings:
        store_in_chroma(pdf_path, chunks, embeddings)

if __name__ == '__main__':
    main()
