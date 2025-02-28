# Generated by Django 5.1 on 2024-10-12 10:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("elections", "0001_initial"),
        ("organizations", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ballot",
            name="voter",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="organizations.member",
            ),
        ),
        migrations.AddField(
            model_name="candidate",
            name="voter",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="organizations.member",
            ),
        ),
        migrations.AddField(
            model_name="ballot",
            name="candidate",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="elections.candidate"
            ),
        ),
        migrations.AddField(
            model_name="election",
            name="organization",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)s",
                to="organizations.organization",
            ),
        ),
        migrations.AddField(
            model_name="poll",
            name="body",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)s",
                to="organizations.body",
            ),
        ),
        migrations.AddField(
            model_name="poll",
            name="election",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="elections.election"
            ),
        ),
        migrations.AddField(
            model_name="poll",
            name="position",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="organizations.position"
            ),
        ),
        migrations.AddField(
            model_name="candidate",
            name="poll",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="elections.poll"
            ),
        ),
        migrations.AddField(
            model_name="ballot",
            name="poll",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="elections.poll"
            ),
        ),
        migrations.AddField(
            model_name="register",
            name="body",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="organizations.body"
            ),
        ),
        migrations.AddField(
            model_name="register",
            name="election",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="elections.election"
            ),
        ),
        migrations.AddField(
            model_name="register",
            name="voter",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="organizations.member",
            ),
        ),
        migrations.AddField(
            model_name="result",
            name="candidate",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="elections.candidate"
            ),
        ),
        migrations.AddField(
            model_name="result",
            name="poll",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(class)s",
                to="elections.poll",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="register",
            unique_together={("election", "voter")},
        ),
        migrations.AlterUniqueTogether(
            name="result",
            unique_together={("poll", "candidate")},
        ),
    ]
