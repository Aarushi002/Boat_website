# Generated by Django 4.1.6 on 2023-06-04 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('Duration1', models.IntegerField()),
                ('price1', models.IntegerField()),
                ('Duration2', models.IntegerField()),
                ('price2', models.IntegerField()),
                ('image', models.ImageField(upload_to='plan_img')),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('mname', models.CharField(blank=True, max_length=10, null=True)),
                ('lname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=100)),
                ('cnum', models.IntegerField()),
                ('arrivedate', models.DateField()),
                ('adults', models.IntegerField(null=True)),
                ('child', models.IntegerField()),
                ('time', models.TimeField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('ispaid', models.BooleanField(default=False)),
                ('amount', models.FloatField(verbose_name='Amount')),
                ('status', models.CharField(default='Pending', max_length=254, verbose_name='Payment Status')),
                ('provider_order_id', models.CharField(max_length=40, verbose_name='Order ID')),
                ('payment_id', models.CharField(max_length=36, verbose_name='Payment ID')),
                ('signature_id', models.CharField(max_length=128, verbose_name='Signature ID')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='booking.plans')),
            ],
        ),
    ]
