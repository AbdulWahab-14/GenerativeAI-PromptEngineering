"""
RAG Mini-Project: Hybrid RAG Pipeline Demonstration
Domain: Autonomous Robot Navigation Project Specs
Concepts: Text Chunking, Context Retrieval, Prompt Grounding, & Boundary Checks
"""

# Project Document Source Text
DOCUMENT_SOURCE = [
    "Perception & Mapping: Simulated 2D LiDAR point-cloud processing builds a real-time 2D Occupancy Grid Map.",
    "Global Path Planning: Route generation relies on A* (A-Star) and Dijkstra pathfinding algorithms over grid maps.",
    "Dynamic Obstacle Avoidance: Local planner continuously updates local costmaps using real-time LiDAR distance vectors.",
    "Simulation Engine: System physics and kinematics are executed in Python utilizing the PyBullet physics engine.",
    "System Constraints: Designed for 2D planar mobile robot platforms with differential drive kinematics."
]

def retrieve_context(query: str, doc_chunks: list) -> tuple:
    """Simulates semantic chunk retrieval from vector store."""
    query_keywords = set(query.lower().replace("?", "").replace(",", "").split())
    retrieved_chunks = []
    
    for chunk in doc_chunks:
        chunk_words = set(chunk.lower().split())
        # Measure keyword overlap relevance score
        if len(query_keywords.intersection(chunk_words)) > 0:
            retrieved_chunks.append(chunk)
            
    return retrieved_chunks

def rag_query_engine(query: str, doc_chunks: list) -> str:
    """Grounds prompt context and enforces retrieval boundary safety."""
    chunks = retrieve_context(query, doc_chunks)
    
    print(f"\n" + "="*60)
    print(f"USER QUERY: {query}")
    print("-" * 60)
    
    if not chunks:
        print("[RETRIEVAL STATUS]: NO RELEVANT CHUNKS FOUND")
        return "RESPONSE: The requested information is NOT present in the project document (Boundary Limit Enforced)."
    
    print(f"[RETRIEVAL STATUS]: {len(chunks)} Chunk(s) Retrived:")
    for i, c in enumerate(chunks, 1):
        print(f"  Chunk {i}: {c}")
        
    return f"RESPONSE (Grounded): Based on the retrieved specification: {' '.join(chunks)}"

if __name__ == "__main__":
    print("=== HYBRID RAG ENGINE PIPELINE DEMO ===")
    
    test_queries = [
        "What path planning algorithms are used?",
        "How is obstacle avoidance handled?",
        "What camera hardware model is used for depth perception?" # Hallucination boundary test
    ]
    
    for q in test_queries:
        output = rag_query_engine(q, DOCUMENT_SOURCE)
        print(output)
        print("="*60)
