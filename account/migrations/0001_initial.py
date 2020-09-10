# Generated by Django 2.2.14 on 2020-09-10 09:41

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import taggit.managers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('taggit', '0004_taggeduuiditem'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_removed', models.BooleanField(default=False)),
                ('id', model_utils.fields.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=40, unique=True, verbose_name='用户')),
                ('password', models.CharField(blank=True, max_length=128, null=True, verbose_name='密码')),
                ('email', models.EmailField(blank=True, max_length=25, null=True, verbose_name='邮箱')),
                ('mobile', models.CharField(blank=True, max_length=11, null=True, verbose_name='手机')),
                ('avatar', models.CharField(default='http://www.gravatar.com/avatar/bf5c77ba8067db6121b6f02d87674dcd?s=80&d=wavatar', max_length=200, verbose_name='头像')),
                ('qq', models.CharField(blank=True, max_length=32, null=True, verbose_name='QQ号')),
                ('wx', models.CharField(blank=True, max_length=32, null=True, verbose_name='微信')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='taggit.TaggedUUIDItem', to='taggit.Tag', verbose_name='Tags')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '- 用户模型',
                'verbose_name_plural': '- 用户模型',
                'ordering': ['-date_joined'],
            },
        ),
    ]