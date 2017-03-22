// loadPostList ajax요청의 response data에 'next'값이 있으면 해당 값을 할당해 놓을 변수
var next;

// PostList GET요청 API함수
function loadPostList() {
  // 첫 loadPostList API요청 URL
  var url = 'http://localhost:8000/api/post/';

  // next값이 있다면 요청 url은 해당값을 사용한다
  if(next != undefined && next != null) {
    url = next;
  }
  console.log(url);
  $.ajax(url)
  .done(function(data) {
    // ajax요청의 응답에서 next값을 가져와 변수에 할당
    next = data.next;
    // 응답의 results를 results의 길이만큼 순회하며
    for(var i = 0; i < data.results.length; i++) {
      // 매 loop마다 results[i(인덱스)]의 값을 curPost변수에 할당
      var curPost = data.results[i];
      // curPost를 사용해서 addArticle함수를 실행 (post-list-container내부에 append)
      addArticle(curPost);
    }
  })
  .fail(function(data) {
    console.log('fail');
    console.log(data);
    $('.content-container').append('<div>Fail!</div>');
  });
}
