"""
URL configuration for cbv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from home import views

app_name = "home"
urlpatterns = [
    path("home/", views.Home.as_view(), name="home"),
    path("hometemplateview/", views.HomeView.as_view(), name="hometemplateview"),
    path("two/", views.Two.as_view(), name="two"),
    path("homelistview/", views.HomeListView.as_view(), name="homelistview"),
    # path("detail/<int:pk>/", views.Detail.as_view(), name="detail"),
    # path("detail/<slug:my_slug>/", views.Detail.as_view(), name="detail"),
    path("detail/<slug:name>/<slug:owner>/<slug:year>/", views.Detail.as_view(), name="detail"),
    path("detail/<slug:name>/<slug:owner>/<slug:year>/", views.Detail.as_view(), name="detail"),
    path("create/", views.Create.as_view(), name="create"),
    path("carcreateview/", views.CarCreateView.as_view(), name="carcreateview"),
    path("delele/<int:pk>/", views.CarDeleteView.as_view(), name="delete"),
    path("update/<int:pk>/", views.CarUpdateView.as_view(), name="update"),
]
