from django.db import models
from django.contrib.auth.models import User

class QuestionManager(models.Manager):
	def new(self):
		return self.order_by('-added_at')
	
	def popular(self):
		return self.order_by('-rating')

class AnswerManager(models.Manager):
	def sorting(self, question):
		return Answer.objects.order_by('added_at').filter(question=question)
		

class Question(models.Model):
	title = models.CharField(default='', max_length=120)
	text = models.TextField(default='')
	added_at = models.DateTimeField(blank=True)
	rating = models.IntegerField(default=0)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	likes = models.ManyToManyField(User, related_name='q_to_l', blank=True)
	objects = QuestionManager()

	def get_url(self):
		return '/question/' + str(self.pk) + '/'

	def __str__(self):
		return self.title

	class Meta:
		ordering = ('-id',)

class Answer(models.Model):
	text = models.TextField(default='')
	added_at = models.DateTimeField(blank=True, auto_now_add=True)
	question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
	author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
	objects = AnswerManager()

	def __str__(self):
		return self.text