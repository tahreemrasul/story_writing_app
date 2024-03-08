from langchain.prompts import PromptTemplate

story_template = """Write a 2 paragraph story based on the following premise about character name {character_name} in
genre {genre}"""

story_prompt = PromptTemplate(
    input_variables=["character_name", "genre"],
    template=story_template
)