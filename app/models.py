from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


# Create your models here.
class Region(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nomi")
    area_info = models.TextField(blank=True, null=True)
    population = models.IntegerField(null=True, verbose_name="Aholisi")
    population_compared_to = models.IntegerField(null=True)
    image = models.ImageField(upload_to='area_img/', null=True)
    published = models.BooleanField(default=True, verbose_name="Sahifaga chiqarish")
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name="Joylash vaqti")
    parent = models.ForeignKey('self', verbose_name="Joylashgan hudud", on_delete=models.CASCADE, related_name='territories', blank=True, null=True)

    def __str__(self):
        return self.name

    def average_rating(self) -> float:
        return Rating.objects.filter(post=self).aggregate(Avg("rating"))["rating__avg"] or 0

    class Meta:
        ordering = ['name']
        verbose_name = "Hudud"
        verbose_name_plural = "Hududlar"


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Region, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.post.header}: {self.rating}"

