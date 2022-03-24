from django.shortcuts import render
from .forms import BackForms


def Index(request):
    if request.method == "POST":
        form = BackForms(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'index/index.html')
