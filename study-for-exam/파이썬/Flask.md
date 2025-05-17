
>[!SUCCESS]  파이썬 웹 프레임워크  ➡ 서버 구동시 필요한 여러 기능 제공 

> [!INFO] 설치 
> `pip install flask`
> 

### 개념
> 적은 노력으로 많은 작업(웹 페이지, API 서버 구축)을 할 수 있는 도구 

**✔마이크로 프레임워크이다.**
- 필수 기능만 제공 ex. 라우팅, 렌더링 등 
	- 추가로 필요한 기능이 있으면 그 때 확장 `pip install`
- 자유도가 매우 높다

**✔ 주요 클래스 - 뒤의 preview 참고** 

| 용어                | 설명               |
| ----------------- | ---------------- |
| `Flask`           | 웹 서버를 만들기 위한 클래스 |
| `@app.route()`    | URL 경로를 지정하는 것   |
| `run()`           | 서버 실행 메서드        |
| `request`         | 요청 처리            |
| `render_template` | HTML 템플릿 렌더링용 도구 |



### preview - 간단한 실행
#### 기본 
```python
from flask import Flask
app = Flask(__name__) 

@app.route('/')
def hello_world():
    return 'Hello, World!'

app.run()
```
- 파이썬은 라우터 설정하고 run() 흠 일단 ok 
- 포트 
	- 파이썬의 기본 포트 = 5000
	- 만약 바꾸고 싶다면 `app.run(port=5001)`
- `app = Flask(__name__)` : Flask 클래스의 인스턴스를 만들어서 웹 서버를 구성하는 핵심 객체(app를 만든다는 뜻 (Flask 앱 인스턴스 생성 + 자동 경로 설정)

>[!tip] 파이썬의 내장 변수 - `__name__`
>파이썬을 보다보면 이런 문장이 많이 보인다.
>얼핏 실행해보기에는 있으나 없으나 큰 차이가 없어보인다.
>ex. `Flask(__name__) == Flask(파일명)  ex. Flask(app.py)
>하지만 이 옵션이 필요한 이유가 몇 가지 있다.
>- 역할 : 라우팅 및 설정 support
>- Flask는 내부적으로 static, teplate 경로 등을 자동으로 설정할 떄 `__name__`값을 기준으로 현재 위치를 추적한다.
>- 즉, 파이썬에서 현재 실행중인 모듈의 위치를 기준으로 **경로를 자동으로 잡아주는** 역할을 한다.
>- 이 파일이 직접 실행되는 경우 ➡ `__name__ = __main__`
>- 다른 파일에서 import되는 경우 ➡ `__name__ =` **"파일명"**

>[!Warning] 만약 Flask("app") 이렇게 썼다면??
>- 이 방식은 직접 문자열을 써서 경로를 잡으려했다.
>- 이 방식으로 한다면 static이나 template에서 경로를 잡으려하기 때문에 잘못된 경로 설정이 될 수 있다.



#### 디버깅 모드로 실행시키기 
일반적으로 서버를 실행시키고 코드를 바꾸면 바로 반영이 안된다.
이럴 때, 파이썬에서는 **디버그 모드**(스프링에서는 devtools였나??)로 설정하면 **코드 변경이 실행중인 서버에 반영**된다. 
```python
app.run(debug=True)
```


### 라우팅 
#### 개념 
- 네트워크에서 경로를 선택하는 프로세스
- Client **요청 URL을 기준으로 어떤 함수를 실행할지를 결정하는 매핑**(mapping) 규칙 
- 즉, 어떤 URL로 접근했을 때 ➡ 어떤 함수로 연결할지를 정해주는 역할 
- 이로 인해, URL 별 다양한 처리 방식 가능
```python
@app.route('/')
def hello_world():
    return 'Hello, World!'
```

> 일종의, URL 과 함수를 연결짓는 매개체

> [!INFO] 라우터 
>URL과 함수를 연결해주는 것 
>Flask는 기본적으로 라우터 객체가 따로 없고 @app.route()로 직접 경로를 지정 
>But 규모가 커지면 Blueprint라는 것을 쓴다내


Flask는 기능도 몇 개 없어서 라우팅 할 줄 알면 Flask의 절반은 안 것 

#### 동적 라우팅 
그 스프링에서 pathvariable 이랑 똑같은거 기호가 < > 이걸 쓰네 
```python
@app.route('/users/<id>/)
def find(id):
		return "user" + id;
```

> [!WARNING]
> ⚠️ Flask의 route는 슬래시`/` 에 아주 민감한 프레임워크
> 스프링에서는 슬래시`/` 대충 써도 상관 없었는데 Flask는 아니네 


#### 렌더링 - render_template
```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')
```

>[!EXAMPLE] render_template("파일명")
>- Flask내부의 템플릿 엔진을 사용해서 template/ 폴더 안에 있는 파일명의 파일을 읽어온다.
>- 즉, 자동으로 templates 폴더를 찾아주고 파일 매핑해준다는 것 
>- 추가 동적 주입
>	- 만약 index.html 에 `{{ name }}`이라는 문장이 있으면 이는 동적으로 주입해야 하는 것이다.
>	- 이 떄 render_template으로 동적 주입이 가능하다
>```python 
>render_template('index.html', name = "craft") 
>```


#### static 폴더 매핑 
> static 폴더에 있는 이미지를 index.html에서 사용하기 위한 방법에는 여러 종류가 있다.

1. **하드 코딩 방법** 
```html
<body>
    <h1>서버를 만들었다!</h1>
    <img src = "../static/flow.png" />
</body>
```


2. **url_for() - flask에서 권장하는 방법**  ⭐⭐
```html
<body>
    <h1>서버를 만들었다!</h1>
    <img src = "{{ url_for('static', filename='flow.png') }}"/>"
</body>
```
- static 폴더의 flow.png라는 파일의 경로를 img로 설정
- Flask는 자동으로 이 경로를 만들어주는데,
- 이렇게 하면, static폴더가 어디에 있든, html파일이 어디에 있든 정확한 경로로 반환한다.
> 정확하고 유지 보수에 편리한 방식 


흠.. 장고는 다른 방식 쓰네 

#### request - Flask의 객체 
> request는 Flask에서 제공하는 HTTP 요청 정보를 담은 객체 

```python
from flask import Flask, request, jsonify
```
- 위처럼 flask 패키지에서 import하면 됨 
- 역할 
	- 클라이언트가 요청한 데이터를 읽을 때 사용한다
	- ex. 파라미터, Body, 헤더 등 

- request 활용 예시 
```python
request.args.get('title') ➡ GET의 URL 파라미터 값
request.form.get('title') ➡ POST의 form 데이터
request.json ➡ POST의 JSON 데이터
```

```python
@app.route("/test", methods=["GET"])
def test_get():
    name = request.args.get("name")
    print(f"요청된 이름은 {name}입니다.")
    return jsonify({"result": "success", "name": name})
```



