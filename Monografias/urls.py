from django.conf.urls import url, include
from django.contrib import admin

from Monografias import settings
from website.views import MainView, NewMonographView, UpdateMonographView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^logout/', include('django.contrib.auth.urls'), name='logout',
        kwargs={'next_page': settings.LOGOUT_REDIRECT_URL}),
    url(r'^accounts/login/', include('django.contrib.auth.urls'), name='login'),
    url(r'^$', MainView.as_view(), name='main_page'),
    url(r'^new/$', NewMonographView.as_view(), name='new_monograph'),
    url(r'^edit/(?P<pk>\d+)/$', UpdateMonographView.as_view(), name='edit_monograph')
]
