from django.db import models


class NewsPost(models.Model):
    title = models.CharField(verbose_name="Title", max_length=255)
    author_name = models.CharField(verbose_name="Author Name", max_length=100)
    link = models.URLField(verbose_name="Link")
    number_of_upvote = models.IntegerField(
        verbose_name="Amount of Upvote", default=0
    )

    created_at = models.DateTimeField(
        verbose_name="Creation Date", auto_now_add=True
    )

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "News Post"
        verbose_name_plural = "News Posts"

    def __str__(self):
        return self.title

    def upvote_post(self):
        """
        Upvote the specified post
        """
        self.number_of_upvote += 1
        self.save()


class Comment(models.Model):
    news_post = models.ForeignKey(
        NewsPost,
        on_delete=models.CASCADE,
        related_name="comments",
        verbose_name="News Post",
    )
    author_name = models.CharField("Author Name", max_length=100)
    content = models.TextField("Content")

    created_at = models.DateTimeField("Creation Date", auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.content
