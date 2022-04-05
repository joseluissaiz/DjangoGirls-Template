from django.conf import settings
from django.db import models
from django.utils import timezone
#...

#Modelo Post >>>> contiene la información de una entrada dentro del blog.
class Post(models.Model):
    #Atributos
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    #Métodos
    #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #Publica la entrada dentro de la base de datos
    def publish(self):
        self.published_date = timezone.now() #fecha automática
        self.save()

    #to string
    def __str__(self):
        return self.title
