# Generated by Django 3.2 on 2022-03-07 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_gig_event_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='gig',
            name='fees',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
        migrations.AddField(
            model_name='gig',
            name='info_notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='gig',
            name='status',
            field=models.IntegerField(choices=[(0, 'Proposal'), (1, 'Approved'), (3, 'Rejected')], default=0),
        ),
    ]
