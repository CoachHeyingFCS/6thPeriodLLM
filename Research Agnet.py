from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate  
from langchain_core.output_parsers import StrOutputParser
from langchain_community.tools import DuckDuckGoSearchRun


model = ChatOllama(
    model="research-llm"
)

prompt = ChatPromptTemplate.from_template("""You are a helpful research AI. bUse the following web search result {question}. Web search result: {context}. Write a concise, well-structured response""")

parser = StrOutputParser()

search = DuckDuckGoSearchRun()


chain = prompt | model | parser

def generate_response(userText):
    context = search.invoke(f"Who is {userText}")

    response = chain.invoke({"question": f"Summarize information about {userText}", "context": context})
    return response

userInput = input("You are tracking the villains who stole the princess. You see a bridge. After looking closely, see signs of a troll living under the bridge. In your quest to find the princess, you wonder if he has any information. Trolls are notoriously unfriendly, so you must be careful with your words. What do you say to the troll?\n\n")
while userInput.lower() != 'walk away':
    aiResponse = generate_response(userInput)
    print(aiResponse + "\n")
    userInput = input("How do you respond? *You can always walk away*\n")
