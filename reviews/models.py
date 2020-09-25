from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.

class Review(models.Model):
    film_name = models.CharField(max_length=256)
    actors = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,

    )

    def __str__(self):
        return self.film_name


    def get_absolute_url(self):
        return reverse('review_detail', args=[str(self.id)])

class Comment(models.Model):
    review = models.ForeignKey(Review, 
    on_delete=models.CASCADE, 
    related_name='comments'
    )
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        
    )

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse('review_list')
