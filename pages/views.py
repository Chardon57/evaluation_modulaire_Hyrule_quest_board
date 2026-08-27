from django.shortcuts import render

# Create your views here.
def home(request):
    context = {"page_title": "Hyrule Quest Board"}
    return render(request, "pages/homepage.html", context)