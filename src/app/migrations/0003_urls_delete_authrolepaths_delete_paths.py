# Generated by Django 5.1.2 on 2024-11-10 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_authrolepaths'),
    ]

    operations = [
        migrations.CreateModel(
            name='Urls',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('path', models.CharField(db_column='path', default='', max_length=256)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='created_date')),
                ('updated_date', models.DateTimeField(auto_now=True, db_column='updated_date')),
            ],
            options={
                'db_table': 'urls',
            },
        ),
        migrations.DeleteModel(
            name='AuthRolePaths',
        ),
        migrations.DeleteModel(
            name='Paths',
        ),
    ]
