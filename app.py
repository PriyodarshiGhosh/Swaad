from flask import Flask,render_template,request
import pred as p
app=Flask(__name__)
@app.route("/")
def hello():
    return render_template("index.html")
@app.route("/sub",methods=["POST"])
def submit():
    if request.method=="POST":
        dish=request.form["dish"]
        dish_pred=p.dish_recommender(dish)
        most = dish_pred[0].split()
        most_dish_1 = (" ".join(most[0:-2])).title()
        print(most_dish_1)
        most_dish_2 = (" ".join(most[-2:])).title()
        print(most_dish_2)
        ing1=request.form["ing1"]
        ing2=request.form["ing2"]
        ing3=request.form["ing3"]
        dishes=p.dish_ing(ing1,ing2,ing3)
        print(dishes)
    return render_template("sub.html",most_dish_1=most_dish_1,most_dish_2=most_dish_2,m=dishes)

if __name__=="__main__":
    app.run()
