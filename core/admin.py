from django.contrib import admin
from core.models import NewsPost, Comment


@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
