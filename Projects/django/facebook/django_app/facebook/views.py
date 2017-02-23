from django.shortcuts import redirect


def index(request):
    return redirect('member:login')
