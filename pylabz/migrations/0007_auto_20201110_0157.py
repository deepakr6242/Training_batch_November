# Generated by Django 2.2.5 on 2020-11-10 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pylabz', '0006_contact_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
