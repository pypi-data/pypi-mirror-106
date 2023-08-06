# **Windlib**

A useful functions library, Created by SNWCreations.

This is a useful functions library for everyone.

If you have any questions, please give me feedback in issues.

But I may not reply in time, please forgive me.

#### English / [简体中文](https://github.com/SNWCreations/windlib/blob/main/README-zh_Hans.md)

## **Usage**

***Tip: If you use the "import windlib" method to import my function, then the function name in the example below should be changed to "windlib.\<function name\>"
If you use the "from windlib import \<function name\>" method, the "windlib" prefix is not required.***

---

### **typeof - Detect the type of a variable.**

    For example, I define a variable "a" as 10 (this is an integer number, that is, "int") and call this function with the following method:

    typeof(a)

    This function returns the string 'int'.

---

### **check_os - Check the OS information.**

Through the "platform" module, the system label (the first parameter) provided in the call parameter is compared with the current system label.

The function "platform.system()" may return a string, which is a system label that can be used for comparison.

If your python works support multiple systems, then you can combine the supported system types into a list, and then call this function.

    For example, if a work supports Windows, Mac OS, Jython (Python in Java Virtual Machine) and Linux, then the labels of these three systems can be defined as support_list: ['win32','darwin','linux','Java']

    Then, call it through the following method:

    check_os(support_list)

---

### **os_info - Get the OS information.**

Get detailed information about the system, **excluding information about computer accessories.**

The full information will returned.

---

### **extract - Unzip the compressed files.**

Unzip the compressed files.

Support ".zip" ".gz" ".tar" ".rar" ".tar.gz" files.

The "rarfile" library is required for support the ".rar" files.

You can download the "rarfile" library at https://sourceforge.net/projects/rarfile.berlios/files/latest/download .

---

### **get_file - Download a file from Internet.**

Download a file from the Internet.

If the "show_progress" parameter is True, progress will be displayed when downloading. The default value of this parameter is False.

String 'DOWNLOAD_FAILED' will be returned when download failed.

The path of target file on local disk will be returned when download completed.

---

### **get_os_partition - Get the drive letter of the system.**

Get the drive letter of the partition where the system is located.

Will return a string. (The content may be any letter from A-Z)

---

### **file_or_dir_exists - Check if the file or directory exists.**

Check if the file or directory exists.

When the target is a file, 'IS_FILE' is returned.

When the target is a directory, 'IS_DIR' is returned.

When the function cannot find the target, it returns 'NOT_FOUND'.

---

### **find_files_with_the_specified_extension - Find the file with the specified extension name in targeted folder.**

Find the file with the specified extension name in targeted folder, and add the file name to the **"file_list"** list.

*The default value of parameter "folder" is '.' (Current dir).*

The "file_type" variable must be an extension, and does not need to carry ".".

For example "txt" "jar" "md" "class", or ".txt" ".jar" ".md" ".class".

---

### **find_str_in_file - Find the string in a file.**

Find target string in a file.

"filename" parameter **must** be a valid file name (can be absolute or relative path).

---

### **copy_file - copy the file (or folder) to the specified directory**

Copy the file (or folder) to the specified directory.

You can copy multiple files to the specified directory by listing.

---

### **is_it_broken - Check a file or directory for corruption.**

Check a file or directory for corruption.

Allow a large number of directories and files to be checked through the list when called once.

---

### **pushd - Temporarily switch to a directory.**

Temporarily switch to a directory and save the current path before switching for return on the next call.

* How to use:

    with pushd(directory):
        #code

---

### **compress_to_zip_file - compress all files in a directory into a zip file.**

Compress all files in a directory to a zip file.

---

### **get_sha1 - Get SHA1 value of a file.**

Get SHA1 value of a file.

---

### **get_md5 - Get MD5 value of a file.**

Get MD5 value of a file.

---

## Copyright (C) 2021 SNWCreations. All rights reserved.
