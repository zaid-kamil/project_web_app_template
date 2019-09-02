from flask import Flask,render_template,jsonify,request,redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])   
def updateSize():
    return jsonify({'status':'hurray'})

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/ajax_register',methods=['POST','GET'])
def ajax_register():
    if request.method == 'POST':
        import time
        time.sleep(3)
        uname = request.form.get('username')
        email = request.form.get('email')
        crap = request.form.get('status')
        if uname and email:
            # save to dbase
            return jsonify({'status':'success'})
        else:
            return jsonify({'status':'error'})
    else:
        return redirect('/register')



if __name__ == '__main__':
    app.run(debug=True)