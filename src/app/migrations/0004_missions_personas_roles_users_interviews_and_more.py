# Generated by Django 5.1.2 on 2024-11-11 14:58

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_urls_delete_authrolepaths_delete_paths'),
    ]

    operations = [
        migrations.CreateModel(
            name='Missions',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('message', models.CharField(db_column='message', default='', max_length=256)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='created_date')),
                ('updated_date', models.DateTimeField(auto_now=True, db_column='updated_date')),
            ],
            options={
                'db_table': 'missions',
            },
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('persona', models.CharField(db_column='persona', default='', max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='created_date')),
                ('updated_date', models.DateTimeField(auto_now=True, db_column='updated_date')),
            ],
            options={
                'db_table': 'personas',
            },
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('name', models.CharField(db_column='name', default='', max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='created_date')),
                ('updated_date', models.DateTimeField(auto_now=True, db_column='updated_date')),
            ],
            options={
                'db_table': 'roles',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('uuid', models.UUIDField(db_column='uuid', default=uuid.uuid4, primary_key=True, serialize=False)),
                ('username', models.CharField(db_column='username', default='', max_length=200)),
                ('first_name', models.CharField(db_column='first_name', default='', max_length=100)),
                ('last_name', models.CharField(db_column='last_name', default='', max_length=100)),
                ('email', models.EmailField(db_column='email', default='', max_length=256)),
                ('password', models.CharField(db_column='password', default='', max_length=256)),
                ('is_active', models.BooleanField(db_column='is_active', default=False)),
                ('last_login', models.DateTimeField(db_column='last_login', null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='created_date')),
                ('updated_date', models.DateTimeField(auto_now=True, db_column='updated_date')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Interviews',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('report', models.CharField(db_column='report', default='', max_length=1000)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='created_date')),
                ('updated_date', models.DateTimeField(auto_now=True, db_column='updated_date')),
                ('mission_id', models.ForeignKey(db_column='mission_id', default='', on_delete=django.db.models.deletion.CASCADE, to='app.missions')),
            ],
            options={
                'db_table': 'interviews',
            },
        ),
        migrations.AddField(
            model_name='missions',
            name='persona_id',
            field=models.ForeignKey(db_column='persona_id', default='', on_delete=django.db.models.deletion.CASCADE, to='app.personas'),
        ),
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('report', models.CharField(db_column='report', default='', max_length=1000)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='created_date')),
                ('updated_date', models.DateTimeField(auto_now=True, db_column='updated_date')),
                ('mission_id', models.ForeignKey(db_column='mission_id', default='', on_delete=django.db.models.deletion.CASCADE, to='app.missions')),
            ],
            options={
                'db_table': 'reports',
            },
        ),
        migrations.CreateModel(
            name='Url_permissions',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='created_date')),
                ('updated_date', models.DateTimeField(auto_now=True, db_column='updated_date')),
                ('role_id', models.ForeignKey(db_column='role_id', on_delete=django.db.models.deletion.CASCADE, to='app.roles')),
                ('url_id', models.ManyToManyField(db_column='url_id', to='app.urls')),
            ],
            options={
                'db_table': 'url_permissions',
            },
        ),
        migrations.CreateModel(
            name='Role_users',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('role_id', models.IntegerField(db_column='role_id', default=1)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='created_date')),
                ('updated_date', models.DateTimeField(auto_now=True, db_column='updated_date')),
                ('user_uuid', models.OneToOneField(db_column='user_uuid', default='', on_delete=django.db.models.deletion.CASCADE, to='app.users')),
            ],
            options={
                'db_table': 'role_users',
            },
        ),
        migrations.AddField(
            model_name='missions',
            name='user_uuid',
            field=models.ForeignKey(db_column='user_uuid', default='', on_delete=django.db.models.deletion.CASCADE, to='app.users'),
        ),
    ]