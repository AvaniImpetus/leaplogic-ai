# ==============================
# SEMANTIC SEARCH & RETRIEVAL
# ==============================
import sqlite3
from typing import List, Tuple

import numpy as np

import config
import utilities as utils
from embedding_manager import EmbeddingManager


class SemanticSearcher:
    """Performs semantic search on the vector database"""

    def __init__(self, embedding_manager: EmbeddingManager):
        self.embedding_manager = embedding_manager

    def search(self, query: str, top_k: int = config.TOP_K_RETRIEVAL) -> List[Tuple[str, str, float]]:
        """
        Search for relevant chunks using semantic similarity
        Returns list of (chunk_content, file_name, similarity_score)
        """
        conn = sqlite3.connect(config.VECTOR_DB_FILE)
        cursor = conn.cursor()

        # Encode query
        query_embedding = self.embedding_manager.encode_single(query)

        # Retrieve all chunks
        cursor.execute("""
            SELECT c.id, c.chunk_content, d.file_name, c.embedding, c.embedding_dim
            FROM chunks c
            JOIN documents d ON c.doc_id = d.id
        """)

        results = cursor.fetchall()
        conn.close()

        if not results:
            return []

        # Calculate similarity scores using cosine similarity
        similarities = []
        for chunk_id, chunk_content, file_name, embedding_blob, embedding_dim in results:
            chunk_embedding = utils.blob_to_embedding(embedding_blob, embedding_dim)

            # Flatten embeddings to 1D for dot product
            query_flat = query_embedding.flatten()
            chunk_flat = chunk_embedding.flatten()

            # Cosine similarity
            dot_product = np.dot(query_flat, chunk_flat)
            norm_query = np.linalg.norm(query_flat)
            norm_chunk = np.linalg.norm(chunk_flat)

            similarity = dot_product / (norm_query * norm_chunk + 1e-10)
            similarities.append((chunk_content, file_name, float(similarity)))

        # Sort by similarity and return top-k
        similarities.sort(key=lambda x: x[2], reverse=True)
        if len(similarities) < top_k:
            top_k = len(similarities)
        return similarities[:top_k]
