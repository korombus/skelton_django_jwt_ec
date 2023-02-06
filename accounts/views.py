from django.contrib.auth import get_user_model

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer

User = get_user_model()

class RegisterView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request):
        try:
            data = request.data
            email = data['email']
            password = data['password']
            first_name = data['first_name']
            last_name = data['last_name']
            address = data['address']
            tel_number = data['tel_number']

            if not User.objects.filter(email=email).exists():
                User.objects.create_user(email, password, first_name, last_name, address, tel_number)

                return Response(
                    {'success': 'Create your account. Please try login.'},
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {'error': 'Already your account. Please try login.'},
                    status=status.HTTP_400_BAD_REQUEST
                )

        except:
            return Response(
                {'error': 'Failed account register. Please contact administer.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class UserView(APIView):
    def get(self, request):
        try:
            user = request.user
            user = UserSerializer(user)

            return Response(
                {'user': user.data},
                status=status.HTTP_200_OK
            )
        except:
            return Response(
                {'error': 'Failed get user. Please contact administer.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )