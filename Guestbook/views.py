from django.shortcuts import render
from models import GuestBook

# Create your views here.

def view_guestbook(request):
    startnum = 0
    if request.POST:
        if 'startnum' in request.POST.keys():
            startnum = request.POST['startnum']

    guestbook_entries = GuestBook.objects.all()[startnum:startnum+20]
    return render(request, 'Guestbook/main.html', {'entries': guestbook_entries, })
