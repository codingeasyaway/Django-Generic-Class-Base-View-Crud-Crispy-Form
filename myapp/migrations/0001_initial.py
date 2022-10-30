# Generated by Django 3.1.7 on 2022-10-29 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'M'), ('F', 'F')], max_length=1, null=True)),
                ('careen', models.CharField(choices=[('Frontend', 'Frontend'), ('Backend', 'Backend'), ('Fullstack', 'Fullstack'), ('Intern', 'Intern')], max_length=50, null=True)),
            ],
        ),
    ]
