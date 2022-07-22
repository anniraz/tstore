# Generated by Django 4.0.6 on 2022-07-21 05:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Characteristics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagonal', models.CharField(max_length=100, verbose_name='Диогональ')),
                ('cpu', models.CharField(max_length=255, verbose_name='Процессор')),
                ('operating_system', models.CharField(default='Без операционной системы', max_length=255, verbose_name='Операционная система')),
                ('ram', models.CharField(max_length=255, verbose_name='Объем оперативной памяти')),
                ('hard_disk_type', models.CharField(max_length=255, verbose_name='Тип жесткого диска')),
                ('storage_capacity', models.CharField(max_length=255, verbose_name='Объем накопителя ')),
                ('video_adapter', models.CharField(max_length=255, verbose_name='Видеоадаптер')),
                ('video_adapter_chipset', models.CharField(max_length=255, verbose_name='Чипсет видеоадаптера ')),
                ('video_adapter_memory_size', models.CharField(max_length=255, verbose_name='Объем памяти видеоадаптера')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='technology/')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=5000, verbose_name='Сообщение')),
                ('rating', models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('time_pub', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('price', models.PositiveIntegerField()),
                ('image', models.ImageField(upload_to='technology/')),
                ('video', models.URLField()),
                ('description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category')),
            ],
        ),
    ]