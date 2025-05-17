

>[!tip] p,m 뒤에 오는 것들의 종류 
>- y : 위아래
>- x : 좌우
>- t : 탑
>- r : 오른쪽
>- b : 아래
>- l : 좌측


### 패딩  
#px  #py 
```html
    <h1 class="py-6">Hello, Bulma</h1>
    <h1 class="">Hello, Bulma</h1>
```
- py : padding + y절 ➡ 위 아래로 padding공간 생기게 하겠다는 뜻 
- 1~6 : 6이 가장 크기 큼
		![[Pasted image 20250515164709.png]]
- px : 좌우로 padding 




### 마진 
#mx #my

#### 위아래 - my 
```html
    <h1 class="my-1">Hello, Bulma</h1>
```
- my : margine + y절 ➡ 위 아래로 마진 남기겠다
- 1~6 :

>[!QUESTION] 마진 vs 패딩
>둘 다 간격 벌리는건데 뭐가 다를까?
>- `margin` : 상자 자체가 주변에서 떨어지게 만드는 바깥 여백
>- `padding` : 상자 안의 콘텐츠가 상자 테두리에서 떨어지는 안쪽 여백이에요.
>- |항목|마진 (`margin`)|패딩 (`padding`)|
|---|---|---|
|**무엇과의 거리?**|**바깥 요소**와의 거리|**내부 콘텐츠**와의 거리|
|**적용 위치**|요소 **외부**|요소 **내부**|
|**겹침 여부**|마진은 **겹칠 수 있음** (margin collapse)|패딩은 겹치지 않음|
|**배경색 영향**|마진은 배경색과 무관|패딩은 배경색이 채워짐|
|**Bulma 예시**|`my-4`, `mx-3` 등|`py-5`, `px-2` 등|


### section class  - 컨테이너 같은 

bulma의 section클래스는 기본으로 패디을제공해준다
```html
  <section class="section">
    <p>
      Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quam, officia.
    </p>
  </section>
```


![[Pasted image 20250515170629.png]]

### 가운데 정렬하기 - container

> class=container ➡ Auto Margin 기능이 있다.(width도 auto)

![[Pasted image 20250515170947.png]]
```html
  <section class="section">
    <div class="container">
      <p>
        Lorem ipsum dolor, sit amet consectetur adipisicing elit. Nihil
        accusamus dicta debitis. Necessitatibus, aliquid illo nostrum nihil
        voluptate soluta reprehenderit quae odit, at quisquam officiis. Optio
        consectetur dolores odit voluptatibus!
      </p>
    </div>
  </section>
```

![[캡처_2025_05_15_17_11_33_930.png]]![[캡처_2025_05_15_17_11_41_410.png]]
- 첫 번째 사진 녹색 : section 패딩 
- 두 번쟤 사진 구역 : container

