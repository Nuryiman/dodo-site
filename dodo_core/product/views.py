from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Pizza
from product.serializers import PizzaSerializer


class PizzaListAPIView(APIView):
    """Вьюшка чтобы вернуть список пицц"""

    def get(self, request, *args, **kwargs):
        pizza_list = Pizza.objects.all()

        serializer = PizzaSerializer(instance=pizza_list, many=True)
        response_body = serializer.data

        return Response(status=200, data=response_body)
