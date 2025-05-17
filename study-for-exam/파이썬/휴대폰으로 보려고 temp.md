
```python
from flask import Flask, render_template, request, jsonify
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient("localhost", 27017)
db = client.jungle

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/memo", methods=["GET"])
def get_article():
    articles = list(db.articles.find({}, {"_id": False}))
    return jsonify({"result": "success", "articles": articles})

@app.route("/memo", methods=["POST"])
def post_article():
    try:
        data = request.get_json()
        url_receive = data.get("url")
        comment_receive = data.get("comment") 
        data = requests.get(url_receive)
        soup = BeautifulSoup(data.text, "lxml")
 
        title = soup.select_one("meta[property='og:title']")["content"]
        description = soup.select_one("meta[property='og:description']")["content"]
        image_url = soup.select_one("meta[property='og:image']")["content"] 

        article = {
            "url": url_receive,
            "title": title,
            "desc": description,
            "image": image_url,
            "comment": comment_receive,
        }

        print(f"article={article}")
        db.articles.insert_one(article)
        
        return jsonify(
            {"result": "success", "message": "Memo가 성공적으로 등록되었습니다."}
        )

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"result": "fail", "message": "Memo 등록에 실패하였습니다."})

if __name__ == "__main__":
    app.run("0.0.0.0", port=5001, debug=True)
```


```javascript
$(function () {
  getMemoList();
  $("#post-box-button").click(togglePostBox);
  $("#submit-button").click(submitMemo);
});


function togglePostBox() {
  $("#post-box").slideToggle();
}


function getMemoList() {
  $.ajax({
    type: "GET",
    url: "http://localhost:5001/memo",
    success: function (response) {
      const articles = response.articles;
      for (const article of articles) {
        make_memoCard(article);
      }
    },

    error: function (error) {
      console.log(`DB로부터 기사를 가져오는데 실패했습니다. ${error}`);
      console.error("Error:", error);
    },
  });
}

function make_memoCard(article) {
  const url = article["url"];
  const title = article["title"];
  const description = article["desc"];
  const image = article["image"];
  const comment = article["comment"];

  let temp_html = `<div class="card">
                      <img class="card-img-top" src="${image}" alt=""/>
                      <div class="card-body">
                        <a class="card-title" href=${url} target="_blank">${title}</a>
                        <p class="card-text">${description}</p>
                        <p class="card-text comment">${comment}</p>
                      </div>
                    </div>`;
  $("#card-boxes").append(temp_html);
}


function submitMemo(e) {
  e.preventDefault();
  const url = $("#input-url").val();
  const comment = $("#input-comment").val();

  $.ajax({
    type: "POST",
    url: "http://localhost:5001/memo",
    data: JSON.stringify({ url: url, comment: comment }),
    contentType: "application/json",
    success: function (response) {
      console.log("Success:", response);
      $("#post-box").slideToggle();
      $("#input-url").val("");
      $("#input-comment").val("");
      alert("성공적으로 업로드 됐습니다!");
      location.reload();
    },

    error: function (error) {
      console.error("Error:", error);
      alert("업로드에 실패했습니다.");
    },
  });
}
```