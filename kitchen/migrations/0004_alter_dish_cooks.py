

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0003_alter_dish_dish_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="cooks",
            field=models.ManyToManyField(
                related_name="dishes", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
