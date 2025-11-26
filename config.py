# CONFIGURATION

import os
import streamlit as st

# Get the parent folder's docs directory
DOCS_FOLDER = "docs" #os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs"))

VECTOR_DB_FILE = "vector.db"
EMBEDDINGS_CACHE = "embeddings_cache.pkl"
DOCS_CACHE = "docs_cache.pkl"
CONFIG_FILE = "rag_config.json"

CHUNK_SIZE = 1000  # Words per chunk (increased for better context)
TOP_K_RETRIEVAL = 5  # Number of chunks to retrieve (increased for more complete answers)
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
DEVICE = "cuda" if os.environ.get("CUDA_VISIBLE_DEVICES") else "cpu"

# GEMMA CONFIGURATION
# GEMMA_MODEL = "gemini-2.5-flash"
# GEMMA_MODEL = "gemini-flash-lite-latest"
GEMMA_MODEL = "gemma-3-27b-it"
API_KEY = st.secrets.get("API_KEY", "")
VERIFY_SSL = False
