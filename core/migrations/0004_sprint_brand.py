# Generated by Django 4.0 on 2021-12-21 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_sprint_brand_remove_subobjective_sprint_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sprint',
            name='Brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.brand'),
        ),
    ]
