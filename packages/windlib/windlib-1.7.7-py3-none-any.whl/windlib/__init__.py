#!/usr/bin/env python3
#
#
#   Windlib (Useful Functions Library)
#
#
#   Copyright (C) 2021 SNWCreations. All rights reserved.
#
#


# import libraries for functions
import contextlib, gzip, os, platform, shutil, sys, tarfile, urllib, zipfile, requests, hashlib
from pathlib import Path
from clint.textui import progress

try:
    import rarfile
except:
    RAR_SUPPORT = False
else:
    RAR_SUPPORT = True


# some variables for functions.
disklst = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
found_letters = []
saved_path = '.'


# The library description...

"""
Windlib by SNWCreations

If you will use this library, I suggest importing the functions in this library through the "from" statement.

A useful function library for me!

I'm so lazy...

(C) 2021 SNWCreations. All rights reserved.
"""

# the copyright message
print('Windlib by SNWCreations')
print('Copyright (C) 2021 SNWCreations. All rights reserved.')


def typeof(variate):
    """
    Detect the type of a variable.
    """
    var_type = None
    if isinstance(variate, int):
        var_type = 'int'
    elif isinstance(variate, str):
        var_type = 'str'
    elif isinstance(variate, float):
        var_type = 'float'
    elif isinstance(variate, list):
        var_type = 'list'
    elif isinstance(variate, tuple):
        var_type = 'tuple'
    elif isinstance(variate, dict):
        var_type = 'dict'
    elif isinstance(variate, set):
        var_type = 'set'
    return var_type


def check_os(wantedOSName):
    """
    Through the "platform" module, the system label (the first parameter) provided in the call parameter is compared with the current system label.

    The function "platform.system()" may return a string, which is a system label that can be used for comparison.

    If your python works support multiple systems, then you can combine the supported system types into a list, and then call this function.

    For example, if a work supports Windows, Mac OS, Jython (Python in Java Virtual Machine) and Linux, then the labels of these three systems can be defined as support_list: ['win32','darwin','linux','Java']

    Then, call it through the following method:

    check_os(support_list)
    """

    wantedOSNameType = typeof(wantedOSName)
    if wantedOSNameType == 'list':
        if 'Java' in wantedOSName:
            if not platform.system() == 'Java':
                return False
            else:
                return True
        if not sys.platform in wantedOSName:
            return False
        else:
            return True
    elif wantedOSNameType == 'str':
        if wantedOSName == 'Java':
            if not platform.system() == wantedOSName:
                return False
            else:
                return True
        elif not platform.system() == wantedOSName:
            return False
        else:
            return True


def os_info():
    """
    Get detailed information about the system, excluding information about computer accessories.
    """
    if sys.platform == 'win32':
        os_version_tmp = platform.platform()
        os_vers = os_version_tmp.split('-')
        os_edition = str(platform.win32_edition())
        os_arch = platform.architecture()
        os_version = 'Microsoft' + \
            os_vers[0] + ' ' + os_vers[1] + ' ' + \
            os_edition + ' ' + os_vers[2] + ' ' + os_arch[0]
    elif sys.platform == 'darwin':
        os_version_tmp = platform.platform()
        os_version = os_version_tmp.replace('-', ' ')
    elif sys.platform == 'linux':
        os_version_tmp = platform.platform()
        os_version = os_version_tmp.replace('-', ' ')
    elif platform.system() == 'Java':
        os_version = 'Java virtual machine (you may be using Jython to call this function)'
    else:
        return 'ERROR'
    return os_version



