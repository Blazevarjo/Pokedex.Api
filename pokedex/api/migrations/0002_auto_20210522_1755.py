# Generated by Django 3.2 on 2021-05-22 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonMove',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
            ],
        ),
        migrations.RenameModel(
            old_name='PokemonStats',
            new_name='PokemonStat',
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='height',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='weight',
            field=models.FloatField(),
        ),
        migrations.AddField(
            model_name='pokemon',
            name='moves',
            field=models.ManyToManyField(related_name='pokemons', to='api.PokemonMove'),
        ),
    ]
