# Generated by Django 5.0.3 on 2025-02-03 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0003_remove_sitesetting_github_contactus_full_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitesetting',
            name='site_about',
        ),
        migrations.AddField(
            model_name='sitesetting',
            name='site_description',
            field=models.TextField(default='sdsd', verbose_name='Description'),
            preserve_default=False,
        ),
    ]
