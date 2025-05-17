
MongoDB라는 프로그램을 조작하기 위해서는 특별한 라이브러리인 `pymongo`가 필요 
`pip install pymongo`


### 기본 - 객체 생성, 서버 연결, Insert
```python
from pymongo import MongoClient
# MongoClient는 MongoDB 서버와 연결하는 클라이언트 객체를 생성하는 클래스

client = MongoClient('localhost', 27017)
# MongoDB 서버에 연결.
# localhost는 기본값이며, 27017은 MongoDB의 기본 포트

db = client.jungle
# jungle이라는 DB를 만든다.
  
# users라는 컬렉션에 {'name': 'John', 'age': 30}이라는 문서를 추가한다.
db.users.insert_one({'name': 'John', 'age': 30})
db.users.insert_one({'name': 'Charles', 'age': 26})
db.users.insert_one({'name': 'Carrel', 'age': 23})

all_users = list(db.users.find({}))
print(all_users)
```

### 여러 메서드 - find, update
```python
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.jungle

  
# 여러개 찾기 find() : 조건에 맞는 모든 문서를 가져온다.
# db.users.find({}) : users 컬렉션에서 모든 문서를 가져온다.
all_users = list(db.users.find({})) # {} 조건 없이 모두
print(all_users)
print(all_users[0])
print(all_users[0]['name'])
print(all_users[0]['age'])

  
# find_one() : 조건에 맞는 첫 번째 문서만 가져온다.
user = db.users.find_one({'name': 'John'})
print(user)

# find_one의 두 번째 인자 : 프로젝션 => 어떤 필드를 포함하고 제외할지를 결정
user2 = db.users.find_one({'name': 'John'},{'_id': False, 'name': False})
print(user2)


# 수정하기
# db.people.update_many(찾을조건,{ '$set': 어떻게바꿀지 })
db.users.update_many({'name': 'Carrel'}, {'$set': {'age': 2222}})
carrel = db.users.find_one({'name': 'Carrel'})
print(f"{carrel['name']}의 나이는 {carrel['age']}입니다.")

# 삭제하기
db.users.delete_one({'name': 'Carrel'})
```



### 영화 스크래핑 후 DB 저장 

>[!SUCCESS]  미션 
>영화 랭킹 사이트가서 title, 출시연도, 러닝타임, 등급 스크래핑 후 MongoDB에 저장 

#### 내 정답 
```python
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36"
}

client = MongoClient("localhost", 27017)
db = client.movie_db

def calculate_running_time(running_time_string):
    running_time_before_split = (
        running_time_string.replace("h", "").replace("m", "").strip()
    )
    hours, minutes = running_time_before_split.split(" ")
    return int(hours) * 60 + int(minutes)

def make_movie_doc():

    url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
    res = requests.get(url, headers=header)
    soup = BeautifulSoup(res.text, "lxml")
    movies = soup.select(".ipc-metadata-list .cli-parent .cli-children")
    print("movies 개수 : ", len(movies))

    for movie in movies:
        title = movie.select_one("h3").text
        metadatas = movie.select(".cli-title-metadata-item")
        released_year = metadatas[0].text
        running_time = calculate_running_time(metadatas[1].text)
        pg_level = metadatas[2].text

        db.movies.insert_one(
           {
                "title": title,
                "released_year": released_year,
                "running_time": running_time,
                "pg_level": pg_level,
            }
        )

make_movie_doc()

all_movies = db.movies.find({})  # Cursor 객체를 반환
print(all_movies)  # 그냥 print하면 Cursor 객체의 주소값이 나옴
print(type(all_movies))  # <type 'pymongo.syncronous.cursor.Cursor'>
print(list(all_movies))  # Cursor 객체를 list로 변환하여 출력 or for문으로 돌리기

```

