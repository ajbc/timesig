from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

from django.contrib import admin
admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'timesig.myapp.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/login/$',  login),
    (r'^accounts/logout/$', logout),
    url(r'^accounts/profile/$', 'timesig.myapp.views.profile', name='profile'),
    url(r'^accounts/register/$', 'timesig.myapp.views.register', name='register'),
    url(r'^docs/$', 'timesig.myapp.views.docs'),
    (r'^doc/(?P<doc_id>\d+)/$', 'timesig.myapp.views.doc'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)