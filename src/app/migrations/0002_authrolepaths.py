# Generated by Django 5.1.2 on 2024-11-03 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthRolePaths',
            fields=[
                ('path_group_id', models.AutoField(primary_key=True, serialize=False)),
                ('group_id', models.ForeignKey(db_column='group_id', default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='auth.group')),
                ('path_id', models.ForeignKey(db_column='path_id', default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.paths')),
            ],
            options={
                'db_table': 'path_group',
            },
        ),
    ]