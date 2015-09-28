from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('blog.urls')),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': '/path/to/media'}),
]
handler404 = 'blog.views.my_custom_page_not_found_view'
handler500 = 'blog.views.my_custom_error_view'
handler403 = 'blog.views.my_custom_permission_denied_view'
handler400 = 'blog.views.my_custom_bad_request_view'
