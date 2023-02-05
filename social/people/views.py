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

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Page not found</h1>')
def Forbidden(request,exception):
    return HttpResponseForbidden('<h1>Access is denied </h1>')

def BadRequest(request,exception):
    return HttpResponseBadRequest('<h1>Bad request </h1>')

def ServerError(request):
    return HttpResponseServerError('<h1>server error </h1>')

