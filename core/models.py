from django.db import models

# Create your models here.

class Post(models.Model):
    #title

    title = models.CharField('Título', max_length= 500, blank= False, null= False)
    #conteudo
    content = models.TextField('Conteudo', blank=False, null=False)
    #data de publi
    date_published = models.DateField('Data da Publicação', auto_now_add= True)
    #slug
    slug = models.SlugField('Slug', editable=False)