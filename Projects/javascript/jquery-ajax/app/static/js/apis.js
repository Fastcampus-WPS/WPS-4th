function obtainAuthToken(username, password) {
  url = 'http://localhost:8000/api/member/token-auth/';
  $.ajax({
    url: url,
    method: 'POST',
    data: {
      username: username,
      password: password,
    }
  })
  .done(function(data) {
    var token = data.token;
    setCookie('instagramToken', token);
  })
  .fail(function(data) {

  });
}


function postCreate() {
  var url = 'http://localhost:8000/api/post/';
  var token = 'Token ' + getCookie('instagramToken');
  console.log(token);
  $.ajax({
    url: url,
    method: 'POST',
    headers: {
      Authorization: token,
    }
  })
  .done(function(data) {
    console.log(data);
  });
}
