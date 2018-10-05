from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <form method="POST">
            <label>Rotate by:</label>
            <type="text" name="rot" value="0"/>
            <textarea name="text"></textarea>
            <input type="submit"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form


@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return '<h1>' + "hello, " + first_name + '</h1>'
    
app.run()