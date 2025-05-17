
>[!EXAMPLE] 추가로 도입해본 것
>- is-max-tablet
>	- 한 row에 카드 한개라 tablet 정도 크기로 container크기 설정 
>- container로 전체 감싸서 반응형 
>- is-flex-wrap-nowrap : 절대 줄 바꿈 안되도록 
>- fullwidth로 버튼 늘리기
>- gap옵션을 통해 버튼간의 간격만 줄이기
>- **모바일 친화적 적용**  ⭐⭐⭐



## button 반응형으로 하나의 row에만

![[Pasted image 20250516192320.png]]
요구 사항 
- 3개의 버튼을 1줄에 
- 화면 크기가 늘어나면 반응형으로 button도 늘어나기 
- button사이 간격 줄이기 



#### 1. 절대 줄 바꿈 없도록 - is-flex-wrap-nowrap

```html
<div class="buttons is-centered is-flex-wrap-nowrap">
	<button
		....
```


#### 2. 버튼 각각 fullwidth 쓰기 

> is-fullwidth : 컨트롤 너비를 100% 채워서, 버튼 텍스트 길이가 달라도 균일한 크기를 유지


>[!warning] 적용 전

![[Pasted image 20250516194632.png]]



>[!tip] 적용 후 


```html
<div class="buttons is-centered is-flex-wrap-nowrap">
  <button id="sort-likes"   class="button is-primary is-fullwidth">
	  좋아요 순으로 정렬
	</button>
  <button id="sort-viewers" class="button is-warning is-fullwidth">
	  누적관객수 순으로 정렬
	</button>
  <button id="sort-date" class="button is-info is-fullwidth">
	  개봉일 순으로 정렬
	</button>
</div>
```

![[Pasted image 20250516191255.png]]




#### 3. 간격 줄이기 : gap 옵션 
#gap #items간격 

```css
.buttons {
	gap: 0.3rem;

}
```
- gap 속성 : item(button)들 사이의 간격을 설정하는 css속성
- margin을 설정하면 좌우로 설정이 되어서 item들 사이가 아닌 양 끝에 영향을 준다.
- But gap속성을 사용하면 grid or flex 내부 item들간의 간경만 줄일 수 있다.
- gap 종류
	- gap : 행+열 둘 다의 간격 지정
	- row-gap : 행 사이의 간격만 지정
	- column-gap : 열 사이의 간격만 지정

bulma에서 기본적으로 제공하는 button에는 간격이 좀 넓다보니 gap속성을 따로 써야 할 경우가 올 것이다. 위처럼 직접 css를 설정할 수도 있고 아래처럼 bulma에서 제공하는 속성값을 활용할 수도 있다.
```html
<div class="columns is-variable is-1">
```



## 수평 카드 만들기 (only bulma)

 #row #card #columns #is-4

bulma는 bootstrap과 달리 수평 카드가 document에 적혀있지 않다.
따라서, columns + row 조합을 써서 분리해야 한다

(설계도)
![[Pasted image 20250516194352.png]]

```html
            <div class="card">
              <div class="row">
                <div class="columns">
                  <div class="column is-4">
                    <figure class="image">
                      <img
                        src=""
                        alt="Movie Poster"
                      />
                    </figure>
                  </div>
                  <div class="column is-8">
                    <p class="title">영화 제목:</p>
                    <span class="icon-text">
                      <span class="icon">
                        <i class="fas fa-thumbs-up" style="color: red"></i>
                      </span>
                      <span>좋아요 수</span>
                    </span>
                    <p class="text">누적 관객수:</p>
                    <p class="text">개봉일:</p>
                  </div>
                </div>
              </div>
              <div class="row">
                <div id="card-btn" class="columns">
                  <div class="column is-6 has-text-centered">
                    <a
                      id="like-btn"
                      class="text-primary like-btn"
                      data-id="${_id}"
                    >
                      <i class="fas fa-thumbs-up"></i>
                      <span>위로!</span>
                    </a>
                  </div>
                  <div class="column is-6 has-text-centered">
                    <a id="trash-btn" class="text-primary" data-id="${_id}">
                      <i class="fas fa-trash"></i>
                      <span>휴지통으로!</span>
                    </a>
                  </div>
                </div>
              </div>
```



## 카드 내 글자 간 간격 줄이기 
#m속성 

bulma 클래스인 my-* 옵션을 써서 줄이기 

### 현재 문제 
> 글자 간 위 아래 간격이 너무 좁다
> 물론 css에서 margin을 따로 설정할 수 있지만 프레임워크를 최대한 활용하고자 bulma의 margin관련  속성 활용

![[Pasted image 20250516195020.png]]


### 마진 적용 시 

```html
<div class="column is-9">
	<p class="title">영화 제목</p>
	<span class="icon-text">
		<span class="icon">
			<i class="fas fa-thumbs-up" style="color: red"></i>
		</span>
		<span class="mb-2">좋아요 수</span>
	</span>
	<p class="text mb-2">누적 관객수:</p>
	<p class="text mb-2">개봉일:</p>
</div>
```

![[Pasted image 20250516195449.png]]


>[!tip] 추가로 : 이미지 사이즈 고정시키고 가운데 정렬 시킨 속성들

```html
		<div class="column is-3 is-flex is-justify-content-center">
			<figure class="image is-128x128">
```


# 모바일 친화적으로 리팩토링 


