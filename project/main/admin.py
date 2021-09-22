from django.contrib import admin
import nested_admin
from django import forms

# Register your models here.

from .models import Question, Tag, Topic, VarList, Relative, RelInitial, ItemList, MultipleImage, Comment

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

class MultipleImageInline(nested_admin.NestedGenericTabularInline ):
    model = MultipleImage

class CommentInline(nested_admin.NestedStackedInline):
    model = Comment

class QuestionAdmin(nested_admin.NestedModelAdmin):
    model = Question
    inlines = [
        CommentInline,
        MultipleImageInline,
        VarLine,
        RelativelLine,
        ItemLine,
    ]

class TagAdmin(nested_admin.NestedModelAdmin):
    model = Tag
    inlines = [TopicLine]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Topic)
admin.site.register(VarList)
admin.site.register(Relative)
admin.site.register(RelInitial)
admin.site.register(ItemList)
admin.site.register(MultipleImage)
admin.site.register(Comment)
