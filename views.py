from django.shortcuts import render_to_response
from blog.models import blog
from django.views.generic import ListView


class BlogList(ListView):
	model = blog


def index(request):
	entries = blog.objects.all()
	return render_to_response('index.html', locals())