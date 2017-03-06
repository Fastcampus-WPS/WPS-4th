from django.http import HttpResponse


def index(request):
    return HttpResponse('''<html>
<body>
<h1>Hello, world!</h1>
</body>
</html>''')
