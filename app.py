import gradio as gr
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
import openai 
import json
from dotenv import load_dotenv
import os

load_dotenv()



print(f"Loadding API Key")
openai.api_key = os.getenv("OPENAI_API_KEY")
print("Data loading and index building...")
documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents=documents)
query_engine = index.as_query_engine()

# Function to handle queries
def query_document(message,history):
    response = query_engine.query(message)
    return str(response)

# # Gradio interface
# interface = gr.Interface(
#     fn=query_document,
#     inputs=gr.Textbox(label="Enter your query", placeholder="Type your question here..."),
#     outputs=gr.Textbox(label="Response"),
#     title="RAG Application Using llama",
#     description="Ask questions about the documents loaded into the system."
# )

interface = gr.ChatInterface(fn=query_document 
                 ,textbox=gr.Textbox(placeholder="Ask any information from DDS HR documents!")
                 ,title="DDS Document Bot", description="Ask about the DDS HR Policy!")

interface.launch(debug=True)

