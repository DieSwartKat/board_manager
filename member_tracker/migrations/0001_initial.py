# Generated by Django 3.2.3 on 2021-05-17 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board_name', models.CharField(max_length=250)),
                ('board_id', models.CharField(max_length=250, unique=True)),
                ('board_description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trello_username', models.CharField(max_length=250)),
                ('trello_member_id', models.CharField(max_length=250, unique=True)),
                ('name', models.CharField(max_length=250)),
                ('surname', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('trello_picture', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Board_Member_Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member_tracker.board')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member_tracker.member')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member_tracker.role')),
            ],
        ),
    ]