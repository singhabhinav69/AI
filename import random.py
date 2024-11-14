import random

# Define a dictionary of user inputs and corresponding bot responses
responses = {
    "hello": ["Hi there!", "Hello! How can I help you?", "Hey! What's up?"],
    "how are you": ["I'm doing great, thanks for asking!", "I'm just a bot, but I'm functioning well!", "I'm doing awesome! How about you?"],
    "bye": ["Goodbye! Have a nice day!", "Bye! Come back anytime.", "See you later!"],
    "help": ["How can I assist you?", "What do you need help with?", "I can help you with anything you need."],
    "default": ["Sorry, I didn't quite understand that.", "Can you please rephrase?", "I'm not sure how to respond to that."]
}

# Function to process user input
def chatbot_response(user_input):
    # Normalize the input (convert to lowercase for easier matching)
    user_input = user_input.lower()
    
    # Search for the input in the responses dictionary
    for key in responses:
        if key in user_input:
            # Return a random response from the list of possible responses
            return random.choice(responses[key])
    
    # If no match, return a default response
    return random.choice(responses["default"])

# Main chatbot loop
def chat():
    print("Chatbot: Hello! How can I help you today?")
    
    while True:
        user_input = input("You: ")
        
        # Exit condition
        if "bye" in user_input.lower():
            print("Chatbot: Goodbye!")
            break
        
        # Get chatbot's response based on user input
        response = chatbot_response(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
chat()
