# Generated by Django 3.2.5 on 2022-01-09 15:31

import DjangoUeditor.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='项目名称')),
                ('description', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('publishDate', models.DateTimeField(default=django.utils.timezone.now, max_length=20, verbose_name='发布时间')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
            ],
            options={
                'verbose_name': '实践项目',
                'verbose_name_plural': '实践项目',
                'ordering': ['-publishDate'],
            },
        ),
        migrations.DeleteModel(
            name='Resource',
        ),
    ]
