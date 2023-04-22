from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import signin, signup
from . serializers import signinSerializer, signupSerializer


class signinList(APIView):


    def get(self, request):
        signin1=signin.objects.all()
        serializer=signinSerializer(signin1, many=True)
        return Response(serializer.data)


    def post(self):
        pass

class signupList(APIView):


    def get(self, request):
        signup1=signup.objects.all()
        serializer=signupSerializer(signup1, many=True)
        return Response(serializer.data)


    def post(self):
        pass