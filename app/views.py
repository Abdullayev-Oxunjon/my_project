from django.shortcuts import render
from .models import  History


def index_view(request):
    word = request.GET.get('query', '')

    if word and word !='':
        natija = History.objects.filter(tarixiy__contains=word).all()[:3]
    else:
        natija=None
        
    return render(request=request,
                  template_name='app/index.html', context={'query':word,'natija': natija})


