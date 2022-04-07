from flask import Flask, request
 
app = Flask(__name__)
 
 
@app.route("/")
def simple():
    id_ = request.args.get('id')
    if id_ == 'one':
        return 'result - one'
    elif id_ == 'two':
        return 'result - two'
    else:
        return 'no result'
 
 
if __name__ == "__main__":
    app.run(debug=True)