## columns 모바일 버전 및 카드 세로 정렬 
> is-mobile, is-vcentered
```html
<div class="columns is-mobile is-flex-wrap-nowrap is-vcentered">
  <div class="column is-3">
    <figure class="image is-128x128">
      <img src="…" alt="Movie Poster">
    </figure>
  </div>
  <div class="column is-9">
    <p class="title">영화 제목</p>
    …
  </div>
```
- is-miobile : 모바일에서도 flex 유지시켜주는 속성
	- 💢근데 `is-mobile` 은 columns 전용이다. columns없으면 불가능 
- is-vcentered : 세로 정렬(중간 높이에) = align-items: center


## 카드 - Media 도입 


#### 도입 이유 
화면이 줄어들 때 이미지의 위치와 크키가 이쁘지 않아서 이를 해결해줄 방법을 모색중 
마침 bulma에서 제공해주는 Media 속성을 활용하면 가능할 것으로 판단

#### Media 속성이란?

**✔ 샘플 사진** 
![[Pasted image 20250516231148.png]]
Media 속성을 활용하면 사진처럼 될 수 있다.
이는 Card의 가로정렬 같은 결과 

**✔ 샘플 코드** 
```html
<article class="media">
  <figure class="media-left">
    <p class="image is-64x64">
      <img src="https://bulma.io/assets/images/placeholders/128x128.png" />
    </p>
  </figure>
  <div class="media-content">
    <div class="content">
```

✔ 주요 속성 
- media
- is-vcentered
- media-left
	- 왼쪽에 올거를 정한다.
- media-content




#### 변화 후 코드 
```html
 <div class="card">
		<div class="row">
			<article class="media">
				<div class="columns is-mobile is-vcentered">
					<figure class="media-left column is-4">
						<p class="iamge">
							<img
								src=""
								alt="movie image"
							/>
						</p>
					</figure>
					<div class="medi-content column is-8">
						<p class="title">영화 제목</p>
						<span class="icon-text">
							<span class="icon">
								<i class="fas fa-thumbs-up" style="color: red"></i>
							</span>
							<span>좋아요 수</span>
						</span>
						<p class="text">누적 관객수:</p>
						<p class="text">개봉일:</p>
					</div>
				</div>
			</article>
		</div>
```


**✔샘플코드와 다른** 
- 샘플코드와 달리 img 태그에 이미지 크기를 설정하지 않았다. 
- 그 이유는 이미지가 일정 크기로 고정되는 것보다 유동적으로 card의 1/3크기를 차지하도록 설정하고 싶었기 때문이다
- 따라서 media-left 속성과 더불어 columns를 활용한 css 스타일링을 했다.



#### 결과 

![[Pasted image 20250516220116.png]]


## 버튼 줄바꿈 없이 크기 조절

### 1. 버튼 크기 조절 
현재 코드에서는 모바일 화면같이 작은 화면에서 버튼이 잘리는 현상이 나타난다
#### 문제 상황과 문제 코드 

**✔ 문제 상황** 

![[Pasted image 20250516214417.png]]

**✔문제 코드** 
```html
<div class="container is-max-tablet">
	<div class="sorter-box">
		<div class="buttons **is-centered is-flex-wrap-nowrap**">
			<button
				id="sort-likes"
				class="button is-danger is-fullwidth has-text-weight-bold"
>
				좋아요 순으로 정렬
			</button>
			<button
				id="sort-viewers"
				class="button is-warning is-fullwidth has-text-weight-bold"
>
				누적관객수 순으로 정렬
			</button>
			<button
				id="sort-date"
				class="button is-info is-fullwidth has-text-weight-bold"
>
				개봉일 순으로 정렬
			</button>
		</div>
```

절대 100% 너비”(`is-fullwidth`)를 물고 있기 때문에, 줄바꿈 없이 한 줄에 그대로 꽉 차려다 보니 화면이 줄어들면 잘려 버리는 거

#### 해결 

우선, is-fullwidth 속성을 없애고 css 속성을 재정의한다.
```css
.buttons .button {
	flex: 1;
	min-width: 0;
```
메인 해결 속성 ➡ flex: 1 
- flex 속성 : 남는 공간을 어떻게 나눌지를 결정 
- flex: 1 ➡ 버튼들이 남는 공간을 1:1비율로 나눠서 가진다.
- Bulma의 buttons는 기본적으로 display:flex가 정의되어있어 각 button에 flex:1 속성을 주면 남은 공간을 균등하게 나눔 

추가 : min-width: 0 
- flex 컨테이너의 최소 너비를 해제한다



### 2. 버튼 내 글자 조절 

#### 문제의 상황
![[Pasted image 20250516215115.png]]

앞서 버튼의 크기가 유연하게 변경되지 않는 문제는 해결했지만, 버튼 내 텍스트가 줄바꿈되지 않아 위의 사진처럼 텍스트가 잘려 보이는 문제가 발생했다.


#### 해결 - 텍스트 줄 바꿈 허용
> CSS를 오버라이드

기본적으로 Bulma의 기본 버튼스타일은 white-space: nowrap 으로 줄바꿈을 허용하지 않는다.
따라서, 이를 덮어씌어서 줄바꿈을 가능하게 설정하면 된다.

```CSS
.buttons .button {
	display: flex;
	flex: 1;
	min-width: 0;
	white-space: normal; /* 기본 nowrap 해제 */
	word-break: keep-all; /* 단어 단위로 줄바꿈 */
}
```
메인 해결 : white-space: normal 
- nowrap을 해제하면 기본적인 문제는 해결된다

추가 : word-break
- 문장이 아닌 단어 단위로 바꾸고 싶을떄 쓰는 옵션 

display: flex : 내부 텍스트를 유연하게 정렬하기 위해 설정 


해결 후 
![[Pasted image 20250516215505.png]]