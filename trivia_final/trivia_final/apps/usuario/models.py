from django.db import models
from thumbs import ImageWithThumbsField
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class datos_adicionales_usuario(models.Model):
	username=models.OneToOneField(User, unique=True)
	pais=models.CharField(max_length=100, null=True)
	avatar=ImageWithThumbsField(upload_to="avatares/", sizes=((50,50),(200,200)), null=True)
	def __unicode__(self):
		return self.username.username
	class Meta:
		verbose_name = _('Datos Adicionales de usuario')
		verbose_name_plural = _('Datos Adicionales de usuarios')
class temas(models.Model):
	username=models.ForeignKey(User)
	tema=models.CharField(max_length=100, null=True)
	class Meta:
		verbose_name = _('Tema')
		verbose_name_plural = _('Temas')
class preguntas(models.Model):
	username=models.ForeignKey(User)
	temas=models.ManyToManyField(temas)
	pregunta=models.CharField(max_length=100, null=True)
	class Meta:
		verbose_name = _('Pregunta')
		verbose_name_plural = _('Preguntas')
class respuestas(models.Model):
	preguntas=models.ForeignKey(preguntas)
	respuesta=models.CharField(max_length=100)
	class Meta:
		verbose_name = _('Respuestas')
		verbose_name_plural = _('Respuestas')
class rate(models.Model):
	preguntas=models.ForeignKey(preguntas)
	rates=((0,0),(1,1),(2,2),(3,3),(4,4),(5,5))
	rate=models.IntegerField(choices=rates,default=0)
	class Meta:
		verbose_name = _('Rate')
		verbose_name_plural = _('Rate')