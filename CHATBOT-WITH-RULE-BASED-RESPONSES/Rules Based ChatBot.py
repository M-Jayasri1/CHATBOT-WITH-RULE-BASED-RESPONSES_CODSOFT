def chatbot():
    print("Bot: Hello! How can I help you today?")
    while True:
        user_input = input("You: ").lower()

        if "hello" in user_input or "hi" in user_input:
            print("Bot: Hi there! How can I assist you?")
        elif "your name" in user_input:
            print("Bot: I'm a rule-based chatbot created as part of a CODSOFT internship task by Jayasri.")
        elif "help" in user_input:
            print("Bot: Sure, I'm here to help. yourPlease ask your question.")
        elif "bye" in user_input or "exit" in user_input:
            print("Bot: Goodbye! Have a great day.")
            break
        else:
            print("Bot: I'm not trained to respond to that. Try asking something else.")

if __name__ == '__main__':
    chatbot()