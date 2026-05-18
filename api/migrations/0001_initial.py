from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='DieMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sapcode', models.CharField(max_length=100, unique=True)),
                ('benkam', models.CharField(max_length=100)),
                ('synced_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'die_map',
                'ordering': ['sapcode'],
            },
        ),
    ]
