def chatBot():
    print("ChatBot: Hello! I'm a Chatbot. Type 'bye' to exit")
    while True:
        user_input = input("You:").lower()
        if user_input=='bye':
            print("ChatBot: bye! Have a nice day")
            break
        elif 'hello' in user_input or 'hi' in user_input:
            print("ChatBot:Hi there! How can I help you?")
        elif 'how' in user_input:
            print("ChatBot: I'm bot, but I'm doing great! How can i help you?")
        elif 'name' in user_input:
            print("ChatBot: I'm ChatBot, your virtual assistant")
        else:
            print("ChatBot: sorry, I don't understand that")
    
chatBot()