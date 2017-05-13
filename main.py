from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
@app.route("/<user>")
def index(user=None):
    return render_template("user.html", user=user)


@app.route('/me')
def sam():
    return '<h2> Hii this is sam</h2>'


@app.route('/account/<username>')
def account(username):
    return "Hey there {}".format(username)


@app.route('/post/<int:post_id>')
def post(post_id):
    return "<h2>The Post ID is {}</h2>".format(post_id)


@app.route("/test",methods=['GET','POST'])
def test():
    if request.method == 'GET':
        return 'Using GET'
    if request.method == 'POST':
        return 'Using POST'


@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', name=name)


@app.route("/shopping")
def shopping():
    fruit = ["Mango","Banana", "Apple"]
    return render_template("shopping.html", fruit=fruit)


if __name__ == "__main__":
    app.run(debug=True)
