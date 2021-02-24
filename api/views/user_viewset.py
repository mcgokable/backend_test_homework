from api.models import User
from api.serializers import UserSerializer, MyTokenObtainPairSerializer
from api.permissions import IsAdmin

from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import permissions, viewsets, status
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage
import random
import string

def mail_confirm(request):
    global conf_code
    global email_to
    email_to = request.POST['email']
    if request.method == "POST":
        letters = string.ascii_lowercase
        conf_code = ''.join(random.choice(letters) for i in range(6))
        email = EmailMessage(
            'Conformation code',
            f'Your conformation code for authentification is {conf_code}.',
            'apostolovdm@gmail.com',
            email_to
        )
        return email.send(fail_silently=False)


class MyTokenObtainPairView(TokenObtainPairView):
    def get_serializer_class(self, request):
        if ('email' in request.data) and ('confirmation_code' in request.data):
            if request.data['confirmation_code'] == conf_code:
                return MyTokenObtainPairSerializer
        return TokenObtainPairSerializer


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
        self.object = get_object_or_404(User, username=request.user.username)
        serializer = self.get_serializer(
            self.object,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)