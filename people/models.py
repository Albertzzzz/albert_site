from django.db import models

# Create your models here.


class Person (models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def my_property(self):
        return self.name + ' ' + str(self.age)
    my_property.short_description = "name and age of the person"

    full_name = property(my_property)
