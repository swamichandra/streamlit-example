import openai
import tiktoken
import pincone
import os
import re
import requests
import urllib.request
from bs4 import BeautifulSoup
from collections import deque
from html.parser import HTMLParser
from urllib.parse import urlparse
from IPython.display import Markdown


OPENAI_API_KEY = "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"
PINECONE_API_KEY = '7794ea9f-20d7-4bc2-9519-c5798db3f6d5'
PINECONE_API_ENV = 'us-central1-gcp'

# initialize pinecone
pinecone.init(
    api_key=PINECONE_API_KEY,  # find at app.pinecone.io
    environment=PINECONE_API_ENV  
)
index_name = "langchainswami"

from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain

llm = OpenAI(temperature=0, openai_api_key=OPENAI_API_KEY)
chain = load_qa_chain(llm, chain_type="stuff")

query = "What will happen when there is a failure to achieve book speeds?"
docs = docsearch.similarity_search(query, include_metadata=True)

chain.run(input_documents=docs, question=query)