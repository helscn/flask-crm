#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import platform
import atexit

fcntl = None
msvcrt = None
bLinux = True
if platform.system() != 'Windows':
    fcntl = __import__("fcntl")
    bLinux = True
else:
    msvcrt = __import__('msvcrt')
    bLinux = False


class FileLock:
    '''
    文件加锁包装类，用于对指定文件进行加锁，程序退出时会自动释放文件锁
    '''

    def __init__(self, filename):
        self.filename = filename    # 需要加锁的文件路径
        self._file = None           # 用于加锁的文件对象
        self._locked = False        # 是否获取了当前文件对象的锁

    @property
    def locked(self):
        '''
        当前 FileLock 对象是否获得了文件锁
        '''
        return self._locked

    def lock(self):
        '''
        申请获取文件锁，成功返回 True，失败返回 False
        '''
        try:
            if bLinux is True:
                self._file = open(self.filename, 'wb')
                fcntl.flock(self._file, fcntl.LOCK_EX | fcntl.LOCK_NB)
                self._locked = True
                atexit.register(self.unlock)
            else:
                self._file = open(self.filename, 'wb')
                msvcrt.locking(self._file.fileno(), msvcrt.LK_NBLCK, 1)
                self._locked = True
                atexit.register(self.unlock)
            return True
        except:
            return False

    def unlock(self):
        '''
        释放文件锁，成功返回 True
        '''
        try:
            if bLinux is True:
                fcntl.flock(self._file, fcntl.LOCK_UN)
                self._file.close()
                self._locked = False
                atexit.unregister(self.unlock)
            else:
                self._file.seek(0)
                msvcrt.locking(self._file.fileno(), msvcrt.LK_UNLCK, 1)
                self._file.close()
                self._locked = False
                atexit.unregister(self.unlock)
            return True
        except:
            return False
