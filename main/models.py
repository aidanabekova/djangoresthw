from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                related_name='reviews')

    def __str__(self):
        return self.text











