"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
import guestbook.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',guestbook.views.index, name="index"),
    path('delete/<int:post_id>',guestbook.views.delete, name="delete"),
    path('comment/<int:post_id>',guestbook.views.comment, name="comment"),
    path('c_delete/<int:comment_id>',guestbook.views.c_delete,name="c_delete"),
]
