from flask import Flask, render_template, request, jsonify
import fakenews

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_fake_news():
    input_data = request.form['text']  # Getting the input from the form
    result = fakenews.detect_fake_news(input_data)
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
