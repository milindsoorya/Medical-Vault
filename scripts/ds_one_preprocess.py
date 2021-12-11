import os
import numpy as np

# Function to save a list as CSV


def saveCsv(fileName, listData):
    """
    fileName: Full path to the data CSV
    listData: The data to be saved in list format
    """
    np.savetxt(f"{fileName}", listData,
               delimiter=", ", fmt='% s', newline='')


def run():
    directory_path = "./staging/raw-data/Dataset 1/Dataset1_VM/VMData/"

    # Please uncomment the lines until 41 only for the first time. It is used to handle some erroneously names files in dataset 1

    # old_name_deoxy = directory_path + "VM010_Viso_HBA_Probe1_Deoxy.csv"
    # old_name_oxy = directory_path + "VM010_Viso_HBA_Probe1_Oxy.csv"
    # old_name_total = directory_path + "VM010_Viso_HBA_Probe1_Total.csv"
    # old_name_mes = directory_path + "VM010_Viso_MES_Probe1.csv"

    # new_name_deoxy = directory_path + "VM0010_Viso_HBA_Probe1_Deoxy.csv"
    # new_name_oxy = directory_path + "VM0010_Viso_HBA_Probe1_Oxy.csv"
    # new_name_total = directory_path + "VM0010_Viso_HBA_Probe1_Total.csv"
    # new_name_mes = directory_path + "VM0010_Viso_MES_Probe1.csv"

    # To read all files except the hidden ones
    all_files = [f for f in os.listdir(
        directory_path) if not f.startswith('.')]

    # if "VM010_Viso_HBA_Probe1_Deoxy.csv" in all_files:
    #     os.rename(old_name_deoxy, new_name_deoxy)
    # if "VM010_Viso_HBA_Probe1_Oxy.csv" in all_files:
    #     os.rename(old_name_oxy, new_name_oxy)
    # if "VM010_Viso_HBA_Probe1_Total.csv" in all_files:
    #     os.rename(old_name_total, new_name_total)
    # if "VM010_Viso_MES_Probe1.csv" in all_files:
    #     os.rename(old_name_mes, new_name_mes)

    # Make a new directory for the processed data
    processed_path = './staging/processedData/Dataset 1/'
    if not os.path.exists(processed_path):
        os.mkdir(processed_path)

    processed_data_path = 'deoxy'
    parent_path = processed_path
    path = os.path.join(parent_path, processed_data_path)
    if not os.path.exists(path):
        os.mkdir(path)

    processed_data_path = 'oxy'
    path = os.path.join(parent_path, processed_data_path)
    if not os.path.exists(path):
        os.mkdir(path)

    processed_data_path = 'mes'
    path = os.path.join(parent_path, processed_data_path)
    if not os.path.exists(path):
        os.mkdir(path)

    processed_data_path = 'total'
    path = os.path.join(parent_path, processed_data_path)
    if not os.path.exists(path):
        os.mkdir(path)

    # Make a new directory for the processed data
    processed_path_patient = './staging/processedData/Dataset 1/patient_info/'
    if not os.path.exists(processed_path_patient):
        os.mkdir(processed_path_patient)

    # Process each file in the directory
    for file in all_files:
        # Make seperate destination for deoxy, oxy, mes
        file_list = file.split("_")
        if file_list[2] == "MES":
            folder_name = "mes/"
        elif file_list[-1] == 'Total.csv':
            folder_name = "total/"
        elif file_list[-1] == 'Deoxy.csv':
            folder_name = "deoxy/"
        elif file_list[-1] == 'Oxy.csv':
            folder_name = "oxy/"

        filepath = directory_path + file
        output_file_loc = processed_path + folder_name + \
            file  # Path to save the processed file

        # Open each CSV file
        with open(filepath) as f:
            temp_data = f.readlines()[40:]

            # strip off unnecessary index column
            csv_data = []
            for line in temp_data:
                line_csv = ''
                chunks = line.split(',')[1:]
                for word in chunks[:-1]:
                    line_csv = line_csv + word + ', '
                line_csv = line_csv + chunks[-1]
                csv_data.append(line_csv)

        # Filter out the data from CSV
        saveCsv(output_file_loc, csv_data)

    # Process each file in the directory for Patient Information
    PatientIDs = []
    for file in all_files:
        filepath = directory_path + file

        file_name = file[0:6]
        if file_name not in PatientIDs:

            # add PatientID to list of IDs and set output name
            PatientIDs.append(file_name)
            output_file_loc = processed_path_patient + file_name + \
                '_PatientInformation.csv'  # Path to save the processed file

            # Open each CSV file
            with open(filepath) as f:

                # take only the important information (rows 4, 6 and 7)
                readf = f.readlines()
                temp_data = []
                temp_data.append(readf[4])
                temp_data.append(readf[6])
                temp_data.append(readf[7])

                # strip off unnecessary index column
                csv_data = []
                for line in temp_data:
                    line_csv = ''
                    chunks = line.split(',')
                    line_csv = line_csv + chunks[1]
                    csv_data.append(line_csv)

            # Filter out the data from CSV
            saveCsv(output_file_loc, csv_data)
