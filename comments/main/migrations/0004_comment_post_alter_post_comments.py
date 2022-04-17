# Generated by Django 4.0.4 on 2022-04-16 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_remove_comment_post_alter_comment_parent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='post_comment', to='main.post'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(related_name='postt', to='main.comment'),
        ),
    ]