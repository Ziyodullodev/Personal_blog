from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    caption = models.TextField()
    topic = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photo')
    data = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.title}"

class Books(models.Model):
    Name = models.CharField(max_length=255)
    about = models.CharField(max_length=255)
    language = models.CharField(max_length=50, choices=(('Uzbek', 'Uzbek'),('English', 'English'),('Russian', 'Russian')))    
    photo = models.ImageField(upload_to='books')
    file = models.FileField(upload_to='books/file')
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.Name}"