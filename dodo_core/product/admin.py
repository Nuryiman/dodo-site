from django.contrib import admin

from product.models import Pizza


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
