# Generated by Django 3.2.12 on 2022-05-24 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookJournalBase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('bookjournalbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.bookjournalbase')),
                ('num_pages', models.IntegerField()),
                ('genre', models.CharField(max_length=50)),
            ],
            bases=('core.bookjournalbase',),
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('bookjournalbase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.bookjournalbase')),
                ('type', models.IntegerField(choices=[(1, 'Bullet'), (2, 'Food'), (3, 'Travel'), (4, 'Sport')])),
                ('publisher', models.CharField(max_length=150)),
            ],
            bases=('core.bookjournalbase',),
        ),
    ]