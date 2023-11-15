

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dish",
            options={"verbose_name_plural": "dishes"},
        ),
    ]
