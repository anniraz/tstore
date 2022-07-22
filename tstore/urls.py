from django.contrib import admin
from django.urls import path ,include

from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


from rest_framework import routers
from apps.user.views import UserAPIView
from apps.store.views import *



router=routers.DefaultRouter()
router.register('tstore',TStoreViewSet)
router.register('characteristics',TStoreCharacteristics)
router.register('users',UserAPIView)
router.register('review',ReviewCreateView)
router.register('category',CategoryCreateView)
# router.register('rating',RatingApiViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
   #  path('r/' , RatingApiViewSet.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    # swagger
    # path('swagger(<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   

   # allauth
   path('accounts/', include('allauth.urls')),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)