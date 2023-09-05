from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.json['message']
    # Burada message ile ChatGPT API'sine istek gönderip cevap alabilirsiniz.
    # Şimdilik basit bir cevap dönelim:
    return jsonify({"reply": "Merhaba, bu bir cevaptır!"})

if __name__ == '__main__':
    app.run(debug=True)
