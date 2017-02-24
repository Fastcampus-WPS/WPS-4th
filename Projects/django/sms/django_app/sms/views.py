from django.shortcuts import render

from sms.forms import SMSForm


def index(request):
    if request.method == 'POST':
        form = SMSForm(request.POST)
    else:
        form = SMSForm(
            initial={
                'recipient_numbers': '010-2995-3874, 01029953874, 01023412, 293849323232, 02394090930',
            }
        )
    context = {
        'form': form,
    }
    return render(request, 'common/index.html', context)
