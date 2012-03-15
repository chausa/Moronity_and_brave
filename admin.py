from django.contrib import admin
from blog.models import blog

class AdminBlog(admin.ModelAdmin):
	pass


admin.site.register(blog, AdminBlog)