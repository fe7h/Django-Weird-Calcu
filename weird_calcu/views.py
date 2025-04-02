from django.http import HttpResponse, HttpResponseBadRequest

from .forms import WeirdCalcuForm
from . import services


def calculated(request):
    form = WeirdCalcuForm(request.GET)

    if form.is_valid():
        first, second = form.cleaned_data.values()
        ans = services.calculate(first, second)
        return HttpResponse(
            services.img_gen(str(ans)),
            content_type='image/png'
        )

    return HttpResponseBadRequest(form.errors.as_json())
