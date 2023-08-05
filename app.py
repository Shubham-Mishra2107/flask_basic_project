from flask import Flask,request,url_for,render_template,redirect

app=Flask(__name__)

#created some small function for better understanding
@app.route('/Home')
def home():
    return f"<h1>welcome to the Home page!</h1>"

@app.route('/Test')
def test():
    return render_template('new.html')

#Project starts below
@app.route('/success/<int:score>')
def success(score):
    if score>=50:
        return f"<h1>The person is pass and score is: {score}</h1>"
    else:
        return f"<h1>The person is fail and score is: {score}</h1>"
    
@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=="GET":
        return render_template('calculate.html')
    else:
        maths= float(request.form['maths'])
        science= float(request.form['science'])
        history= float(request.form['history'])
        average_marks = (maths+science+history)/3
        result="success"
        return redirect(url_for(result,score=average_marks))
# Some other ways to get it done
        #return render_template('calculateme.html',result=average_marks)
        
        #return f"<h1>the average marks is: {average_marks}</h1>"



if __name__=="__main__":
    app.run(debug=True)