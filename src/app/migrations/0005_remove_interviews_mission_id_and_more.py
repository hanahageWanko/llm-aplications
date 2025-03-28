# Generated by Django 5.1.7 on 2025-03-22 16:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_personas_persona'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interviews',
            name='mission_id',
        ),
        migrations.RemoveField(
            model_name='reports',
            name='mission_id',
        ),
        migrations.CreateModel(
            name='RequirementDefinitions',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('future_outlook', models.CharField(db_column='future_outlook', db_comment='今後の展望', default='', max_length=256)),
                ('issues_and_solutions', models.CharField(db_column='issues_and_solutions', db_comment='課題と対策', default='', max_length=256)),
                ('key_Features', models.CharField(db_column='key_Features', db_comment='主要機能', default='', max_length=256)),
                ('kpi', models.CharField(db_column='kpi', db_comment='kpi', default='', max_length=256, null=True)),
                ('load_map_year1', models.CharField(db_column='load_map_year1', db_comment='3年間のプロダクトロードマップ1年目', default='', max_length=256, null=True)),
                ('load_map_year2', models.CharField(db_column='load_map_year2', db_comment='3年間のプロダクトロードマップ2年目', default='', max_length=256, null=True)),
                ('load_map_year3', models.CharField(db_column='load_map_year3', db_comment='3年間のプロダクトロードマップ3年目', default='', max_length=256, null=True)),
                ('message', models.CharField(db_column='message', db_comment='追加指示や留意点', default='', max_length=256)),
                ('milestone', models.CharField(db_column='milestone', db_comment='マイルストーン', default='', max_length=256)),
                ('monetization_plan', models.CharField(db_column='monetization_plan', db_comment='収益化構想', default='', max_length=256, null=True)),
                ('non_functional_requirements', models.CharField(db_column='non_functional_requirements', db_comment='非機能用件', default='', max_length=256)),
                ('overview', models.CharField(db_column='overview', db_comment='概要', default='', max_length=256)),
                ('risk', models.CharField(db_column='risk', db_comment='risk', default='', max_length=256, null=True)),
                ('technical_requirements', models.CharField(db_column='technical_requirements', db_comment='技術用件', default='', max_length=256)),
                ('created_date', models.DateTimeField(auto_now_add=True, db_column='created_date')),
                ('updated_date', models.DateTimeField(auto_now=True, db_column='updated_date')),
                ('persona_id', models.ForeignKey(db_column='persona_id', db_comment='ペルソナID', default='', on_delete=django.db.models.deletion.CASCADE, to='app.personas')),
                ('user_uuid', models.ForeignKey(db_column='user_uuid', default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'requirement_definitions',
            },
        ),
        migrations.AddField(
            model_name='interviews',
            name='requirement_definition_id',
            field=models.ForeignKey(db_column='requirement_definition_id', default='', on_delete=django.db.models.deletion.CASCADE, to='app.requirementdefinitions'),
        ),
        migrations.AddField(
            model_name='reports',
            name='requirement_definition_id',
            field=models.ForeignKey(db_column='requirement_definition_id', default='', on_delete=django.db.models.deletion.CASCADE, to='app.requirementdefinitions'),
        ),
        migrations.DeleteModel(
            name='Missions',
        ),
    ]
