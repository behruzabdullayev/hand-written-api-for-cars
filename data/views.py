from rest_framework import status
from rest_framework.response import Response

from .models import Car
from .serializers import CarSerializer
from rest_framework.views import APIView



class CarListAPIView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        context = {
            'status_code': status.HTTP_200_OK,
            'message': 'Success',
            'data': serializer.data
        }
        return Response(context)

class CarCreateAPIView(APIView):
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                'status_code': status.HTTP_201_CREATED,
                'message': 'Created',
                'data': serializer.data
            }
            return Response(context)

class CarDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            car = Car.objects.get(id=pk)
            serializer = CarSerializer(car)
            context = {
                'status_code': status.HTTP_200_OK,
                'message': 'Success',
                'data': serializer.data
            }
            return Response(context)
        except Car.DoesNotExist:
            context = {
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'Not Found',

            }
            return Response(context)

class CarUpdateAPIView(APIView):
    def put(self, request, pk):
        car = Car.objects.get(id=pk)
        serializer = CarSerializer(car, data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status_code': status.HTTP_200_OK,
                    'message': 'Updated',
                    'data': serializer.data
                })
        except Car.DoesNotExist:
            return Response({
                'message': 'There is no car with this id',
                'status_code': status.HTTP_404_NOT_FOUND,
            })

class CarDeleteAPIView(APIView):
    def delete(self, request, pk):
        try:
            car = Car.objects.get(id=pk)
            car.delete()
            return Response({
                'status_code': status.HTTP_200_OK,
                'message': 'Deleted Successfully',

            })
        except Car.DoesNotExist:
            return Response({
                'message': 'There is no car with this id',
                'status_code': status.HTTP_404_NOT_FOUND,
            })

class CarDetailUpdateAPIView(APIView):
    def get(self, request, pk):
        try:
            car = Car.objects.get(id=pk)
            serializer = CarSerializer(car)
            context = {
                'status_code': status.HTTP_200_OK,
                'message': 'Success',
                'data': serializer.data
            }
            return Response(context)
        except Car.DoesNotExist:
            context = {
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'Not Found',

            }
            return Response(context)

    def put(self, request, pk):
        car = Car.objects.get(id=pk)
        serializer = CarSerializer(car, data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status_code': status.HTTP_200_OK,
                    'message': 'Updated',
                    'data': serializer.data
                })
        except Car.DoesNotExist:
            return Response({
                'message': 'There is no car with this id',
                'status_code': status.HTTP_404_NOT_FOUND,
            })

class CarListCreateAPIView(APIView):
    def get(self, request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response({
            'status_code': status.HTTP_200_OK,
            'message': 'Success',
            'data': serializer.data
        })
    def post(self, request):
        serializer = CarSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status_code': status.HTTP_200_OK,
                    'message': 'Created',
                    'data': serializer.data
                })
        except Car.DoesNotExist:
            return Response({
                'message': 'Error',
            })























