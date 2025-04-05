
from django.contrib import admin
from django.urls import path, include
from Student.views import home


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('Student/', include('Student.urls')),
    
]
