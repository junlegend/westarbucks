# Generated by Django 4.0.dev20210615100128 on 2021-06-18 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'allergy',
            },
        ),
        migrations.CreateModel(
            name='Nutrition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_serving_kcal', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sodium_mg', models.DecimalField(decimal_places=2, max_digits=6)),
                ('saturated_fat_g', models.DecimalField(decimal_places=2, max_digits=6)),
                ('sugars_g', models.DecimalField(decimal_places=2, max_digits=6)),
                ('protein_g', models.DecimalField(decimal_places=2, max_digits=6)),
                ('caffeine_mg', models.DecimalField(decimal_places=2, max_digits=6)),
                ('size_ml', models.CharField(max_length=45)),
                ('size_fluid_ounce', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'nutritions',
            },
        ),
        migrations.RemoveField(
            model_name='product',
            name='name',
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='product',
            name='english_name',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AddField(
            model_name='product',
            name='korean_name',
            field=models.CharField(default='', max_length=45),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.category'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=2000)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.image')),
            ],
            options={
                'db_table': 'images',
            },
        ),
        migrations.CreateModel(
            name='Allergy_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.allergy')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'db_table': 'allergy_products',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='nutrition',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='products.nutrition'),
        ),
    ]
