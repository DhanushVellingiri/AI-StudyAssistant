from textwrap import wrap

def chunk_text(text, chunk_size=500):
    return wrap(text, width=chunk_size)
