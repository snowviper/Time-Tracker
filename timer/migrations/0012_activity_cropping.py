# Generated by Django 2.0.6 on 2018-08-22 00:22

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('timer', '0011_auto_20180821_0307'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('activity_image', '250x250', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
