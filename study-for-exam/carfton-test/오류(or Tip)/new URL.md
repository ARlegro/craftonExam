
> js가 제공하는 URL 인터페이스 



```javascript
function isValidUrl(url) {

  try {
    new URL(url);
    return true;
  } catch {
    return false;
  }
}

function submitMemo(e) {
  e.preventDefault();

  const url = $("#input-url").val();
  const comment = $("#input-comment").val();

  if (!isValidUrl(url)) {
    alert("유효하지 않은 URL입니다.");
    $("#input-url").focus();
    return;
  }
```


- e.preventDefault()를 써서 HTML에서 URL 검증 못한 이슈
- new URL 써서 올바른 URL 문법인지 검증 

