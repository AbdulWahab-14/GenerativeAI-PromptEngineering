"""
Week 4 Task: Multi-Agent Basics — Two AIs Working Together
Orchestration Strategy: Sequential 2-Agent Chain (Writer -> Editor/Critic)
"""

import json

# ---------------------------------------------------------------------------
# AGENT SYSTEM PROMPTS & PERSONAS
# ---------------------------------------------------------------------------

WRITER_SYSTEM_PROMPT = """
You are "Agent 1: Technical Content Writer".
Your goal is to draft a short, informative 3-paragraph explanation on a given topic for a developer audience.

Structure your draft as follows:
- Paragraph 1: Overview & Core Concept
- Paragraph 2: Technical Inner Workings / Key Mechanics
- Paragraph 3: Real-World Use Case or Value Proposition

Tone: Professional, informative, but slightly conversational.
Constraint: Do NOT worry about strict grammar polish or formatting perfection—focus on getting raw technical concepts onto paper.
"""

EDITOR_SYSTEM_PROMPT = """
You are "Agent 2: Senior Editorial Critic".
Your task is to review and refine the raw draft written by Agent 1.

Your Editorial Responsibilities:
1. Technical Precision: Fix vague generalities or minor technical oversights.
2. Structure & Clarity: Improve flow, transition words, and paragraph scannability using Markdown bolding/bullets where appropriate.
3. Concise Polish: Eliminate filler words and tighten prose without losing depth.
4. Editorial Feedback: Provide a concise summary of what you changed and WHY it improves the draft.

Output Format:
### 1. Refined Final Output
[Your polished, publication-ready version]

### 2. Editorial Improvements Log
- [Fix 1]: Reason for change
- [Fix 2]: Reason for change
- [Fix 3]: Reason for change
"""

# ---------------------------------------------------------------------------
# MOCK LLM SIMULATOR FOR TEST EXECUTION & PIPELINE VERIFICATION
# ---------------------------------------------------------------------------

TOPICS = [
    "Retrieval-Augmented Generation (RAG) in Enterprise Search",
    "Autonomous Mobile Robot (AMR) Pathfinding with A* and Occupancy Grids"
]

MOCK_WRITER_OUTPUTS = [
    """Retrieval-Augmented Generation or RAG is basically when you combine a search system with an LLM so it doesn't hallucinate. Instead of relying only on pre-trained weights, RAG lets the model pull up fresh data from a database or company documents before it generates a response.

Under the hood, documents are turned into embeddings using a vector database like Pinecone or Milvus. When a user asks something, the system vectorizes the question, finds the top most similar document chunks using cosine similarity, and passes those chunks into the LLM prompt context window.

This is super useful for enterprise internal search where company policies change constantly. You don't have to re-train or fine-tune models every week, saving thousands of dollars in compute while keeping answers grounded in factual internal data.""",

    """Autonomous mobile robots need to navigate environments without bumping into walls or dynamic obstacles. They do this by mapping the room into an occupancy grid, which is a 2D matrix where each cell represents free space, an obstacle, or unknown area usually generated from LiDAR data.

To move from point A to point B, the robot uses the A* search algorithm. A* evaluates nodes using the formula f(n) = g(n) + h(n), where g(n) is the actual movement cost from the start, and h(n) is the heuristic distance to the goal like Euclidean or Manhattan distance. It continuously expands the lowest-cost nodes first.

This pathfinding approach is essential for warehouse robots moving inventory around fulfillment centers. By re-planning dynamically when LiDAR detects a human worker, the robot safely navigates around unexpected obstacles while staying on the optimal route."""
]

