# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 18:31:02 2020

@author: keisuke
"""

if __name__ == '__main__':
    try:#メッセージボックスがなければエラーが出せない
        import tkinter as tk
        from tkinter import messagebox as mbox
    except:
        raise Exception('エラー:tkinterがインポートできません。')

if __name__ == '__main__':
    window_for_error = tk.Tk()#tkinterではウィンドウを作成しなければメッセージボックスが出せない
    window_for_error.withdraw()#不要なので隠しておく

#エラー定義
class FileReadError(Exception):
    def Error(self,file_not_found):
        self.file_not_found = file_not_found
        mbox.showerror('エラー','ファイルが読み込めませんでした。\n読み込めなかったファイル:'+'・'.join(self.file_not_found))
        window_for_error.destroy()
        time.sleep(3)
class LibraryReadError(Exception):
    def Error(self,library_not_found):
        self.library_not_found = library_not_found
        mbox.showerror('エラー','ライブラリが読み込めませんでした。\n読み込めなかったライブラリ:'+'・'.join(self.library_not_found))
        window_for_error.destroy()
        time.sleep(3)
class VariableError(Exception):
    def Error(self,ErrorVariableName):
        self.ErrorVariableName = ErrorVariableName
        mbox.showerror('エラー','変数が予期していない値になった、あるいは読み込めませんでした。\nエラーが起きた変数:'+self.ErrorVariableName)
        window_for_error.destroy()
        time.sleep(3)
  
#読み込なかったライブラリ
read_not_library = []
all_library = ['pygame','sys','time']
try:
    import pygame
except:
    read_not_library.append('pygame')
    library_not_found = read_not_library
    error = LibraryReadError()
    error.Error(library_not_found)
    raise LibraryReadError('エラー:ライブラリが読み込めませんでした。\n読み込めなかったライブラリ:'+'・'.join(library_not_found))
try:
    import sys
except:
    read_not_library.append('sys')
    library_not_found = read_not_library
    error = LibraryReadError()
    error.Error(library_not_found)
    raise LibraryReadError('エラー:ライブラリが読み込めませんでした。\n読み込めなかったライブラリ:'+'・'.join(library_not_found))
try:
    import time
except:
    read_not_library.append('time')
    library_not_found = read_not_library
    error = LibraryReadError()
    error.Error(library_not_found)
    raise LibraryReadError('エラー:ライブラリが読み込めませんでした。\n読み込めなかったライブラリ:'+'・'.join(library_not_found))
try:
    import threading
except:
    read_not_library.append('time')
    library_not_found = read_not_library
    error = LibraryReadError()
    error.Error(library_not_found)
    raise LibraryReadError('エラー:ライブラリが読み込めませんでした。\n読み込めなかったライブラリ:'+'・'.join(library_not_found))

#
#使用しているフォント
#・http://itouhiro.hatenablog.com/entry/20130602/font(PixelMplus12-Bold)(PATH=Fonts/PixelMplus12-Bold.ttf)
#
#

#メモ
####
#self == (main = Game() のようにインスタンス変数を定義したときの、インスタンス変数(ここではmain)の代名詞)
#例
#main = main()
#main.GameMainLoop == self.GameMainLoop
#
####
#
#
#

#FileCheckファイル呼び出し
try:#FileCheckファイルが存在するか
    import FileCheck
except:
    #警告メッセージボックス呼び出し
    mbox.showerror('エラー','FileCheckファイルが読み込めません。')
    raise FileReadError('FileCheckファイルが読み込めません。')
#
filecheck = FileCheck.FileCheck('All')
#すべてのファイルがあったか
all_file_exists_bool_and_file_not_found = filecheck.FileCheckBool()
all_file_exists_bool = all_file_exists_bool_and_file_not_found[0]
file_not_found = all_file_exists_bool_and_file_not_found[1]
if all_file_exists_bool == True:
    pass
else:
    #警告メッセージボックス呼び出し
    error = FileReadError()
    error.Error(file_not_found)
    raise FileReadError('エラー:ファイルが読み込めませんでした。\n読み込めなかったファイル:'+'・'.join(file_not_found))
    


class Main(object):#親クラスはobjectクラスを継承しないとだめらしい....
    def __init__(self,):
        #いまどれをしているか
        self.game_on= True
        self.game_start_screen_on = False
        self.game_play_mode_serect_screen_on = False
        #windowの縦横比(main_window)
        self.HEIGHT,self.WIDTH = 400,300
        self.GAME_START_BACK_SCREEAN_COLOR = '#669966'
        self.PXMF_B_PATH = r'Fonts\PixelMplus12-Bold.ttf'
        self.KREMLINSTAR_PXCEL_ART_PATH = r'Images/Kremlinstar/OriginalKremlinStar(400x300)PixelArt.png'
        self.OUSPENSKI_CATHEDRAL_PATH = r'Images/OuspenskiCathedral/OuspenskiCathedral(400x300)PxcelArt.png'
        self.TITLE_PATH = r'Images/Title/Tetris.png'
        self.ICON_PATH = r'Images/Icon/Icon.png'
        self.arrow_flashing_display = False#スタート画面時に矢印が画面上に出ているか
        self.flame_rate = 60
        self.clock = pygame.time.Clock()#フレームレート実体化
        #設定ファイル(SettingsSaveFile.json)があるか
        self.filecheck = FileCheck.FileCheck('SettingsSaveFile.json')
        self.file_exists_bool = all_file_exists_bool_and_file_not_found[0]
        self.file_not_found = all_file_exists_bool_and_file_not_found[1]
        if self.file_exists_bool != True:
            #警告メッセージボックス呼び出し
            error = FileReadError()
            error.Error(file_not_found)
            raise FileReadError('エラー:ファイルが読み込めませんでした。\n読み込めなかったファイル:'+'・'.join(file_not_found))
        else:
            pass
        #設定ファイル読み込み
        
        #
        #pygame初期化
        pygame.init()
        #
        self.game_start_screen_on = True
        if __name__ == '__main__':#これしないと関数呼び出しをめちゃくちゃしてエラー出る
            self.GameDrawRelation()
            self.GameMainLoop()
    def GameDrawRelation(self,):
        #GameDraw.pyが存在するか
        self.filecheck = FileCheck.FileCheck('GameDraw.py')
        self.file_exists_bool = all_file_exists_bool_and_file_not_found[0]
        self.file_not_found = all_file_exists_bool_and_file_not_found[1]
        if self.file_exists_bool != True:
            #警告メッセージボックス呼び出し
            error = FileReadError()
            error.Error(file_not_found)
            raise FileReadError('エラー:ファイルが読み込めませんでした。\n読み込めなかったファイル:'+'・'.join(file_not_found))
        else:
            pass
        #GameDrawファイル呼び出し
        import GameDraw
        #GameDrawクラスインスタンス化
        self.gamedraw = GameDraw.Main()
        #最初の画面
        self.gamedraw.GameStartScreen('first_time')
    def TetrisVariableSharing(self,variables):
        #まずlocalできたvariablesを解凍
        #items()で辞書の中の変数の名前と、変数を取り出すため、forの代入する変数は二つ(変数名,値)
        for self.variable_name , self.value in variables.items():
            self.variable_name = self.variable_name[self.variable_name]#わざわざリストにすることで変数名に代入することができる
            self.variable_name[0] = self.value
        #localsでこのメソッド内にある変数名と内容を取得
        #items()で辞書の中の変数の名前と、変数を取り出すため、forの代入する変数は二つ(変数名,値)
        for self.variable_name , self.value in locals().items():
            if self.variable_name != 'self':#変数名がselfでなければ
                self.variable_name = [self.variable_name]#わざわざリストにすることで変数名に代入することができる
                self.variable_name[0] = self.value
    def OtherFileVariableSharing(self,):
        time.sleep(0.0001)
        thread_game_draw_variable_sharing = threading.Thread(target=self.gamedraw.GameDrawVariableSharing,args=locals())
        thread_game_draw_variable_sharing.start()
    def GameMainLoop(self,):
        #矢印点滅タイマー
        ONE_TIME_TICK = pygame.USEREVENT + 0#event場所取得
        ONE_TIME_TICK_EVENT = pygame.event.Event(ONE_TIME_TICK,attr1='ONE_TIME_TICK_EVENT')#イベント設定
        pygame.event.post(ONE_TIME_TICK_EVENT)#イベント実行
        pygame.time.set_timer(ONE_TIME_TICK_EVENT,1000)#イベントを使いタイマー実行
        while self.game_on:
            #pygame.time.wait(30)
            self.clock.tick(self.flame_rate)
            for event in pygame.event.get():
                #画面ｕｐｄａｔｅ
                pygame.display.update()
                #key取得
                self.event_key = pygame.key.get_pressed()
                #
                if event.type == pygame.QUIT:
                    self.GameExit()
                if self.game_start_screen_on:
                    #矢印点滅
                    if event == ONE_TIME_TICK_EVENT:
                        if self.arrow_flashing_display == True:#もし矢印が画面上に表示されていたら
                            self.gamedraw.GameStartScreen()#矢印なしの画面を表示する
                            self.arrow_flashing_display = False
                        else:
                            self.arrow_flashing_display = True
                            self.gamedraw.GameStartScreen()#矢印なしの画面を表示する
                            self.gamedraw.GameArrow(self.arrow_flashing_display,self.gamedraw.position,'game_start_screen')#矢印を表示
                    if self.event_key[pygame.K_UP] == 1:  
                        #次の場所を設定
                        self.next_position = self.gamedraw.position - 1#関数は変数を持っておらず、クラスが所持している
                        self.gamedraw.GameArrow(self.arrow_flashing_display,self.next_position,'game_start_screen')
                    elif self.event_key[pygame.K_DOWN] == 1:
                        #次の場所を設定
                        self.next_position = self.gamedraw.position + 1
                        self.gamedraw.GameArrow(self.arrow_flashing_display,self.next_position,'game_start_screen')
                    if self.event_key[pygame.K_RETURN] == 1:#エンターキーを押したら
                        if self.gamedraw.position == 0:
                            self.game_start_screen_on = False
                            self.game_play_mode_serect_screen_on = True
                            self.arrow_flashing_display = False
                            self.gamedraw.GamePlayModeSerect('first_time')
                        elif self.gamedraw.position == 1:
                            pass
                        elif self.gamedraw.position == 2:
                            pass
                        else:#エラー
                            error = VariableError()
                            error.Error('GameDraw.py/Main/GameArrow.position')
                if self.game_play_mode_serect_screen_on:
                    #矢印点滅
                    if event == ONE_TIME_TICK_EVENT:
                        if self.arrow_flashing_display == True:#もし矢印が画面上に表示されていたら
                            self.gamedraw.GamePlayModeSerect()#矢印なしの画面を表示する
                            self.arrow_flashing_display = False
                        else:
                            self.arrow_flashing_display = True
                            self.gamedraw.GamePlayModeSerect()#矢印なしの画面を表示する
                            #矢印を表示
                            self.gamedraw.GameArrow(self.arrow_flashing_display,self.gamedraw.position,'game_play_mode_serect')#矢印を表示
                    if self.event_key[pygame.K_UP] == 1:  
                        #次の場所を設定
                        self.next_position = self.gamedraw.position - 1#関数は変数を持っておらず、クラスが所持している
                        self.gamedraw.GameArrow(self.arrow_flashing_display,self.next_position,'game_play_mode_serect')
                    elif self.event_key[pygame.K_DOWN] == 1:
                        #次の場所を設定
                        self.next_position = self.gamedraw.position + 1
                        self.gamedraw.GameArrow(self.arrow_flashing_display,self.next_position,'game_play_mode_serect')
                    if self.event_key[pygame.K_RETURN] == 1:#エンターキーを押したら
                        if self.gamedraw.position == 0:
                            pass
                        elif self.gamedraw.position == 1:
                            pass
                        elif self.gamedraw.position == 2:
                            self.game_start_screen_on = True
                            self.game_play_mode_serect_screen_on = False
                            self.arrow_flashing_display = False
                            #
                            #最初の画面
                            self.gamedraw.GameStartScreen('first_time')
                        else:#予期しない値が変数に入っているのでエラー
                            error = VariableError()
                            error.Error('GameDraw.py/Main/GameArrow.position')
                ####変数共有###
                thread_other_file_variable_sharing = threading.Thread(target=self.OtherFileVariableSharing)
                thread_other_file_variable_sharing.start()
                
    def GameExit(self,):
        self.game_on = False
        pygame.quit()
        window_for_error.destroy()
        sys.exit()
    def Settings_save(self,):
        pass

if __name__ == '__main__':
    Game = Main()