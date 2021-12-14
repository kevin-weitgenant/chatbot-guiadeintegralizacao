from flask import Flask, render_template, request, jsonify
import orquestrador
import os
app = Flask(__name__)



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    result = orquestrador.askDiscovery(userText)

    
    answers = [result[x]["passage_text"] for x in range (len(result)) if x< 3]           #retorna até 3 respostas, 
                                                                                         #limitadas por até 1000 caracteres
    return jsonify(answers)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port= port)
