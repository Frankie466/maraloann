# Generated by Django 5.0.7 on 2024-12-04 14:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_loanapplicationforms_email'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='loanapplicationforms',
            options={'verbose_name': 'Loan Application Form', 'verbose_name_plural': 'Loan Application Forms'},
        ),
        migrations.CreateModel(
            name='EmployerAgreement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer_name', models.CharField(max_length=255)),
                ('employer_contact', models.CharField(max_length=15)),
                ('agreement_file', models.FileField(upload_to='agreements/')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Employer Agreement',
                'verbose_name_plural': 'Employer Agreements',
            },
        ),
        migrations.CreateModel(
            name='LoanRepayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Loan Repayment',
                'verbose_name_plural': 'Loan Repayments',
            },
        ),
    ]
