# Generated by Django 5.2.1 on 2025-05-21 16:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smart', '0004_rename_igm_notice_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='活动标题')),
                ('text', models.TextField(blank=True, null=True, verbose_name='活动描述')),
                ('date', models.DateField(verbose_name='举办活动日期')),
                ('count', models.IntegerField(default=0, verbose_name='报名人数')),
                ('total_count', models.IntegerField(default=0, verbose_name='总人数')),
                ('score', models.IntegerField(default=0, verbose_name='积分')),
            ],
            options={
                'verbose_name_plural': '活动表',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='姓名')),
                ('avatar', models.FileField(max_length=128, upload_to='avatar', verbose_name='头像')),
                ('create_date', models.DateField(auto_now_add=True, verbose_name='日期')),
                ('score', models.IntegerField(default=0, verbose_name='积分')),
                ('mobile', models.CharField(max_length=11, null=True, verbose_name='手机号')),
            ],
            options={
                'verbose_name_plural': '用户表',
            },
        ),
        migrations.CreateModel(
            name='JoinRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exchange', models.BooleanField(default=False, verbose_name='是否已兑换')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ac', to='smart.activity', verbose_name='活动')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smart.userinfo', verbose_name='用户')),
            ],
            options={
                'verbose_name_plural': '活动报名记录',
            },
        ),
        migrations.AddField(
            model_name='activity',
            name='join_record',
            field=models.ManyToManyField(through='smart.JoinRecord', through_fields=('activity', 'user'), to='smart.userinfo', verbose_name='参与者'),
        ),
    ]
