from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
import json, os
from flask.json.provider import JSONProvider

app = Flask(__name__)

database = "dbjungle"
collection = "memos"
user = "root"
password = "pwd1234"
port = 27018
ip = "localhost"  # 나중에 수정

client = MongoClient(
    f"mongodb://{user}:{password}@localhost:{port}/{database}?authSource=admin"
)

db = client[database]


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


class CustomJSONProvider(JSONProvider):
    def dumps(self, obj, **kwargs):
        return json.dumps(obj, **kwargs, cls=CustomJSONEncoder)

    def loads(self, s, **kwargs):
        return json.loads(s, **kwargs)


# 위에 정의되 custom encoder 를 사용하게끔 설정한다.
app.json = CustomJSONProvider(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/memos", methods=["POST"])
def registerMemo():
    data = request.get_json()
    title = data["title"]
    content = data["content"]
    if not title:
        return jsonify({"reuslt": " error", "messgae": "제목을 입력하세요."})

    memo = {"title": title, "content": content, "likes": 0}

    print(f"서버에서 등록할 메모 : {memo}")
    result = db[collection].insert_one(memo)

    if not result.acknowledged:
        return jsonify({"result": "error", "message": "메모 등록 실패"})

    return jsonify({"result": "success", "message": "메모 등록 완료"})


@app.route("/memos", methods=["GET"])
def getMemos():
    sort = "likes"
    sortdirection = -1
    memos = list(db[collection].find().sort(sort, sortdirection))
    print(f"조회된 메모 : {memos}")
    return jsonify({"result": "success", "memos": memos})


@app.route("/memos/<id>", methods=["DELETE"])
def deleteMemo(id):
    result = db[collection].delete_one({"_id": ObjectId(id)})

    if result.deleted_count != 1:
        return jsonify({"result": "error", "message": "메모 삭제 실패"})

    return jsonify({"result": "success", "message": "메모 삭제 완료"})


@app.route("/memos/<id>", methods=["PUT"])
def editMemo(id):
    data = request.get_json()
    print(f"수정할 메모 : {data}")
    title = data["title"]
    content = data["content"]
    result = db[collection].update_one(
        {"_id": ObjectId(id)}, {"$set": {"title": title, "content": content}}
    )

    if result.matched_count != 1:
        return jsonify({"result": "error", "message": "메모 좋아요 실패"})

    return jsonify({"result": "success", "message": "메모 좋아요 완료"})


@app.route("/memos/<id>/like", methods=["PATCH"])
def likeMemo(id):
    result = db[collection].update_one({"_id": ObjectId(id)}, {"$inc": {"likes": 1}})

    if result.matched_count != 1:
        return jsonify({"result": "error", "message": "메모 좋아요 실패"})

    return jsonify({"result": "success", "message": "메모 좋아요 완료"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
