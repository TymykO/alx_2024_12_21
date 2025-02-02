from django.shortcuts import render
from django.conf import settings
from django.utils.translation import gettext as _

def home(request):
    context = {
        'message': _('Welcome'),
        'description': _('This is a sample internationalization page'),
        'LANGUAGES': settings.LANGUAGES,
    }
    return render(request, 'home.html', context)