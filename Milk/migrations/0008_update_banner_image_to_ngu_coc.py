from django.db import migrations


def update_banner_image(apps, schema_editor):
    Sua = apps.get_model("Milk", "Sua")

    Sua.objects.filter(ma_sua="S10").update(hinh="suas/ngu_coc.jpg")


def revert_banner_image(apps, schema_editor):
    Sua = apps.get_model("Milk", "Sua")

    Sua.objects.filter(ma_sua="S10").update(hinh="suas/suachuaan.jpg")


class Migration(migrations.Migration):
    dependencies = [
        ("Milk", "0007_banner_quang_cao"),
    ]

    operations = [
        migrations.RunPython(update_banner_image, revert_banner_image),
    ]
