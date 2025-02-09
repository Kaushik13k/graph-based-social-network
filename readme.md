# Decentralized Social Network with AI-Driven Graph Recommendations

## Overview
This project is a fully decentralized social networking platform built entirely from scratch using graph algorithms. The backend logic, recommendations, ranking, and clustering are all implemented without using any backend libraries (except for the database).

## Contents
| Feature              | Approach                            |
|----------------------|----------------------------------|
| Data Storage       | Custom Graph DB (Adjacency List) |
| Friend Suggestions | Graph Traversal (BFS/DFS)      |
| Trending Topic     | Custom PageRank on Graph       |
| Personalized Feed  | Graph-Based Collaborative Filtering |
| Messaging         | Graph Routing (Dijkstra)       |
| AI Recommendations | Graph Neural Networks         |

## Project Structure
```
.
├── app
│   ├── __init__.py
│   ├── configs
│   │   └── __init__.py
│   ├── constants
│   │   ├── __init__.py
│   │   └── envs.py
│   ├── exceptions
│   │   └── exceptions.py
│   ├── graph
│   │   ├── __init__.py
│   │   ├── algorithm
│   │   │   ├── __init__.py
│   │   │   ├── ranking
│   │   │   │   ├── __init__.py
│   │   │   │   ├── base.py
│   │   │   │   ├── hits.py
│   │   │   │   ├── pagerank.py
│   │   │   │   └── ranking_factory.py
│   │   │   ├── recommendation
│   │   │   │   ├── __init__.py
│   │   │   │   ├── base.py
│   │   │   │   ├── jaccard.py
│   │   │   │   └── recommendation_factory.py
│   │   │   └── traversal
│   │   │       ├── __init__.py
│   │   │       ├── base.py
│   │   │       ├── bfs.py
│   │   │       ├── dfs.py
│   │   │       ├── dijkstra.py
│   │   │       └── traversal_factory.py
│   │   ├── core
│   │   │   ├── __init__.py
│   │   │   ├── graph.py
│   │   │   ├── graph_factory.py
│   │   │   └── observer.py
│   │   ├── exceptions
│   │   │   ├── __init__.py
│   │   │   └── exceptions.py
│   │   └── models
│   │       ├── __init__.py
│   │       ├── edge.py
│   │       └── node.py
│   ├── main.py
│   ├── models
│   │   └── __init__.py
│   ├── routers
│   │   ├── __init__.py
│   │   └── health.py
│   ├── schemas
│   │   └── __init__.py
│   ├── services
│   │   └── __init__.py
│   └── utils
│       └── __init__.py
├── notebook
│   └── test.ipynb
├── readme.md
├── requirements.txt
└── tests
    ├── __init__.py
    └── test_graph
        ├── __init__.py
        ├── test_egde.py
        ├── test_graph.py
        └── test_node.py
```


### Explanation:
- **`graph/algorithm/`**: Contains various graph algorithms.
  - **`ranking/`**: Implements ranking methods like PageRank and HITS.
  - **`recommendation/`**: Implements recommendation algorithms such as Jaccard similarity.
  - **`traversal/`**: Implements graph traversal techniques like BFS, DFS, and Dijkstra.
- **`graph/core/`**: Core graph implementation, including the graph structure, factories, and observer pattern.
- **`graph/exceptions/`**: Handles custom exceptions for graph operations.
- **`graph/models/`**: Defines graph components such as `Node` and `Edge`.
- **`main.py`**: Entry point of the project.

## Implementation Plan
The project is being implemented step-by-step:
1. **Graph Data Structure Implementation** ✅ *(In Progress)*
2. **Basic User & Connections Graph** (Upcoming)
3. **Graph-Based Recommendations** (Upcoming)
4. **AI-Driven Features using GNN** (Upcoming)
5. **Cloud Deployment** (Upcoming)

## Tech Stack
- **Backend**: Custom implementation (No backend frameworks)
- **Database**: To be decided
- **Machine Learning**: Custom Graph Neural Network (GNN)
- **Deployment**: Cloud

## Getting Started
1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd decentralized-social-network
