from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('pythonInter_app.api.urls')),
    # path('', include('pythonInter_app.api.urls')),
]
