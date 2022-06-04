from django.shortcuts import render


def IndexView(request):
    return render(request, 'htmx_app/index.html')