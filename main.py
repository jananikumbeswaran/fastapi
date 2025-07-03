from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def getmark():
    return{"welocme world"}
