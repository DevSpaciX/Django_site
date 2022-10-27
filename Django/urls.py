"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.conf.urls.static import static
from django.conf import settings
from groups import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(),name="home"),
    path("search/", views.SearchView.as_view(), name='search'),
    path("category/<int:categories_id>/", views.GroupByCategory.as_view(), name='category'),
    path('create/student/',views.CreateStudent.as_view(),name="create_student"),
    path('students/', views.StudentList.as_view(),name="students"),
    path('profile/', views.ProfileView.as_view(),name="profile"),
    path("login/", LoginView.as_view(template_name='login.html'), name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path('edit/<int:student_id>/student/',views.EditUser.as_view(),name="edit_student"),

    path('',include(('groups.urls' , 'groups'),namespace='course')),
    


    path('__debug__/', include('debug_toolbar.urls')),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
