# Generated by Django 5.1.7 on 2025-06-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_noticia_capa_noticia_alter_noticia_corpo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='corpo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