def extract(filename, target_dir):
    """
    Unzip the compressed files.

    The "rarfile" library is required for support the rar files.

    You can download the "rarfile" library at https://sourceforge.net/projects/rarfile.berlios/files/latest/download .

    """
    if file_or_dir_exists(target_dir) == 'NOT_FOUND':
        os.mkdir(target_dir)
    if filename.endswith('.zip'):
        zip_file = zipfile.ZipFile(filename)
        for names in zip_file.namelist():
            zip_file.extract(names, target_dir)
        zip_file.close()
    elif filename.endswith('.gz'):
        f_name = filename.replace(".gz", "")
        # 获取文件的名称，去掉
        g_file = gzip.GzipFile(filename)
        # 创建gzip对象
        open(f_name, "w+").write(g_file.read())
        # gzip对象用read()打开后，写入open()建立的文件里。
        g_file.close()
        # 关闭gzip对象
    elif filename.endswith('.tar'):
        tar = tarfile.open(filename)
        names = tar.getnames()
        for name in names:
            tar.extract(name, target_dir)
        tar.close()
    elif filename.endswith('.rar'):
        if RAR_SUPPORT == False:
            print('.rar files are not supported.')
            return
        rar = rarfile.RarFile(filename)
        with pushd(target_dir):
            rar.extractall()
        rar.close()
    elif filename.endswith("tar.gz"):
        tar = tarfile.open(filename, "r:gz")
        with pushd(target_dir):
            tar.extractall()
        tar.close()



def get_file(url, save_path='.', show_progress=False):
    """
    Download a file from the Internet.

    If the "show_progress" parameter is True, progress will be displayed when downloading.
    
    The default value of this parameter is False.
    """
    if show_progress == False:
        filename = save_path + '/' + os.path.basename(url)
        try:
            r = requests.get(url, stream=True, timeout=30)
        except:
            return 'DOWNLOAD_FAILED'
        f = open(filename, "wb")
        # chunk是指定每次写入的大小，每次只写了1024byte
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    else:
        try:
            res = requests.get(url, stream=True)
        except:
            return 'DOWNLOAD_FAILED'
        total_length = int(res.headers.get('content-length'))
        filename = save_path + '/' + os.path.basename(url)
        with open(filename, "wb") as pypkg:
            for chunk in progress.bar(res.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1, width=50):
                if chunk:
                    pypkg.write(chunk)
    return os.path.abspath(filename)



def find_file_on_all_partitions(filename, slient=True):
    """
    Find files on all hard disk partitions.

    For example, if you want to find a file called "example.txt" on all hard disk partitions, then you should call it like this:

    find_file_on_all_partitions('example.txt')

    This function will search for this file in the order of "A:\\example.txt", "B:\\example.txt", etc.

    For another example, if you want to find a file called "example.txt" in the "example" folder on all hard disk partitions, then you should call:

    find_file_on_all_partitions('example/example.txt')

    This function will find this file in the order of "A:\\example\\example.txt", "B:\\example\\example.txt", etc.

    If found, the drive letter of the partition where the target file can be found will be placed in the "found_letters" list.
    """
    for now in disklst:
        now_file = now + ':' + os.sep + filename
        os.path.isfile(now_file)
        if now_file.isfile():
            found_letters.insert(0, now)
    if not found_letters == []:
        return found_letters
    return 'NOT_FOUND'


def get_os_partition():
    """
    Get the drive letter of the partition where the system is located.

    Will return a variable "os_partition".
    """

    os_partition_tmp = os.getenv("SystemDrive")
    os_partition = os_partition_tmp.replace(':', '')
    del os_partition_tmp
    return os_partition


def file_or_dir_exists(target):
    """
    Check if the file or directory exists.

    When the target is a file, 'IS_FILE' is returned.

    When the target is a directory, 'IS_DIR' is returned.

    When the function cannot find the target, it returns 'NOT_FOUND'.

    """
    try:
        file = Path(target)
    except:
        return 'TARGET_INVAILD'
    if file.is_file():
        return 'IS_FILE'
    elif file.is_dir():
        return 'IS_DIR'
    else:
        return False


def find_files_with_the_specified_extension(file_type, folder='.', slient=True):
    """
    Find the file with the specified extension name in targeted folder, and add the file name to the "file_list" list.

    The default value of parameter "folder" is '.' (Current dir).

    The "file_type" variable must be an extension, and does not need to carry ".".

    For example "txt" "jar" "md" "class"

    Cannot be ".txt" ".jar" ".md" ".class"

    If the "slient" parameter is False, a prompt will be generated when the function starts and finishes.
    """
    if not file_type[0] == '.':
        f_type = '.' + file_type
    items = os.listdir(folder)
    file_list = []
    for names in items:
        if names.endswith(f_type):
            file_list.append(names)
    del items
    return file_list


