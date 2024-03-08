import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from prompts import story_prompt
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-pro")

tweet_chain = LLMChain(llm=llm, prompt=story_prompt, verbose=True)

if __name__ == "__main__":
    character_name = "John"
    topic = "give me a story about John stuck in a mystery relating to his parent's occupation"
    prompt = {"character_name": character_name,
              "genre": topic}
    resp = tweet_chain.invoke(prompt)
    print(resp)

