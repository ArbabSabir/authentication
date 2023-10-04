from rest_framework import serializers
from Api.models import CustomUser

#Custome code
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=CustomUser
        fields=['id','username','email','password']
        