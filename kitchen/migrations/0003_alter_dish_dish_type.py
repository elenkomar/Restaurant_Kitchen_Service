

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0002_alter_dish_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dish",
            name="dish_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="dishes",
                to="kitchen.dishtype",
            ),
        ),
    ]
