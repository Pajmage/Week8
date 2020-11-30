'''
MSc Digital and Technology Solutions
CETM65 Software Engineering Principles
Author: Paul Jones
Date: 27/11/2020

Week 8 - ePortfolio Task 2 - Adding a Database via SQLAlchemy   
'''
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from Rivers import *
from array import *
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///River_Database.db'
db = SQLAlchemy(app)

class River(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    RiverName = db.Column(db.String(25), unique=False, nullable=False)
    RiverLengthKm = db.Column(db.Float, unique=False, nullable=False)
    RiverLengthMiles = db.Column(db.Float, unique=False, nullable=False)
    RiverRating = db.Column(db.String(10))

    def __repr__(self):
        obj_repr = f'ID: {self.id},' \
                   f'River Name: {self.RiverName},' \
                   f'Length (Km): {self.RiverLengthKm},' \
                   f'Length (M): {self.RiverLengthMiles},' \
                   f'Rating: {self.RiverRating}' \

        return obj_repr


def Add_River(rivername, length, Miles, RiverRating):
     New_River = River(RiverName = rivername,
                        RiverLengthKm = length,
                        RiverLengthMiles = Miles,
                        RiverRating = RiverRating,)
                        
     print(New_River)
     db.session.add(New_River)
     db.session.commit()
     


# Flask routes support GET requests by default.
# However it must be declared if the methods argument is provided.
@app.route("/river", methods=["GET", "POST"])
def New_River():

    if request.method == "POST":

        req = request.form
        rivername = req.get("rivername")
        length = req.get("length")
        rapids = req.get("rapids")

        
        description = (f"\nRiver name is: {rivername}\n"
                       f"Length is: {length}km\n"
                       f"Rapids are Grade {rapids}\n")
        
        print(description)

        MissingFields = list()

        for DicKey, DicValue in req.items():
            if DicValue == "":
                MissingFields.append(DicKey)

        if MissingFields:
            feedback = f"Missing fields for {', '.join(MissingFields)}"
            return render_template("river.html", feedback=feedback)
        else:        
            rapids = int(rapids)
            length = int(length)
            Miles = Km_To_Miles(length)
            RiverScore = Rating(length, rapids)
            RiverRating = River_Grade(RiverScore)
            Add_River(rivername, length, Miles, RiverRating)
        print(Miles)
        print(RiverScore)
        print(RiverRating)
        
        #render_template("results.html")

    return render_template("river.html")


@app.route("/results", methods=["GET", "POST"])
def View_River_Details():
    print(request.method)
    if request.method =='POST':
        print("inside")
        print(request.method)
        all_rivers = River.query.all()
        if request.form['Display'] == 'Display':
            return render_template("results.html", all_rivers = all_rivers)
    
    return render_template("results.html")


app.run(debug=True)
