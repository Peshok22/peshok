from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField('название статьи', max_length = 50)
    anons = models.CharField('анонс статьи', max_length = 250)
    full_text = models.TextField('текст статьи')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.id}'