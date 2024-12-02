# Generated by Django 5.1.2 on 2024-10-24 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='position',
            name='department',
        ),
        migrations.RemoveField(
            model_name='employeeskill',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='employeeskill',
            name='skill',
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('manager', 'Manager'), ('laborer', 'Laborer'), ('carpenter', 'Carpenter'), ('electrician', 'Electrician'), ('plumber', 'Plumber'), ('mason', 'Mason')], default='laborer', max_length=50),
            preserve_default=False,
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='emergency_contact_phone',
            new_name='emailAddress',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='EmployeeSkill',
        ),
        migrations.DeleteModel(
            name='Skill',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]