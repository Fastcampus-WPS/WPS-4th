function obtainAuthToken(username, password) {
  var url = 'http://localhost:8000/api/member/token-auth/';
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
