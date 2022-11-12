from flask import Flask,render_template,request
import pred as p
app=Flask(__name__)
@app.route("/hi")
def hello():
    return render_template("index.html")
@app.route("/sub",methods=["POST"])
def submit():
    if request.method=="POST":
        dish=request.form["dish"]
        dish_pred=p.dish_recommender(dish)
    return render_template("sub.html",n=dish_pred)

if __name__=="__main__":
    app.run()