from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
	def new(self):
		return self.order_by('-added_at')
	
	def popular(self):
		return self.order_by('-rating')

class Question(models.Model):
	title = models.CharField(default='')
	text = models.TextField(default='')
	added_at = models.DateField(null=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	likes = models.ManyToManyField(User, related_name='q_to_l', blank=True)
	object = QuestionManager()

	def get_url(self):
		return '/question/' + str(self.pk) + '/'

	class Meta:
		ordering = ('-id',)

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField()
	question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
	author = models.ForeingKey(User, null=True, on_delete=models.SET_NULL)

