# from django.shortcuts import render
#
# # Create your views here.
#
# from django.shortcuts import render_to_response
#
#
# def index(request):
#     return render_to_response("index.html")
#
# def examples(request):
#     return render_to_response("examples.html")
#
# def page(request):
#     return render_to_response("page.html")
#
# def another_page(request):
#     return render_to_response("another_page.html")
#
# def contact(request):
#     return render_to_response("contact.html")

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def examples(request):
    return render(request, "examples.html")

def page(request):
    return render(request, "page.html")

def another_page(request):
    return render(request, "another_page.html")

def contact(request):
    return render(request, "contact.html")
