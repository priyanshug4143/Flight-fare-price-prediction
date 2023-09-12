from flask import Flask , render_template , request
import pandas as pd
import numpy as np
import pickle
train=pd.read_excel(r'C:\Users\Dr. Poonam\Documents\Priyanshu Gupta\Machine Learning All Datasets\Data_Train.xlsx')

unique_airline=train["Airline"].unique()
unique_source=train["Source"].unique()
unique_destination=train["Destination"].unique()
unique_additional=train["Additional_Info"].unique()

model=pickle.load(open("Catboosting2.pkl" , "rb"))

#model.predict()

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/predict" , methods=["POST"])
def predict_price():
    Airline=request.form.get("Airline Name")
    Source=request.form.get("Source")
    Destination=request.form.get("Destination")
    Total_Stops=request.form.get("Total Stops")
    Additional_info=request.form.get("Additional Info")
    Month_of_Jounrey=request.form.get("Month of Journey")
    Dep_hour=request.form.get("Dep_hour")    
    Total_Hours=request.form.get("Total_Hours")
    result = model.predict(np.array([[Airline , Source , Destination , Total_Stops , Additional_info , Month_of_Jounrey , Dep_hour , Total_Hours]]))
    final=np.round(result[0])

    return render_template("index.html" , final=final)
    

if __name__=="__main__":
    app.run(debug=True)