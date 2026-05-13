from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=300)

class Author(models.Model):
    name = models.CharField(max_length=200)
    DOB = models.DateField(null=True)

class Book(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=1)
    pubdate = models.DateTimeField()
    rating = models.SmallIntegerField(default=1)

    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.SET_NULL)
    authors = models.ManyToManyField(Author)


class Book7(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    price = models.FloatField(default=0.0)
    edition = models.SmallIntegerField(default=1)

    def __str__(self):
        return self.title


class Address11(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class Student11(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.ForeignKey(Address11, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Address22(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


class Student22(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    addresses = models.ManyToManyField(Address22)

    def __str__(self):
        return self.name


class Product11(models.Model):

    name = models.CharField(max_length=100)

    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name