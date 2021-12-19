# Generated by Django 4.0 on 2021-12-19 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_brand_cohort'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='cohort',
        ),
        migrations.AddField(
            model_name='sprint',
            name='Brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand_sprint', to='core.brand'),
        ),
        migrations.AddField(
            model_name='sprint',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]