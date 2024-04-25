'''from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model='llama3')

result = llm.invoke('Hello World!')
print(result)'''

import requests

url = "http://localhost:11434/api/chat"

def llama3(prompt):
    data = {
        "model": "llama3",
        "messages": [
            {
              "role": "user",
              "content": prompt
            }
        ],
        "stream": False
    }
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    return(response.json()['message']['content'])


response = llama3("Tell me a joke!")
print(response)