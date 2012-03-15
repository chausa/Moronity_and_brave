from django.shortcuts import render_to_response
from blog.models import blog
from django.views.generic import ListView
from comments.models import comment


class BlogList(ListView):
	model = blog


def index(request):
	entries = blog.objects.all()
	comments = comment.objects.all()
	return render_to_response('index.html', locals())