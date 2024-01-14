from django.shortcuts import redirect
from patient.serializers import PatientSerializers,UserRegistrationSerializer,UserLoginSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from patient.models import Patient
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import authenticate,login,logout
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User

# send email
def send_email(user,confirm_link, mail_subject,template):
    message = render_to_string(template, {
        'user': user,
        'link': confirm_link,
    })
    from_email = "Smart Care <delwarjnu24@gmail.com>"
    send_email = EmailMultiAlternatives(mail_subject, '', to=[user.email], from_email=from_email, reply_to=[from_email])
    send_email.attach_alternative(message, 'text/html')
    send_email.send()

# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers

class UserRegistrationViewSet(APIView):
    serializer_class = UserRegistrationSerializer

    def post(self,request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            user = serializer.save()
            print(user)
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f'http://127.0.0.1:8000/patients/activate/{uid}/{token}'
            send_email(user,confirm_link,'Email Verification Message', 'email.html')
            return Response('Verify your email')
        return Response(serializer.errors)

def activate(self,uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user  = User._default_manager.get(pk = uid)
    except(User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')


class UserLoginViewSet(APIView):
    def post(Self,request):
        serializer = UserLoginSerializer(data = request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username = username, password = password)

            if user:
                token,_create = Token.objects.get_or_create(user = user)
                login(request, user)
                return Response({'token': token.key, 'user_id': user.id})
            else:
                return Response({'error': 'Invalid Credentials'})
        return Response(serializer.errors)
    
class UserLogoutViewSet(APIView):
    def get(self,request):
        request.user.auth_token.delete()
        return redirect('login')