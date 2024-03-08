import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


def get_gemini_pro_text_response(prompt, prompt_dict, config):
    llm = ChatGoogleGenerativeAI(model="gemini-pro",
                                 temperature=config["temperature"],
                                 max_output_tokens=config["max_output_tokens"])
    print(prompt)
    chain = LLMChain(llm=llm, prompt=prompt, verbose=True)

    response = chain.invoke(prompt_dict)
    return response["text"]


st.write("Using Gemini 1.0 Pro - Text only model")
st.header("Story Writing App")
st.subheader("Generate a story")

character_name = st.text_input(
    "Enter character name: \n\n", key="character_name", value="Mittens"
)
character_type = st.text_input(
    "What type of character is it? \n\n", key="character_type", value="Cat"
)
character_persona = st.text_input(
    "What personality does the character have? \n\n",
    key="character_persona",
    value="Mitten is a very friendly cat.",
)
character_location = st.text_input(
    "Where does the character live? \n\n",
    key="character_location",
    value="Andromeda Galaxy",
)
story_premise = st.multiselect(
    "What is the story premise? (can select multiple) \n\n",
    [
        "Love",
        "Adventure",
        "Mystery",
        "Horror",
        "Comedy",
        "Sci-Fi",
        "Fantasy",
        "Thriller",
    ],
    key="story_premise",
    default=["Love", "Adventure"],
)
creative_control = st.radio(
    "Select the creativity level: \n\n",
    ["Low", "High"],
    key="creative_control",
    horizontal=True,
)
length_of_story = st.radio(
    "Select the length of the story: \n\n",
    ["Short", "Long"],
    key="length_of_story",
    horizontal=True,
)

if creative_control == "Low":
    temperature = 0.30
else:
    temperature = 0.95

if length_of_story == "Short":
    max_output_tokens = 1000
else:
    temperature = 2048

story_template = """Write a {length_of_story} story based on the following premise: \n
character_name: {character_name} \n
character_type: {character_type} \n
character_persona: {character_persona} \n
character_location: {character_location} \n
story_premise: {story_premise} \n
If the story is "short", then make sure to have 5 chapters or else if it is "long" then 10 chapters.
Important point is that each chapters should be generated based on the premise given above.
First start by giving the book introduction, chapter introductions and then each chapter. It should also have a 
proper ending.
The book should have prologue and epilogue.
"""

story_prompt = PromptTemplate(
    input_variables=["length_of_story", "character_name", "character_type", "character_persona", "character_location",
                     "story_premise"],
    template=story_template
)
config = {
    "temperature": temperature,
    "max_output_tokens": max_output_tokens,
}
# # format the prompt to add variable values
prompt_formatted = {
    "length_of_story": length_of_story,
    "character_name": character_name,
    "character_type": character_type,
    "character_persona": character_persona,
    "character_location": character_location,
    "story_premise": story_premise
}

generate_t2t = st.button("Generate my story", key="generate_t2t")
if generate_t2t and story_prompt:
    with st.spinner("Generating your story using Gemini 1.0 Pro ..."):
        first_tab1, first_tab2 = st.tabs(["Story", "Prompt"])
        with first_tab1:
            print(story_prompt)
            response = get_gemini_pro_text_response(story_prompt, prompt_formatted, config)
            if response:
                st.write("Your story:")
                st.write(response)
        with first_tab2:
            st.text(story_prompt)
