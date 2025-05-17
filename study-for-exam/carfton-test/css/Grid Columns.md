


column들을 다룰떄 미리 정의해야하는 것이 columns이다
```html
<div class="columns">
	~~~ column 여러개 
</div>
```
이 안에서 column들이 사용?

3개의 content를 넣는다고 가정할 때 각 content는 자신만의 div 요소를 갖고, 각자 column클래스를 갖는다.


하나의 div는 12개의 column grid를 갖는다.
지정안하면 자동으로 나눠지지만
어던 요소에 몇 grid를 넣을지는 지정할 수 있따.

column 주는 법
```html
<div class="column is-2">

<div class="column is-5">
```



card안에 card-content로 감싼다음에 media 구조로 감싸기 


### 가로 정렬 카드 만들기

>[!tip] Card로 감싸기 ➡ Card-Content로 감싸기 ➡ Columns로 감싸고 Column마다 is-? 부여

![[Pasted image 20250515174717.png]]

```html
  <section class="section">
    <div class="container">
      <h3 class="title has-text-centered is-size4">Related Products</h3>
      <div class="card">
        <div class="card-content">
          <div class="columns">
            <div class="column is-4">
              <img
                alt="Product Image"
              />
            </div>
            <div class="column is-8">
              <p>$14</p>
              <p class="title is-size-5">Cortard Cup</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
```

### is-multiline 활용하기

- `is-multiline`은 Bulma의  **그리드 옵션 클래스**
- **자동 줄 바꿈** : 컬럼들이 한 줄을 넘어서 아래 줄로 내려갈 수 있게 해주는 속성
```html
<div class="columns is-multiline">
  <div class="column is-4">1</div>
  <div class="column is-4">2</div>
  <div class="column is-4">3</div>
  <div class="column is-4">4</div> <!-- 자동 줄바꿈되어 아래로 -->
</div>
```

> 참고 : 만약 최대 너비 제한 + 가운데 정렬이 필요하면 container 클래스랑 같이 쓰기 






### is-multiline 활용한 가로정렬 카드 만들기
![[Pasted image 20250516124022.png]]
>[!tip] 순서
>1. columns is-multiline의 div 만들기
>2. 1번 내부 card is-one-third 만들기 
>3. 각 card별 columns > 이미지 column + content column 부여

```html
    <section class="section">
      <div class="columns is-multiline">
        <div class="card is-one-third">
          <!-- 가운데 정렬 옵션 : is-vcentered -->
          <div class="columns">
            <div class="column is-4">
              <figure class="image">
                <img
                  src="https://movie-phinf.pstatic.net/20190115_228/1547528180168jgEP7_JPEG/movie_image.jpg?type=m665_443_2"
                  alt="Image"
                />
              </figure>
            </div>
            <div class="column is-8">
              <div class="card-content">
                <p class="title">카드 제목</p>
                <p class="subtitle">카드 부제목</p>
              </div>
            </div>
          </div>
        </div>
        <div class="card is-one-third">
          <!-- 가운데 정렬 옵션 : is-vcentered -->
          <div class="columns">
            <div class="column is-4">
              <figure class="image">
                <img
                  src="https://movie-phinf.pstatic.net/20190115_228/1547528180168jgEP7_JPEG/movie_image.jpg?type=m665_443_2"
                  alt="Image"
                />
              </figure>
            </div>
            <div class="column is-8">
              <div class="card-content">
                <p class="title">카드 제목</p>
                <p class="subtitle">카드 부제목</p>
              </div>
            </div>
          </div>
        </div>
```

> [!INFO]  추가 : card가 y축 가운데 정렬하게 만드는 옵션  ➡ is-vcentered
```html
<div class="columns is-vcentered">	
   		<div class="column is-4">
```






