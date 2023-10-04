from django.shortcuts import render
from Api.models import CustomUser
from Api.serializers import UserSerializer
from rest_framework.response import Response
from knox.models import AuthToken
from django.contrib.auth import login,logout
from rest_framework import generics,permissions,status

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer
    permission_classes=(permissions.AllowAny,)
    
    def post(self, request, *args, **kwargs):
        serializers=self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        user=serializers.save()
        _, token = AuthToken.objects.create(user)
        
        return Response( 
            {
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                
            },
            status=status.HTTP_200_OK,
            headers={
                "token": token
            },
        )

class Loginview(generics.CreateAPIView):
    serializer_class=UserSerializer
    permission_classes=(permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        user=request.user
        _,token=AuthToken.objects.create(user)
        apiname="LoginApi"
        return Response(
            {
                "ApiName":apiname,
                "user" : UserSerializer(user,context=self.get_serializer_context()).data,
            },
            headers={"token" : token},
            status=status.HTTP_200_OK,
        )
    
class Logoutview(generics.DestroyAPIView):
    permission_classes=(permissions.IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        request.auth.delete()
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class ListUserView(generics.ListAPIView):
    queryset=CustomUser.objects.all()
    serializer_class=UserSerializer
    permission_classes=(permissions.IsAuthenticated,)