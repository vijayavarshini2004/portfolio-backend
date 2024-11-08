# Generated by Django 5.0.6 on 2024-09-15 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_1', models.TextField()),
                ('point_2', models.TextField()),
                ('point_3', models.TextField()),
                ('point_4', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('resume', models.FileField(upload_to='resumes/')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('caption', models.CharField(max_length=255)),
                ('demo_video', models.FileField(upload_to='videos/')),
                ('project_overview', models.TextField()),
                ('tech_stack_used', models.TextField()),
                ('key_features', models.TextField()),
                ('challenges_faced', models.TextField()),
                ('use_cases', models.TextField()),
                ('future_enhancements', models.TextField()),
                ('repository_link', models.URLField()),
                ('documentation', models.FileField(upload_to='documents/')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='icons/')),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
    ]
