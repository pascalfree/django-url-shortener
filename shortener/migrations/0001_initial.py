# -*- coding: utf-8 -*-


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('usage_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
