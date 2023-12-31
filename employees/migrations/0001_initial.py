# Generated by Django 4.2.4 on 2023-08-08 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('designation', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'HR'), (2, 'DEVELOPMENT'), (3, 'BUSSINESS'), (4, 'TESTING')], default=1, null=True)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'employees',
            },
        ),
    ]
