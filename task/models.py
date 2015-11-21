from django.db import models
from django.contrib.auth.models import User

class Feedback(models.Model):

    class Meta:
        verbose_name_plural = 'Сообщения'
        verbose_name = 'Сообщение'

    email = models.EmailField(verbose_name='Эл. Почта')
    message = models.TextField(verbose_name='Сообщение')
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ', '.join([str(self.date), self.user.username])
