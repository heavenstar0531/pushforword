# Generated by Django 2.2.1 on 2019-06-26 19:41

from django.db import migrations, models
import job_applications.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=50)),
                ('current_company', models.CharField(blank=True, max_length=255)),
                ('position', models.CharField(choices=[('agent', 'Agent')], max_length=255)),
                ('resume', models.FileField(upload_to=job_applications.utils.resume_path, validators=[job_applications.utils.validate_pdf_file])),
            ],
        ),
    ]
