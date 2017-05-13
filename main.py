from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return 'Method used {}'.format(request.method)


@app.route('/sam')
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


if __name__ == "__main__":
    app.run(debug=True)
