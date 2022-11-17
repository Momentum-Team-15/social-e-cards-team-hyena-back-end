


from django.urls import path, include
from hyena import views, admin
from hyena.models import SocialCard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('hyena.urls')),  
]

