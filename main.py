from modules import Interface, parser, embedder, vector, utils
import numpy as np

def process_pdf(file_path):
    raw_text = parser.extract_text_from_pdf(file_path)
    chunks = utils.chunk_text(raw_text)
    embeddings = embedder.get_embeddings(chunks)
    index = vector.create_index(np.array(embeddings))
    vector.save_index(index)
    return chunks, index

def query_notes(user_question, chunks, index):
    question_vec = embedder.get_embeddings([user_question])
    relevant_idxs = vector.search_index(index, np.array(question_vec))[0]
    context = "\n".join([chunks[i] for i in relevant_idxs])
    prompt = f"Answer based on notes:\n{context}\n\nQuestion: {user_question}"
    return Interface.ask_llama(prompt)
