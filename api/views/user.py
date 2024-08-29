import json
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from ..models import User
from ..serializers import UserSerializer

class UserView(APIView):

	def get(self, request: Request):
		return Response("hello world")

	def post(self, request: Request):
		data = request.data
		serializer = UserSerializer(data=data)
		if serializer.is_valid():
			user = User(**data)
			user.set_password(data["password"])
			user.save()
			token = Token.objects.create(user=user)
			return Response(json.dumps({
				"success": True,
				"message": {
					"user": serializer.data,
					"token": token.key
				}
			}))
		
		return Response(json.dumps({
			"success": False,
			"message": {
				"errors": serializer.errors
			} 
		}), status.HTTP_400_BAD_REQUEST)
