# Generated by Django 3.2.25 on 2024-08-26 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('contents', models.TextField()),
                ('views', models.IntegerField()),
                ('create_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
