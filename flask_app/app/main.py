from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

def predictText(textFromUser):
  return textFromUser + " hello :)"
  
@app.route('/', methods=['POST'])
def index():
    content = request.get_json(silent=True)
    text = predictText(content)
    return {"text": text}

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
 
