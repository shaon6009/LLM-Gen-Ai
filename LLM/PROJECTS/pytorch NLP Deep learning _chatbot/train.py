import json

with open('G:\pytorch NLP Deep learning _chatbot\intents.json', 'r') as f:
    intents = json.load(f)
    
print(intents)