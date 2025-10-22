#!/usr/bin/env python3
"""
Multiple Language Models with LangChain Demo

This script demonstrates how to use LangChain to work with different language models:
- OpenAI GPT models
- Anthropic Claude models  

Required environment variables:
- OPENAI_API_KEY: Your OpenAI API key
- ANTHROPIC_API_KEY: Your Anthropic API key

For Ollama models:
- Install Ollama from https://ollama.com/
- Run: ollama run llama3.2:1b (or your preferred model)
"""

import os

from anthropic import Anthropic
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_openai import AzureChatOpenAI
from openai import AzureOpenAI

# Load environment variables from .env file
load_dotenv(override=True)

# Pure OpenAI GPT model without LangChain
client = AzureOpenAI()
question = "Why is the sky blue?"
response = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": question}])
print(response.choices[0].message.content)

# Pure Anthropic Claude model without LangChain
api_key = os.getenv('ANTHROPIC_API_KEY')
client = Anthropic(api_key=api_key)

question = "Why is the sky blue?"
response = client.messages.create(model="claude-sonnet-4-20250514",  # Remember to update to current model
    max_tokens=1000, temperature=1, messages=[{"role": "user", "content": [{"type": "text", "text": question}]}])
print(response.content[0].text)

# OpenAI GPT model via LangChain
api_key = os.getenv('OPENAI_API_KEY')
llm = AzureChatOpenAI(model="gpt-4o-mini")
question = "Why is the sky blue?"
response = llm.invoke(question)
print(response.content)

# Claude model via LangChain
api_key = os.getenv('ANTHROPIC_API_KEY')
llm = ChatAnthropic(model="claude-3-5-sonnet-20241022", anthropic_api_key=api_key)
question = "Why is the sky blue?"
response = llm.invoke(question)
print(response.content)

# Do it Yourself: test ollama models via LangChain

from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM

template = """Question: {question}
Answer: Let's think step by step."""
prompt = ChatPromptTemplate.from_template(template)
model = OllamaLLM(model="llama3.1")
chain = prompt | model
output = chain.invoke({"question": "What is LangChain?"})
print(output)

llm = OllamaLLM(model="gemma3:270m")
response = model.invoke(question)
print(response)
