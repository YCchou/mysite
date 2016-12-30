# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from taggit.managers import TaggableManager


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(
            status='published')


class Post(models.Model):
    objects = models.Manager()
    published = PublishedManager()
    STATUS_CHOICES = (('draft', 'Draft'),
                      ('published', 'Published'), )

    title = models.CharField('标题', max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    author = models.ForeignKey(User, related_name='blog_posts')
    body = models.TextField('正文')
    publish = models.DateTimeField('发布时间', default=timezone.now)
    created = models.DateTimeField('创建时间', auto_now=True)
    status = models.CharField('文章状态',
                              max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    tags = TaggableManager()

    summary = models.CharField('摘要', max_length=54, blank=True, null=True)
    views = models.PositiveIntegerField('浏览量', default=0)
    likes = models.PositiveIntegerField('点赞数', default=0)
    topped = models.BooleanField('置顶', default=False)
    category = models.ForeignKey('Category',
                                 verbose_name='分类',
                                 null=True,
                                 on_delete=models.SET_NULL)

    class Meta:
        ordering = ('-publish', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.publish.year, self.publish.strftime('%m'),
                             self.publish.strftime('%d'), self.slug])
