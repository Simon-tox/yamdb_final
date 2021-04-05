# Generated by Django 3.0.5 on 2020-12-03 19:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('titles', '0004_auto_20201203_1030'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0007_auto_20201203_1934'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='title',
            new_name='title_id',
        ),
        migrations.AlterField(
            model_name='reviews',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='reviews',
            unique_together={('title_id', 'author')},
        ),
    ]