MOCK_EDITOR_OUTPUTS = [
    """### 1. Refined Final Output
**Retrieval-Augmented Generation (RAG)** bridges the gap between static Large Language Models (LLMs) and real-time enterprise knowledge base retrieval. Rather than relying solely on frozen parametric memory—which leads to hallucinations—RAG dynamically retrieves authoritative external data during inference to ground the LLM's responses.

**Technical Architecture & Workflow:**
* **Vectorization:** Unstructured documents are broken into chunks and embedded into high-dimensional vector spaces stored in specialized databases (e.g., Pinecone, Milvus, Qdrant).
* **Semantic Retrieval:** User queries are embedded on the fly; nearest-neighbor algorithms compute cosine similarity to extract the top-$k$ most contextually relevant chunks.
* **Contextual Prompting:** Retrieved passages are injected directly into the LLM's prompt window alongside the user query as reference context.

**Value Proposition:**
RAG is vital for enterprise search systems. By decoupling knowledge retrieval from model parameters, organizations eliminate costly weekly model fine-tuning while enforcing strict data freshness and auditability.

### 2. Editorial Improvements Log
- **Precision Enhancement:** Replaced vague language ("pull up fresh data") with precise terminology (*parametric memory*, *nearest-neighbor algorithms*, *inference grounding*).
- **Structural Upgrade:** Transformed raw paragraph 2 into structured bullet points (*Vectorization*, *Semantic Retrieval*, *Contextual Prompting*) for immediate scannability.
- **Tone Polish:** Elevated conversational phrasing ("super useful", "saving thousands") into a professional, enterprise engineering tone.""",

    """### 1. Refined Final Output
**Autonomous Mobile Robots (AMRs)** rely on spatial mapping and algorithmic path planning to navigate complex environments safely. Environment geometry is digitized into a **2D Occupancy Grid**—a discrete spatial matrix built from real-time LiDAR point clouds where matrix cells classify space as *occupied*, *free*, or *unexplored*.

**Algorithmic Mechanics (A* Pathfinding):**
To compute optimal trajectory routes from origin to goal, AMRs execute the **A* Search Algorithm**, which evaluates candidate grid nodes via the cost function:
$$f(n) = g(n) + h(n)$$
* **$g(n)$:** Exact path cost accumulated from start node to current node $n$.
* **$h(n)$:** Admissible heuristic estimate (e.g., Euclidean or Manhattan distance) from $n$ to the goal.

By priority-queuing candidate paths based on the lowest total estimated cost $f(n)$, the planner minimizes search space expansion.

**Industrial Application:**
This architecture underpins modern warehouse automation. When onboard LiDAR detects dynamic obstacles (such as human operators or forklifts), the local planner recalculates grid costs and triggers real-time dynamic re-routing without interrupting overall mission flow.

### 2. Editorial Improvements Log
- **Formatting Improvements:** Added mathematical notation ($f(n) = g(n) + h(n)$) to make the algorithm breakdown clearer.
- **Clarity & Depth:** Explicitly detailed how occupancy grid cell classifications (*free*, *occupied*, *unexplored*) interface with LiDAR point clouds.
- **Industrial Context:** Replaced general phrasing ("bumping into walls") with domain terms (*dynamic re-routing*, *local planner*, *mission flow*)."""
]

# ---------------------------------------------------------------------------
# PIPELINE EXECUTION
# ---------------------------------------------------------------------------

def run_multi_agent_pipeline():
    print("=" * 70)
    print("      WEEK 4: MULTI-AGENT ORCHESTRATION PIPELINE (WRITER -> EDITOR)")
    print("=" * 70 + "\n")

    for idx, (topic, raw_draft, edited_output) in enumerate(zip(TOPICS, MOCK_WRITER_OUTPUTS, MOCK_EDITOR_OUTPUTS), 1):
        print(f"======================================================================")
        print(f" TOPIC {idx}: {topic.upper()}")
        print(f"======================================================================\n")

        print("--- [AGENT 1: WRITER] RAW DRAFT ---")
        print(raw_draft.strip())
        print("\n" + "-" * 70 + "\n")

        print("--- [AGENT 2: EDITOR] REFINED OUTPUT & CRITIQUE ---")
        print(edited_output.strip())
        print("\n" + "=" * 70 + "\n\n")

if __name__ == "__main__":
    run_multi_agent_pipeline()
