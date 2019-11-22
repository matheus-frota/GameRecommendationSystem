from flask import Flask, request, render_template,jsonify
#import src
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    text1 = request.form['text1']
    text2 = request.form['text2']
    #combine = recommender(text1,text2)
    combine = "aaaaaaaaaaaaaaa"
    result = {
        "output": combine
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
if __name__ == '__main__':
    app.run(debug=True)