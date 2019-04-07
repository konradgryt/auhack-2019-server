from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from deepworkapi import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.api_root),
    path('sessions/',
         views.SessionList.as_view(),
         name='session-list'),
    path('sessions/<int:pk>/',
         views.SessionDetail.as_view(),
         name='session-detail'),
    path('users/',
         views.UserList.as_view(),
         name='user-list'),
    path('users/<int:pk/>',
         views.UserDetail.as_view(),
         name='user-detail'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
