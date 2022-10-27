# Generated by Django 4.0.5 on 2022-10-08 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0007_remove_tag_tags_group_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='group',
        ),
        migrations.AddField(
            model_name='group',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='groups.category'),
        ),
        migrations.AddField(
            model_name='group',
            name='mentor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='groups.teacher'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='groups',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='groups.group'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.PositiveIntegerField(default=0, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
