# import zipfile as zf
#
#
# def create_zip(instance, files):
#     with zf.ZipFile(instance.title.join('.zip'), 'w') as myZip:
#         for file in files:
#             myZip.write(file)
#         return myZip

import os
import zipfile
from io import StringIO

from django.http import HttpResponse


def create_zip(hw_instance, files):
    # Files (local path) to put in the .zip
    # FIXME: Change this (get paths from DB etc)
    # filenames = ["/tmp/file1.txt", "/tmp/file2.txt"]

    # Folder name in ZIP archive which contains the above files
    # E.g [thearchive.zip]/somefiles/file2.txt
    # FIXME: Set this to something better
    zip_subdir = '/media/homeworks/1/1'# str(hw_instance.id)
    print(zip_subdir, "++++++++")
    zip_filename = zip_subdir.join(["HW", str(hw_instance.id), ".zip"])
    print(zip_filename, '&&&&&&&&&&&&&')
    # Open StringIO to grab in-memory ZIP contents
    s = StringIO()

    # The zip compressor
    zf = zipfile.ZipFile(s, "w")

    # for ans in hw_instance.get_answers():
    for fpath in files:
        fpath = os.path.join(fpath)
        # Calculate path for file in zip
        fdir, fname = os.path.split(fpath)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~>", fpath)
        zip_path = os.path.join(zip_subdir, fname)

        # Add file, at correct path
        print(fpath,',,,',zip_path)
        zf.write(fpath, zip_path)

    # Must close zip for all contents to be written
    zf.close()

    # Grab ZIP file from in-memory, make response with correct MIME-type
    resp = HttpResponse(s.getvalue(), content_type="application/x-zip-compressed")
    # ..and correct content-disposition
    resp['download_all'] = 'attachment; filename=%s' % zip_filename

    return resp
