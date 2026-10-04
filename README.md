# RAG with Reranking

Level: 7 — Intermediate & Advanced RAG

Skills: Python, overlap rank as a stand-in for a reranker

Passages are ranked by overlapping terms, a local stand-in for a cross-encoder.

```bash
pip install -r requirements.txt
pytest -q
```

This is a local laptop proof. It does not call a hosted model and it does not apply production changes.
