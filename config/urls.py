from django.urls import path, include
from hyena import views, admin
from django.contrib.admin import site
from hyena.models import SocialCard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('hyena.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),

]
