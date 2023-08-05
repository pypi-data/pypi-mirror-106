# Generated by Django 2.2.2 on 2019-07-06 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("edc_visit_schedule", "0005_auto_20190706_0137")]

    operations = [
        migrations.AlterUniqueTogether(
            name="visitschedule",
            unique_together={
                ("visit_schedule_name", "schedule_name", "visit_code"),
                ("visit_schedule_name", "schedule_name", "timepoint"),
            },
        ),
        migrations.AddIndex(
            model_name="visitschedule",
            index=models.Index(
                fields=["visit_schedule_name", "schedule_name", "timepoint"],
                name="edc_visit_s_visit_s_31f7c7_idx",
            ),
        ),
    ]
