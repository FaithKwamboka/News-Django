# Generated by Django 4.0.4 on 2022-05-25 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_article_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(default='Faith', null=True, upload_to='articles/'),
        ),
    ]
