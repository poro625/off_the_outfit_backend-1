
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0001_initial'),
        ('taggit', '0005_auto_20220424_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(verbose_name='댓글 본문')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='댓글 생성 일자')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='댓글 수정 일자')),
                ('comment_like', models.ManyToManyField(blank=True, related_name='like_comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='게시글 본문')),
                ('image', models.ImageField(blank=True, null=True, upload_to='feed_images/', verbose_name='게시글 사진')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='게시글 생성 일자')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='게시글 수정 일자')),
                ('report_point', models.PositiveIntegerField(default=0, verbose_name='신고 포인트')),
                ('like', models.ManyToManyField(blank=True, related_name='like_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'feeds',
            },
        ),
        migrations.CreateModel(
            name='SearchWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=30, verbose_name='검색어')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='검색일자')),
            ],
            options={
                'db_table': 'search_words',
            },
        ),
        migrations.CreateModel(
            name='TaggedFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communities.feed')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_items', to='taggit.tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReportFeed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.TextField(verbose_name='신고내용')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='신고일자')),
                ('feed', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='reports', to='communities.feed')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'report_feeds',
            },
        ),
        migrations.CreateModel(
            name='ReComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recomment', models.TextField(blank=True, null=True, verbose_name='대댓글 본문')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='대댓글 생성 일자')),
                ('comment', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='communities.comment')),
                ('recomment_like', models.ManyToManyField(blank=True, related_name='like_recomments', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'recomments',
            },
        ),
        migrations.CreateModel(
            name='FeedProductRelation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='communities.feed')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'db_table': 'feed_product_relation',
            },
        ),
        migrations.AddField(
            model_name='feed',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='communities.TaggedFeed', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='feed',
            name='unlike',
            field=models.ManyToManyField(blank=True, related_name='unlike_posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='feed',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feeds', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='feed',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='feeds', to='communities.feed'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
