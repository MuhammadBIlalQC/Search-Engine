# Generated by Django 2.1.4 on 2018-12-20 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TermPosting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=30)),
                ('docIDs', models.CharField(max_length=100)),
            ],
        ),
    ]
