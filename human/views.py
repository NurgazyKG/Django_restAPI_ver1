from rest_framework import  generics
from django.shortcuts import render
from .models import Human
from .serializers import HumanSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
#class HumanAPIView(generics.ListAPIView):
#    queryset = Human.objects.all()
#    serializer_class = HumanSerializer

class HumanAPIView(APIView):
    def get(self, request):
        lst = Human.objects.all().values()
        return Response({'posts': list(lst)})

    def post(self, request):
        post_new = Human.objects.create(
            firstname=request.data('firstname'),
            surname=request.data['surname'],

        )
        return Response({'firstname': 'Altynbek', 'surname': 'Baimuratov'})