from django.conf.urls import url
from . import views

urlpatterns = [
    #/map/
    url(r'^$', views.homepage, name = 'homepage'),

    #/map/report/
    url(r'^report/', views.reportpage, name = 'reportpage')
]
