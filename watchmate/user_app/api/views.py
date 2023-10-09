from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from user_app.api.serializers import RegistrationSerializer
from user_app import models


@api_view(['POST',])
def registration_view(request):

  if request.method == 'POST':
    serializer = RegistrationSerializer(data=request.data)

    data = {}

    if serializer.is_valid():
      account = serializer.save()

      data['response'] = "Registration successful"
      data['username'] = account.username
      data['email'] = account.email
      data['token'] = Token.objects.get(user=account).key
    else:
      data = serializer.errors
      
    return Response(data) 
