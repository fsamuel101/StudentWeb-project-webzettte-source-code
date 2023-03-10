# Generated by Django 4.1.2 on 2023-01-14 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_remove_wall_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='picture',
            field=models.ImageField(default='achievements.png', null=True, upload_to='achievements/'),
        ),
        migrations.AlterField(
            model_name='council',
            name='picture',
            field=models.ImageField(default='default-dp.jpg', null=True, upload_to='council/'),
        ),
        migrations.AlterField(
            model_name='developers',
            name='picture',
            field=models.ImageField(default='default-dp.jpg', null=True, upload_to='developers/'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='picture',
            field=models.ImageField(default='default-dp.jpg', null=True, upload_to='faculty/'),
        ),
        migrations.AlterField(
            model_name='items',
            name='picture1',
            field=models.ImageField(blank=True, default='item.jpg', null=True, upload_to='shop/'),
        ),
        migrations.AlterField(
            model_name='items',
            name='picture2',
            field=models.ImageField(blank=True, default='item.jpg', null=True, upload_to='shop/'),
        ),
        migrations.AlterField(
            model_name='items',
            name='picture3',
            field=models.ImageField(blank=True, default='item.jpg', null=True, upload_to='shop/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='default-dp.jpg', null=True, upload_to='user/'),
        ),
    ]
