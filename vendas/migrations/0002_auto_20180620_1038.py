# Generated by Django 2.0.1 on 2018-06-20 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ItensDoPedido',
            new_name='ItemDoPedido',
        ),
    ]
