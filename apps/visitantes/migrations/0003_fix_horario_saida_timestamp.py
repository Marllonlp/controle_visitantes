from django.db import migrations, models


def clear_exit_times_for_open_visits(apps, schema_editor):
    Visitante = apps.get_model("visitantes", "Visitante")
    Visitante.objects.using(schema_editor.connection.alias).exclude(
        status="FINALIZADO"
    ).update(horario_saido=None)


class Migration(migrations.Migration):

    dependencies = [
        ("visitantes", "0002_visitante_status"),
    ]

    operations = [
        migrations.RunPython(
            clear_exit_times_for_open_visits,
            migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name="visitante",
            name="horario_saido",
            field=models.DateTimeField(
                blank=True,
                null=True,
                verbose_name="Horário de saída",
            ),
        ),
    ]
