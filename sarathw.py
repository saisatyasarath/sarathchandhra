from flask import Flask
app=Flask(_filename_)

@app.route("/")
def hello():
    return "hello, world"

if _name_ == "_main_":
    app.run()