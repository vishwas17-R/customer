from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets 
from .models import Customer 
from .serializers import CustomerSerializer 

class CustomerViewSet(viewsets.ModelViewSet):    
    # Full CRUD: list, create, retrieve, update,    
    # partial_update, destroy    
    queryset = Customer.objects.all()    
    serializer_class = CustomerSerializer