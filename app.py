from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections
import nltk

nltk.download('punkt')

# Chatbot logic (you can also import from nltk_chatbot.py if preferred)
pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you today?", "Hi there! What can I do for you?"]],
    [r"how are you", ["yeah! I am good, what about you?"]],
    [r"The app keeps crashing  Can you help", 
     ["Please update the app and restart your device. Let me know your device model if it keeps crashing."]],
    [r"my name is (.*)", ["Hello %1, how can I assist you today?"]],
    [r"(.*) (problem|issue|error|not working)", 
     ["I'm sorry to hear that you're facing a %2. Can you provide more details?"]],
    [r"how to reset (.*)", 
     ["To reset your %1, go to settings, then select 'Reset'. Let me know if you need help!"]],
    [r"(.*) refund(.*)", 
     ["To process a refund, please provide your order ID. I'll assist you from there."]],
    [r"(.*) (bye|exit|quit)", 
     ["Thank you for contacting support. Have a great day!", "Bye! Feel free to reach out anytime."]],
    [r"(.*)", 
     ["I'm sorry, I didn’t understand that. Could you rephrase or ask something else?"]],
    [r"thankyou", 
     ["You're welcome! If you have any more questions, feel free to ask."]],
    [r"How to Download apps in Mobile", 
     ["Let me know which Android device you are using?"]],
    [r"Android", 
     ["To download apps on Android, open the Google Play Store, search for the app you want, and tap 'Install'."]],
    [r"iOS", 
     ["To download apps on iOS, open the App Store, search for the app you want, and tap 'Get'."]],
    [r"How to set screen password", 
     ["Go to Settings > Security > Screen Lock, then choose your preferred lock method."]]
]



chatbot = Chat(pairs, reflections)

# Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_input = request.json['msg']
    response = chatbot.respond(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
