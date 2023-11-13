# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Product, Promotion
# from django.shortcuts import get_object_or_404

# @receiver(post_save, sender=Promotion)
# def new_price(sender, instance, **kwargs):
#     for product in instance.products.all():
#         # Calculate the product multiplier
#         discount_multiplier = 1 - (instance.percentage_discount / 100)
#         # Get the products that are in the promotion
#         # product = get_object_or_404(Product, id=product_id)
#         # Update the new price of the product with the discount price
#         product.new_price = product.price * discount_multiplier
#         product.save()

