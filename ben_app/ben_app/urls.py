"""ben_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from tickets.views import IndexView, EditTicket, SearchTickets, CreateTicket, ListTickets, DeleteTicket, SearchResults, StatusBoard
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^tickets/create/$', CreateTicket.as_view(), name='ticket_create'),
    url(r'^tickets/delete/(?P<pk>\d+)/$', DeleteTicket.as_view(), name='ticket_delete'),
    url(r'^tickets/edit/(?P<pk>\d+)/$', EditTicket.as_view(), name='ticket_edit'),
    url(r'^tickets/$', ListTickets.as_view(), name='ticket_form'),
    url(r'^tickets/search/$', SearchTickets.as_view(), name='ticket_search'),
    url(r'^tickets/search/results/$', SearchResults.as_view(), name='ticket_search_result'),
    url(r'^status_board/$', StatusBoard.as_view(), name='status_board'),

]
