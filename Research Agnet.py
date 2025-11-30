from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate  
from langchain_core.output_parsers import StrOutputParser
from langchain_community.tools import DuckDuckGoSearchRun


model = ChatOllama(
    model="research-llm"
)

prompt = ChatPromptTemplate.from_template("""You are a helpful research AI. Use the following web search result: {context}. To write a concise, well-structured response to this question : {question}""")

parser = StrOutputParser()

search = DuckDuckGoSearchRun()


chain = prompt | model | parser

def generate_response(userText):
    context = search.invoke(f"Who is {userText}")

    response = chain.invoke({"question": f"Summarize information about {userText}", "context": context})
    return response

userInput = input("Who would you like to learn about today? \n type exit to leave\n\n")
while userInput.lower() != 'exit':
    aiResponse = generate_response(userInput)
    print(aiResponse + "\n")
    userInput = input("Who else do you want to learn about? *You can always type exit to leave*\n")
