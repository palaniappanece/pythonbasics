from flask import Flask, render_template, request, redirect, url_for, flash, session
import os
app=Flask(__name__)

@app.get("/home")
def home():
    return "Get method called"



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
    
#localhost:5000/home

    

