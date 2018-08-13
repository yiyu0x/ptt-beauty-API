import random
from task import timedTask
from flask import Flask, jsonify


app = Flask(__name__)
 
@app.route('/', methods=['GET'])
def home():
    f = open('url_list.txt')
    lines = f.readlines()
    max_line = len(lines)
    ranline = random.randint(0,max_line)
    
    data = {
        # -1 is mean delete last character '\n'
        'url':lines[ranline][:-1]
    }

    return jsonify(data)

@app.route('/times/<times>', methods=['GET'])
def times(times):
    try:
        if int(times) <= 0 or int(times) > 100:
            return "number error"

        f = open('url_list.txt')
        lines = f.readlines()
        max_line = len(lines)

        data = {}
        box = []
        counter = 0
        while counter != int(times):
            ranline = random.randint(0,max_line)
            if lines[ranline][:-1] not in box :
                counter += 1
                data[str(counter)] = lines[ranline][:-1]
                box.append(lines[ranline][:-1])
        return jsonify(data)

    except:
        return "error"


if __name__ == '__main__':
    app.run(host="0.0.0.0" ,port="5487")
    timedTask()
