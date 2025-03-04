from django.shortcuts import render,redirect
from .models import registration
from .serializers import registerserializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
# Create your views here.


from django.shortcuts import render  
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status    
from django.shortcuts import get_object_or_404  
# Create your views here.  
  
class UserRegisterView(APIView):  
    def get(self,request):
        result = registration.objects.all()  
        serializers = registerserializer(result, many=True)  
        return Response({'status': 'success', "students":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = registerserializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
class UserFetch(APIView):
    def get(self, request, id):  
        result = registration.objects.get(id=id)  
        if id:  
            serializers = registerserializer(result)  
            return Response({'success': 'success', "students":serializers.data}, status=200)  
    def patch(self, request, id):  
        result = registration.objects.get(id=id)  
        serializer = registerserializer(result, data = request.data, partial=True)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data})  
        else:  
            return Response({"status": "error", "data": serializer.errors})  
  
class UserLogin(APIView):
    def get(self,request):
        email=request.GET['emailid']
        password1=request.GET['password']

        result=registration.objects.filter(emailid=email).filter(password=password1)

        print(result)

        while len(result)>0:
            if result[0]['emailid']==email and result[0]['password']==password1:
                print(result[0]['firstname'],result[0]['lastname'],result[0]['emailid'],result[0]['dateofbirth'])
            else:
                print("enter valid details")
        else:
            print("dear user please register user deatails")
