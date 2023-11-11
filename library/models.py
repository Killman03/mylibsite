from django.db import models
from django.urls import reverse


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
    title = models.CharField("Название", max_length=80)
    slug = models.CharField(max_length=80, unique=True, db_index=True, verbose_name='URL')
    author = models.ForeignKey('Author', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    image = models.ImageField("Обложка", upload_to='images/%Y/%m/%d/')
    file = models.FileField("Загрузить", upload_to='books/')
    description = models.CharField("Описание", max_length=1000)
    year = models.IntegerField(null=True, blank=True)
    genre = models.CharField("Жанр", max_length=30)
    language = models.CharField("Язык", max_length=20)
    pages = models.IntegerField(null=True, blank=True)
    ISBN = models.IntegerField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_page', kwargs={'book_slug': self.slug})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class RatingStar(models.Model):
    value = models.SmallIntegerField('Количество', default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = 'Звезда рейтинга'
        verbose_name_plural = 'Звезды рейтинга'
        ordering = ["-value"]


class Rating(models.Model):
    ip = models.CharField('IP адрес', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name='Звезда')
    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name='Книга')

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


