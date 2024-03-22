from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ServiceSerializer
from .models import Service
# Create your views here.
"""
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/service-list/',
        'Detail View': '/service-detail/<int:id>/',
        'Create': '/service-create/',
        'Update': '/service-update/<int:id>/',
        'Delete': '/service-detail/<int:id>/',
    }
    return Response(api_urls);
"""
@api_view(['GET'])
def ShowAll(request):
    services = Service.objects.all()
    serializer = ServiceSerializer(services, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ViewService(request, pk):
    try:
        service = Service.objects.get(id_service=pk)
    except Service.DoesNotExist:
        return Response({"message": "Service does not exist"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ServiceSerializer(service)
    return Response(serializer.data)


@api_view(['POST'])
def CreateService(request):
    if request.method == 'POST':
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def updateService(request, pk):
    try:
        service_instance = Service.objects.get(id_service=pk)
    except Service.DoesNotExist:
        return Response({"error": "Service not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ServiceSerializer(instance=service_instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteService(request, pk):
    try:
        service_instance = Service.objects.get(id_service=pk)
    except Service.DoesNotExist:
        return Response({"error": "Service not found"}, status=status.HTTP_404_NOT_FOUND)

    service_instance.delete()
    return Response('Item deleted successfully!', status=status.HTTP_200_OK)


@api_view(['GET'])
def searchServiceById(request, pk):
    try:
        service_instance = Service.objects.get(id_service=pk)
        serializer = ServiceSerializer(service_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Service.DoesNotExist:
        return Response({"error": "Service not found"}, status=status.HTTP_404_NOT_FOUND)