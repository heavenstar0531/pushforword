# Generated by Django 2.2 on 2019-04-30 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0006_auto_20190425_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentproperty',
            name='amenities',
            field=models.CharField(help_text='Press Enter to add another amenity', max_length=255),
        ),
    ]