from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f"<h1>Hello, {name}! Your email is {email}.</h1>"
    

if __name__ == "__main__":
    app.run(debug=True)