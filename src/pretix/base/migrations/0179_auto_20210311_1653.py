# Generated by Django 3.0.10 on 2021-03-11 16:53

from django.db import migrations


def clean_duplicates(apps, schema_editor):
    for i in range(100):  # no infinite loops
        # Double subquery to avoid MySQL error 1093
        delete_options = """
            DELETE
            FROM pretixbase_questionanswer_options
            WHERE questionanswer_id IN (
                SELECT minid FROM (
                    SELECT MIN(qa.id) minid
                    FROM pretixbase_questionanswer qa
                    GROUP BY qa.cartposition_id, qa.orderposition_id, qa.question_id
                    HAVING COUNT(*) > 1
                ) AS tmptable
            );
        """
        delete_answers = """
            DELETE
            FROM pretixbase_questionanswer
            WHERE pretixbase_questionanswer.id IN (
                SELECT minid FROM (
                    SELECT MIN(qa.id) minid
                    FROM pretixbase_questionanswer qa
                    GROUP BY qa.cartposition_id, qa.orderposition_id, qa.question_id
                    HAVING COUNT(*) > 1
                ) AS tmptable
            );
        """
        with schema_editor.connection.cursor() as cursor:
            cursor.execute(delete_options)
            cursor.execute(delete_answers)
            if cursor.rowcount == 0:
                return

class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0178_auto_20210308_1326'),
    ]

    operations = [
        migrations.RunPython(
            clean_duplicates,
            migrations.RunPython.noop,
        ),
    ]