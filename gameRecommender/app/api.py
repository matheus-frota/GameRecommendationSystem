import flask
from knnRecommender.knn import recommender
#import src
app = flask.Flask(__name__)

@app.route('/')
def home():
    return flask.render_template('home.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = flask.request.form['text1']
    text2 = flask.request.form['text2']
    #combine = recommender(text1,text2)
    combine = "aaaaaaaaaaaaaaa"
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    return flask.jsonify(result=result)
if __name__ == '__main__':
    app.run(debug=True)