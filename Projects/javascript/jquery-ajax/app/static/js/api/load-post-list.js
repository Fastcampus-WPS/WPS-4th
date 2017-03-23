// loadPostList ajax요청의 response data에 'next'값이 있으면 해당 값을 할당해 놓을 변수
var next;
var isLoading = false;
var url = 'http://localhost:8000/api/post/';

// 스크롤 이벤트를 감지, 하단으로부터 100px미만 위치까지 스크롤되면 loadPostList를 실행
$(window).scroll(function() {
   if($(window).scrollTop() + $(window).height() > $(document).height() - 100) {
     if(isLoading == false) {
       loadPostList();
     }
   }
});

// PostList GET요청 API함수
function loadPostList() {
  isLoading = true;
  $('.post-list-container').append('<div class="loading">Loading...</div>');

  // next값이 있다면 요청 url은 해당값을 사용한다
  if(url == undefined && url == null) {
    return;
  }
  console.log(url);
  $.ajax(url)
  .done(function(data) {
    // ajax요청의 응답에서 next값을 가져와 변수에 할당
    url = data.next;
    // 응답의 results를 results의 길이만큼 순회하며
    for(var i = 0; i < data.results.length; i++) {
      // 매 loop마다 results[i(인덱스)]의 값을 curPost변수에 할당
      var curPost = data.results[i];
      // curPost를 사용해서 addArticle함수를 실행 (post-list-container내부에 append)
      addArticle(curPost);
    }
    isLoading = false;
    $('.post-list-container').find('.loading').remove();
  })
  .fail(function(data) {
    console.log('fail');
    console.log(data);
    $('.content-container').append('<div>Fail!</div>');
  });
}
