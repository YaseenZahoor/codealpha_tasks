import random
import nltk
from nltk.chat.util import Chat, reflections
patterns=[
    (r'hi|hello|hey there',['Hello!','Hey!','Hi there!']),
    (r'how are you?',['I am good,thank you.','I am doing well, thanks.']),
    (r'what is your name?',['I am a chatbot.']),
    (r'what can you do?',['I can chat with you and provide information.']),
    (r'how old are you?',['I don\'t have an age.I am a chatbot.']),
    (r'what is the weather like today?',['I am sorry,I cannot provide real-time weather information.']),
    (r'do you read books?',['I don\'t read books, but I can recommend some.']),
    (r'suggest some books',['Sure! Here are some books you might like:\n"Rich dad Poor dad" by Robert T.Kiyosaki\n"Forty Rules of Love" by Elif Shafak\n"You Can Win" by Shiv Khera']),
    (r'bye',['Goodbye! have a nice day!']),
    (r'exit',['Goodbye! See you later.']),
    (r'.*',['I am sorry, I didn\'t understand that.']),
]
stories= [
    ("The Boy Who Cried Wolf", "A young shepherd boy repeatedly tricks the villagers by pretending a wolf is attacking his sheep. "
     "\nWhen a real wolf appears and the boy cries for help, the villagers don't believe him, and the wolf eats his sheep.",
     "Honesty is important, and if you lie repeatedly, people won't believe you even when you're telling the truth."),
    ("The Lion and the Mouse", "A lion catches a mouse and is about to eat it when the mouse pleads for mercy, promising to help the lion someday. "
     "\nThe lion laughs but lets the mouse go. Later, the lion gets trapped in a hunter's net, "
     "and the mouse gnaws through the ropes, setting the lion free.",
     "Even small acts of kindness can be repaid in unexpected ways; no act of kindness, no matter how small, is ever wasted."),
    ("The Milkmaid and Her Pail",
     "A milkmaid carries a pail of milk on her head and dreams of all the things she will buy with the money she earns from selling the milk. "
     "\nShe gets lost in her daydreams and tosses her head, spilling the milk.",
     "Don't count your chickens before they hatch; it's wise to focus on the task at hand."),
]
chatbot=Chat(patterns, reflections)
print("Welcome! How can I help you?")
while True:
    user_input=input("User: ").lower()
    if 'tell me a story' in user_input:
        story=random.choice(stories)
        print("Chatbot:")
        print("Title:", story[0])
        print("Story:", story[1])
        print("Moral:", story[2])
    else:
        response=chatbot.respond(user_input)
        print("Chatbot:",response)
    if user_input=='exit':
        break



