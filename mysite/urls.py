from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
<<<<<<< HEAD
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
=======
        url(r'^admin/', include(admin.site.urls)),
        url(r'', include('blog.urls')),
>>>>>>> 31e8a87a52ff581219ef4b6ae0d8e3d7881a80f7
]
