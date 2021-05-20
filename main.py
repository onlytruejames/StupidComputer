from flask import Flask, render_template, request, abort, jsonify, make_response
import uuid, json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', id=uuid.uuid1())

@app.route('/data', methods=["GET", "POST"], defaults={"jsondata": None})
@app.route('/data/<jsondata>', methods=["GET", "POST"])
def data(jsondata):
    file = open("data.json")
    if request.method=="POST":
        data = request.args.get('jsondata')
        if not data:
            abort(400)
        data = json.loads(data)
        moredata = json.load(file)
        done = False
        for i in range(len(moredata)):
            if moredata[i]["id"]==data["id"]:
                moredata[i]=data
                file = open("data.json", "w")
                json.dump(moredata, file, indent=6)
                done = True
        if not done:
            moredata.append({
                "id": data["id"],
                "x": data["x"],
                "y": data["y"]
            })
            file = open("data.json", "w")
            json.dump(moredata, file, indent=6)
        return "ok"
    else:
        resp = make_response(jsonify(json.load(file)))
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp

@app.route('/screen')
def screen():
    return render_template("screen.html")

if __name__=='__main__':
    app.run()