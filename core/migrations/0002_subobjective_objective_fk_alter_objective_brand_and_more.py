# Generated by Django 4.0 on 2021-12-16 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subobjective',
            name='objective_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='objective_sub_objective', to='core.sprint'),
        ),
        migrations.AlterField(
            model_name='objective',
            name='Brand',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='brand_objective', to='core.brand'),
        ),
        migrations.AlterField(
            model_name='objective',
            name='Quarter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quarter_objective', to='core.quarter'),
        ),
        migrations.AlterField(
            model_name='sprint',
            name='quarter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sprint', to='core.quarter'),
        ),
        migrations.AlterField(
            model_name='subobjective',
            name='sprint',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sprint_sub_objective', to='core.sprint'),
        ),
    ]
