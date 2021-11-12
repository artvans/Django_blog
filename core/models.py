from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Post(models.Model):
    #title

    title = models.CharField('Título', max_length= 500, blank= False, null= False)
    #resumo
    resume =models.TextField(default='')
    #conteudo
    content = RichTextField()
    #data de publi
    date_published = models.DateField('Data da Publicação', auto_now_add= True)
    #slug
    slug = models.SlugField('Slug', editable=False)


    def __str__(self):
       return self.title

    def save(self, *args, **kwargs):

        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args,**kwargs)