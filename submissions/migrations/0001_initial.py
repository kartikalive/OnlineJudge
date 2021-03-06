# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-26 02:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contests', '0005_auto_20170126_1015'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('utils', '0001_initial'),
        ('problems', '0006_auto_20170125_1218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='运行编号')),
                ('submit_time', models.DateTimeField(auto_now_add=True, verbose_name='提交时间')),
                ('status', models.IntegerField(choices=[(-1, 'Reserved'), (0, 'Accept'), (1, 'Presentation Error'), (2, 'Wrong Answer'), (3, 'Time Limit Exceed'), (4, 'Memory Limit Exceed'), (5, 'Output Limit Exceed'), (6, 'Run Time Error'), (7, 'Compile Error'), (8, 'Pending'), (9, 'Pending Rejudge'), (10, 'Compiling'), (11, 'Rejudging')], default=-1, verbose_name='判题状态')),
                ('exec_memory', models.IntegerField(default=0, verbose_name='使用内存')),
                ('exec_time', models.IntegerField(default=0, verbose_name='使用时间')),
                ('source_code', models.TextField(blank=True, verbose_name='源代码')),
                ('public', models.BooleanField(default=False, verbose_name='公开代码')),
                ('notes', models.CharField(blank=True, max_length=200, null=True, verbose_name='备注')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('contest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contests.Contest')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utils.CodeLang')),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='problems.Problem')),
            ],
            options={
                'verbose_name': '提交记录',
                'verbose_name_plural': '提交记录',
                'ordering': ['-id'],
            },
        ),
    ]
