# Generated by Django 4.0.4 on 2022-04-17 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_post_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ManyToManyField(blank=True, null=True, related_name='children', to='main.comment'),
        ),
    ]