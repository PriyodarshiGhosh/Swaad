# from flask import Flask,render_template,request,redirect,flash
from flask import *
import pred as p
app=Flask(__name__)
@app.route("/")
def hello():
    return render_template("index.html")
@app.route("/sub",methods=["GET","POST"])
def submit():
    if request.method=="POST":
        dish=request.form["dish"]
        ing1=request.form["ing1"]
        ing2=request.form["ing2"]
        ing3=request.form["ing3"]

        # print("<!--",dish, ing1, ing2, ing3,"-->")
        if (dish != "") & (ing1 == "") & (ing2 == "") & (ing3 == ""):
            dish_pred=p.dish_recommender(dish)
            print(dish_pred)
            most = dish_pred[0][0]
            most_desc = dish_pred[1][0]
            sim_2 = dish_pred[0][1]
            sim_2_desc = dish_pred[1][1]
            sim_3 = dish_pred[0][2]
            sim_3_desc = dish_pred[1][2]
            sim_4 = dish_pred[0][3]
            sim_4_desc = dish_pred[1][3]
            sim_5 = dish_pred[0][4]
            sim_5_desc = dish_pred[1][4]
            return render_template("sub.html",most=most, sim_2=sim_2, sim_3=sim_3, sim_4=sim_4, sim_5=sim_5, most_desc=most_desc, sim_2_desc=sim_2_desc, sim_3_desc=sim_3_desc, sim_4_desc=sim_4_desc, sim_5_desc=sim_5_desc)
        
        elif (dish == "") & (ing1 != "") & (ing2 != "") & (ing3 != ""):
            dishes=p.dish_ing(ing1,ing2,ing3)
            print(dishes)
            return render_template("mel.html",m=dishes[0])

        else:
            print("breaking out")
            return redirect('/')

if __name__=="__main__":
    app.run()
