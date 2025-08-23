import google.generativeai as genai

API_KEY = "<Create API Key for your AI - https://aistudio.google.com/apikey>"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat()

print("Chat with Gemini AI! type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = chat.send_message(user_input)
    print("Gemini:", response.text)
