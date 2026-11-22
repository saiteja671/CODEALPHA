def chatbot_response(user_input):

    user_input = user_input.lower()

    
    if user_input == "hello":
        return "Hi!"

    elif user_input == "how are you":
        return "I'm fine, thanks!"

    elif user_input == "what is your name":
        return "I am a Python chatbot."

    elif user_input == "good morning":
        return "Good morning! Have a nice day!"

    elif user_input == "thank you":
        return "You're welcome!"

    elif user_input == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand."


print("Welcome to Basic Chatbot!")
print("Type 'bye' to exit.")


while True:

    user_input = input("You: ")

    response = chatbot_response(user_input)

    print("Chatbot:", response)

    if user_input.lower() == "bye":
        break
