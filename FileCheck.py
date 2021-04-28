# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 16:06:00 2020

@author: keisuke
"""

import os

#filecheck = FileCheck.FileCheck()#実体化
#(引数に何も指定しないとすべてのファイルがあるか調べる)
#'All'を引数にしていすると...同様にすべてのファイルがあるか調べる
#r'Fonts\PixelMplus12-Bold.ttf'のようにファイルパスをしていすると...そのファイルがあるか調べる
#[r'Fonts\PixelMplus12-Bold.ttf',r'Test.py']のようにリスト化されたファイルパスを指定すると...そのファイルたちがあるか調べる
#調べた結果はfilecheck.FileCheckBool()の返り値で出てくる(リスト)
#返り値[0] = そのファイルがあったか,そのファイルたちがあったか、すべてのファイルがあったか(あったらTrue)
#返り値[1] = もし指定したファイルがなかったらそのファイルパスをlist化する。なければ空のリスト

class FileCheck():
    def AllFileCheck(self,FILEPATH):
        self.FILEPATH = FILEPATH
        if os.path.isfile(FILEPATH) == True:
            pass
        else:
            return self.FILEPATH;
    def ParticularFileCheck(self,FILEPATH):
        self.file_not_found = list()
        if type(FILEPATH) == list:
            self.FILEPATHS = FILEPATH
            for self.FILEPATH in self.FILEPATHS:
                if os.path.isfile(self.FILEPATH) == False:
                    self.file_not_found.append(self.FILEPATH)
                else:
                    pass
            if len(self.file_not_found) == 0:
                self.all_file_exists_bool = True
                self.file_not_found = self.file_not_found
            else:
                self.all_file_exists_bool = False
                self.file_not_found = self.file_not_found
            self.FileCheckBool()
        elif type(FILEPATH) == str:
            self.FILEPATH = FILEPATH
            if os.path.isfile(self.FILEPATH) == False:
                self.all_file_exists_bool = False
                self.file_not_found.append(self.FILEPATH)
            else:
                self.all_file_exists_bool = True
            self.FileCheckBool()
        else:
            raise TypeError('エラー:list,str以外の型を指定しました。(FileCheck.py/FileCheck/ParticularFileCheck)')
    def __init__(self,EXISTS_SPECIFIED_FILE=None):
        self.EXISTS_SPECIFIED_FILE = EXISTS_SPECIFIED_FILE
        if self.EXISTS_SPECIFIED_FILE == None or self.EXISTS_SPECIFIED_FILE == 'All':
            self.FILEPATHS = [r'Fonts\PixelMplus12-Bold.ttf',r'GameDraw.py',r'SettingsSaveFile.json',r'Config.py']
            self.file_not_found = list(map(self.AllFileCheck,self.FILEPATHS))
            for i in range(len(self.file_not_found)):
                if None in self.file_not_found:
                    del self.file_not_found[self.file_not_found.index(None)]
                else:
                    pass
            if len(self.file_not_found) == 0:
                self.all_file_exists_bool = True
            else:
                self.all_file_exists_bool = False
        else:
            self.FILEPATH = self.EXISTS_SPECIFIED_FILE
            self.ParticularFileCheck(self.FILEPATH)
        
    def FileCheckBool(self,):
        return self.all_file_exists_bool,self.file_not_found
    
if __name__ == '__main__':
    pass