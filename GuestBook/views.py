from django.shortcuts import render
from models import GuestBook
from HackDoorMenu.settings import ADMIN_EMAILS
from django.core import mail

# Create your views here.


def create_entry(request):
    if request.method == 'POST':
        #We have recieved data! Process!
        entry = GuestBook()
        entry.name = request.POST['name']
        entry.twitter = request.POST['twitter']
        entry.email = request.POST['email']
        entry.message = request.POST['message']
        entry.spam_me = request.POST['spam_me']
        entry.save()

        #Now raise the emails for all the things
        mail.send_mail('Guestbook Signed', '{0} {1} said {2}'.format(entry.name, entry.email, entry.message))
        if request.POST['email_me']:
            mail.send_mail('RLab Guestbook', 'Thank you for signing the RLab Guestbook {0}. '
                                             'You said: \n{1}\nRlab Door Machine', [request.POST['email']])

        return render(request, '/templates/guestbook/thanks.html', {entry.name, })
    else:
        #We have not recieved data, sadface :(
        return render(request, '/templates/guestbook/new_entry.html', {'post': request.POST, })