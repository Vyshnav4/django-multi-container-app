from django.contrib import admin

from .models import Question, Choice

# This class allows us to customize the admin interface for the Question model.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3 # Provides 3 empty slots for adding new choices directly on the Question page.

class QuestionAdmin(admin.ModelAdmin):
    # This defines the layout of the fields on the add/change page.
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    # This adds the Choice model as an inline editable section on the Question page.
    inlines = [ChoiceInline]
    
    # These fields will be displayed on the main list view of questions.
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    # Adds a filter sidebar for filtering by publication date.
    list_filter = ['pub_date']
    # Adds a search box for searching by question text.
    search_fields = ['question_text']

# Register the Question model with the customized QuestionAdmin class.
admin.site.register(Question, QuestionAdmin)
