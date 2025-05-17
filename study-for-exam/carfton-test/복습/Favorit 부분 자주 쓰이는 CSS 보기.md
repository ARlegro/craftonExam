
## 부트스트랩 부분 

>[!tip] mx-auto`, `d-flex`, `btn`, `btn-group`, `btn-primary, w-100, justify-content-end

- 이 클래스들은 **Bootstrap 4/5**의 대표적인 **유틸리티 클래스*

| 클래스명                | 의미                                              |
| ------------------- | ----------------------------------------------- |
| **mx-auto**         | **좌우 마진 자동 → 가운데 정렬**                           |
| **d-flex**          | display: flex 적용                                |
| `btn`               | 기본 버튼 스타일                                       |
| btn-primary         | 파란색 기본 버튼                                       |
| **btn-group**       | **버튼을 묶어서 한 줄로 정렬**                             |
| w-100               | `width: 100%` → 부모 요소(`.sorter-box`) 너비를 전부 사용함 |
| justify-content-end | flex item(자식 요소들)을 **오른쪽 정렬**                   |

## Bulma 부분 

```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.8.0/css/bulma.min.css"/>
```

>[!tip] hero-body, container, subtitle, title

- `hero-body`, `hero`, `title`, `subtitle`, `container` 이 조합은 **Bulma**라는 CSS 프레임워크에서 제공
- 이 코드에는 아래 링크처럼 Bulma가 포함되어 있었지:

```html
<section class="hero is-warning">   
		<div class="hero-body">     
				<div class="container">
				       <h1 class="title">제목</h1>
								<h2 class="subtitle">부제목</h2>     
				</div>
		 </div>
</section>`
```


### 1. `hero`
- **전체 페이지 또는 섹션을 강조**할 때 쓰는 큰 영역(히어로 영역)을 만드는 데 사용.
- 일반적으로 `is-primary`, `is-warning`, `is-dark` 등의 색상 클래스와 함께 사용됨.

```html
<section class="hero is-warning">...</section>
```
- `is-warning`: 노란색 배경을 적용.
    
---
### 2. `hero-body`

- `hero` 내부에서 **본문 내용이 들어가는 부분**.
- 내부에 `container`, `title`, `subtitle` 같은 콘텐츠가 위치함.

```html
<div class="hero-body">...</div>
```

---

### 3. `container`

- Bulma에서 콘텐츠의 **가로폭을 일정하게 제한**해주는 클래스.    
- Bootstrap에도 동일한 개념이 있지만, Bulma에서도 사용됨.
```html
`<div class="container">...</div>`
```
- 브라우저 너비가 커도 콘텐츠가 지나치게 넓어지지 않도록 **가운데 정렬 + 가로폭 제한** 효과


--- 
### 4. icon
> 참고 : https://bulma.io/documentation/elements/icon/
 
![[Pasted image 20250514151157.png]]
```html
<span class="icon">
  <i class="fas fa-trash"></i>
</span>
```


```html
<span class="icon-text">
  <span class="icon">
    <i class="fas fa-home"></i>
  </span>
  <span>Home</span>
</span>
```






현재 HTML 코드에서는 링크(`<a>` 태그)에만 `text-primary` 색상이 적용되어 있어서 아이콘과 텍스트가 모두 같은 색상으로 표시됩니다. 아이콘만 다른 색상으로 강조하려면 아래와 같이 수정하세요:

```html
<!-- 아이콘에 빨간색(danger) 적용 예시 -->
<a href="#" class="text-primary trash-btn" data-id="${_id}">
  <i class="fas fa-trash text-danger"></i> 휴지통으로!
</a>

<!-- 아이콘에 주황색(warning) 적용 예시 -->
<a href="#" class="text-primary trash-btn" data-id="${_id}">
  <i class="fas fa-trash text-warning"></i> 휴지통으로!
</a>
```

Bootstrap에서 사용할 수 있는 주요 색상 클래스:

- `text-primary`: 파란색 (기본 테마색)
- `text-secondary`: 회색
- `text-success`: 녹색
- `text-danger`: 빨간색
- `text-warning`: 노란색/주황색
- `text-info`: 하늘색
- `text-dark`: 검정색에 가까운 색