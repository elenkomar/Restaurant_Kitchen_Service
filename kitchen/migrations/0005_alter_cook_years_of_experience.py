

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0004_alter_dish_cooks"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cook",
            name="years_of_experience",
            field=models.PositiveIntegerField(),
        ),
    ]
