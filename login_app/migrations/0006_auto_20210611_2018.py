# Generated by Django 3.1.7 on 2021-06-11 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0005_food'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='food',
        ),
        migrations.AddField(
            model_name='food',
            name='food',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='food', to='login_app.user'),
            preserve_default=False,
        ),
    ]
