from rest_framework import routers
from django.conf.urls import url, include
from . import views

router = routers.DefaultRouter()
router.register(r'Musicians', views.MusiciansView)
router.register(r'Talent_management', views.Talent_managementView)
router.register(r'Production', views.ProductionView)
router.register(r'Events', views.EventView)

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]

urlpatterns = [
    url(r'^', include(router.urls)),
]
