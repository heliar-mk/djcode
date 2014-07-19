from django.conf.urls import patterns, include, url

from django.contrib import admin

import views
import books.views
import contact.views

admin.autodiscover()

urlpatterns = patterns('',
        url(r'^hello/', views.hello),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^time/$', views.current_datetime),
        url(r'^time/plus/(\d{1,2})$', views.hours_ahead),
        url(r'^metadata/$',books.views.display_meta),
        url(r'^search/$', books.views.search),
        url(r'^contact/$', contact.views.contact),
        url(r'^contact/thanks/$', contact.views.thanks),
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
)
