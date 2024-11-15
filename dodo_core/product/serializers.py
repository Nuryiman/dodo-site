from rest_framework import serializers

from product.models import Pizza


class PizzaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza
        fields = (
            'id',
            'name',
            'price',
            'consist',
            'image',
        )
