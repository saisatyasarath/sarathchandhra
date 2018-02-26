from flask import Flask
from flask import jsonify
app=Flask(_name_)

@app.route("/")
def hello():
    return jsonify({
            'message':'vineeth likes keyboards',
              'flag':True
                   })
if _name_ == "_main_":
    app.run(debug==True)
