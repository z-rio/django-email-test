from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from . import tasks
from .serializers import CustomRegistrationSerializer

class CustomRegistrationView(APIView):

    def _send_success_email(self, email):
        tasks.send_email_notification.delay(email)

    def post(self, request):
        ser = CustomRegistrationSerializer(data=request.data)
    
        ser.is_valid(raise_exception=True)
        user = ser.save()
        
        email = ser.validated_data['email']
        
        self._send_success_email(email)
        
        return Response({'detail': 'Success creating user'}, status=status.HTTP_201_CREATED)