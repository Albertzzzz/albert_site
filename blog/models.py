from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True, editable=True)
    update_time = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title
