# Generated by Django 3.0.8 on 2020-07-24 09:05

from django.db import migrations

from pretix.base.channels import get_all_sales_channels

def set_sales_channels(apps, schema_editor):
    # We now allow restricting some mails to certain sales channels
    # The default is changing from all channels to "web" only
    # Therefore, for existing events, we enable all sales channels
    Event_SettingsStore = apps.get_model('pretixbase', 'Event_SettingsStore')
    Event = apps.get_model('pretixbase', 'Event')
    all_sales_channels = "[" + ", ".join('"' + sc + '"' for sc in get_all_sales_channels()) + "]"
    batch_size = 1000
    Event_SettingsStore.objects.bulk_create([
        Event_SettingsStore(
            object=event,
            key="mail_sales_channel_placed_paid",
            value=all_sales_channels)
        for event in Event.objects.all()
    ], batch_size=batch_size)
    Event_SettingsStore.objects.bulk_create([
        Event_SettingsStore(
            object=event,
            key="mail_sales_channel_download_reminder",
            value=all_sales_channels)
        for event in Event.objects.all()
    ], batch_size=batch_size)


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0158_auto_20200724_0754'),
    ]

    operations = [
        migrations.RunPython(set_sales_channels, migrations.RunPython.noop),
    ]
