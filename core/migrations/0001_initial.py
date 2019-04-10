# Generated by Django 2.1.7 on 2019-02-23 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.CharField(blank=True, help_text="User's unique user id that is always used to login.", max_length=24, null=True, unique=True)),
                ('full_name', models.CharField(blank=True, help_text="User's full name", max_length=255, null=True)),
                ('gender', models.CharField(blank=True, choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('TRANSGENDER', 'TRANSGENDER'), ('PREFER_NOT_TO_SAY', 'PREFER_NOT_TO_SAY')], help_text="User's Gender", max_length=255, null=True)),
                ('email', models.EmailField(blank=True, default='', help_text="User's Email", max_length=255, null=True)),
                ('mobile_number', models.CharField(blank=True, help_text="User's Mobile number", max_length=10, null=True)),
                ('profile_photo', models.ImageField(blank=True, help_text="User's Profile photo", max_length=255, null=True, upload_to='images_profilephoto')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_executive', models.BooleanField(default=False)),
                ('is_photographer', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]