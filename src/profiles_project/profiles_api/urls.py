from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSets, 'hello-viewset')
router.register('profile', views.UserProfileViewSet)


urlpatterns = [
    # url(r'^hello-view/',views.HelloApiView.as_view()),
    # url(r'', include(router.urls))
    path('hello-view/',views.HelloApiView.as_view()),
    path('',include(router.urls))
    # path('',views.HelloViewSets.as_view({'get':'list'}))


]

# This will also work
# from django.conf.urls import url
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('hello-view/',views.HelloApiView.as_view())
# ]
