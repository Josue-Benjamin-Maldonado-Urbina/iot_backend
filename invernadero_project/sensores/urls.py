from rest_framework.routers import DefaultRouter
from .views import RegistroSensorViewSet

router = DefaultRouter()
router.register(r'sensores', RegistroSensorViewSet, basename='sensor')

urlpatterns = router.urls
