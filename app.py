from flask import Flask, render_template, request
import orquestrador 
import orquestrador2
import json

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    result = orquestrador2.orquestrador2(userText)

    #data = {
        #'respostas': [result[x]["text"][0:1000] for x in range (len(result)) if x< 3]    #retorna até 3 respostas, 
                                                                                         #limitadas por até 1000 caracteres
    #}

    #json_object = json.dumps(data, indent = 4) 
    return result[0]["text"][0:1000]


if __name__ == "__main__":
    app.run()