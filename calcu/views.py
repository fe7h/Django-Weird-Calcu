from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.finders import find

from . import services
from .forms import WeirdCalcuForm


def helo(request):
    return render(request,'calcu/home.html', {'form': WeirdCalcuForm()})


def calculated(request):

    form = WeirdCalcuForm(request.GET)
    # print(form.as_p())
    print(form.is_valid())
    if form.is_valid():
        print(form.cleaned_data)

        first = form.cleaned_data.get('first_number')
        second = form.cleaned_data.get('second_number')

        ans = services.calculate(first, second)
        img = services.img_gen(str(ans), find('calcu/img/meme.png'))

        return HttpResponse(img, content_type='image/png')
