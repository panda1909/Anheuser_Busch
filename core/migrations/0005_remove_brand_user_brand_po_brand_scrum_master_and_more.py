# Generated by Django 4.0 on 2021-12-19 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0004_brand_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='User',
        ),
        migrations.AddField(
            model_name='brand',
            name='PO',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='po', to='auth.user'),
        ),
        migrations.AddField(
            model_name='brand',
            name='scrum_master',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='scrum_master', to='auth.user'),
        ),
        migrations.AddField(
            model_name='quarter',
            name='name',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]