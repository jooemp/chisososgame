# Generated by Django 2.0.2 on 2021-10-05 23:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0009_auto_20210924_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChooseCharacter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='NightGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.IntegerField(blank=True, choices=[(1, 'Primero'), (2, 'Segundo'), (3, 'Tercero'), (0, 'Ninguno')], default=0, verbose_name='puesto')),
                ('score', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('passive', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('choose_character', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.ChooseCharacter')),
            ],
        ),
        migrations.AddField(
            model_name='games',
            name='first',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='games',
            name='second',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='games',
            name='thrid',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='games',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.RenameModel(
            old_name='Character',
            new_name='Characte',
        ),
        migrations.AddField(
            model_name='nightgame',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Games'),
        ),
        migrations.AddField(
            model_name='choosecharacter',
            name='character',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Characte'),
        ),
        migrations.AddField(
            model_name='choosecharacter',
            name='player',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
