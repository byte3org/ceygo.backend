import json
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.authtoken.models import Token
from ..models import User
from ..serializers import UserSerializer

def login_required(route):
	@authentication_classes([TokenAuthentication])
	@permission_classes([IsAuthenticated])
	def inner(request, *args, **kwargs):
		return route(request, *args, **kwargs)
	return inner

@api_view(["POST"])
def login(request: Request):
	data = request.data
	user = User.objects.get(username=data["username"])

	if not user:
		return Response({
			"success": False,
			"message": "User not found"
		}, status.HTTP_404_NOT_FOUND)

	if user.check_password(data["password"]):
		token, _ = Token.objects.get_or_create(user=user)
		return Response({
			"success": True,
			"message": {
				"user": UserSerializer(user).data,
				"token": token.key
			}
		})

	return Response({
		"success": False,
		"message": {
			"errors": "Invalid password"
		} 
	}, status.HTTP_401_UNAUTHORIZED)



@api_view(["GET"])
@login_required
def test_token(request: Request):
	if request.user:
		return Response({
			"success": True,
			"message": {
				"user": UserSerializer(request.user).data
			}
		}, status.HTTP_200_OK)
	
	return Response({
		"success": False,
		"message": "Invalid token"
	}, status.HTTP_401_UNAUTHORIZED)
