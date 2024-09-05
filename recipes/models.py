from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField(help_text='Spaced ingredients with a ", "')
    cooking_time = models.IntegerField(help_text='time in minutes')
    difficulty = models.CharField(max_length=120,help_text='optional',blank=True)
    pic = models.ImageField(upload_to='recipes', default='no-picture.png')
    about = models.TextField(default='No info')

    def __str__(self):
        return f"Name: {self.name}\nIngredients: {self.ingredients}\nCooking Time: {self.cooking_time}\n Difficulty: {self.difficulty}"
    
    def get_absolute_url(self):
        return reverse('recipes:recipes_detail', kwargs={'pk': self.pk})
    
    def calculate_difficulty(self):
        ingredient = len(self.ingredients.split(", "))
        if self.cooking_time < 10 and ingredient < 4:
            return "Easy"
        elif self.cooking_time < 10 and ingredient >= 4:
            return "Medium"
        elif self.cooking_time >= 10 and ingredient < 4:
            return "Intermediate"
        elif self.cooking_time >= 10 and ingredient >= 4:
            return "Hard"
    
    def save(self, *args, **kwargs):
        self.difficulty = self.calculate_difficulty() # Set the difficulty level before saving.
        super().save(*args, **kwargs) # Call the parent class's save method to handle saving the instance.