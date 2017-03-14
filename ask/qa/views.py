from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_GET
from .models import Question, Answer
from .utils.sh_paginate import paginate

def test(request, *args, **kwargs):
	return HttpResponse('OK')

@require_GET
def index(request):
	questions = Question.objects.new()
	page, paginator = paginate(request, questions)
	paginator.baseurl = '/?page='
	return render(request, 'index.html',{
		'questions': page.object_list,
		'paginator': paginator,
		'page': page
		})

@require_GET
def popular(request):
	questions = Question.objects.popular()
	page, paginator = paginate(request,questions)
	paginator.baseurl = '/popular/?page='
	return render(request, 'index.html',{
		'questions': page.object_list,
		'paginator': paginator,
		'page': page
		})

@require_GET
def show_question(request, id):
	question = get_object_or_404(Question, id=id)
	answers = Answer.objects.filter(question=question)
	return render(request, 'question.html',{
		'question': question,
		'answers': answers
		})