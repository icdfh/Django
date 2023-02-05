from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest, \
    HttpResponseServerError
from django.shortcuts import render


menu = ["About page", "Add friend" , "Profile" , "Login"]

def index(request):
    return render(request, 'people/index.html', {'menu': menu, 'name': 'Main page'})

def about(request):
    return render(request, 'people/about.html', {'menu': menu, 'name': 'About page'})

def friends(request, friendid):
    if(request.POST):
        print(request.POST)
    return HttpResponse(f"<h1>Ur friends<h1><p>{friendid}</p>")

def PagenotFound(request,exception):
    return HttpResponseNotFound('<img src="https://media.licdn.com/dms/image/C5612AQEPYce5KpNLyg/article-cover_image-shrink_720_1280/0/1551659700811?e=2147483647&v=beta&t=O9mBMiF-V12jCRJwaBNDWLKNL8cku2QSoCXtKP3vCHg" alt="#" width="90%">')
def Forbidden(request,exception):
    return HttpResponseForbidden('<h1>Access is denied </h1>')

def BadRequest(request,exception):
    return HttpResponseBadRequest('<h1>Bad request </h1>')

def ServerError(request):
    return HttpResponseServerError('<h1>server error </h1>')

