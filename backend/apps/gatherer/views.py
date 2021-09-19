from django.shortcuts import render


def view_test_selenium(request):
    return render(request, "gatherer/index.html")
