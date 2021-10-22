# Generated by Django 3.2.4 on 2021-10-18 10:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0199_auto_20211005_1050'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('datetime', models.DateTimeField(db_index=True)),
                ('migrated', models.BooleanField(default=False)),
                ('positionid', models.PositiveIntegerField(default=1, null=True)),
                ('count', models.IntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tax_rate', models.DecimalField(decimal_places=2, max_digits=7)),
                ('tax_value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('fee_type', models.CharField(max_length=100, null=True)),
                ('internal_type', models.CharField(max_length=255, null=True)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pretixbase.item')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='transactions', to='pretixbase.order')),
                ('subevent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pretixbase.subevent')),
                ('tax_rule', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pretixbase.taxrule')),
                ('variation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pretixbase.itemvariation')),
            ],
            options={
                'ordering': ('datetime', 'pk'),
            },
        ),
    ]