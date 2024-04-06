import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot and I'm here to help.",]
    ],
    [
        r"how are you?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright","It's OK, never mind",]
    ],
    [
        r"(.*) thank you (.*)",
        ["You're welcome", "No problem",]
    ],
]
chatbot= Chat(pairs,reflections)
print("Hi, I am chatbot! How can I serve you ")
while True:
    user_input = input("you: ")
    response=chatbot.respond(user_input)
    print("Chatbot:", response)
    
    
    
    
    
# Here, we import the NLTK library and the Chat class and reflections dictionary from the nltk.chat.util module. Chat class is used to create a chatbot, and reflections is a dictionary that maps first-person pronouns to second-person pronouns and vice versa, which helps in generating appropriate responses.


# Here, we define a list of patterns and corresponding responses. Each pattern is a regular expression (r"pattern") that matches a user input. When a user input matches a pattern, one of the corresponding responses is randomly selected and returned.

# We create a Chat instance named chatbot by passing the pairs list and the reflections dictionary to the constructor. This initializes the chatbot with the defined patterns and responses.

# In the pairs defined in the code snippet you provided, the r before the regex patterns indicates that they are raw string literals, and any special characters (such as \) within them are treated as literal characters. This makes it easier to write and read regular expressions, especially when dealing with patterns that contain backslashes.

#nltk is Natural Language Toolkit


# The nltk.chat.util module in NLTK provides utilities for building chatbots and conversational agents. It includes classes and functions that are helpful for creating chatbots, managing conversations, and handling user inputs and responses.




    