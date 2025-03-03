# Generated by Django 5.1.6 on 2025-03-03 21:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('song', models.CharField(max_length=100)),
                ('singer_image', models.ImageField(upload_to='')),
                ('time_created', models.DateTimeField()),
                ('time_updated', models.DateTimeField()),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='singer_creator', to='users.user')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='singer_modifier', to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('team_image', models.ImageField(upload_to='')),
                ('time_created', models.DateTimeField()),
                ('time_updated', models.DateTimeField()),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_creator', to='users.user')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_modifier', to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_added', models.DateTimeField()),
                ('added_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_member_assignor', to='users.user')),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.singer')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teams.team')),
            ],
        ),
    ]
