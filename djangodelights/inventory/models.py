from django.db import models

# Create your models here.
class Ingredient(models.Model):
    UNIT_CHOICES = [
     ("tbsp", "TBSP"),
     ("tsp", "TSP"),
     ("cup", "CUP"),
     ("Kg", "KG"),
     ("litres", "LITRES"),
     ("ml", "ML"),
     ("piece", "PIECE"),
     ("g", "G"),
     ("OT", "OTHERS"),
  ]
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length = 10, choices=UNIT_CHOICES ,default="tbsp")
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Ingredients"

class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = "Menu Items"

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE, related_name='recipe_requirements')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.menu_item.title} - {self.ingredient.name} ({self.quantity} units)"
        
    class Meta:
        verbose_name_plural = "Recipe Requirments"

    

class Purchase(models.Model):
    time_stamp = models.DateTimeField(auto_now_add=True)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    def __str__(self):
        return f"Purchase #{self.id} - {self.time_stamp}"

    class Meta:
        verbose_name_plural = "Purchase"

