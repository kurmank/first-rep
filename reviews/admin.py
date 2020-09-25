from django.contrib import admin
from .models import Review, Comment

# Register your models here.

class CommentInLine(admin.TabularInline):
    model = Comment

class ReviewAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine,
    ]

admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment)

