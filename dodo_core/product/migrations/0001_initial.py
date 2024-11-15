# Generated by Django 5.1.3 on 2024-11-15 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.PositiveSmallIntegerField(verbose_name='цена')),
                ('compound', models.TextField(verbose_name='состав')),
                ('is_new', models.BooleanField()),
                ('image', models.ImageField(upload_to='products', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
