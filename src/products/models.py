from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Timer(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["created_at"]

class Product(Timer):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='images/', blank=True)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name
    

class Wishlist(Timer):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    def __str__(self) -> str:
        return f"{self.user.username} {self.products.name}"
    

class Review(Timer):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.user.username} {self.product.name}"
    

class Support(Timer):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    result = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.user.username
    

class OrderItem(Timer):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.CharField(max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.user.username
    
class PaymentGateway(Timer):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name

class Shipping(Timer):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return self.user.username
    