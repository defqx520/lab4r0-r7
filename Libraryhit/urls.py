from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pythondjangotest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'libweb.views.homepage'),
    url(r'^bookshow/$', 'libweb.views.getbook'),
    url(r'^authorshow/$', 'libweb.views.getauthor'),
    url(r'^authoradd/$', 'libweb.views.showauthoradd'),
    url(r'^saveauthor/$', 'libweb.views.saveauthor'),
    url(r'^bookadd/$', 'libweb.views.showbookadd'),
    url(r'^savebook/$', 'libweb.views.savebook'),
    url(r'^searchauthor/$', 'libweb.views.searchauthor'),
    url(r'^lackauthorerror/$', 'libweb.views.showerrorpage'),
    url(r'^bookupdate/(.+)/$', 'libweb.views.bookupdate'),
    url(r'^updatebook/$', 'libweb.views.updatebook'),
    url(r'^delbook/(.+)/$', 'libweb.views.delbook'),
    url(r'^bookdetail/(.+)/$', 'libweb.views.bookdetail'),
    url(r'^authordetail/(.+)/$', 'libweb.views.authordetail'),
    url(r'^admin/', include(admin.site.urls)),
    
)
