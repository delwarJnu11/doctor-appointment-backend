from rest_framework import serializers
from patient.models import Patient
from django.contrib.auth.models import User

class PatientSerializers(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Patient
        fields = '__all__'

class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']


        if password != password2:
                raise serializers.ValidationError({'error': "Password doesn't matched"})

        if User.objects.filter(email = email).exists():
                raise serializers.ValidationError({'error': "email already exists"})
            
        account = User(username = username , first_name = first_name, last_name = last_name, email = email)
        account.set_password(password)
        account.is_active = False
        account.save()
        return account
    
class UserLoginSerializer(serializers.Serializer):
     username = serializers.CharField(required=True)
     password = serializers.CharField(required=True)