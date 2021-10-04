# Generated by Django 3.2.7 on 2021-10-01 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Product title')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Product image')),
                ('description', models.TextField(null=True, verbose_name='Product description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Product price')),
                ('diagonal', models.CharField(max_length=255, verbose_name='diagonal')),
                ('matrix', models.CharField(max_length=255, verbose_name='display matrix')),
                ('accum', models.CharField(max_length=255, verbose_name='accum volume')),
                ('ram', models.CharField(max_length=255, verbose_name='RAM')),
                ('sd', models.CharField(max_length=255, verbose_name='SD volume')),
                ('main_cam_mp', models.CharField(max_length=255, verbose_name='main camera')),
                ('front_cam_mp', models.CharField(max_length=255, verbose_name='frontal camera')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Product category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Product title')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Product image')),
                ('description', models.TextField(null=True, verbose_name='Product description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Product price')),
                ('diagonal', models.CharField(max_length=255, verbose_name='diagonal')),
                ('matrix', models.CharField(max_length=255, verbose_name='display matrix')),
                ('proccesor_freq', models.CharField(max_length=255, verbose_name='proccesor freq')),
                ('ram', models.CharField(max_length=255, verbose_name='RAM')),
                ('videp_card', models.CharField(max_length=255, verbose_name='videp card')),
                ('time_without_charge', models.CharField(max_length=255, verbose_name='time without charge')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Product category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
