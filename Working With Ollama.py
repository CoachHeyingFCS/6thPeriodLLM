from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate  
from langchain_core.output_parsers import StrOutputParser
from langchain_community.tools import DuckDuckGoSearchRun


model = ChatOllama(
    model="tiny"
)

prompt = ChatPromptTemplate.from_template("""Use the following web search result to answer the user's statement. Web search result: {context} User prompt: {question} Write a concise, well-structured response as a cranky, knowlegable troll""")

parser = StrOutputParser()

search = DuckDuckGoSearchRun()


chain = prompt | model | parser

def generate_response(userText):
   context = search.invoke("What is a troll?")

   response = chain.invoke({"question": userText, "context": context})
   return response

userInput = input("You are tracking the villains who stole the princess. You see a bridge. After looking closely, see signs of a troll living under the bridge. In your quest to find the princess, you wonder if he has any information. Trolls are notoriously unfriendly, so you must be careful with your words. What do you say to the troll?\n\n")
while userInput.lower() != 'walk away':
    aiResponse = generate_response(userInput)
    print(aiResponse + "\n")
    userInput = input("How do you respond? *You can always walk away*\n")
