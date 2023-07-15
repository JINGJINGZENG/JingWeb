from django.db import models
from DjangoUeditor.models import UEditorField
import django.utils.timezone as timezone


class Resource(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    description = UEditorField(u'内容',
                               default='',
                               width=1000,
                               height=300,
                               imagePath='resource/images',
                               filePath='resource/files')
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='发布时间')
    views = models.PositiveIntegerField('浏览量', default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publishDate']
        verbose_name = "资源分享"
        verbose_name_plural = verbose_name