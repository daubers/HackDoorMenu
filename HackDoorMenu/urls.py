from django.conf.urls import patterns, include, url

from HackDoor.views import main
from Guestbook.views import view_guestbook

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HackDoorMenu.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main),
    url(r'^guestbook/', view_guestbook),
)

