from flask import Flask , render_template 
data ={
    "python":{
        "name":"python",
        "lesson":[
                    {
                        "id":"001",
                        "title":"About python",
                        "image":"iii",
                        "text":"learn python basics",
                        "example":"print(\"hellow world\")"
                    },
                    {
                        "id":"002",
                        "title":"Python basics",
                        "image":"",
                        "text":"learn python print",
                        "example":"print(\"hellow world\")"
                    }
                    ,
                    {
                        "id":"002",
                        "title":"Python basics",
                        "image":"",
                        "text":"learn python print",
                        "example":None
                    }
                ]
        },
    
    "java":{
        "name":"java",
        "lesson":[
                    {
                        "id":"001",
                        "title":"About java",
                        "image":"iii",
                        "text":"learn java basics",
                        "example":"java(\"hellow world\")"
                    },
                    {
                        "id":"002",
                        "title":"java basics",
                        "image":"",
                        "text":"learn java print",
                        "example":"print(\"hello world\")"
                    }
                    ,
                    {
                        "id":"002",
                        "title":"java basics",
                        "image":"",
                        "text":"learn python print",
                        "example":None
                    }
                ]
        },
}

# load data
app = Flask(__name__)


@app.route("/")
def f():
    return render_template("lessons.html",langs=data.keys(),data=data)


app.run(debug=True,host="127.0.0.1",port="8080")