def find_str_in_file(string, filename):
    """
    Find target string in a file.

    "filename" parameter must be a valid file name (can be absolute or relative path).
    """
    with open(filename, 'r') as f:
        counts = 0
        for line in f.readlines():
            time = line.count(string)
            counts += time
    return counts


def copy_file(src, dst):
    """
    Copy the file (or folder) to the specified directory.

    You can copy multiple files to the specified directory by listing.
    """
    src_type = typeof(src)
    dst_type = typeof(dst)
    if not src_type == 'str' or 'list':
        return 'SRC_INVAILD'
    if not dst_type == 'str':
        return 'DST_INVAILD'
    try:
        dst_tmp = Path(dst)
    except:
        return 'DST_INVAILD'
    if not os.path.exists(dst):
        os.mkdir(dst)
    if src_type == 'list':
        for tmp in src:
            try:
                filename_tmp = Path(tmp)
            except:
                continue
            if filename_tmp.is_file():
                shutil.copyfile(tmp, dst_tmp)
            elif filename_tmp.is_dir():
                shutil.copytree(tmp, dst_tmp)
            else:
                continue
    elif src_type == 'str':
        try:
            filename_tmp = Path(tmp)
        except:
            return 'SRC_INVAILD'
        if filename_tmp.is_file():
            shutil.copyfile(tmp, dst_tmp)
        elif filename_tmp.is_dir():
            shutil.copytree(tmp, dst_tmp)
        else:
            return 'SRC_NOT_FOUND'


def is_it_broken(path):
    """
    Check a file or directory for corruption.

    Allow a large number of directories and files to be checked through the list when called once.
    """
    if typeof(path) == 'list':
        broken_files = []
        for tmp in path:
            if os.path.lexists(tmp) == True:
                if os.path.exists(path) == False:
                    broken_files.append(tmp)
        return broken_files
    elif typeof(path) == 'str':
        if os.path.lexists(path) == True:
            if os.path.exists(path):
                return 'IS_BROKEN'
            else:
                return 'NOT_BROKEN'
        else:
            return 'NOT_FOUND'


@contextlib.contextmanager
def pushd(new_dir):
    """
    Temporarily switch the working directory to a specified directory to perform some operations.

    After the operation is completed, return to the previous working directory.

    How to use:

    with pushd(directory):
        #code

    """
    previous_dir = os.getcwd()
    os.chdir(new_dir)
    try:
        yield
    finally:
        os.chdir(previous_dir)


def get_zip_file(input_path, result):
    """
    Depth first traversal of the directory, with "compress_to_zip_file" function, no other purpose.
    :param input_path:
    :param result:
    :return:
    """
    files = os.listdir(input_path)
    for file in files:
        if os.path.isdir(input_path + '/' + file):
            get_zip_file(input_path + '/' + file, result)
        else:
            result.append(input_path + '/' + file)


def compress_to_zip_file(input_path, output_path, output_name):
    """
    Compress all files in a path to a zip file.
    :param input_path: 压缩的文件夹路径
    :param output_path: 解压（输出）的路径
    :param output_name: 压缩包名称
    :return:
    """
    f = zipfile.ZipFile(output_path + '/' + output_name,
                        'w', zipfile.ZIP_DEFLATED)
    filelists = []
    get_zip_file(input_path, filelists)
    for file in filelists:
        f.write(file)
    f.close()


def get_sha1(path):
    sha1_obj = hashlib.sha1()
    try:
        a = open(fr'{path}', 'rb')
    except:
        return 'FILENAME_INVAILD'
    while True:
        b = a.read(128000)
        sha1_obj.update(b)
        if not b:
            break
    a.close()
    return sha1_obj.hexdigest()


def get_md5(path):
    md5_obj = hashlib.md5()
    try:
        a = open(path, 'rb')
    except:
        return 'FILENAME_INVAILD'
    while True:
        b = a.read(128000)
        md5_obj.update(b)
        if not b:
            break
        a.close()
        return md5_obj.hexdigest()


