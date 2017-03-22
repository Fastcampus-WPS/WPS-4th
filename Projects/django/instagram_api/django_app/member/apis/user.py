from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from member.serializers import UserSerializer

__all__ = (
    'ProfileView',
)


class ProfileView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)
