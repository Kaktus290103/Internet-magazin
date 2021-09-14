# Generated by Django 3.2.6 on 2021-09-10 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.AlterModelOptions(
            name='tovary',
            options={'ordering': ('name',)},
        ),
        migrations.AddField(
            model_name='tovary',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tovary',
            name='image',
            field=models.ImageField(blank=True, upload_to='products/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='tovary',
            name='sale',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tovary',
            name='slug',
            field=models.SlugField(default=None, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='tovary',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterIndexTogether(
            name='tovary',
            index_together={('id', 'slug')},
        ),
        migrations.AddField(
            model_name='tovary',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='catalog.category'),
        ),
    ]