# Generated by Django 2.2.5 on 2019-09-17 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Sport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Olympian',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sex', models.CharField(max_length=1)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
                ('team', models.CharField(max_length=255)),
                ('games', models.CharField(max_length=255)),
                ('medal', models.CharField(max_length=255, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='koroibos.Event')),
                ('sport', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='koroibos.Sport')),
            ],
        ),
    ]
