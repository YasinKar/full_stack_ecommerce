# Generated by Django 5.0.3 on 2024-11-01 08:47

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='نام برند')),
                ('logo', models.ImageField(upload_to='brands', verbose_name='لوگو برند')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, default='')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیر فعال')),
            ],
            options={
                'verbose_name': 'برند',
                'verbose_name_plural': 'برند ها',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='دسته بندی')),
                ('title_url', models.SlugField(blank=True, default='', verbose_name='(دسته بندی(نام لینک')),
                ('image', models.ImageField(blank=True, null=True, upload_to='categories', verbose_name='عکس دسته بندی')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیر فعال')),
            ],
            options={
                'verbose_name': 'دسته بندی',
                'verbose_name_plural': 'دسته بندی ها',
            },
        ),
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=200, verbose_name='تگ')),
            ],
            options={
                'verbose_name': 'تگ',
                'verbose_name_plural': 'تگ ها',
            },
        ),
        migrations.CreateModel(
            name='SiteSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='sliders', verbose_name='عکس')),
                ('url', models.URLField(verbose_name='ادرس اسلایدر')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیر فعال')),
            ],
            options={
                'verbose_name': 'اسلایدر سایت',
                'verbose_name_plural': 'اسلایدر',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='نام محصول')),
                ('price', models.IntegerField(verbose_name='قیمت')),
                ('image', models.ImageField(upload_to='products', verbose_name='تصویر')),
                ('description', models.TextField(max_length=800, verbose_name='توضیحات')),
                ('gender', models.CharField(choices=[('مردانه', 'مردانه'), ('زنانه', 'زنانه'), ('ندارد', 'ندارد')], default='ندارد', max_length=100, verbose_name='جنسیت')),
                ('slug', models.SlugField(allow_unicode=True, blank=True, default='')),
                ('stars', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], verbose_name='ستاره های محصول')),
                ('inventory', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='تعداد موجودی')),
                ('is_sale', models.BooleanField(default=False, verbose_name='تخفیف')),
                ('sale_price', models.IntegerField(blank=True, null=True, verbose_name='قیمت در تخفیف')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال / غیر فعال')),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.brand', verbose_name='برند')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category', verbose_name='دسته بندی')),
                ('tags', models.ManyToManyField(blank=True, to='products.producttag', verbose_name='تگ های محصول')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='products-gallery', verbose_name='تصویر')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'تصویر محصول',
                'verbose_name_plural': 'تصاویر محصولات',
            },
        ),
        migrations.CreateModel(
            name='ProductInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, verbose_name='کلید')),
                ('value', models.CharField(max_length=100, verbose_name='مقدار')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Information', to='products.product', verbose_name='محصول')),
            ],
            options={
                'verbose_name': 'مشخصات',
                'verbose_name_plural': 'مشخصات محصولات',
            },
        ),
    ]
