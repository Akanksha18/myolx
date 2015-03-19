from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from userapp.views import ProfileImageIndexView, ProfileImageView, ProfileDetailView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'myolx.views.home', name='home'),
    url(r'^myapp/$', 'userapp.views.app'),
    url(r'^register/$', 'userapp.views.register'),
    url(r'^thanks/$', 'userapp.views.thanks'),
    url(r'^login/$', 'userapp.views.login'),
    url(r'^auth/$', 'userapp.views.auth_view'),
    url(r'^logout/$', 'userapp.views.logout'),
    url(r'^loggedin/$', 'userapp.views.loggedin'),
    url(r'^invalid/$', 'userapp.views.invalid_login'),
  
# profile uploads
    url(r'^hello-app/$', ProfileImageIndexView.as_view(), name= 'app'),
    url(r'^upload/$', ProfileImageView.as_view(), name = 'profile_image_upload'),
    url(r'^uploaded/(?P<pk>\d+)/$', ProfileDetailView.as_view(), name='profile_image'),

# profile details add form
    url(r'^profile/$', 'userapp.views.profile'),

    url(r'^admin/', include(admin.site.urls)),
)
