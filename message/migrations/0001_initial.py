# Generated by Django 2.2.14 on 2020-09-14 08:34

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0004_taggeduuiditem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('id', models.CharField(default='d1b23d36aa324d6fa7d40c59f5f60f86', max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='id')),
                ('project', models.CharField(max_length=50, verbose_name='项目标识')),
                ('ds', models.CharField(max_length=50, verbose_name='数据源')),
                ('type', models.CharField(max_length=128, verbose_name='消息标识')),
                ('host', models.CharField(max_length=128, verbose_name='主机标识')),
                ('title', models.CharField(max_length=128, verbose_name='消息标题')),
                ('level', models.PositiveSmallIntegerField(choices=[(0, '警告'), (1, '危险'), (2, '灾难')], verbose_name='消息等级')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, '告警'), (1, '恢复')], verbose_name='消息状态')),
                ('raw', models.TextField(blank=True, null=True, verbose_name='原始数据')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedUUIDItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': '- 消息管理',
                'verbose_name_plural': '- 消息管理',
                'ordering': ['-created'],
            },
        ),
    ]