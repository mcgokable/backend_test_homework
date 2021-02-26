import random

from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from api.models import Confirmation, User
from api.permissions import IsAdmin
from api.serializers import UserSerializer
from api_yamdb.settings import DEFAULT_FROM_EMAIL


@api_view(['POST'])
def mail_confirm(request):
    email_from = DEFAULT_FROM_EMAIL
    email_to = request.data.get('email')
    confirmation_code = make_password(
        "".join(map(str, random.sample(range(10), 6))),
        salt=None,
        hasher="default"
    )

    try:
        current_user = Confirmation.objects.get(email=email_to)
        current_user.confirmation_code = confirmation_code
        current_user.save()
    except Confirmation.DoesNotExist:
        Confirmation.objects.create(
            email=email_to,
            confirmation_code=confirmation_code
        )
    send_mail(
        'Confirmation code for your Yamdb profile!',
        f'Your confirmation code: {confirmation_code}',
        from_email=email_from,
        recipient_list=[email_to, ],
        fail_silently=False,
    )
    return Response({'email': email_to}, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_token(request):
    try:
        request_email = request.data.get('email')
        request_code = request.data.get('confirmation_code')
        current_user = Confirmation.objects.get(email=request_email)
    except Confirmation.DoesNotExist:
        return Response({'error': 'wrong email'},
                        status=status.HTTP_400_BAD_REQUEST)
    if request_code == current_user.confirmation_code:
        new_user, _ = User.objects.get_or_create(email=request_email)
        current_user.delete()
        refresh = RefreshToken.for_user(new_user)
        return Response({'token': str(refresh.access_token)},
                        status=status.HTTP_200_OK)
    return Response({'error': 'wrong code'},
                    status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdmin]
    pagination_class = PageNumberPagination
    lookup_field = 'username'
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @action(
        detail=False,
        methods=['GET', 'PATCH'],
        permission_classes=[IsAuthenticated]
    )
    def me(self, request, *args, **kwargs):
        if request.method == 'GET':
            queryset = User.objects.get(username=request.user.username)
            serializer = UserSerializer(queryset)
            return Response(serializer.data)
        self.object = get_object_or_404(User, username=request.user.username)
        serializer = self.get_serializer(
            self.object,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
