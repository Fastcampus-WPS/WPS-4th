from django.utils import timezone


def current_time(request):
    now = timezone.now()
    now_str = now.strftime('%Y%m%d%H%M%S')
    return {
        'current_time': now_str,
    }
