
# main.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home', methods=['GET'])
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
