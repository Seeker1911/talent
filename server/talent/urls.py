from rest_framework import routers
from django.conf.urls import url, include
from . import views

router = routers.DefaultRouter()
router.register(r'Musicians', views.MusiciansView)
# router.register(r'Talent_management', views.Talent_managementView)
# router.register(r'Production', views.ProductionView)
router.register(r'Events', views.EventView)
router.register(r'Songs', views.SongView)
router.register(r'Users', views.UserView)



# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]

urlpatterns = [
    url(r'^login/$', views.login_user, name='login'),
    url(r'^register/$', views.register_user, name='register_user'),
    url(r'^', include(router.urls)),
]
