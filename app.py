from flask import Flask, render_template, request, redirect, url_for, flash, session

app=Flask(__name__)

@app.get("/home")
def home():
    return "Get method called"



if __name__ == '__main__':
    app.run(debug=True)
    
#localhost:5000/home
    