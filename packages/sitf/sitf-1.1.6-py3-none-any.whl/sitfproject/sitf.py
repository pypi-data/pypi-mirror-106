import os, sys, shutil, argparse, logging
from datetime import datetime
from collections import defaultdict
from sitfproject.progressbar import printProgressBar
from sitfproject.fileinfo import FileInfo

version = '1.1.6'
media_file_ext = ['jpg', 'JPG', 'jpeg', 'png', 'mp4']
fulldate_conv_format = '%Y-%m-%d' #Directory name date format
monthdate_conv_format = '%Y-%m' #Directory name date format
  

def isMediaFile(name):    
    for ext in media_file_ext:
        if name.endswith('.' + ext):
            return True
    return False
    
# Movie Files
def moveFiles(list, src_path, dst_folder):

    if (len(list) == 0):
        return

    if not os.path.exists(dst_folder) : # Creat Dir
            os.mkdir(dst_folder)

    print('Moving files...')
    for date,  filenames in list.items():
        #print(f'Date->{k.strftime(date_conv_format)} File->{v}\n\n')
        if len(filenames) <= 4:
            dateStr = os.path.join(dst_folder, date.strftime(monthdate_conv_format))
        else:
            dateStr = os.path.join(dst_folder, date.strftime(fulldate_conv_format))

        if not os.path.exists(dateStr) : # Creat Dir
            os.mkdir(dateStr)

        for filename in filenames:
            src_file = os.path.join(src_path, filename)
            dst_file = os.path.join(os.path.join(src_path, dateStr), filename)                    
            shutil.move(src_file, dst_file)
            logging.info(f'{src_file}->{dst_file}')

# Sort Image
def sort_image():    
    
    file_list = {}
    for type in FileInfo.types():
        file_list[type] = defaultdict(lambda: [])

    msg = f'Sorting in -> {os.getcwd()}'
    print(msg)
    logging.info(msg)

    n_file = 0 
    total_files = sum(1 for _ in os.scandir())
    
    for i, entry in enumerate(os.scandir()):
        printProgressBar(i + 1, total_files, prefix = 'Checking:', suffix = 'Complete', length = 50)
        if not entry.is_file():
            continue

        filename = entry.name
        if isMediaFile(filename):
            fileInfo = FileInfo(filename)
            if fileInfo.is_null:
                continue
            file_list[fileInfo.type][fileInfo.date].append(filename)
            n_file += 1
    
    print()
    for k, v in file_list.items():
        moveFiles(v, os.getcwd(), k)
        
    msg = f'Moved {str(n_file)} files'
    logging.info(msg)
    print(msg)

# Delete Empty Dirctory
def delEmptyDirecs():    
    path = os.getcwd()
    logging.info(f'Cleaning in -> {path}')
    n_dirs = 0
    for (root, dirs, files) in os.walk(path, topdown=False):        
        if path == root:
            continue
        
        # Delete No Media file of andriod
        no_media_file = os.path.join(root, '.nomedia')
        if os.path.exists(no_media_file):
            os.remove(no_media_file)
            logging.info(f'Deleting .nomedia file->{no_media_file}')

        if len(os.listdir(root)) == 0:            
            os.rmdir(root)
            logging.info(f'Deleting Directory->{root}')
            n_dirs += 1

    msg = f'Deleted {n_dirs} Directories'
    logging.info(msg)
    print(msg)

# Extract Sort Media file Back
def extract():    
    path = os.getcwd()
    print(f'Extacting in->{path}')
    logging.info(f'Extacting in->{path}')
    n_files = 0
    for (root, dirs, files) in os.walk(path):
        #print(f'Root->{root}\nDirs->{dirs}\nFiles->{files}\n\n')
        if path == root or os.path.basename(root).startswith('.'):
            continue

        for file in files:
            if isMediaFile(file):                
                fp = os.path.join(root, file)
                fileInfo = FileInfo(fp)
                if fileInfo.is_null:
                    continue
                logging.info(f'{fp}->dst_dir')
                try:
                    shutil.move(fp, path)
                except:
                    msg = f'{fp} already exists'
                    logging.warning(msg)
                    print(msg)
                else:
                    n_files += 1
    msg = f'Extracted {n_files}'
    logging.info(msg)
    print(msg)
    #Delete Empty Directory's
    #delEmptyDirecs(dst_dir)

# Main       
def main():    
    #print('Image file sorter By Shatak Gurukar\n')
    parser = argparse.ArgumentParser(description=f'Image file sorter.\nVersion: {version}')
    parser.add_argument('-C', '--clean', action='store_true', help='Clean Empty Folders')    
    parser.add_argument('--extract', action='store_true', help='Extract Media files from Folders')
    parser.add_argument('path', help='Path to Directory')
    args = parser.parse_args()
    os.chdir(args.path)
    #logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', filename='sitf.log', encoding='utf-8', level=logging.INFO) # Encoding 3.9 and above
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p', filename='sitf.log', level=logging.INFO)
        
    if args.clean:
        delEmptyDirecs()
    elif args.extract:
        extract()
    else:
        sort_image()

if __name__ == "__main__":
    main()

