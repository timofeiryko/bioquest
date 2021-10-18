from django.contrib import admin
import nested_admin
from django import forms

# Register your models here.

from .models import Question, QuImage, Tag, Topic, VarList, Relative, RelInitial, ItemList
from .models import Comment, CoImage, CoFile

class VarLine(nested_admin.NestedTabularInline):
    model = VarList

class TopicLine(nested_admin.NestedStackedInline):
    model = Topic

class ItemLine(nested_admin.NestedStackedInline):
    model = ItemList

class RelInitialLine(nested_admin.NestedStackedInline):
    model = RelInitial

class RelativelLine(nested_admin.NestedStackedInline):
    model = Relative
    inlines=[RelInitialLine]

class QuImageInline(nested_admin.NestedStackedInline):
    model = QuImage

class CoImageInline(nested_admin.NestedStackedInline):
    model = CoImage

class CoFileInline(nested_admin.NestedStackedInline):
    model = CoFile

class CommentInline(nested_admin.NestedStackedInline):
    model = Comment
    inlines = [CoImageInline, CoFileInline]

class QuestionAdmin(nested_admin.NestedModelAdmin):
    model = Question
    inlines = [
        QuImageInline,
        CommentInline,
        VarLine,
        RelativelLine,
        ItemLine,
    ]

class TagAdmin(nested_admin.NestedModelAdmin):
    model = Tag
    inlines = [TopicLine]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(QuImage)
admin.site.register(Topic)
admin.site.register(VarList)
admin.site.register(Relative)
admin.site.register(RelInitial)
admin.site.register(ItemList)
admin.site.register(Comment)
admin.site.register(CoImage)
admin.site.register(CoFile)
