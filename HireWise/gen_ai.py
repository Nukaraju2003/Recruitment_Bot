import genai

# Replace with your API key
api_key = "YOUR_API_KEY"

# Configure the API key
genai.configure(api_key=api_key)

# Select the Gemini model (choose "text-davinci-003" for best results)
model_name = "text-davinci-003"

def chat(user_input):
    prompt = f"You: {user_input}\nAgent:"
    response = genai.text_generation(
        model_name=model_name,
        prompt=prompt,
        max_tokens=100  # Adjust for longer responses
    )
    return response.generated_text[0].strip()

# Chat loop
while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    agent_response = chat(user_input)
    print(agent_response)
