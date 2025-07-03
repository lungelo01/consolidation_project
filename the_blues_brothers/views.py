from django.shortcuts import render


"""The web app home page

return: The home page
"""
# Create your views here.
def home(request):
    return render(request, 'home.html')