#### 모범 답안 
```python
import requests

from bs4 import BeautifulSoup
from pymongo import MongoClient           # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbjungle                      # 'dbjungle'라는 이름의 db를 만듭니다.


def insert_all():
    # URL을 읽어서 HTML를 받아오고,
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get('https://www.imdb.com/chart/top/?ref_=nv_mv_250', headers=headers)
    
    # HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
    soup = BeautifulSoup(data.text, 'html.parser')

    # select를 이용해서, li들을 불러오기
    movies = soup.select('.ipc-page-grid__item--span-2 > .ipc-metadata-list--base > li')
    print(len(movies))

    # movies (li들) 의 반복문을 돌리기
    for movie in movies:
        # movie 안에 a 가 있으면,
        # (조건을 만족하는 첫 번째 요소, 없으면 None을 반환한다.)
        tag_element = movie.select_one('.ipc-title-link-wrapper > h3')
        if not tag_element:
            continue

        # 영화번호.영화 제목 가져오기.
        # 영화 타이틀은 "1. 쇼생크 탈출"과 같이  ". " 으로 
        # 구분되어 있으므로 ". " 을 기준으로 split 한 뒤 index가 1인 요소에 접근한다.
        title = tag_element.text.split(". ", 1)[1]

        # 영화 개봉 연도 가져오기
        released_year = movie.select_one('.cli-title-metadata-item:nth-child(1)').text
        # 영화 개봉 연도의 타입을 int로 변환
        released_year = int(released_year)

        # 영화 상영시간 가져오기
        running_time = movie.select_one('.cli-title-metadata-item:nth-child(2)').text

        # 영화 상영시간 분으로 변환하기
        # 1. running_time에서 'h'와 'm'을 제거
        running_time = running_time.replace("h", "").replace("m", "")  # "2 55"로 변경

        # 2. 공백으로 나누기
        hours, minutes = running_time.split(" ")  # "2"와 "55"로 분리

        # 3. 문자열을 숫자로 변환
        hours = int(hours)
        minutes = int(minutes)

        # 4. 시간과 분을 계산
        running_time_minutes = hours * 60 + minutes

        # 영상물 등급 가져오기
        pg_level = movie.select_one('.cli-title-metadata-item:nth-child(3)').text

        doc = { 
            'title': title,
            'released_year': released_year,
            'running_time': running_time_minutes,
            'pg_level': pg_level,
        }
        db.movies.insert_one(doc)
        print('완료: ', title, released_year, running_time, pg_level)


if __name__ == '__main__':
    # 기존의 movies 콜렉션을 삭제하기
    db.movies.drop()
    # 영화 사이트를 scraping 해서 db 에 채우기
    insert_all()
```




#### 모범 답안과의 비교 
##### 1.  `:nth-child(숫자)` vs `[숫자]` 
```python
모범 답안 
running_time = movie.select_one('.cli-title-metadata-item:nth-child(2)').text

나의 답안 
running_time = movie.select(".cli-title-metadata-item")[1].text 
```
**`:nth-child(숫자)` 의미** 
- 부모 요소의 자식 중에서 n번째 위치한 요소 
- 1‍⃣ movie라는 부모의 자식 요소 중 2번쨰에 위치한 요소  
  2‍⃣ .cli-title-metadata-item 이 클래스명인 요소 

**내가 쓴 [1] 방법** 
- 리스트에서 2번째 요소 
- 간결함, 직관적, 
- **단점** 
	- 구조에 변화 민감도 높다 
	- 코드를 보고 의도 파악하기 힘들다 
	- 예외 발생 가능성 높다
		- 모범답안의 경우 없을 경우 None을 반환하는데 나의 답안은 IndexError 발생 가능 


> 그니까, [숫자] 이 방법이 명시성-유연성이 너무 떨어지므로, `:nth-child(n)` 추천 
> nth ➡  n + th  ➡ n 번쨰 



##### 2.  `if __name__ == '__main__'`

**`__name__ == '__main__'` 의미** 
- 파이썬 파일이 실행될 때 `__name__`이라는 특별한 변수가 자동으로 설정된다.
- 이 파일을 **직접 실행한** 경우 `__name__` : `__main__`
- 이 파일을 **모듈로 import한** 경우 `__name__` : `파일 이름`

목적 
- 직접 실행할 떄만 특정 코드를 실행하기 위해 
- 즉, 모듈로 재사용할 떄는 실행되지 않도록 하기 위해 
- DB drop은 위험한 것이므로 이렇게 보호한 듯??



###  조회 및 update
```python
from pymongo import MongoClient
client = MongoClient("localhost", 27017)
db = client.movie_db


# 영화 제목으로 영화 정보 찾기
target_movie = db.movies.find_one({"title": "쉰들러 리스트"})
print(target_movie["released_year"])

  
# 저장된 영화들의 title을 출력
movies = list(db.movies.find({}))
for movie in movies:
    print(movie["title"])

# update
db.movies.update_one({"title": "매트릭스"}, {"$set": {"title": "매트릭스2"}})
  
metrics = db.movies.find_one({"title": "매트릭스2"}, {"_id": False})
print(metrics)
```


