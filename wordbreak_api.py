from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__,template_folder="templates")
breaked_words = []
dict =[]
def dictionaryContains(word):
    global dict
    return word in dict
def wordBreakUtil(string, n, result):
    for i in range(1, n + 1):
        prefix = string[:i]
        if dictionaryContains(prefix):
            if i == n:
                global breaked_words
                result += prefix
                breaked_words.append(result)
                return
            wordBreakUtil(string[i:], n - i, result + prefix + " ")

@app.route('/')
def index():
    return render_template('index.html')
@app.route("/wordBreak",methods = ['GET','POST'])

def wordBreak():
    string = [str(x) for x in request.form.values()]
    if request.method == 'POST':
        try:
            wordBreakUtil(string[0], len(string[0]), "")
            return render_template('index.html',result = str(breaked_words[-1]),got_dict=dict)
        except:
            return render_template('index.html',result = "get the dictionary words!")
@app.route("/dictwords",methods = ['GET','POST'])
def dictwords():
    global dict
    dictionary = [str(x) for x in request.form.values()]
    dict = dictionary[0].split(",")
    return render_template("index.html",got_dict = dict)

if __name__=="__main__":
    app.run(debug=True)
