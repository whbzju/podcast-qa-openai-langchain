"""Ask a question to the podcast database."""
import faiss
from langchain import OpenAI
from langchain.chains import VectorDBQAWithSourcesChain
from langchain.chains import VectorDBQA
import pickle
import argparse

parser = argparse.ArgumentParser(description='Ask a question to the podcast DB.')
parser.add_argument('question', type=str, help='The question to ask the podcast DB')
args = parser.parse_args()

# Load the LangChain.
index = faiss.read_index("docs.index")

with open("faiss_store.pkl", "rb") as f:
    store = pickle.load(f)

store.index = index
chain = VectorDBQAWithSourcesChain.from_llm(llm=OpenAI(temperature=0), vectorstore=store)
result = chain({"question": args.question})


#chain = VectorDBQA(llm=OpenAI(), vectorstore=store)
#result = chain({"query": args.question})
print(f"Answer: {result['answer']}")
print(f"Sources: {result['sources']}")
