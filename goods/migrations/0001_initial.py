# Generated by Django 2.1 on 2020-01-04 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gtitle', models.CharField(max_length=20)),
                ('gpic', models.ImageField(upload_to='goods')),
                ('gprice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('isDelete', models.BooleanField(default=False)),
                ('gunit', models.CharField(default='500克', max_length=20)),
                ('gclick', models.IntegerField()),
                ('gdigest', models.CharField(max_length=50)),
                ('gcontext', models.CharField(max_length=100)),
                ('gkucun', models.IntegerField(max_length=10)),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
                'db_table': 'goods_goodinfo',
            },
        ),
        migrations.CreateModel(
            name='typeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttitle', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '商品分类',
                'verbose_name_plural': '商品分类',
                'db_table': 'goods_typeInfo',
            },
        ),
        migrations.AddField(
            model_name='goods',
            name='gtype',
            field=models.ForeignKey(on_delete=1, to='goods.typeInfo'),
        ),
    ]