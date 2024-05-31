from django.db import models

# Create your models here.



class Category(models.Model):
    category_name = models.CharField(max_length=150)

    def __str__(self):
        return self.category_name

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    review = models.ForeignKey('Review', on_delete=models.CASCADE, null=True)




    def __str__(self):
        return self.name


class Review(models.Model):
    content = models.TextField()


    def __str__(self):
        return self.content


