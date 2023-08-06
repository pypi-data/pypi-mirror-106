from datetime import datetime
from typing import ClassVar
from PIL import Image
import re



filename_patterns = [    
    [r'WhatsApp Image \b\d{4}-\d{2}-\d{2}', r'\b\d{4}-\d{2}-\d{2}', '%Y-%m-%d', 'WhatsApp'], # Watsapp Pattern    
    [r'Screenshot_\d{4}-\d{2}-\d{2}', r'\d{4}-\d{2}-\d{2}', '%Y-%m-%d', 'Screenshot'],  # Screen Shoot Pattern
    [r'scanner_\d{4}\d{2}\d{2}', r'\d{4}\d{2}\d{2}', '%Y%m%d', 'Scanner'],  # IMG- Pattern
    [r'IMG_\d{4}\d{2}\d{2}', r'\d{4}\d{2}\d{2}', '%Y%m%d', 'WhatsApp'],  # IMG- Pattern
    [r'IMG-\d{4}\d{2}\d{2}', r'\d{4}\d{2}\d{2}', '%Y%m%d', 'WhatsApp'],  # IMG_ Pattern
    [r'SAVE_\d{4}\d{2}\d{2}', r'\d{4}\d{2}\d{2}', '%Y%m%d', 'WhatsApp'],  # SAVE Pattern
    [r'VID_\d{4}\d{2}\d{2}', r'\d{4}\d{2}\d{2}', '%Y%m%d', 'Camera'],  # VID_ Pattern
    [r'VID-\d{4}\d{2}\d{2}', r'\d{4}\d{2}\d{2}', '%Y%m%d', 'WhatsApp'],  # VID- Pattern
    [r'video-\d{4}-\d{2}-\d{2}', r'\d{4}-\d{2}-\d{2}', '%Y-%m-%d', 'Camera']  # video- Pattern
]

exif_type = 'Camera'

class FileInfo:

    def __init__(self, path):
        self.is_null = True
        self.get_date_exif(path)        
        if self.is_null == False:            
            return
        self.get_date_in_filename(path)

    # Date in file name    
    def get_date_in_filename(self, path):
        #print(path)
        for filename_pattern in filename_patterns:
            match = re.search(filename_pattern[0], path)
            if (match):
                match = re.search(filename_pattern[1], path)
                dts = match.group()
                #return datetime.strptime(dts, filename_pattern[2]).strftime(date_conv_format)
                self.is_null = False
                self.date = datetime.strptime(dts, filename_pattern[2]).date()
                self.type = filename_pattern[3]
                break
        else:        
            self.is_null = True

    # Date from EXIF
    def get_date_exif(self, path):
        #print(path)    
        try:        
            dts = Image.open(path)._getexif()[36867]    
        except:
            self.is_null = True
        else:        
            #sdate = datetime.strptime(dts, '%Y:%m:%d %H:%M:%S').strftime(date_conv_format)
            self.is_null = False
            self.date = datetime.strptime(dts, '%Y:%m:%d %H:%M:%S').date()
            self.type = exif_type

    @staticmethod
    def nTypes():
        return len(filename_patterns) + 1
        
    @staticmethod
    def types():        
        typ = []
        for filename_pattern in filename_patterns:
            typ.append(filename_pattern[3])
        typ.append(exif_type)
        return typ