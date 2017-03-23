from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Question, Answer

class AskForm(forms.Form):
	title = forms.CharField(max_length=100)
	text = forms.CharField(widget=forms.Textarea)

	def clean(self):
		pass

	def save(self):
		question = Question(**self.cleaned_data)
		#question.author_id = self._user.id
		question.save()
		return question

class AnswerForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea)
	question = forms.IntegerField(widget=forms.HiddenInput)

	def clean_question(self):
		question_id = self.cleaned_data['question']
		try:
			question = Question.objects.get(id=question_id)
		except Question.DoesNotExist:
			question = None
		return question

	def save(self):
		comment = Answer(** self.cleaned_data)
		comment.save()
		return comment

class SignupForm(forms.Form):
	username = forms.CharField(max_length=100)
	first_name=forms.CharField(max_length=100, required=False)
	last_name=forms.CharField(max_length=100, required=False)
	email = forms.EmailField(required=False)
	password = forms.CharField(widget=forms.PasswordInput)

	def clean_username(self):
		username = self.cleaned_data['username']
		if len(username) < 3:
			raise forms.ValidationError('Username is too small')
		return username

	def clean_password(self):
		password = self.cleaned_data['password']
		if len(password) < 3:
			raise forms.ValidationError('Password is too small')
		return password

	def save(self):
		return User.objects.create_user(**self.cleaned_data)

class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(widget=forms.PasswordInput)

	def clean_username(self):
		username = self.cleaned_data['username']
		if len(username) < 3:
			raise forms.ValidationError('Username is too small')
		return username

	def clean_password(self):
		password = self.cleaned_data['password']
		if len(password) < 3:
			raise forms.ValidationError('Password is too small')
		return password

	def clean(self):
		user = authenticate(username = self.cleaned_data['username'], password=self.cleaned_data['password'])
		if not user:
			raise forms.ValidationError('The username or password is wrong!')

		if user and not user.is_active:
			raise forms.ValidationError('This user is not active')

		return self.cleaned_data

	def save(self):
		return authenticate(username = self.cleaned_data['username'], password=self.cleaned_data['password'])