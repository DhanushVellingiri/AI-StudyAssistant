import faiss
import numpy as np
import os

def create_index(vectors):
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)
    return index

def load_index(path="data/index.faiss"):
    if not os.path.exists(path):
        return None
    return faiss.read_index(path)

def search_index(index, query_vector, k=3):
    distances, indices = index.search(query_vector, k)
    return indices

def save_index(index, path="data/index.faiss"):
    os.makedirs(os.path.dirname(path), exist_ok=True)  # <- creates the folder if missing
    faiss.write_index(index, path)
