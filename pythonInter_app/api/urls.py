from django.urls import path, include
# from pythonInter_app.api.views import user_list, user_details
from pythonInter_app.api.views import UserListAV, UserDetailAV, ProjectPlatformAV, ProjectPlatformDetailAV

urlpatterns = [
    path('list/', UserListAV.as_view(), name='user-list'),
    path('<int:pk>/', UserDetailAV.as_view(), name='user-detail'),
    path('project', ProjectPlatformAV.as_view(), name='project'),
    path('project/<int:pk>/', ProjectPlatformDetailAV.as_view(), name='project-detail'),
]
