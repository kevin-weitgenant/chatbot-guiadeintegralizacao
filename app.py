from flask import Flask, render_template, request, jsonify
import orquestrador

app = Flask(__name__)



@app.route("/")
def home():
    return render_template("home.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    result = orquestrador.askDiscovery(userText)

    
    answers = [result[x]["text"] for x in range (len(result)) if x< 3]           #retorna até 3 respostas, 
                                                                                         #limitadas por até 1000 caracteres
    return jsonify(answers)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
