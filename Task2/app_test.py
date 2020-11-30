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
RiverID = 1

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
