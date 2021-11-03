from flask import Flask, render_template, request
import orquestrador 
import orquestrador2

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    result = orquestrador2.orquestrador2(userText)

    data = {
        'respostas': [result[x]["text"][0:1000] for x in range (len(result)) if x< 3]    #retorna até 3 respostas, 
                                                                                         #limitadas por até 1000 caracteres
    }

    return render_template("home.html", data = data)


if __name__ == "__main__":
    app.run()