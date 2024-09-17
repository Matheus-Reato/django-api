from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Car
from .serializers import CarSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def get_by_id(request, id):

    try:
        car = Car.objects.get(pk=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':

        serializer = CarSerializer(car)
        return Response(serializer.data)

    if request.method == 'PUT':

        serializer = CarSerializer(car, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':

        try:
            car.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def car_manager(request):

    if request.method == 'GET':

        cars = Car.objects.all()                       

        serializer = CarSerializer(cars, many=True)      

        return Response(serializer.data)

    if request.method == 'POST':

        new_car = request.data
        
        serializer = CarSerializer(data=new_car)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_400_BAD_REQUEST)


