from flask import Flask, jsonify
 
app = Flask(__name__)
 
tasks = [
    {
        'id': 1,
        'title': u'OSPA',
        'description': u'This is ospaf-api test', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Garvin',
        'description': u'I am garvin', 
        'done': False
    }
]
 
@app.route('/', methods=['GET'])
def home():
    return jsonify({'tasks': tasks})
 
if __name__ == '__main__':
    app.run(debug=True)