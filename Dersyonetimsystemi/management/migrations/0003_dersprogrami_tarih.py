

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_dersprogrami_delete_userschedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='dersprogrami',
            name='tarih',
            field=models.DateField(blank=True, null=True),
        ),
    ]
