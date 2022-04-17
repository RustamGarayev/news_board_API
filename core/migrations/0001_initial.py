# Generated by Django 3.2.13 on 2022-04-17 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="NewsPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(max_length=255, verbose_name="Title"),
                ),
                (
                    "author_name",
                    models.CharField(
                        max_length=100, verbose_name="Author Name"
                    ),
                ),
                ("link", models.URLField(verbose_name="Link")),
                (
                    "number_of_upvote",
                    models.IntegerField(
                        default=0, verbose_name="Amount of Upvote"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation Date"
                    ),
                ),
            ],
            options={
                "verbose_name": "News Post",
                "verbose_name_plural": "News Posts",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "author_name",
                    models.CharField(
                        max_length=100, verbose_name="Author Name"
                    ),
                ),
                ("content", models.TextField(verbose_name="Content")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Creation Date"
                    ),
                ),
                (
                    "news_post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="core.newspost",
                        verbose_name="News Post",
                    ),
                ),
            ],
            options={
                "verbose_name": "Comment",
                "verbose_name_plural": "Comments",
                "ordering": ("-created_at",),
            },
        ),
    ]
