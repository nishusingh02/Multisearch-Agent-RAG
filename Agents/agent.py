from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
#from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun
from langchain.tools.retriever import create_retriever_tool
from langchain.agents import create_openai_tools_agent
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor
from langchain import hub
from dotenv import load_dotenv
import os

load_dotenv()  # Load variables from .env

api_key = os.getenv("OPENAI_API_KEY")
user_agent = os.getenv("WIKIPEDIA_USER_AGENT")


api_wrapper=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=200,user_agent=user_agent)
wiki=WikipediaQueryRun(api_wrapper=api_wrapper)

#print(wiki.name)

loader = WebBaseLoader("https://docs.smith.langchain.com/")
docs = loader.load()
documents = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200).split_documents(docs)
#embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
embeddings = OpenAIEmbeddings(openai_api_key=api_key)
vectordb = FAISS.from_documents(documents,embeddings)
retriever = vectordb.as_retriever()
#print(retriever)

retriever_tool=create_retriever_tool(retriever,"langsmith_search","Search for information about LangSmith. For any question about LangSmith, you must use this tool")

arxiv_wrapper=ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv=ArxivQueryRun(api_wrapper=arxiv_wrapper)
#print(arxiv.name)

tools=[wiki,arxiv,retriever_tool]
#print(tools)

llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)

prompt = hub.pull("hwchase17/openai-functions-agent")
#print(prompt.messages)

#agent
agent=create_openai_tools_agent(llm,tools,prompt)

agent_executor=AgentExecutor(agent=agent,tools=tools,verbose=True)

agent_executor.invoke({"input":"give archives of the research paper audio super resolution using cnn"})
