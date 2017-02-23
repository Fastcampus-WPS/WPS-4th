from django.shortcuts import render


def login_fbv(request):
    context = {

    }
    return render(request, 'member/login.html', context)
