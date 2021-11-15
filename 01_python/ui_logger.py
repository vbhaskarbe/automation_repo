'''
 Created on 24-April-2019
 @author: syoonus
'''

import os
import time
import inspect
from cctaf.cctaf_lib.uiReport import UIReport
from cctaf.cctaf_lib.cctaf_logger import logger as apilogger
from cctaf.cctaf_lib.cctaf_config_utils import CCTAFConfigUtil

class uiLogger():
    
    def __init__(self,logs_dir=str(CCTAFConfigUtil().getDefault().LOGS_DIR)):
        self.logs_dir = logs_dir
        self.initialize_logger = False

    def initialize_ui_logger(self, test_name):
        file_name = (inspect.getsourcefile(test_name).split("/"))[-1].replace(".py","")
        file_name = self.logs_dir + "/" + file_name + "/" + file_name + ".html"    
        self.report = UIReport(file_name)
        self.initialize_logger = True

    def ui_initialize_screenshots(self, test_name):
        self.file_name        = (inspect.getsourcefile(test_name).split("/"))[-1].replace(".py","")
        self.snapshot_name    = os.path.join( self.logs_dir, self.file_name, test_name.__name__)
        self.snapshot_counter = 1

    ## Method to create screenshots zip file and then remove screenshot files.
    def ui_process_screenshots(self, test_status = 'pass'):
        import glob
        from zipfile import ZipFile
        try:
            png_files_list = glob.glob( os.path.join( self.snapshot_name + '_*.png'))
            if test_status == 'fail':
                with ZipFile( self.snapshot_name + '.zip', 'w') as zipObj:
                    for filename in png_files_list:
                        zipObj.write( filename, os.path.basename(filename))
                        os.remove( filename)
                zipObj.close()
        except Exception as e:
            apilogger.info("ui_process_screenshots: Failed: %s" % str(e))

    def time_format(self):
        named_tuple = time.localtime()
        return time.strftime("%H:%M:%S", named_tuple)
        
    def info(self,msg, *args, **kwargs):
        if self.initialize_logger == False:
            file_name = self.logs_dir + "/cctaf_ui.html"
            self.report = UIReport(file_name)
            self.initialize_logger = True
        apilogger.info(msg,*args, **kwargs)
        self.report.ui_info(self.time_format(),msg)
    
    def step(self,msg,*args,**kwargs):
        if self.initialize_logger == False:
            file_name = self.logs_dir + "/cctaf_ui.html"
            self.report = UIReport(file_name)
            self.initialize_logger = True
        apilogger.info(msg,*args, **kwargs)
        self.report.ui_step(self.time_format(), msg)
    
    def error(self,msg,*args,**kwargs):
        apilogger.error(msg,*args, **kwargs)
        self.report.ui_info(self.time_format(), msg)
    
    def debug(self,msg, *args, **kwargs):
        apilogger.info(msg,*args, **kwargs)
        self.report.ui_info(self.time_format(),msg)
    
    def failed(self,msg,*args,**kwargs):
        apilogger.error(msg,*args, **kwargs)
        self.report.ui_fail(self.time_format(), msg)
      
    def passed(self,msg,*args,**kwargs):
        apilogger.info(msg,*args, **kwargs)
        self.report.ui_pass(self.time_format(), msg)
        

logger = uiLogger()



    
