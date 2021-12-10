# Generated by Django 3.2.9 on 2021-12-10 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('smdproject', '0011_medicalvault_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='eeg_dataset2_hub',
            fields=[
                ('eeg_dataset2_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('eeg_dataset2_name', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('business_key', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='experiment_hub',
            fields=[
                ('experiment_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('experiment_name', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('business_key', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='fnirs_dataset1_hub',
            fields=[
                ('fnirs_dataset1_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fnirs_dataset1_name', models.TextField()),
                ('measuredate', models.DateTimeField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('business_key', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='fnirs_dataset2_hub',
            fields=[
                ('fnirs_dataset2_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('fnirs_dataset2_name', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('business_key', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='patient_hub',
            fields=[
                ('patient_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('patient_name', models.TextField()),
                ('patient_age', models.IntegerField()),
                ('patient_sex', models.TextField()),
                ('patient_label', models.CharField(default='001', max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('business_key', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='session_hub',
            fields=[
                ('session_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('session_name', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('business_key', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='medicalvault',
            name='vault_owner',
            field=models.ManyToManyField(blank=True, to='smdproject.VaultOwner'),
        ),
        migrations.CreateModel(
            name='fnirs_dataset2_wl2',
            fields=[
                ('fnirs_dataset2_wl2_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('data_1', models.FloatField()),
                ('data_2', models.FloatField()),
                ('data_3', models.FloatField()),
                ('data_4', models.FloatField()),
                ('data_5', models.FloatField()),
                ('data_6', models.FloatField()),
                ('data_7', models.FloatField()),
                ('data_8', models.FloatField()),
                ('data_9', models.FloatField()),
                ('data_10', models.FloatField()),
                ('data_11', models.FloatField()),
                ('data_12', models.FloatField()),
                ('data_13', models.FloatField()),
                ('data_14', models.FloatField()),
                ('data_15', models.FloatField()),
                ('data_16', models.FloatField()),
                ('data_17', models.FloatField()),
                ('data_18', models.FloatField()),
                ('data_19', models.FloatField()),
                ('data_20', models.FloatField()),
                ('data_21', models.FloatField()),
                ('data_22', models.FloatField()),
                ('data_23', models.FloatField()),
                ('data_24', models.FloatField()),
                ('data_25', models.FloatField()),
                ('data_26', models.FloatField()),
                ('data_27', models.FloatField()),
                ('data_28', models.FloatField()),
                ('data_29', models.FloatField()),
                ('data_30', models.FloatField()),
                ('data_31', models.FloatField()),
                ('data_32', models.FloatField()),
                ('data_33', models.FloatField()),
                ('data_34', models.FloatField()),
                ('data_35', models.FloatField(default='001')),
                ('data_36', models.FloatField()),
                ('data_37', models.FloatField()),
                ('data_38', models.FloatField()),
                ('data_39', models.FloatField()),
                ('data_40', models.FloatField()),
                ('data_41', models.FloatField()),
                ('data_42', models.FloatField()),
                ('data_43', models.FloatField()),
                ('data_44', models.FloatField()),
                ('data_45', models.FloatField()),
                ('data_46', models.FloatField()),
                ('data_47', models.FloatField()),
                ('data_48', models.FloatField()),
                ('data_49', models.FloatField()),
                ('data_50', models.FloatField()),
                ('data_51', models.FloatField()),
                ('data_52', models.FloatField()),
                ('data_53', models.FloatField()),
                ('data_54', models.FloatField()),
                ('data_55', models.FloatField()),
                ('data_56', models.FloatField()),
                ('data_57', models.FloatField()),
                ('data_58', models.FloatField()),
                ('data_59', models.FloatField()),
                ('data_60', models.FloatField()),
                ('data_61', models.FloatField()),
                ('data_62', models.FloatField()),
                ('data_63', models.FloatField()),
                ('data_64', models.FloatField()),
                ('data_65', models.FloatField()),
                ('data_66', models.FloatField()),
                ('data_67', models.FloatField()),
                ('data_68', models.FloatField()),
                ('data_69', models.FloatField()),
                ('data_70', models.FloatField()),
                ('data_71', models.FloatField()),
                ('data_72', models.FloatField()),
                ('data_73', models.FloatField()),
                ('data_74', models.FloatField()),
                ('data_75', models.FloatField()),
                ('data_76', models.FloatField()),
                ('data_77', models.FloatField()),
                ('data_78', models.FloatField()),
                ('data_79', models.FloatField()),
                ('data_80', models.FloatField()),
                ('data_81', models.FloatField()),
                ('data_82', models.FloatField()),
                ('data_83', models.FloatField()),
                ('data_84', models.FloatField()),
                ('data_85', models.FloatField()),
                ('data_86', models.FloatField()),
                ('data_87', models.FloatField()),
                ('data_88', models.FloatField()),
                ('data_89', models.FloatField()),
                ('data_90', models.FloatField()),
                ('data_91', models.FloatField()),
                ('data_92', models.FloatField()),
                ('data_93', models.FloatField()),
                ('data_94', models.FloatField()),
                ('data_95', models.FloatField()),
                ('data_96', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('patient_name', models.CharField(default='001', max_length=50)),
                ('business_key', models.IntegerField()),
                ('fnirs_dataset2_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smdproject.fnirs_dataset2_hub')),
            ],
        ),
        migrations.CreateModel(
            name='fnirs_dataset2_wl1',
            fields=[
                ('fnirs_dataset2_wl1_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('data_1', models.FloatField()),
                ('data_2', models.FloatField()),
                ('data_3', models.FloatField()),
                ('data_4', models.FloatField()),
                ('data_5', models.FloatField()),
                ('data_6', models.FloatField()),
                ('data_7', models.FloatField()),
                ('data_8', models.FloatField()),
                ('data_9', models.FloatField()),
                ('data_10', models.FloatField()),
                ('data_11', models.FloatField()),
                ('data_12', models.FloatField()),
                ('data_13', models.FloatField()),
                ('data_14', models.FloatField()),
                ('data_15', models.FloatField()),
                ('data_16', models.FloatField()),
                ('data_17', models.FloatField()),
                ('data_18', models.FloatField()),
                ('data_19', models.FloatField()),
                ('data_20', models.FloatField()),
                ('data_21', models.FloatField()),
                ('data_22', models.FloatField()),
                ('data_23', models.FloatField()),
                ('data_24', models.FloatField()),
                ('data_25', models.FloatField()),
                ('data_26', models.FloatField()),
                ('data_27', models.FloatField()),
                ('data_28', models.FloatField()),
                ('data_29', models.FloatField()),
                ('data_30', models.FloatField()),
                ('data_31', models.FloatField()),
                ('data_32', models.FloatField()),
                ('data_33', models.FloatField()),
                ('data_34', models.FloatField()),
                ('data_35', models.FloatField()),
                ('data_36', models.FloatField()),
                ('data_37', models.FloatField()),
                ('data_38', models.FloatField()),
                ('data_39', models.FloatField()),
                ('data_40', models.FloatField()),
                ('data_41', models.FloatField()),
                ('data_42', models.FloatField()),
                ('data_43', models.FloatField()),
                ('data_44', models.FloatField()),
                ('data_45', models.FloatField()),
                ('data_46', models.FloatField()),
                ('data_47', models.FloatField()),
                ('data_48', models.FloatField()),
                ('data_49', models.FloatField()),
                ('data_50', models.FloatField()),
                ('data_51', models.FloatField()),
                ('data_52', models.FloatField()),
                ('data_53', models.FloatField()),
                ('data_54', models.FloatField()),
                ('data_55', models.FloatField()),
                ('data_56', models.FloatField()),
                ('data_57', models.FloatField()),
                ('data_58', models.FloatField()),
                ('data_59', models.FloatField()),
                ('data_60', models.FloatField()),
                ('data_61', models.FloatField()),
                ('data_62', models.FloatField()),
                ('data_63', models.FloatField()),
                ('data_64', models.FloatField()),
                ('data_65', models.FloatField()),
                ('data_66', models.FloatField()),
                ('data_67', models.FloatField()),
                ('data_68', models.FloatField()),
                ('data_69', models.FloatField()),
                ('data_70', models.FloatField()),
                ('data_71', models.FloatField()),
                ('data_72', models.FloatField()),
                ('data_73', models.FloatField()),
                ('data_74', models.FloatField()),
                ('data_75', models.FloatField()),
                ('data_76', models.FloatField()),
                ('data_77', models.FloatField()),
                ('data_78', models.FloatField()),
                ('data_79', models.FloatField()),
                ('data_80', models.FloatField()),
                ('data_81', models.FloatField()),
                ('data_82', models.FloatField()),
                ('data_83', models.FloatField()),
                ('data_84', models.FloatField()),
                ('data_85', models.FloatField()),
                ('data_86', models.FloatField()),
                ('data_87', models.FloatField()),
                ('data_88', models.FloatField()),
                ('data_89', models.FloatField()),
                ('data_90', models.FloatField()),
                ('data_91', models.FloatField()),
                ('data_92', models.FloatField()),
                ('data_93', models.FloatField()),
                ('data_94', models.FloatField()),
                ('data_95', models.FloatField()),
                ('data_96', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('patient_name', models.CharField(default='001', max_length=50)),
                ('business_key', models.IntegerField()),
                ('fnirs_dataset2_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smdproject.fnirs_dataset2_hub')),
            ],
        ),
        migrations.CreateModel(
            name='fnirs_dataset2_dat',
            fields=[
                ('fnirs_dataset2_dat_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('data_1', models.FloatField()),
                ('data_2', models.FloatField()),
                ('data_3', models.FloatField()),
                ('data_4', models.FloatField()),
                ('data_5', models.FloatField()),
                ('data_6', models.FloatField()),
                ('data_7', models.FloatField()),
                ('data_8', models.FloatField()),
                ('data_9', models.FloatField()),
                ('data_10', models.FloatField()),
                ('data_11', models.FloatField()),
                ('data_12', models.FloatField()),
                ('data_13', models.FloatField()),
                ('data_14', models.FloatField()),
                ('data_15', models.FloatField()),
                ('data_16', models.FloatField()),
                ('data_17', models.FloatField()),
                ('data_18', models.FloatField()),
                ('data_19', models.FloatField()),
                ('data_20', models.FloatField()),
                ('data_21', models.FloatField()),
                ('data_22', models.FloatField()),
                ('data_23', models.FloatField()),
                ('data_24', models.FloatField()),
                ('data_25', models.FloatField()),
                ('data_26', models.FloatField()),
                ('data_27', models.FloatField()),
                ('data_28', models.FloatField()),
                ('data_29', models.FloatField()),
                ('data_30', models.FloatField()),
                ('data_31', models.FloatField()),
                ('data_32', models.FloatField()),
                ('data_33', models.FloatField()),
                ('data_34', models.FloatField()),
                ('data_35', models.FloatField()),
                ('data_36', models.FloatField()),
                ('data_37', models.FloatField()),
                ('data_38', models.FloatField()),
                ('data_39', models.FloatField()),
                ('data_40', models.FloatField()),
                ('data_41', models.FloatField()),
                ('data_42', models.FloatField()),
                ('data_43', models.FloatField()),
                ('data_44', models.FloatField()),
                ('data_45', models.FloatField()),
                ('data_46', models.FloatField()),
                ('data_47', models.FloatField()),
                ('data_48', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('patient_name', models.CharField(default='001', max_length=50)),
                ('business_key', models.IntegerField()),
                ('fnirs_dataset2_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smdproject.fnirs_dataset2_hub')),
            ],
        ),
        migrations.CreateModel(
            name='fnirs_dataset1_oxy',
            fields=[
                ('fnirs_dataset1_oxy_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('data_ch1', models.FloatField()),
                ('data_ch2', models.FloatField()),
                ('data_ch3', models.FloatField()),
                ('data_ch4', models.FloatField()),
                ('data_ch5', models.FloatField()),
                ('data_ch6', models.FloatField()),
                ('data_ch7', models.FloatField()),
                ('data_ch8', models.FloatField()),
                ('data_ch9', models.FloatField()),
                ('data_ch10', models.FloatField()),
                ('data_ch11', models.FloatField()),
                ('data_ch12', models.FloatField()),
                ('data_ch13', models.FloatField()),
                ('data_ch14', models.FloatField()),
                ('data_ch15', models.FloatField()),
                ('data_ch16', models.FloatField()),
                ('data_ch17', models.FloatField()),
                ('data_ch18', models.FloatField()),
                ('data_ch19', models.FloatField()),
                ('data_ch20', models.FloatField()),
                ('data_ch21', models.FloatField()),
                ('data_ch22', models.FloatField()),
                ('data_ch23', models.FloatField()),
                ('data_ch24', models.FloatField()),
                ('data_mark', models.FloatField()),
                ('data_time', models.CharField(max_length=60)),
                ('bodymovement', models.FloatField()),
                ('prescan', models.FloatField()),
                ('removalmark', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('patient_name', models.CharField(default='001', max_length=50)),
                ('business_key', models.IntegerField()),
                ('fnirs_dataset1_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smdproject.fnirs_dataset1_hub')),
            ],
        ),
        migrations.CreateModel(
            name='fnirs_dataset1_mes',
            fields=[
                ('fnirs_dataset1_mes_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('data_ch1', models.FloatField()),
                ('data_ch2', models.FloatField()),
                ('data_ch3', models.FloatField()),
                ('data_ch4', models.FloatField()),
                ('data_ch5', models.FloatField()),
                ('data_ch6', models.FloatField()),
                ('data_ch7', models.FloatField()),
                ('data_ch8', models.FloatField()),
                ('data_ch9', models.FloatField()),
                ('data_ch10', models.FloatField()),
                ('data_ch11', models.FloatField()),
                ('data_ch12', models.FloatField()),
                ('data_ch13', models.FloatField()),
                ('data_ch14', models.FloatField()),
                ('data_ch15', models.FloatField()),
                ('data_ch16', models.FloatField()),
                ('data_ch17', models.FloatField()),
                ('data_ch18', models.FloatField()),
                ('data_ch19', models.FloatField()),
                ('data_ch20', models.FloatField()),
                ('data_ch21', models.FloatField()),
                ('data_ch22', models.FloatField()),
                ('data_ch23', models.FloatField()),
                ('data_ch24', models.FloatField()),
                ('data_mark', models.FloatField()),
                ('data_time', models.CharField(max_length=60)),
                ('bodymovement', models.FloatField()),
                ('prescan', models.FloatField()),
                ('removalmark', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('patient_name', models.CharField(default='001', max_length=50)),
                ('business_key', models.IntegerField()),
                ('fnirs_dataset1_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smdproject.fnirs_dataset1_hub')),
            ],
        ),
        migrations.CreateModel(
            name='fnirs_dataset1_deoxy',
            fields=[
                ('fnirs_dataset1_deoxy_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('data_ch1', models.FloatField()),
                ('data_ch2', models.FloatField()),
                ('data_ch3', models.FloatField()),
                ('data_ch4', models.FloatField()),
                ('data_ch5', models.FloatField()),
                ('data_ch6', models.FloatField()),
                ('data_ch7', models.FloatField()),
                ('data_ch8', models.FloatField()),
                ('data_ch9', models.FloatField()),
                ('data_ch10', models.FloatField()),
                ('data_ch11', models.FloatField()),
                ('data_ch12', models.FloatField()),
                ('data_ch13', models.FloatField()),
                ('data_ch14', models.FloatField()),
                ('data_ch15', models.FloatField()),
                ('data_ch16', models.FloatField()),
                ('data_ch17', models.FloatField()),
                ('data_ch18', models.FloatField()),
                ('data_ch19', models.FloatField()),
                ('data_ch20', models.FloatField()),
                ('data_ch21', models.FloatField()),
                ('data_ch22', models.FloatField()),
                ('data_ch23', models.FloatField()),
                ('data_ch24', models.FloatField()),
                ('data_mark', models.FloatField()),
                ('data_time', models.CharField(max_length=60)),
                ('bodymovement', models.FloatField()),
                ('prescan', models.FloatField()),
                ('removalmark', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('patient_name', models.CharField(default='001', max_length=50)),
                ('business_key', models.IntegerField()),
                ('fnirs_dataset1_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smdproject.fnirs_dataset1_hub')),
            ],
        ),
        migrations.CreateModel(
            name='experiment_session_link',
            fields=[
                ('link_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('business_key', models.IntegerField()),
                ('experiment_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smdproject.experiment_hub')),
                ('session_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smdproject.session_hub')),
            ],
        ),
        migrations.CreateModel(
            name='experiment1_metadata',
            fields=[
                ('metadata_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('analyzemode', models.TextField()),
                ('pretimes', models.IntegerField()),
                ('posttimes', models.IntegerField()),
                ('recoverytimes', models.IntegerField()),
                ('basetimes', models.IntegerField()),
                ('fittingdegree', models.IntegerField()),
                ('hpfhz', models.TextField()),
                ('lpfhz', models.TextField()),
                ('movingaverages', models.IntegerField()),
                ('mode', models.TextField()),
                ('samplingperiods', models.IntegerField()),
                ('stimtype', models.TextField()),
                ('repeatcount', models.IntegerField()),
                ('exception', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('business_key', models.IntegerField()),
                ('experiment_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smdproject.experiment_hub')),
            ],
        ),
        migrations.CreateModel(
            name='eeg_dataset2_satelite',
            fields=[
                ('eeg_dataset2_data_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('data_1', models.FloatField()),
                ('data_2', models.FloatField()),
                ('data_3', models.FloatField()),
                ('data_4', models.FloatField()),
                ('data_5', models.FloatField()),
                ('data_6', models.FloatField()),
                ('data_7', models.FloatField()),
                ('data_8', models.FloatField()),
                ('data_9', models.FloatField()),
                ('data_10', models.FloatField()),
                ('data_11', models.FloatField()),
                ('data_12', models.FloatField()),
                ('data_13', models.FloatField()),
                ('data_14', models.FloatField()),
                ('data_15', models.FloatField()),
                ('data_16', models.FloatField()),
                ('data_17', models.FloatField()),
                ('data_18', models.FloatField()),
                ('data_19', models.FloatField()),
                ('data_20', models.FloatField()),
                ('data_21', models.FloatField()),
                ('data_22', models.FloatField()),
                ('data_23', models.FloatField()),
                ('data_24', models.FloatField()),
                ('data_25', models.FloatField()),
                ('data_26', models.FloatField()),
                ('data_27', models.FloatField()),
                ('data_28', models.FloatField()),
                ('data_29', models.FloatField()),
                ('data_30', models.FloatField()),
                ('data_31', models.FloatField()),
                ('data_32', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('patient_name', models.CharField(default='001', max_length=50)),
                ('business_key', models.IntegerField()),
                ('eeg_dataset2_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smdproject.eeg_dataset2_hub')),
            ],
        ),
        migrations.CreateModel(
            name='data_source_link',
            fields=[
                ('link_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('business_key', models.IntegerField()),
                ('eeg_dataset2_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smdproject.eeg_dataset2_hub')),
                ('fnirs_dataset1_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smdproject.fnirs_dataset1_hub')),
                ('fnirs_dataset2_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='smdproject.fnirs_dataset2_hub')),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smdproject.patient_hub')),
                ('session_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='smdproject.session_hub')),
            ],
        ),
    ]
