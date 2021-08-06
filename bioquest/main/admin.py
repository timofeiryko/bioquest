from django.contrib import admin
import nested_admin

# Register your models here.

from .models import Question, Tag, Topic, VarList, Relative, RelInitial

class VarLine(nested_admin.NestedStackedInline):
    model = VarList


class RelInitialLine(nested_admin.NestedStackedInline):
    model = RelInitial

class RelativelLine(nested_admin.NestedStackedInline):
    model = Relative
    inlines=[RelInitialLine]

class QuestionAdmin(nested_admin.NestedModelAdmin):
    inlines = [
        VarLine,
        RelativelLine
    ]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Tag)
admin.site.register(Topic)
admin.site.register(VarList)
admin.site.register(Relative)
admin.site.register(RelInitial)
