# Generated by Django 2.1.15 on 2020-02-26 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateField()),
                ('body', models.CharField(max_length=2000)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
