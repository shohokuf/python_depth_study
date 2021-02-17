from flask import Flask

app = Flask(__name__)


@app.route('/user/<user_name>')
def show_user_profile(user_name):
    # show the user profile for that user
    return 'User %s' % user_name


@app.route('/post/<int:id>')
def show_post(id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % id


app.run()
