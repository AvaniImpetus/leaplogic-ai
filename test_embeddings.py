"""
Test script to verify embeddings and vector database are working correctly
"""

import sqlite3

import config
import utilities as utils
from embedding_manager import EmbeddingManager


def test_embeddings():
    """Test embedding generation and storage"""
    print("=" * 60)
    print("Testing Embedding System")
    print("=" * 60)

    # Initialize embedding manager
    print("\n1. Loading embedding model...")
    try:
        embedding_manager = EmbeddingManager()
        print("✓ Embedding model loaded successfully")
    except Exception as e:
        print(f"✗ Error loading embedding model: {e}")
        return

    # Test encoding
    print("\n2. Testing text encoding...")
    test_texts = [
        "This is a test document about AWS S3",
        "Gemma is an AI language model",
        "Vector databases store embeddings efficiently"
    ]

    try:
        embeddings = embedding_manager.encode(test_texts)
        print(f"✓ Successfully encoded {len(test_texts)} texts")
        print(f"  Embedding shape: {embeddings.shape}")
        print(f"  Embedding dimension: {embeddings.shape[1]}")
    except Exception as e:
        print(f"✗ Error encoding texts: {e}")
        return

    # Check vector database
    print("\n3. Checking vector database...")
    try:
        conn = sqlite3.connect(config.VECTOR_DB_FILE)
        cursor = conn.cursor()

        # Check documents
        cursor.execute("SELECT COUNT(*) FROM documents")
        doc_count = cursor.fetchone()[0]
        print(f"✓ Documents in database: {doc_count}")

        # Check chunks
        cursor.execute("SELECT COUNT(*) FROM chunks")
        chunk_count = cursor.fetchone()[0]
        print(f"✓ Chunks in database: {chunk_count}")

        # Sample a chunk and verify embedding
        if chunk_count > 0:
            print("\n4. Testing chunk retrieval and embedding conversion...")
            cursor.execute("""
                SELECT c.chunk_content, c.embedding, c.embedding_dim
                FROM chunks c
                LIMIT 1
            """)
            result = cursor.fetchone()
            if result:
                chunk_content, embedding_blob, embedding_dim = result
                print(f"✓ Retrieved sample chunk: {chunk_content[:50]}...")

                # Convert blob back to embedding
                try:
                    embedding = utils.blob_to_embedding(embedding_blob, embedding_dim)
                    print(f"✓ Successfully converted embedding blob")
                    print(f"  Embedding shape: {embedding.shape}")
                    print(f"  Expected dimension: {embedding_dim}")

                    if embedding.shape[1] == embedding_dim:
                        print(f"✓ Embedding dimension matches!")
                    else:
                        print(f"✗ Dimension mismatch: {embedding.shape[1]} != {embedding_dim}")
                except Exception as e:
                    print(f"✗ Error converting embedding: {e}")

        conn.close()
    except Exception as e:
        print(f"✗ Error accessing vector database: {e}")
        return

    print("\n" + "=" * 60)
    print("✓ Embedding system test completed!")
    print("=" * 60)


if __name__ == "__main__":
    test_embeddings()
