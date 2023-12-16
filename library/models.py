from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

RATING = (
    (1, "⭐☆☆☆☆"),
    (2, "⭐⭐☆☆☆"),
    (3, "⭐⭐⭐☆☆"),
    (4, "⭐⭐⭐⭐☆"),
    (5, "⭐⭐⭐⭐⭐"),
)

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
    ISBN = models.CharField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    # def total_books(self, ):

    def get_absolute_url(self):
        return reverse('book_page', kwargs={'book_slug': self.slug})

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'


class BookReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    book = models.ForeignKey(Books, on_delete=models.SET_NULL, null=True, related_name='book_reviews')
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-create_at']
        indexes = [
            models.Index(fields=['create_at']),
        ]

    def __str__(self):
        return self.book.title

    def get_rating(self):
        return self.rating