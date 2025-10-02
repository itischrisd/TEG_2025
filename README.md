# GenAI Course 2025

A comprehensive course on Generative AI—from foundational concepts to advanced implementations with RAG, agents, and workflows.

[YouTube Playlist](https://www.youtube.com/playlist?list=PLOiItT5FLNRqp8sK9t-Hi2xRjZgg1SE44)

---

## 📚 Course Materials

### 1. Introduction
**Lectures:** 
- [Course Introduction (03:33)](https://www.youtube.com/watch?v=46FcfsccTyk)
- [How GenAI Works? (26:38)](https://youtu.be/q-As4OK1f5E)

**Demo**:

[First Interaction with the LLM (20:53)](https://youtu.be/xwz0UPodgHY)
[Your First Chatbot App (06:10)(https://youtu.be/C9ireExNgvU?si=3vRY_Sv43WGmaa8a)

**Slides:** [slides/1. Intro](https://github.com/wodecki/TEG_2025/blob/main/slides/1.%20Intro)

**Code:** [src/1. Intro](https://github.com/wodecki/TEG_2025/tree/main/src/1.%20Intro)

---

### 2. Tokenization, Embeddings, and Transformers
**Lectures:** 
- [Tokenization (6:14)](https://youtu.be/mltPLwiCPZM)
- [Embeddings (23:54)](https://youtu.be/P2DnCGjcukA)
- [Transformers - attention (49:36)](https://youtu.be/8iarkQsyzbw)
- [Transformers - Multi-Layer Perceptron (15:38)](https://youtu.be/hpQcTglAByo)
- [Transformers - Prediction (13:55)](https://youtu.be/4pRkJuKTaR0)

**Demo:**
- [Embeddings (17:38)](https://youtu.be/zkfbIZlD89M)

**Slides:** [slides/2. Transformers](https://github.com/wodecki/TEG_2025/blob/main/slides/2.%20Transformers)

**Code:** [src/2. Models](https://github.com/wodecki/TEG_2025/tree/main/src/2.%20Models)

---

### 3. Retrieval Augmented Generation (RAG)
**Lectures:** 
- [RAG - foundations (21:41)](https://youtu.be/xtctSETgUgM)
- [RAG - evaluation (17:59)](https://youtu.be/MiTLJKbO1Q8)

**Demo:** [Placeholder - Will appear here soon]

**Slides:** [slides/3. Retrieval Augmented Generation](https://github.com/wodecki/TEG_2025/blob/main/slides/3.%20Retrieval%20Augmented%20Generation)

**Code:** [src/3. Retrieval Augmented Generation](https://github.com/wodecki/TEG_2025/tree/main/src/3.%20Retrieval%20Augmented%20Generation)

---

### 4. Graphs
**Lectures:** [Placeholder - Will appear here soon]

**Demo:** [Placeholder - Will appear here soon]

**Slides:** [slides/4. Graphs](https://github.com/wodecki/TEG_2025/blob/main/slides/4.%20Graphs)

**Code:** [src/4. Graphs](https://github.com/wodecki/TEG_2025/tree/main/src/4.%20Graphs)

---

### 5. Tools and Agents
**Lectures:** [Placeholder - Will appear here soon]

**Demo:** [Placeholder - Will appear here soon]

**Slides:** [slides/5. Tools and Agents](https://github.com/wodecki/TEG_2025/blob/main/slides/5.%20Tools%20and%20Agents)

**Code:** [src/5. Tools and Agents](https://github.com/wodecki/TEG_2025/tree/main/src/5.%20Tools%20and%20Agents)

---

### 6. Model Context Protocol (MCP)
**Lectures:** [Placeholder - Will appear here soon]
**Demo:** [Placeholder - Will appear here soon]

**Slides:** [slides/6. MCP](https://github.com/wodecki/TEG_2025/blob/main/slides/6.%20MCP)

**Code:** [src/6. MCP](https://github.com/wodecki/TEG_2025/tree/main/src/6.%20MCP)

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+ (3.11+ recommended)
- [uv](https://github.com/astral-sh/uv) package manager

### Installation

1. **Install uv:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. **Clone the repository:**
```bash
git clone https://github.com/wodecki/TEG_2025.git
cd TEG_2025
```

3. **Install dependencies:**
```bash
uv sync
```

4. **Set up API keys:**
Create `.env` files in relevant module directories:
```bash
cd "src/3. Retrieval Augmented Generation"
echo "OPENAI_API_KEY=your_key_here" > .env
```

### Required API Keys
- `OPENAI_API_KEY` - Most modules
- `ANTHROPIC_API_KEY` - Claude examples
- `TAVILY_API_KEY` - Web search (optional)

---

## 📝 License

Educational purposes only.
