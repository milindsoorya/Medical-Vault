import os
from smdproject.models import fnirs_dataset1_deoxy
from smdproject.models import fnirs_dataset1_oxy
from smdproject.models import fnirs_dataset1_mes
from smdproject.models import fnirs_dataset1_hub
from smdproject.models import patient_hub
from smdproject.models import experiment_hub
from smdproject.models import session_hub
from smdproject.models import fnirs_dataset2_wl1
from smdproject.models import fnirs_dataset2_wl2
from smdproject.models import eeg_dataset2_satelite

directory_path = './staging/processedData/Dataset 1/'
patient_files = ["deoxy", "oxy", "mes"]
patient_info = directory_path + "patient_info/"
session_1 = directory_path + "fNIRS-Data/1raSessionDR/"
session_2 = directory_path + "fNIRS-Data/2daSessionDR/"
eegdata = directory_path + "EEG-Data/"


def insertPatientDetails():
    patient_hub.objects.all().delete()
    all_files = os.listdir(patient_info)
    for file in all_files:
        patientlbl = file[:6]
        file_path = patient_info
        print("Processing", file)
        filepath = file_path + file
        with open(filepath, 'r', encoding='windows-1252') as read_file:
            patient_details = read_file.read().splitlines()
            patientname = patient_details[0].strip()
            patientage = patient_details[1].strip()[:-1]
            patientsex = patient_details[2].strip()
            patientlabel = patientlbl
            patient_hub.objects.create(patient_name=patientname, patient_age=patientage,
                                       patient_sex=patientsex, patient_label=patientlabel, business_key=(1))


