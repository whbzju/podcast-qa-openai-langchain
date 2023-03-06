# podcast-qa-openai-langchain

It's amazing what ChatGPT has done for me! This project was created with the help of ChatGPT with the aim of transcribing the podcast [Gradient Dissent](https://podcasts.google.com/feed/aHR0cHM6Ly9mZWVkcy5jYXB0aXZhdGUuZm0vZ3JhZGllbnQtZGlzc2VudC8?sa=X&ved=2ahUKEwielruquML9AhUmhY4IHeKPDhgQ9sEGegQIARAG) to text. We used OpenAI embedding API and Langchain to build a podcast vector database for QA.

90% of the code in this project was created by ChatGPT, including scape.py, segment.py, scrape_url_title.py, and transcribe.py. We referred to the repository [notion qa](https://github.com/hwchase17/notion-qa) for ingest.py and qa.py. If ChatGPT updates its training data to the current version, I believe it can finish the remaining code for me. 

```
bash
python scrape_url_title.py
python segment.py
python transcribe.py
python ingest.py
python qa.py "how can I be a good deep learning researcher"

```

It's been so much fun coding with ChatGPT!

PS: The README was rewrited by ChatGPT.