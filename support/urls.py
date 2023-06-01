from django.urls import path
from support import views

urlpatterns = [
    path("",views.home),
    path("predict/",views.predict),
    path("predict/result/",views.result)
]