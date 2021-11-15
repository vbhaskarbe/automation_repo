import fnmatch 
import os 
from zipfile import ZipFile


def ui_process_screenshots( test_status):
    png_files_dict = {}
    for filename in os.listdir('/tmp/cctaf_logs/test_ui_clouds'):
        if filename.endswith('.png'):
            png_files_dict[filename] = os.path.join('/tmp/cctaf_logs/test_ui_clouds', filename)

    if test_status == 'fail':
        pattern = '%s*.png' % 'test_ui_clouds'
        with ZipFile('/tmp/cctaf_logs/test_ui_clouds/test_ui_clouds.zip', 'w') as zipObj:
            for filename in png_files_dict.keys():
                zipObj.write(png_files_dict[filename], os.path.basename(png_files_dict[filename]))
        zipObj.close()
        print("Created /tmp/cctaf_logs/test_ui_clouds/test_ui_clouds.zip")
    else:
        print("Testcase Passed...Remove PNG files")
    ## Remove all PNG files. Pass - not required. Fail - Zip file created already.
    for filename in png_files_dict.keys():
        ##print("Removing file %s" % png_files_dict[filename])
        os.remove( png_files_dict[filename])

if __name__ == '__main__':
    #ui_process_screenshots('pass')

    #ui_process_screenshots('fail')

    import glob
    print( os.path.join( '/tmp', 'cctaf_logs', 'test_ui_clouds', 'test_ui_clouds' + '*.png'))
    list_files = glob.glob( os.path.join( '/tmp', 'cctaf_logs', 'test_ui_clouds', 'test_ui_clouds' + '*.png'))
    print(list_files)
    print("BYE BYE")
    with ZipFile('/tmp/cctaf_logs/test_ui_clouds/test_ui_clouds.zip', 'w') as zipObj:
        for filename in glob.glob( os.path.join( '/tmp', 'cctaf_logs', 'test_ui_clouds', 'test_ui_clouds' + '*.png')):
            zipObj.write(filename, os.path.basename(filename))
    zipObj.close()
    print("Created /tmp/cctaf_logs/test_ui_clouds/test_ui_clouds.zip")


