from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField("Имя", max_length=30, blank=False, null=False)
    middle_name = models.CharField("Отчество", max_length=30)
    second_name = models.CharField("Фамилия", max_length=30)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
class Books(models.Model):
    title = models.CharField("Название", max_length=30)
    author = models.ForeignKey('Author', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    image = models.ImageField("Обложка", blank=True, upload_to='images/')
    description = models.CharField("Описание", max_length=200)
    year = models.IntegerField(null=True, blank=True)
    genre = models.CharField("Жанр", max_length=30)
    language = models.CharField("Язык", max_length=20)
    pages = models.IntegerField(null=True, blank=True)
    ISBN = models.IntegerField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'