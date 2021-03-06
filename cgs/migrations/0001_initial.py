# Generated by Django 2.1.7 on 2019-06-15 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
                ('datePlayed', models.DateTimeField()),
                ('dateAdded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='O', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Scores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score1', models.IntegerField(verbose_name='Round 1 Score')),
                ('score2', models.IntegerField(verbose_name='Round 2 Score')),
                ('score3', models.IntegerField(verbose_name='Round 3 Score')),
                ('score4', models.IntegerField(verbose_name='Round 4 Score')),
                ('score5', models.IntegerField(verbose_name='Round 5 Score')),
                ('score6', models.IntegerField(verbose_name='Round 6 Score')),
                ('score7', models.IntegerField(verbose_name='Round 7 Score')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cgs.Games')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cgs.Player')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
