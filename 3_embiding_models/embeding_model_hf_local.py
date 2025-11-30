from langchain_huggingface import HuggingFaceEmbeddings

embiding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')


text = "SUNDER IS THE CEO OF GOOGLE"

vector =  embiding.embed_query(text)

print(str(vector))