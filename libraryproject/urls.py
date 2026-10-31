from django.contrib import admin
from django.urls import path, include
from apps.bookmodule import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index2/<int:val1>/', views.index2),
    path('books/', include('apps.bookmodule.urls')),
]
