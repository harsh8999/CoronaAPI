from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions, status
from rest_framework.response import Response
# from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.views import APIView

from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from django.contrib.auth.models import User
from .models import (DocumentRegistration,)
from .serializers import (HospitalSerializer,
                            DocumentRegistrationSerializer
                            )


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": Token.objects.get(user=user).key
        })


# class HospitalAPI(APIView):
#     def post(self, request):
#         print(request.data)        
#         serializer = HospitalSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_304_NOT_MODIFIED)

#     # get all hospital lists
#     def get(self,request):
#         queryset = Response.objects.all()
#         serilizer = HospitalSerializer(queryset, many=True)    
#         return Response(serilizer.data)

class DocumentRegistrationAPI(APIView):
    def post(self, request):
        print(request.data)        
        serializer = DocumentRegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_304_NOT_MODIFIED)

    # get all hospital lists
    def get(self,request):
        queryset = DocumentRegistration.objects.all()
        serilizer = DocumentRegistrationSerializer(queryset, many=True)    
        return Response(serilizer.data)

    def put(self, request, pk):
        queryset = DocumentRegistration.objects.filter()
