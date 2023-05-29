from django.db import models
from django.urls import reverse


class Post(models.Model):
    tag = models.CharField(max_length=30, verbose_name="Тег")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    subtitle = models.CharField(max_length=255, blank=True, verbose_name="Подзаголовок")
    content = models.TextField(blank=True, verbose_name="Текст поста")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")  # height_field=355,width_field=710,Cha
    video = models.CharField(max_length=255, blank=True, null=True, verbose_name="Видео")  # Charfield
    created_at = models.DateTimeField(verbose_name="Время создания", auto_now_add=True)  # DateTimeField (%m/%d 'в' %h/%m)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")  # DateTimeField (%m/%d 'в' %h/%m)
    is_published = models.BooleanField(default=True, verbose_name="Публикация")

    def __str__(self):
        return f"{self.tag}: {self.title} | {self.created_at} | {self.is_published}"

    def get_absolute_url(self):
        return reverse('tags', kwargs={'tag': self.tag, 'slug':self.slug})

    class Meta:
        verbose_name = "Посты"
        verbose_name_plural = "Посты"
        ordering = ['-id']


class User:
    ...


