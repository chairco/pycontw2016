# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-21 14:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20161219_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customevent',
            name='conference',
            field=models.SlugField(choices=[('pycontw-2016', 'PyCon Taiwan 2016'), ('pycontw-2017', 'PyCon Taiwan 2017')], default='pycontw-2017', verbose_name='conference'),
        ),
        migrations.AlterField(
            model_name='keynoteevent',
            name='conference',
            field=models.SlugField(choices=[('pycontw-2016', 'PyCon Taiwan 2016'), ('pycontw-2017', 'PyCon Taiwan 2017')], default='pycontw-2017', verbose_name='conference'),
        ),
        migrations.AlterField(
            model_name='keynoteevent',
            name='slug',
            field=models.SlugField(help_text="This is used to link to the speaker's introduction on the Keynote page, e.g. 'liang2' will link to '/en/events/keynotes/#keynote-speaker-liang2'.", verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='proposedtalkevent',
            name='conference',
            field=models.SlugField(choices=[('pycontw-2016', 'PyCon Taiwan 2016'), ('pycontw-2017', 'PyCon Taiwan 2017')], default='pycontw-2017', verbose_name='conference'),
        ),
        migrations.AlterField(
            model_name='sponsoredevent',
            name='conference',
            field=models.SlugField(choices=[('pycontw-2016', 'PyCon Taiwan 2016'), ('pycontw-2017', 'PyCon Taiwan 2017')], default='pycontw-2017', verbose_name='conference'),
        ),
        migrations.AlterField(
            model_name='sponsoredevent',
            name='python_level',
            field=models.CharField(choices=[('NOVICE', 'Novice'), ('INTERMEDIATE', 'Intermediate'), ('EXPERIENCED', 'Experienced')], help_text='The choice of talk level matters during the review process. More definition of talk level can be found at the <a href="/en/speaking/talk/" target="_blank">How to Propose a Talk</a> page. Note that a proposal won\'t be more likely to be accepted because of being "Novice" level. We may contact you to change the talk level when we find the content is too-hard or too-easy for the target audience.', max_length=12, verbose_name='Python level'),
        ),
        migrations.AlterField(
            model_name='sponsoredevent',
            name='recording_policy',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, help_text="Whether you agree to give permission to PyCon Taiwan to record, edit, and release audio and video of your presentation. More information can be found at <a href='/en/speaking/recording/' target='_blank'>Recording Release</a> page.", verbose_name='recording policy'),
        ),
    ]
