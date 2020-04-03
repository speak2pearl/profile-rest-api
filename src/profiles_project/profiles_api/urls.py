from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^hello-view/',views.HelloApiView.as_view())
]

# This will also work
# from django.conf.urls import url
# from django.urls import path
# from . import views
#
# urlpatterns = [
#     path('hello-view/',views.HelloApiView.as_view())
# ]
