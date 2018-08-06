import random
from flask import Flask, jsonify


app = Flask(__name__)
 
@app.route('/', methods=['GET'])

def home():
    f = open('url_list.txt')
    lines = f.readlines()
    max_line = len(lines)
    ranline = random.randint(0,max_line)
    
    data = {
        'url':lines[ranline][:-1]
    }

    return jsonify(data)
 
if __name__ == '__main__':
    app.run(debug=True)