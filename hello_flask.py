import flask
import os

app = flask.Flask(__name__)
# import os.path
print(os.path.isfile('hello.html'))
# print(os.path.abspath('templates/index.html')) 
# working =os.path.abspath('templates/index.html')

@app.route('/hello/<name>/')
def hello(name):

    return flask.render_template('hello.html',name=name)

if __name__ == "__main__":
    app.debug=True
    app.run()
#     app.run(debug=True)