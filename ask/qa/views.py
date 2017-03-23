from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm
from .utils.sh_paginate import paginate

def test(request, *args, **kwargs):
	return HttpResponse('OK')

@login_required(login_url='/login/')
def index(request):
	questions = Question.objects.order_by('-id')
	page, paginator = paginate(request, questions)
	paginator.baseurl = '/?page='
	return render(request, 'index.html',{
		'questions': page.object_list,
		'paginator': paginator,
		'page': page,
		})

@login_required(login_url='/login/')
def popular(request):
	questions = Question.objects.popular()
	page, paginator = paginate(request,questions)
	paginator.baseurl = '/popular/?page='
	return render(request, 'index.html',{
		'questions': page.object_list,
		'paginator': paginator,
		'page': page,
		})

@login_required(login_url='/login/')
def show_question(request, id):
	try:
		question = Question.objects.get(id=id)
	except Question.DoesNotExist:
		raise Http404
	if request.method == "POST":
		form = AnswerForm(request.POST)
		if form.is_valid():
			form._user = request.user
			comment = form.save()
			url = question.get_url()
			return HttpResponseRedirect(url)
	else:
		form = AnswerForm(initial={'question': question.id})

	return render(request, 'question.html',{
		'question': question,
		'form':form,
		})

@login_required(login_url='/login/')
def ask(request):
	if request.method == "POST":
		form = AskForm(request.POST)
		if form.is_valid():
			form._user = request.user
			post = form.save()
			url = post.get_url()
			return HttpResponseRedirect(url)
	else:
		form = AskForm()
	return render(request, 'ask.html', {
		'form': form,
		})

def signup(request):
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			user = form.save()
			auth_user = authenticate(username=user.username, password=form.cleaned_data['password'])
			login(request, auth_user)
			return HttpResponseRedirect('/')
	else:
		form = SignupForm()
	return render(request, 'signup.html',{
		'form': form
		})

def login_view(request):
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return HttpResponseRedirect('/')
	else:
		form = LoginForm()
		return render(request, 'login.html',{
			'form': form
			})