def run():
    print("Inserting session details")
    session_hub.objects.all().delete()
    sess_name = ["1raSession", "2daSession"]
    for sess in sess_name:
        session_hub.objects.create(session_name=sess, business_key=(1))
    print("Finished inserting session details")
    print("Inserting experiment details")
    experiment_hub.objects.all().delete()
    exp_name = ["Visuomotor functional connectivity", "Multimodal pre-autism "]
    for name in exp_name:
        experiment_hub.objects.create(experiment_name=name, business_key=(1))
    print("finished inserting experiment details")
    print("Inserting patient details")
    insertPatientDetails()
    print("finished inserting patient details")

    i = 0
    all_files = os.listdir(directory_path)
    for folder in all_files:
        if folder in patient_files:
            file_path = directory_path + folder + "/"
            experiment_files = os.listdir(file_path)
            print("Processing", folder)

            modelname = [fnirs_dataset1_deoxy,
                         fnirs_dataset1_oxy, fnirs_dataset1_mes]

            modelname[i].objects.all().delete()

            for file in experiment_files:
                patientname = file[:6]
                filepath = file_path + file

                incomplete_files = [
                    "VM0010_Viso_HBA_Probe1_Deoxy.csv", "VM0010_Viso_HBA_Probe1_Oxy.csv"]
                if file in incomplete_files:
                    with open(filepath, 'r', encoding='windows-1252') as read_file:
                        all_lines = read_file.readlines()
                        count = 1
                        print(filepath)
                        for row in all_lines:
                            row_as_list = row.split(",")
                            record = row_as_list
                            if count == 1 or len(record) < 2:
                                pass
                            else:
                                modelname[i].objects.create(data_ch1=record[0], data_ch2=record[1], data_ch3=record[2],
                                                            data_ch4=record[3],
                                                            data_ch5=record[4], data_ch6=record[5], data_ch7=record[6],
                                                            data_ch8=record[7],
                                                            data_ch9=record[8], data_ch10=record[9], data_ch11=record[10],
                                                            data_ch12=record[11],
                                                            data_ch13=record[12], data_ch14=record[13], data_ch15=record[14],
                                                            data_ch16=record[15],
                                                            data_ch17=record[16], data_ch18=record[17], data_ch19=record[18],
                                                            data_ch20=record[19],
                                                            data_ch21=record[20], data_ch22=record[21], data_ch23=record[22],
                                                            data_ch24=record[23],
                                                            data_mark=record[24], data_time=record[25], bodymovement=0,
                                                            removalmark=0,
                                                            prescan=0, patient_name=patientname, business_key=(1))

                            count += 1
                else:
                    with open(filepath, 'r', encoding='windows-1252') as read_file:
                        all_lines = read_file.readlines()
                        count = 1
                        print(filepath)
                        for row in all_lines:
                            row_as_list = row.split(",")
                            record = row_as_list
                            if count == 1 or len(record) < 2:
                                pass
                            else:
                                modelname[i].objects.create(data_ch1=record[0], data_ch2=record[1], data_ch3=record[2],
                                                            data_ch4=record[3],
                                                            data_ch5=record[4], data_ch6=record[5], data_ch7=record[6],
                                                            data_ch8=record[7],
                                                            data_ch9=record[8], data_ch10=record[9], data_ch11=record[10],
                                                            data_ch12=record[11],
                                                            data_ch13=record[12], data_ch14=record[13], data_ch15=record[14],
                                                            data_ch16=record[15],
                                                            data_ch17=record[16], data_ch18=record[17], data_ch19=record[18],
                                                            data_ch20=record[19],
                                                            data_ch21=record[20], data_ch22=record[21], data_ch23=record[22],
                                                            data_ch24=record[23],
                                                            data_mark=record[24], data_time=record[25], bodymovement=record[26],
                                                            removalmark=record[27],
                                                            prescan=record[28], patient_name=patientname, business_key=(1))

                            count += 1
            i += 1

    # print("inserting fnirs session1 data")
    # all_files = os.listdir(session_1)
    # fnirs_dataset2_wl1.objects.all().delete()
    # for folder in all_files:
    #     file_path = session_1 + folder + "/"
    #     experiment_files = os.listdir(file_path)
    #     pat_labl = folder[8:10]
    #     for filename in experiment_files:

    #         val = int(filename[-5])
    #         newpath = file_path+"/"+filename

    #         if val == 1:
    #             print(newpath)
    #             with open(newpath, 'r', encoding='windows-1252') as read_file:
    #                 all_lines = read_file.readlines()
    #                 for row in all_lines:
    #                     row_as_list = row.split(",")
    #                     record = row_as_list
    #                     fnirs_dataset2_wl1.objects.create(data_1=record[0], data_2=record[1], data_3=record[2],
    #                                                       data_4=record[3], data_5=record[4], data_6=record[5], data_7=record[6], data_8=record[7], data_9=record[8], data_10=record[9], data_11=record[10], data_12=record[11], data_13=record[12], data_14=record[13], data_15=record[14], data_16=record[15], data_17=record[16], data_18=record[17], data_19=record[18], data_20=record[19], data_21=record[20], data_22=record[21], data_23=record[22], data_24=record[23], data_25=record[24], data_26=record[25], data_27=record[26], data_28=record[27], data_29=record[28], data_30=record[29], data_31=record[30], data_32=record[31], data_33=record[32], data_34=record[33], data_35=record[34], data_36=record[35], data_37=record[36], data_38=record[37], data_39=record[38], data_40=record[39], data_41=record[40], data_42=record[41], data_43=record[42], data_44=record[43], data_45=record[44], data_46=record[45], data_47=record[46], data_48=record[47], data_49=record[48], data_50=record[49], data_51=record[50], data_52=record[51], data_53=record[52], data_54=record[53], data_55=record[54], data_56=record[55], data_57=record[56], data_58=record[57], data_59=record[58], data_60=record[59], data_61=record[60], data_62=record[61], data_63=record[62], data_64=record[63], data_65=record[64], data_66=record[65], data_67=record[66], data_68=record[67], data_69=record[68], data_70=record[69], data_71=record[70], data_72=record[71], data_73=record[72], data_74=record[73], data_75=record[74], data_76=record[75], data_77=record[76], data_78=record[77], data_79=record[78], data_80=record[79], data_81=record[80], data_82=record[81], data_83=record[82], data_84=record[83], data_85=record[84], data_86=record[85], data_87=record[86], data_88=record[87], data_89=record[88], data_90=record[89], data_91=record[90], data_92=record[91], data_93=record[92], data_94=record[93], data_95=record[94], data_96=record[95], patient_name=pat_labl, business_key=(1))
    # print("finished inserting fnirs session1 data")

    # print("inserting fnirs session2 data")
    # all_files = os.listdir(session_2)
    # fnirs_dataset2_wl2.objects.all().delete()
    # for folder in all_files:

    #     file_path = session_2 + folder + "/"
    #     experiment_files = os.listdir(file_path)
    #     pat_labl = folder[8:10]
    #     for filename in experiment_files:
    #         newpath = file_path+"/"+filename
    #         val = int(filename[-5])
    #         if val == 2:
    #             print(newpath)
    #             with open(newpath, 'r', encoding='windows-1252') as read_file:
    #                 all_lines = read_file.readlines()
    #                 for row in all_lines:
    #                     row_as_list = row.split(",")
    #                     record = row_as_list
    #                     fnirs_dataset2_wl2.objects.create(data_1=record[0], data_2=record[1], data_3=record[2],
    #                                                       data_4=record[3], data_5=record[4], data_6=record[5], data_7=record[6], data_8=record[7], data_9=record[8], data_10=record[9], data_11=record[10], data_12=record[11], data_13=record[12], data_14=record[13], data_15=record[14], data_16=record[15], data_17=record[16], data_18=record[17], data_19=record[18], data_20=record[19], data_21=record[20], data_22=record[21], data_23=record[22], data_24=record[23], data_25=record[24], data_26=record[25], data_27=record[26], data_28=record[27], data_29=record[28], data_30=record[29], data_31=record[30], data_32=record[31], data_33=record[32], data_34=record[33], data_35=record[34], data_36=record[35], data_37=record[36], data_38=record[37], data_39=record[38], data_40=record[39], data_41=record[40], data_42=record[41], data_43=record[42], data_44=record[43], data_45=record[44], data_46=record[45], data_47=record[46], data_48=record[47], data_49=record[48], data_50=record[49], data_51=record[50], data_52=record[51], data_53=record[52], data_54=record[53], data_55=record[54], data_56=record[55], data_57=record[56], data_58=record[57], data_59=record[58], data_60=record[59], data_61=record[60], data_62=record[61], data_63=record[62], data_64=record[63], data_65=record[64], data_66=record[65], data_67=record[66], data_68=record[67], data_69=record[68], data_70=record[69], data_71=record[70], data_72=record[71], data_73=record[72], data_74=record[73], data_75=record[74], data_76=record[75], data_77=record[76], data_78=record[77], data_79=record[78], data_80=record[79], data_81=record[80], data_82=record[81], data_83=record[82], data_84=record[83], data_85=record[84], data_86=record[85], data_87=record[86], data_88=record[87], data_89=record[88], data_90=record[89], data_91=record[90], data_92=record[91], data_93=record[92], data_94=record[93], data_95=record[94], data_96=record[95], patient_name=pat_labl, business_key=(1))

    # print("finished inserting fnirs session2 data")

    # print("inserting eegdata")
    # all_files = os.listdir(eegdata)
    # eeg_dataset2_satelite.objects.all().delete()
    # for file in all_files:
    #     patlabl = file[8:10]
    #     filepath = eegdata + file
    #     with open(filepath, 'r', encoding='windows-1252') as read_file:
    #         all_lines = read_file.readlines()
    #         print("processing ", read_file)
    #         for row in all_lines:
    #             row_as_list = row.split(",")
    #             record = row_as_list
    #             eeg_dataset2_satelite.objects.create(data_1=record[0], data_2=record[1], data_3=record[2], data_4=record[3], data_5=record[4], data_6=record[5], data_7=record[6], data_8=record[7], data_9=record[8], data_10=record[9], data_11=record[10], data_12=record[11], data_13=record[12], data_14=record[13], data_15=record[14], data_16=record[15], data_17=record[16],
    #                                                  data_18=record[17], data_19=record[18], data_20=record[19], data_21=record[20], data_22=record[21], data_23=record[22], data_24=record[23], data_25=record[24], data_26=record[25], data_27=record[26], data_28=record[27], data_29=record[28], data_30=record[29], data_31=record[30], data_32=record[31], patient_name=patlabl, business_key=(1))

    # print("finished inserting dataset 2 eegdata")
