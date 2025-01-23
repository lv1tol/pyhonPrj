from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

users = [
    { "id": 1, "name": "Leanne Graham", "email": "Sincere@april.biz"},
    { "id": 2, "name": "Ervin Howell", "email": "Shanna@melissa.tv"},
    { "id": 3, "name": "Clementine Bauch", "email": "Nathan@yesenia.net"}
]

def home(request):
    return HttpResponse("• Hello • World •")
    #return render(request, "home.html")

def list(request):
    html = "<h1>Users</h1> <ul>"
    for user in users:
        html += f"<li>{user['name']}</li>"
    html += "</ul>"
    return HttpResponse(html)