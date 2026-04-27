from django.db import migrations


IMAGE_MAP = {
    "S01": "suas/th-true-milk.jpg",
    "S02": "suas/ensure.jpg",
    "S03": "suas/grow plus.jpg",
    "S04": "suas/dutch lady.jpg",
    "S05": "suas/grow-1.jpg",
    "S06": "suas/ngoisao.jpg",
    "S07": "suas/suachuaan.jpg",
    "S08": "suas/sua fami.jpg",
    "S09": "suas/sua optimum.jpg",
}


def set_jpg_images(apps, schema_editor):
    Sua = apps.get_model("Milk", "Sua")
    for ma_sua, hinh in IMAGE_MAP.items():
        Sua.objects.filter(ma_sua=ma_sua).update(hinh=hinh)


class Migration(migrations.Migration):
    dependencies = [
        ("Milk", "0005_set_milk_images"),
    ]

    operations = [
        migrations.RunPython(set_jpg_images, migrations.RunPython.noop),
    ]
