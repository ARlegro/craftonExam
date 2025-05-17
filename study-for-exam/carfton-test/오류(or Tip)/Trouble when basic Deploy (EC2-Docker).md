---
dg-publish: true
dg-home: false
---

,

> [!EXAMPLE] **✔막혔던 부분 체크**
>
> - 컨테이너끼리 접근 시 사용할 포트 및 host명 헷갈렸던 점
> - docker 파일 내부 명령어 설정 (mongodb 헬스체크 + 순차 실행)
> - 인증관련 문제

> MONGO_URI=mongodb://jungle:pwd1234//mongo:27017/dbjungle

### 시작 전 참고 : 사용된 docker 파일들

#### Dockerfile

```Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir flask pymongo bs4 requests
#CMD ["python", "app.py"]
CMD ["sh", "-c", "python init_db.py && python app.py"]
```

#### docker-compose.yml

```yaml
services:
  my-server:
    build: .
    volumes:
      - movie-data:/app
    environment:
      - MONGO_URI=mongodb://jungle:pwd1234//mongo:27017/dbjungle
    ports:
      - "5000:5000"
    depends_on:
      my-db:
        condition: service_healthy

  my-db:
    image: mongo
    ports:
      - 27018:27017
    environment:
      MONGO_INITDB_ROOT_USERNAME: jungle
      MONGO_INITDB_ROOT_PASSWORD: pwd1234
    volumes:
      - mongo-data:/data/db
    healthcheck:
      test: ["CMD", "mongosh", "--eval", "db.adminCommand('ping')"]
      interval: 5s
      retries: 10
      start_period: 5s
     
volumes:
  mongo-data:
  movie-data:
```

### 복합적 문제 (포트 + 서버명)

> 참고 : - `mongodb://<user>:<password>@<host>:<port>/<database>?authSource=admin`

❌잘못된

```python
client = MongoClient("mongodb://jungle:pwd1234@mongo:27018/dbjungle")
```

- 이 코드는 2가지 문제가 동시에 존재한다.

**1‍⃣ 잘못된 호스트 이름 사용** : @mongo

- docker 컨테이너는 서로를 ⭐ **"서비스 이름"으로 DNS 조회**한다 ⭐
- docker-compose 에서 정의된 MongoDB 서비스 이름은 `my-db`이다
- 현재 잘못된 코드에서의 host명은 mongo로 적었다. 이는 존재하지 않는 컨테이너 이름이라 DNS 해석이 되지 않는 문제가 발생

**2‍⃣ 잘못된 포트 사용** : 27018

- 처음 생각
  - MongoDB 컨테이너와 application 컨테이너가 다르니까 27018:27017로 설정되어잇는 매핑에 따라 application이 27018로 포트를 접속해야하는 줄 알았다.
- **실제** ⭐
  - 다른 컨테이너라도 **'같은 네트워크'안에 있으면 내부 포트로 접근**해야 한다
  - 즉, 27018:27017의 27018은 도커 외부에서만 통하는 포트이다.

💚제대로

```python
client = MongoClient("mongodb://jungle:pwd1234@my-mongo:27017/dbjungle")
```

- 도커 컨테이너끼리 서로 조회하는 것이므로 host명을 서비스명으로
- 포트도 내부 포트로 접근하도록

### docker 파일 내부 명령어 설정 (mongodb 헬스체크 + 순차 실행)

> 검색하면 바로 stackoverflow에 나오는 부분이라 가볍게 패스

#### 몽고DB 헬스체크

```yaml
    healthcheck:
      test: ["CMD", "mongosh", "--eval", "db.adminCommand('ping')"]
     
      interval: 5s
      retries: 10
      start_period: 5s
```

#### 순차 실행

> 일단 특정 파이썬 파일을 실행시키고 그 다음 메인 파일을 실행시켜야 하는 상황

원래, 단순 하나 였다면

```yaml
CMD ["python", "app.py"]
```

2개 순차적 실행

```yaml
CMD ["sh", "-c", "python init_db.py && python app.py]
```

### 인증관련 문제

앱 실행 도중 발생한 오류

```
`pymongo.errors.OperationFailure: Authentication failed.`
```

- MongoDB의 사용자 인증에 실패한 것

❌잘못된

```python
client = MongoClient("mongodb://jungle:pwd1234@my-db:27017/dbjungle")
```

💚제대로 된

```python
client = MongoClient("mongodb://jungle:pwd1234@my-db:27017/dbjungle?authSource=admin")
```

이유 분석

> [!INFO] MongoDB URI인증 동작 방식
>
> 1. URI에 authSource가 있는지 확인 ➡ 있으면 admin 인증
> 2. authSource가 없다면 ➡ 접속하려는 DB(/jungle)에서 인증 시도

- 도커 파일을 보면 MONGO_INITDB_ROOT_USERNAME 되어 있다.
- 기본 **`MONGO_INITDB_ROOT_USERNAME` 설정을 통해 생성한 유저는** **"항상 admin DB에서 생성된다"**
  - 따라서, `authSource=admin`은 필수

```python
client = MongoClient("mongodb://jungle:pwd1234@my-db:27017/dbjungle?authSource=admin")
```
