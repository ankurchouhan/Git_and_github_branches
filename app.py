from flask import Flask, render_template, request, jsonify
from api.routes import api_blueprint

app = Flask(__name__)
app.register_blueprint(api_blueprint, url_prefix="/api")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/todo')
def todo():
    return render_template('todo.html')

if __name__ == '__main__':
    app.run(debug=True)
