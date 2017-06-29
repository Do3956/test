#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @author jinqinghua@gmail.com
# @version 2013-05-28

import os
import shutil
import tarfile
from ftplib import FTP

# 以下部分可能要修改
project_home = "C:\Users\admin\Desktop\upServer"
update_home = "E:\Server\login"


# ftp settings
ftp_server = "120.24.5.155"
ftp_port = "21"
ftp_user = "administrator"
ftp_password = "admin"


def copy_web_files():
    cmd_xcopy = 'xcopy %s %s /I /Y /S /D:%s %s' % (path_src_web, path_dst_web, time_modify, exclude_all)
    print(cmd_xcopy)
    os.system(cmd_xcopy)
    print("copy_web_files end...")


def copy_jar_files():
    cmd_xcopy = "xcopy %s %s /I /Y /S %s" % (path_src_lib, path_dst_lib, exclude_lib)
    print(cmd_xcopy)
    os.system(cmd_xcopy)


def copy_class_files():
    if not os.path.exists(path_dst_cls):
        cmd_xcopy = "xcopy %s %s /I /Y /S /D:%s %s" % (path_src_cls, path_dst_cls, time_modify, exclude_all)
        print(cmd_xcopy)
        os.system(cmd_xcopy)
        print("copy_web_files end...")


def tar_files():
    print("taring files...")
    tar = tarfile.open(file_zip, "w:gz")
    tar.add(path_dst_web, "")
    tar.close()


def ftp_stor_files():
    cmd_stor = "STOR %s" % (os.path.split(file_zip)[1])
    print(cmd_stor)
    ftp = FTP(ftp_server, ftp_user, ftp_password)
    ftp.getwelcome()
    ftp.storbinary(cmd_stor, open(file_zip, "rb"), 1024)
    ftp.close()
    # ftp.quit()


def clear():
    cmd_rmdir = "rmdir /S /Q %s" % (path_dst_web)
    cmd_del = "del /S /Q %s" % (file_zip)
    print cmd_rmdir
    print cmd_del
    os.system(cmd_rmdir)
    os.system(cmd_del)


# 主运行程序，可能要修改
if __name__ == "__main__":
    copy_web_files()
    # copy_jar_files()
    copy_class_files()
    tar_files()
    ftp_stor_files()
    # clear()
    print("done, python is great!")