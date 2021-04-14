from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method== "POST":
        info = []
        info.append(request.form.get('firstName'))
        info.append(request.form.get('lastName'))
        info.append(request.form.get('email'))
        # info.append(request.form.get('password'))
        return render_template('show.html', info=info)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)