from django.contrib import admin

from .models import AdvUser, SubRubric, SuperRubric, Bb, AdditionalImage
from .forms import SubRubricForm

admin.site.register(AdvUser)


class SubRubricInline(admin.TabularInline):
    model = SubRubric


class SuperRubricAdmin(admin.ModelAdmin):
    exclude = ('super_rubric',)
    inlines = (SubRubricInline,)


admin.site.register(SuperRubric, SuperRubricAdmin)


class SubRubricAdmin(admin.ModelAdmin):
    form = SubRubricForm


admin.site.register(SubRubric, SubRubricAdmin)


class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage


class BbAdmin(admin.ModelAdmin):
    list_display = ('rubric', 'title', 'content', 'author', 'created_at')
    fields = (('rubric', 'author'), 'title', 'content', 'price', 'contacts', 'image', 'is_active')
    inlines = (AdditionalImageInline,)


admin.site.register(Bb, BbAdmin)
