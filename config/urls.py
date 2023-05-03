from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('app.urls', 'app'), namespace='app')),
    path('user/', include(('users.urls', 'users'), namespace='users')),
]


urlpatterns += static(settings.STATIC_URL, 
                      document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)