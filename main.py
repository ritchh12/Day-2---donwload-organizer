import os 
import shutil
source = r'D:\Workbench\Python Automation\Day 2 - donwload organizer\source'
target = r'D:\Workbench\Python Automation\Day 2 - donwload organizer\target'

def get_available_filename(path):
    file_path , extn = os.path.splitext(path)

    count = 1
    while os.path.exists(path):
        path = file_path + '_' + '(' + str(count) + ')' +extn
        count += 1

    return path
    

def organize_downloads(source,target):
    images = ['jpg', 'jpeg', 'png', 'gif', 'webp', 'bmp', 'svg', 'ico']
    videos = ['mp4', 'mkv', 'avi', 'mov', 'wmv', 'flv', 'webm']
    audio = ['mp3', 'wav', 'flac', 'aac', 'ogg', 'm4a']
    documents = ['pdf', 'doc', 'docx', 'txt', 'ppt', 'pptx', 'xls', 'xlsx', 'csv']
    archives = ['zip', 'rar', '7z', 'tar', 'gz']
    applications = ['exe', 'msi']
    python_files = ['py']

    files = os.listdir(source)

    for file in files :

        f_path = os.path.join(source,file)
        if not os.path.isfile(f_path) :
            continue

        file_name = os.path.splitext(file)[0]
        extn = os.path.splitext(file)[1].split(sep='.')[1].lower()

        print(f"File name : {file_name}")
        print(f'Extension : {extn}')

        if extn in images :
            file_type = 'images'

        elif extn in videos:
            file_type = 'videos'

        elif extn in audio:
            file_type = 'audio'

        elif extn in documents:
            file_type = 'documents'

        elif extn in archives:
            file_type = 'archives'

        elif extn in applications:
            file_type = 'applications'

        elif extn in python_files:
            file_type = 'python_files'
        else: 
            file_type = 'others'

            
        print(f'File type : {file_type} \n')

        source_path = os.path.join(source,file)
        targeted_folder = os.path.join(target,file_type)
        targeted_path = os.path.join(target,file_type,file)

        if not os.path.exists(targeted_folder):
            print("Folder doesn't exist .....")
            print(f"Creating folder: '{file_type}'.....")

            os.mkdir(targeted_folder)
            print(f"Folder {os.path.basename(targeted_folder)} created successfully!!!")   
        else :
            print("Folder already exists!!!")     

        if os.path.exists(targeted_path):
            print('File already exists!!!')
            print('Creating new filename.....')
            targeted_path = get_available_filename(targeted_path)
            print(f'New filename generated: {os.path.basename(targeted_path)}!!!')

        
        shutil.copy(source_path, targeted_path)
        print('File moved successfully!!!!\n')
        print('******************************************************************\n')


if __name__ == "__main__":
    organize_downloads(source,target)
