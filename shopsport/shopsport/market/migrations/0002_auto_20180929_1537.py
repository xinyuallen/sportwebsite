# Generated by Django 2.0.4 on 2018-09-29 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='clickUrl',
        ),
        migrations.RemoveField(
            model_name='products',
            name='name',
        ),
        migrations.RemoveField(
            model_name='products',
            name='product_desc',
        ),
        migrations.AddField(
            model_name='categorys',
            name='desc',
            field=models.TextField(default="this is category's description"),
        ),
        migrations.AddField(
            model_name='categorys',
            name='imgUrl',
            field=models.ImageField(default='test.jpg', upload_to='categorysimg'),
        ),
        migrations.AddField(
            model_name='products',
            name='product_desc1',
            field=models.TextField(blank=True, default='product desc 1', null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='product_desc2',
            field=models.TextField(default='product desc 2'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='page_desc',
            field=models.TextField(default="this is homepage's picture description"),
        ),
    ]
