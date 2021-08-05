from django.contrib import admin

# Register your models here.

from .models import Question, Tag, Topic

admin.site.register(Question)
admin.site.register(Tag)
admin.site.register(Topic)
