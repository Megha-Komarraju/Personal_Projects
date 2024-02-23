import os
import nltk
import ssl
import streamlit as st
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import joblib

# Import emoji library
from emoji import emojize
import pyjokes

ssl._create_default_https_context = ssl._create_unverified_context

# Lazy loading of NLTK data
nltk.download('punkt', quiet=True)

intents = [
    {
        "tag": "greeting",
        "patterns": ["Hi", "Hello", "Hey", "How are you", "What's up"],
        "responses": ["Hi there 😊", "Hello 👋", "Hey! How can I assist you today?", "I'm fine, thank you 😊", "Nothing much, how about you?"]
    },
    {
        "tag": "goodbye",
        "patterns": ["Bye", "See you later", "Goodbye", "Take care"],
        "responses": ["Goodbye! Have a great day 😊", "See you later 👋", "Take care!"]
    },
    {
        "tag": "thanks",
        "patterns": ["Thank you", "Thanks", "Thanks a lot", "I appreciate it"],
        "responses": ["You're welcome 😊", "No problem! Happy to help 😊", "Glad I could help! 😊"]
    },
    {
        "tag": "about",
        "patterns": ["What can you do", "Who are you", "What are you", "What is your purpose"],
        "responses": ["I am a chatbot designed to assist you with your queries. Feel free to ask anything! 😊", "My purpose is to help you with information and tasks. 😊", "I'm here to provide assistance and answer your questions. 😊"]
    },
    {
        "tag": "help",
        "patterns": ["Help", "I need help", "Can you help me", "What should I do"],
        "responses": ["Sure, what do you need help with? 😊", "I'm here to help. What's the problem? 😊", "How can I assist you? 😊"]
    },
    {
        "tag": "age",
        "patterns": ["How old are you", "What's your age"],
        "responses": ["I don't have an age. I'm a chatbot. 😊", "I was just born in the digital world. 😊", "Age is just a number for me. 😊"]
    },
    {
        "tag": "weather",
        "patterns": ["What's the weather like", "How's the weather today"],
        "responses": ["I'm sorry, I cannot provide real-time weather information. 😊", "You can check the weather on a weather app or website. 😊"]
    },
    {
        "tag": "budget",
        "patterns": ["How can I make a budget", "What's a good budgeting strategy", "How do I create a budget"],
        "responses": ["To make a budget, start by tracking your income and expenses. Then, allocate your income towards essential expenses like rent, food, and bills. Next, allocate some of your income towards savings and debt repayment. Finally, allocate the remainder of your income towards discretionary expenses like entertainment and hobbies. 😊", "A good budgeting strategy is to use the 50/30/20 rule. This means allocating 50% of your income towards essential expenses, 30% towards discretionary expenses, and 20% towards savings and debt repayment. 😊", "To create a budget, start by setting financial goals for yourself. Then, track your income and expenses for a few months to get a sense of where your money is going. Next, create a budget by allocating your income towards essential expenses, savings and debt repayment, and discretionary expenses. 😊"]
    },
    {
        "tag": "credit_score",
        "patterns": ["What is a credit score", "How do I check my credit score", "How can I improve my credit score"],
        "responses": ["A credit score is a number that represents your creditworthiness. It is based on your credit history and is used by lenders to determine whether or not to lend you money. The higher your credit score, the more likely you are to be approved for credit. 😊", "You can check your credit score for free on several websites such as Credit Karma and Credit Sesame. 😊"]
    },
    {
    "tag": "joke",
    "patterns": ["Tell me a joke", "I want to laugh", "Do you know any jokes?"],
    "responses": ["Sure, here's a joke for you:", "Get ready to laugh:", "I hope this makes you smile:"]
}
]

# Create the vectorizer and classifier
vectorizer = TfidfVectorizer()
clf = MultinomialNB()

# Preprocess the data
tags = []
patterns = []
for intent in intents:
    for pattern in intent['patterns']:
        tags.append(intent['tag'])
        patterns.append(pattern)

# Training the model
x = vectorizer.fit_transform(patterns)
y = tags
clf.fit(x, y)

# Save the trained model and vectorizer
joblib.dump(vectorizer, "vectorizer.pkl")
joblib.dump(clf, "model.pkl")

def chatbot(input_text):
    input_text = vectorizer.transform([input_text])
    tag = clf.predict(input_text)[0]
    if tag == 'joke':
            return get_joke()
    else:
        for intent in intents:
            if intent['tag'] == tag:
                response = random.choice(intent['responses'])
                return response
        
# Function to get a random joke
def get_joke():
    return pyjokes.get_joke()

counter = 0

def main():
    global counter
    st.title("Meg's Chatbot")
    st.write("Welcome to the chatbot. Please type a message and press Enter to start the conversation.")

    counter += 1
    user_input = st.text_input("You:", key=f"user_input_{counter}")

    if user_input:
        response = chatbot(user_input)
        st.text_area("Chatbot:", value=response, height=100, max_chars=None, key=f"chatbot_response_{counter}")

        if response.lower() in ['goodbye', 'bye']:
            st.write("Thank you for chatting with me. Have a great day!")
            st.stop()

if __name__ == '__main__':
    main()
