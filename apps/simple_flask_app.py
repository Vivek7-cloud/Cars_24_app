from flask import Flask

app = Flask(__name__) 

# points to the name of the current file. Here instead of hard coding the name of the file, _name_ 
#This allows Flask to know where to look for resources such as templates and static files.  


@app.route("/hello", methods=["GET"]) # Here "@" is a decorator that controls the behavior of the function 
def hello():
    return "Hello from flask!"

if __name__ == "__main__":
    app.run(debug=True)
