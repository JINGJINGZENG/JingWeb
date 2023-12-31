from django.db import models
from DjangoUeditor.models import UEditorField
import django.utils.timezone as timezone


class Projects(models.Model):
    title = models.CharField(max_length=50, verbose_name='项目名称')
    description = UEditorField(u'内容',
                               default='',
                               width=1000,
                               height=300,
                               imagePath='projects/images',
                               filePath='projects/files')
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='发布时间')
    views = models.PositiveIntegerField('浏览量', default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publishDate']
        verbose_name = "实践项目"
        verbose_name_plural = verbose_name