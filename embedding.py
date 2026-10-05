import numpy as np

def create_embeddings(words):
    embeddings = []

    for word in words:
        values = [ord(c) for c in word[:10]]

        while len(values) < 10:
            values.append(0)

        embeddings.append(values)

    return np.array(embeddings, dtype=float)