from langchain_huggingface import HuggingFaceEmbeddings

embiding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')


docs = ["SUNDER IS THE CEO OF GOOGLE", "Delhi is the capital of india", "khamanduis the capital of nepal"]

vector =  embiding.embed_documents(docs)

print(str(vector))