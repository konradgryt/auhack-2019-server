from deepworkapi.models import Session
from deepworkapi.serializers import SessionSerializer, UserSerializer
from deepworkapi.permissions import IsOwner
from rest_framework import generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from rest_framework import mixins

class SessionList(generics.ListCreateAPIView):
    # Filter only user sessions
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SessionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = (permissions.IsAuthenticated,
                          IsOwner,)


class UserList(generics.ListAPIView):
    # For debug only
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'sessions': reverse('session-list', request=request, format=format),
        'login': reverse('api_token_auth', request=request, format=format),
    })
    