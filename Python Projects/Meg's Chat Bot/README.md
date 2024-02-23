# **Meg's Chatbot**
Meg's Chatbot is a simple conversational agent built using Streamlit, scikit-learn, and NLTK. It can respond to user queries on various topics such as greetings, farewells, weather inquiries, budgeting tips, and more.

## **Features**
* Responds to greetings, farewells, thanks, and general inquiries.
* Provides information on topics like budgeting, credit scores, and weather.
* Uses TF-IDF vectorization and Multinomial Naive Bayes for classification.
* Supports emoji responses to add a touch of personality.
* Has jokes functionality to brighten up your day

## **Setup**
Copy code:
  streamlit run chatbot.py
Interact with the chatbot through your browser.

## **Usage**
* Type a message in the input field and press Enter to start the conversation.
* The chatbot will respond with appropriate messages based on the input.

## **File Structure**
* chatbot.py: Contains the main Streamlit application code.
* requirements.txt: Lists the Python dependencies required to run the application.
* README.md: The project's README file.
  
## **Contributing**
Contributions are welcome! If you'd like to contribute to Meg's Chatbot, feel free to open an issue or submit a pull request.

### **_Jokes Functionality_**
Meg's Chatbot now comes with an additional fun Jokes functionality to brighten up your day! The chatbot can tell you random jokes upon request. Whether you need a good laugh or just want to lighten the mood, the Jokes feature has got you covered.

##### How it Works
To trigger the Jokes functionality, simply type one of the following phrases in the chat input:

"Tell me a joke"
"I want to laugh"
"Do you know any jokes?"
Upon receiving one of these prompts, the chatbot will respond with a randomly selected joke from its collection of jokes.

#### Example Interaction
User: "Tell me a joke"
Chatbot: "Sure, here's a joke for you: Why don't scientists trust atoms? Because they make up everything!"

User: "I want to laugh"
Chatbot: "Get ready to laugh: Why couldn't the bicycle stand up by itself? It was two-tired!"

User: "Do you know any jokes?"
Chatbot: "I hope this makes you smile: Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!"

#### Notes
* The Jokes functionality is intended to add a touch of humor and light-heartedness to your interactions with the chatbot.
* Jokes are randomly selected from a collection of jokes available in the pyjokes library.
* Now, go ahead and ask Meg's Chatbot for a joke to brighten up your day!
