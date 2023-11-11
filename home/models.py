from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.urls import reverse


# Create your models here.
class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False')
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(blank=True, max_length=50)
    whatsapp = models.CharField(blank=True, max_length=50)
    telegram = models.CharField(blank=True, max_length=50)
    email = models.CharField(blank=True, max_length=50)
    instagram = models.CharField(blank=True, max_length=50)
    about_us = RichTextUploadingField(blank=True)
    contacts = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'

class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed')
    )

    name = models.CharField("Имя", max_length=30)
    your_email = models.CharField("Почта", max_length=50)
    subject = models.CharField("Тема", max_length=50)
    your_message = models.TextField("Сообщение", blank=True, max_length=255)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=20)
    note = models.CharField(blank=True, max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = "Контакты"

class Events(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False')
    )
    title = models.CharField("Название", max_length=50)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, verbose_name='URL')
    details = models.CharField("Детали", max_length=150)
    image = models.ImageField("Картинка", upload_to='images/%Y/%m/%d/')
    location = models.CharField("Место проведения", blank=True, max_length=50)
    for_who = models.CharField('Для кого?', blank=True, max_length=50)
    descriptions = RichTextUploadingField("Описание", blank=True)
    date = models.DateField('Дата события')
    start_time = models.TimeField('Время начала')
    end_time = models.TimeField("Время конца")
    is_important = models.BooleanField('Важное', default=False)
    is_attractive = models.BooleanField('Интересное', default=False)
    status = models.CharField("Опубликовать", max_length=10, choices=STATUS, default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('meeting_details', kwargs={'meeting_slug': self.slug})
    class Meta:
        verbose_name = 'Встреча'
        verbose_name_plural = 'Встречи'