
몇 가지 카드만 깨진 채로 보이는 건, 저장된 URL 자체가 잘못된 게 아니라 **원호스트(네이트 뉴스)의 ‘핫링크 방지(Referrer 검사)’** 때문에 브라우저가 이미지를 거부하는 경우가 많아 발생하는 현상이야.  
직접 URL을 주소창에 넣었을 땐 referer 헤더가 없거나 허용된 상태이니 이미지가 잘 뜨지만, 너의 페이지에서 `<img src="…">` 로 불러올 때는 referer가 `http://localhost:5001` 등으로 설정돼서 차단되는 거지.


>[!tip] 해결방법 - html head부분에 아래 코드 넣기 
```html
<meta name="referrer" content="no-referrer">`
```

