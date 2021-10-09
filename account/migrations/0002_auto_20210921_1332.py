# Generated by Django 3.2.6 on 2021-09-21 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='وضعیت مدیر'),
        ),
        migrations.AlterField(
            model_name='Film',
            name='status',
            field=models.CharField(choices=[('d', '\u200d\u200d\u200d\u200dبیش نویس'), ('p', 'منتشر')], default='d', max_length=1, verbose_name='وضعیت مقاله'),
        ),
    ]
