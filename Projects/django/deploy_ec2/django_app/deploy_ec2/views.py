from django.http import HttpResponse


def index(request):
    return HttpResponse('''<html>
<body>
<h1>Hello, world!</h1>
<img src="http://newsroom.etomato.com/userfiles/_MG_9496.jpg">
<img src="https://40.media.tumblr.com/795409fb917e7dff3fb9d1589e2b402f/tumblr_nj0w5roP8L1tmxi3oo1_1280.jpg">
<img src="http://img.tenasia.hankyung.com/webwp_kr/wp-content/uploads/2015/09/2015090714401115495-540x811.jpg">
</body>
</html>''')
