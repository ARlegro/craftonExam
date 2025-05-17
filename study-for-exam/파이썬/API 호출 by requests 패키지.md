>[!SUCCESS]  파이썬으로 간단한 API 호출해보기

백엔드는 자바만 쓰다가 파이썬 써보니까 이렇게 편할수가...

미세먼지 실시간 정보 제공해주는 url에 GET 요청하는건데 
이게 끝이다.......
```python
import requests

r = requests.get("http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99")

rjson = r.json()

rows = rjson['RealtimeCityAir']['row']

for row in rows:
  print(row["IDEX_MVL"])
```

get.... json()... 끝????

>[!QUESTION] 궁금증 
아직 좀 더 파이썬을 알아봐야 하겠지만, 
변수 설정도 무슨 타입인지 설정도 안하네
예외 처리는 어떻게 할까??

