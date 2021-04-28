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
    
#すべて読み込めたので...
import Config
import GameDraw

class Main(object):#親クラスはobjectクラスを継承しないとだめらしい....
    def __init__(self,):
        #pygame初期化
        pygame.init()
        #設定ファイル読み込み
        
        ####
        self.clock = pygame.time.Clock()#フレームレート実体化
        self.key_repeat = pygame.key.set_repeat(5000,10)#引数はdelay,interbalの順(どちらもミリ秒)delayは何秒長押ししたら?interbalは長押ししていたらキーをどれくらいおしたことにするか?
        ####
        #
        Config.game_on = True
        Config.game_start_screen_on = True
        #
        if __name__ == '__main__':#これしないと関数呼び出しをめちゃくちゃしてエラー出る
            self.GameDrawRelation()
            self.GameMainLoop()
        #
    def GameDrawRelation(self,):
        #GameDrawクラスインスタンス化
        self.gamedraw = GameDraw.Main()
        #最初の画面
        self.gamedraw.GameStartScreen('first_time')
    def GameMainLoop(self,):
        #矢印点滅タイマー
        ONE_TIME_TICK = pygame.USEREVENT + 0#event場所取得
        ONE_TIME_TICK_EVENT = pygame.event.Event(ONE_TIME_TICK,attr1='ONE_TIME_TICK_EVENT')#イベント設定
        pygame.event.post(ONE_TIME_TICK_EVENT)#イベント実行
        pygame.time.set_timer(ONE_TIME_TICK_EVENT,1000)#イベントを使いタイマー実行
        while Config.game_on:
            #pygame.time.wait(30)
            self.clock.tick(Config.flame_rate)
            for event in pygame.event.get():
                #画面update
                pygame.display.update()
                #key取得
                self.event_key = pygame.key.get_pressed()
                #
                if event.type == pygame.QUIT:
                    self.GameExit()
                if Config.game_start_screen_on:
                    #矢印点滅
                    if event == ONE_TIME_TICK_EVENT:
                        if Config.arrow_flashing_display == True:#もし矢印が画面上に表示されていたら
                            self.gamedraw.GameStartScreen()#矢印なしの画面を表示する
                            Config.arrow_flashing_display = False
                        else:
                            Config.arrow_flashing_display = True
                            self.gamedraw.GameStartScreen()#矢印なしの画面を表示する
                            self.gamedraw.GameArrow()#矢印を表示
                    if self.event_key[pygame.K_UP] == 1:  
                        #次の場所を設定
                        Config.next_position = Config.position - 1#関数は変数を持っておらず、クラスが所持している
                        self.gamedraw.GameArrow()
                    elif self.event_key[pygame.K_DOWN] == 1:
                        #次の場所を設定
                        Config.next_position = Config.position + 1
                        self.gamedraw.GameArrow()
                    if self.event_key[pygame.K_RETURN] == 1:#エンターキーを押したら
                        if Config.position == 0:
                            Config.game_start_screen_on = False
                            Config.game_play_mode_serect_screen_on = True
                            Config.arrow_flashing_display = False
                            self.gamedraw.GamePlayModeSerect('first_time')
                        elif Config.position == 1:
                            pass
                        elif Config.position == 2:
                            pass
                        else:#エラー
                            error = VariableError()
                            error.Error('GameDraw.py/Main/GameArrow.position')
                elif Config.game_play_mode_serect_screen_on:
                    #矢印点滅
                    if event == ONE_TIME_TICK_EVENT:
                        if Config.arrow_flashing_display == True:#もし矢印が画面上に表示されていたら
                            self.gamedraw.GamePlayModeSerect()#矢印なしの画面を表示する
                            Config.arrow_flashing_display = False
                        else:
                            Config.arrow_flashing_display = True
                            self.gamedraw.GamePlayModeSerect()#矢印なしの画面を表示する
                            #矢印を表示
                            self.gamedraw.GameArrow()#矢印を表示
                    if self.event_key[pygame.K_UP] == 1:  
                        #次の場所を設定
                        Config.next_position = Config.position - 1#関数は変数を持っておらず、クラスが所持している
                        self.gamedraw.GameArrow()
                    elif self.event_key[pygame.K_DOWN] == 1:
                        #次の場所を設定
                        Config.next_position = Config.position + 1
                        self.gamedraw.GameArrow()
                    if self.event_key[pygame.K_RETURN] == 1:#エンターキーを押したら
                        if Config.position == 0:
                            self.gamedraw.GamePlayScreen('120secconds','first_time')
                        elif Config.position == 1:
                            self.gamedraw.GamePlayScreen('endless','first_time')
                        elif Config.position == 2:
                            Config.game_start_screen_on = True
                            Config.game_play_mode_serect_screen_on = False
                            Config.arrow_flashing_display = False
                            #
                            #最初の画面
                            self.gamedraw.GameStartScreen('first_time')
                        else:#予期しない値が変数に入っているのでエラー
                            error = VariableError()
                            error.Error('GameDraw.py/Main/GameArrow.position')
                elif Config.game_play_120_mode == True or Config.game_play_endless == True:
                    if event == ONE_TIME_TICK_EVENT:
                        pass
                    elif self.event_key[pygame.K_RIGHT]:
                        break_command = False
                        if break_command == True:
                            break_command = False
                            return 0;
                        if Config.game_play_120_mode == True:
                            self.gamedraw.GamePlayScreen('120secconds')
                        else:
                            self.gamedraw.GamePlayScreen('endless')
                        self.height = -1#リストの順番が0,1,2...と続くため,変数に0を代入すると+1されると値が1になりリスト指定がうまくいかない
                        self.i = -1#リストの順番が0,1,2...と続くため,変数に0を代入すると+1されると値が1になりリスト指定がうまくいかない
                        self.j = -1#Jは段数のうち何個参照したか、段数が変わるとまたカウントしなおす。
                        for tetromino_line in Config.tetromino_postion:
                            if break_command == True:
                                break
                            self.height += 1
                            self.weight = -1#リストの順番が0,1,2...と続くため,変数に0を代入すると+1されると値が1になりリスト指定がうまくいかない
                            self.j = -1
                            for tetromino_block in tetromino_line:
                                self.i += 1#iは何個参照したか
                                self.j += 1#書いてあります
                                if tetromino_block != 9:
                                    self.weight += 1#weightはiと違って何個参照したかでなく壁を含めずに何個参照しているかという変数。座標と一致させやすい
                                    if [self.weight,self.height] == Config.moving_tetromino_postion:
                                        Config.moving_tetromino_data = tetromino_line[self.j]#動かしているテトロミノブロックの情報取得
                                        #何ミノか確認(衝突判定)
                                        if Config.moving_tetromino_data[0] == 0:#Iミノ
                                            if Config.moving_tetromino_data[1] == 0:
                                                if Config.moving_tetromino_postion[0] + 1 == 10:#行くところの座標(weight)が10だったらbreak
                                                    for k in range(4):#Iミノはブロックが4つだから
                                                        Config.main_window.blit(Config.lb_tetromino,[295+(self.weight)*20,100+(self.height+k)*20])#weight+1しないのはテトロミノを動かさないから
                                                    break_command == True
                                                    break
                                        elif Config.moving_tetromino_data[0] == 1:#Oミノ
                                            if Config.moving_tetromino_data[1] == 0:
                                                if Config.moving_tetromino_postion[0] + 2 == 10:#行くところの座標(weight)が10だったらbreak
                                                    for k in range(2):
                                                        Config.main_window.blit(Config.y_tetromino,[295+(self.weight)*20,100+(self.height+k)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    for k in range(2):
                                                        Config.main_window.blit(Config.y_tetromino,[295+(self.weight+1)*20,100+(self.height+k)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    break_command == True
                                                    break
                                        elif Config.moving_tetromino_data[0] == 2:#Tミノ
                                            if Config.moving_tetromino_data[1] == 0:
                                                if Config.moving_tetromino_postion[0] + 4 == 10:#行くところの座標(weight)が10だったらbreak
                                                    Config.main_window.blit(Config.p_tetromino,[295+(self.weight+2)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    for k in range(3):
                                                       Config.main_window.blit(Config.p_tetromino,[295+(self.weight+1+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから 
                                                    break_command == True
                                                    break
                                        elif Config.moving_tetromino_data[0] == 3:#Jミノ
                                            if Config.moving_tetromino_data[1] == 0:
                                                if Config.moving_tetromino_postion[0] + 4 == 10:#行くところの座標(weight)が10だったらbreak
                                                    Config.main_window.blit(Config.b_tetromino,[295+(self.weight+1)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    for k in range(3):
                                                        Config.main_window.blit(Config.b_tetromino,[295+(self.weight+1+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    break_command == True
                                                    break
                                        elif Config.moving_tetromino_data[0] == 4:#Lミノ
                                            if Config.moving_tetromino_data[1] == 0:
                                                if Config.moving_tetromino_postion[0] + 4 == 10:#行くところの座標(weight)が10だったらbreak
                                                    Config.main_window.blit(Config.o_tetromino,[295+(self.weight+3)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    for k in range(3):
                                                        Config.main_window.blit(Config.o_tetromino,[295+(self.weight+1+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    break_command == True
                                                    break
                                        elif Config.moving_tetromino_data[0] == 5:#Sミノ
                                            if Config.moving_tetromino_data[1] == 0:
                                                if Config.moving_tetromino_postion[0] + 4 == 10:#行くところの座標(weight)が10だったらbreak
                                                    for k in range(2):
                                                        Config.main_window.blit(Config.g_tetromino,[295+(self.weight+2+k)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    for k in range(2):
                                                        Config.main_window.blit(Config.g_tetromino,[295+(self.weight+1+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    break_command = True
                                                    break
                                        elif Config.moving_tetromino_data[0] == 6:#Zミノ
                                            if Config.moving_tetromino_data[1] == 0:
                                                if Config.moving_tetromino_postion[0] + 4 == 10:#行くところの座標(weight)が10だったらbreak
                                                    for k in range(2):
                                                        Config.main_window.blit(Config.r_tetromino,[295+(self.weight+1+k)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    for k in range(2):
                                                        Config.main_window.blit(Config.r_tetromino,[295+(self.weight+2+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    break_command = True
                                                    break
                                        else:
                                            pass
                                        #Config.moving_tetromino_index = tetromino_line.index(tetromino_line[self.i])#動かしているテトロミノブロックの場所を確認。
                                        Config.tetromino_postion[self.height][self.j] = 0#動かすために今いるところを空白にする
                                        Config.tetromino_postion[self.height][self.j+1] = Config.moving_tetromino_data#動かされるところにデータを移行。これで完全に動かされたことになる
                                        Config.moving_tetromino_postion[0] += 1#座標も変更
                                        #動かしたあとの座標はheightそのままweight+1
                                        #何ミノか確認
                                        if Config.moving_tetromino_data[0] == 0:#Iミノ
                                            for k in range(4):#Iミノはブロックが4つだから
                                                Config.main_window.blit(Config.lb_tetromino,[295+(self.weight+1)*20,100+(self.height+k)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                        elif Config.moving_tetromino_data[0] == 1:#Oミノ
                                            for k in range(2):
                                                Config.main_window.blit(Config.y_tetromino,[295+(self.weight+1)*20,100+(self.height+k)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                            for k in range(2):
                                                Config.main_window.blit(Config.y_tetromino,[295+(self.weight+2)*20,100+(self.height+k)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                        elif Config.moving_tetromino_data[0] == 2:#Tミノ
                                            Config.main_window.blit(Config.p_tetromino,[295+(self.weight+2)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                            for k in range(3):
                                               Config.main_window.blit(Config.p_tetromino,[295+(self.weight+1+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから 
                                        elif Config.moving_tetromino_data[0] == 3:#Jミノ
                                            Config.main_window.blit(Config.b_tetromino,[295+(self.weight+1)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                            for k in range(3):
                                                Config.main_window.blit(Config.b_tetromino,[295+(self.weight+1+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                        elif Config.moving_tetromino_data[0] == 4:#Lミノ
                                            Config.main_window.blit(Config.o_tetromino,[295+(self.weight+3)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                            for k in range(3):
                                                Config.main_window.blit(Config.o_tetromino,[295+(self.weight+1+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                        elif Config.moving_tetromino_data[0] == 5:#Sミノ
                                            for k in range(2):
                                                Config.main_window.blit(Config.g_tetromino,[295+(self.weight+2+k)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                            for k in range(2):
                                                Config.main_window.blit(Config.g_tetromino,[295+(self.weight+1+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                        elif Config.moving_tetromino_data[0] == 6:#Zミノ
                                            for k in range(2):
                                                Config.main_window.blit(Config.r_tetromino,[295+(self.weight+1+k)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                            for k in range(2):
                                                Config.main_window.blit(Config.r_tetromino,[295+(self.weight+2+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                        else:
                                            pass
                                        break_command= True
                                        break
                                    
                                else:
                                    pass
                    elif self.event_key[pygame.K_LEFT]:
                        break_command = False
                        if break_command == True:
                            break_command = False
                            return 0;
                        if Config.game_play_120_mode == True:
                            self.gamedraw.GamePlayScreen('120secconds')
                        else:
                            self.gamedraw.GamePlayScreen('endless')
                        self.height = -1#リストの順番が0,1,2...と続くため,変数に0を代入すると+1されると値が1になりリスト指定がうまくいかない
                        self.i = -1#リストの順番が0,1,2...と続くため,変数に0を代入すると+1されると値が1になりリスト指定がうまくいかない
                        self.j = -1#Jは段数のうち何個参照したか、段数が変わるとまたカウントしなおす。
                        for tetromino_line in Config.tetromino_postion:
                            if break_command == True:
                                break
                            self.height += 1
                            self.weight = -1#リストの順番が0,1,2...と続くため,変数に0を代入すると+1されると値が1になりリスト指定がうまくいかない
                            self.j = -1
                            for tetromino_block in tetromino_line:
                                self.i += 1#iは何個参照したか
                                self.j += 1#書いてあります
                                if tetromino_block != 9:
                                    self.weight += 1#weightはiと違って何個参照したかでなく壁を含めずに何個参照しているかという変数。座標と一致させやすい
                                    if [self.weight,self.height] == Config.moving_tetromino_postion:
                                        Config.moving_tetromino_data = tetromino_line[self.j]#動かしているテトロミノブロックの情報取得
                                        #何ミノか確認(衝突判定)
                                        if Config.moving_tetromino_data[0] == 0:#Iミノ
                                            if Config.moving_tetromino_data[1] == 0:
                                                if Config.moving_tetromino_postion[0] - 1 == -1:#行くところの座標(weight)が10だったらbreak
                                                    for k in range(4):#Iミノはブロックが4つだから
                                                        Config.main_window.blit(Config.lb_tetromino,[295+(self.weight)*20,100+(self.height+k)*20])#weight+1しないのはテトロミノを動かさないから
                                                    break_command == True
                                                    break
                                        elif Config.moving_tetromino_data[0] == 1:#Oミノ
                                            if Config.moving_tetromino_data[1] == 0:
                                                if Config.moving_tetromino_postion[0] - 1 == -1:#行くところの座標(weight)が10だったらbreak
                                                    for k in range(2):
                                                        Config.main_window.blit(Config.y_tetromino,[295+(self.weight)*20,100+(self.height+k)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    for k in range(2):
                                                        Config.main_window.blit(Config.y_tetromino,[295+(self.weight+1)*20,100+(self.height+k)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    break_command == True
                                                    break
                                        elif Config.moving_tetromino_data[0] == 2:#Tミノ
                                            if Config.moving_tetromino_data[1] == 0:
                                                if Config.moving_tetromino_postion[0] -1 == -1:#行くところの座標(weight)が10だったらbreak
                                                    Config.main_window.blit(Config.p_tetromino,[295+(self.weight+1)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    for k in range(3):
                                                       Config.main_window.blit(Config.p_tetromino,[295+(self.weight+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから 
                                                    break_command == True
                                                    break
                                        elif Config.moving_tetromino_data[0] == 3:#Jミノ
                                            if Config.moving_tetromino_data[1] == 0:
                                                if Config.moving_tetromino_postion[0] -1 == -1:#行くところの座標(weight)が10だったらbreak
                                                    Config.main_window.blit(Config.b_tetromino,[295+(self.weight)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    for k in range(3):
                                                        Config.main_window.blit(Config.b_tetromino,[295+(self.weight+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    break_command == True
                                                    break
                                        elif Config.moving_tetromino_data[0] == 4:#Lミノ
                                            if Config.moving_tetromino_data[1] == 0:
                                                if Config.moving_tetromino_postion[0] - 1 == -1:#行くところの座標(weight)が10だったらbreak
                                                    Config.main_window.blit(Config.o_tetromino,[295+(self.weight+2)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    for k in range(3):
                                                        Config.main_window.blit(Config.o_tetromino,[295+(self.weight+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    break_command == True
                                                    break
                                        elif Config.moving_tetromino_data[0] == 5:#Sミノ
                                            if Config.moving_tetromino_data[1] == 0:
                                                if Config.moving_tetromino_postion[0] - 1 == -1:#行くところの座標(weight)が10だったらbreak
                                                    for k in range(2):
                                                        Config.main_window.blit(Config.g_tetromino,[295+(self.weight+1+k)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    for k in range(2):
                                                        Config.main_window.blit(Config.g_tetromino,[295+(self.weight+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    break_command = True
                                                    break
                                        elif Config.moving_tetromino_data[0] == 6:#Zミノ
                                            if Config.moving_tetromino_data[1] == 0:
                                                if Config.moving_tetromino_postion[0] - 1 == -1:#行くところの座標(weight)が10だったらbreak
                                                    for k in range(2):
                                                        Config.main_window.blit(Config.r_tetromino,[295+(self.weight+k)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    for k in range(2):
                                                        Config.main_window.blit(Config.r_tetromino,[295+(self.weight+1+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    break_command = True
                                                    break
                                        else:
                                            pass
                                        #Config.moving_tetromino_index = tetromino_line.index(tetromino_line[self.i])#動かしているテトロミノブロックの場所を確認。
                                        Config.tetromino_postion[self.height][self.j] = 0#動かすために今いるところを空白にする
                                        Config.tetromino_postion[self.height][self.j-1] = Config.moving_tetromino_data#動かされるところにデータを移行。これで完全に動かされたことになる
                                        Config.moving_tetromino_postion[0] -= 1#座標も変更
                                        #動かしたあとの座標はheightそのままweight-1
                                        #何ミノか確認
                                        if Config.moving_tetromino_data[0] == 0:#Iミノ
                                            for k in range(4):#Iミノはブロックが4つだから
                                                Config.main_window.blit(Config.lb_tetromino,[295+(self.weight-1)*20,100+(self.height+k)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                        elif Config.moving_tetromino_data[0] == 1:#Oミノ
                                            for k in range(2):
                                                Config.main_window.blit(Config.y_tetromino,[295+(self.weight-1)*20,100+(self.height+k)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                            for k in range(2):
                                                Config.main_window.blit(Config.y_tetromino,[295+(self.weight)*20,100+(self.height+k)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                        elif Config.moving_tetromino_data[0] == 2:#Tミノ
                                            Config.main_window.blit(Config.p_tetromino,[295+(self.weight)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                            for k in range(3):
                                               Config.main_window.blit(Config.p_tetromino,[295+(self.weight-1+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから 
                                        elif Config.moving_tetromino_data[0] == 3:#Jミノ
                                            Config.main_window.blit(Config.b_tetromino,[295+(self.weight-1)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                            for k in range(3):
                                                Config.main_window.blit(Config.b_tetromino,[295+(self.weight-1+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                        elif Config.moving_tetromino_data[0] == 4:#Lミノ
                                            Config.main_window.blit(Config.o_tetromino,[295+(self.weight+1)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                            for k in range(3):
                                                Config.main_window.blit(Config.o_tetromino,[295+(self.weight-1+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                        elif Config.moving_tetromino_data[0] == 5:#Sミノ
                                            for k in range(2):
                                                Config.main_window.blit(Config.g_tetromino,[295+(self.weight+k)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                            for k in range(2):
                                                Config.main_window.blit(Config.g_tetromino,[295+(self.weight-1+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                        elif Config.moving_tetromino_data[0] == 6:#Zミノ
                                            for k in range(2):
                                                Config.main_window.blit(Config.r_tetromino,[295+(self.weight-1+k)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                            for k in range(2):
                                                Config.main_window.blit(Config.r_tetromino,[295+(self.weight+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                        else:
                                            pass
                                        
                                        break_command= True
                                        break
                                else:
                                    pass
                    elif self.event_key[pygame.K_DOWN]:
                        break_command = False
                        if break_command == True:
                            break_command = False
                            return 0;
                        if Config.game_play_120_mode == True:
                            self.gamedraw.GamePlayScreen('120secconds')
                        else:
                            self.gamedraw.GamePlayScreen('endless')
                        self.height = -1#リストの順番が0,1,2...と続くため,変数に0を代入すると+1されると値が1になりリスト指定がうまくいかない
                        self.i = -1#リストの順番が0,1,2...と続くため,変数に0を代入すると+1されると値が1になりリスト指定がうまくいかない
                        self.j = -1#Jは段数のうち何個参照したか、段数が変わるとまたカウントしなおす。
                        for tetromino_line in Config.tetromino_postion:
                            if break_command == True:
                                break_command = False
                                break
                            self.height += 1
                            self.weight = -1#リストの順番が0,1,2...と続くため,変数に0を代入すると+1されると値が1になりリスト指定がうまくいかない
                            self.j = -1
                            for tetromino_block in tetromino_line:
                                self.i += 1#iは何個参照したか
                                self.j += 1#書いてあります
                                if tetromino_block != 9:
                                    self.weight += 1#weightはiと違って何個参照したかでなく壁を含めずに何個参照しているかという変数。座標と一致させやすい   
                                    if [self.weight,self.height] == Config.moving_tetromino_postion:
                                        Config.moving_tetromino_data = tetromino_line[self.j]#動かしているテトロミノブロックの情報取得
                                        #何ミノか確認(衝突判定)
                                        if Config.moving_tetromino_data[0] == 0:#Iミノ
                                            if Config.moving_tetromino_data[1] == 0:#回転
                                                if Config.moving_tetromino_postion[1] + 4 == 20:#行くところの座標(height)が20だったらbreak
                                                    for k in range(4):#Iミノはブロックが4つだから
                                                        Config.main_window.blit(Config.lb_tetromino,[295+(self.weight)*20,100+(self.height+k)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    break_command == True
                                                    break
                                        elif Config.moving_tetromino_data[0] == 1:#Oミノ
                                            if Config.moving_tetromino_data[1] == 0:
                                                if Config.moving_tetromino_postion[1] + 2 == 20:#行くところの座標(height)が20だったらbreak
                                                    for k in range(2):
                                                        Config.main_window.blit(Config.y_tetromino,[295+(self.weight)*20,100+(self.height+k)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    for k in range(2):
                                                        Config.main_window.blit(Config.y_tetromino,[295+(self.weight+1)*20,100+(self.height+k)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    break_command == True
                                                    break
                                        elif Config.moving_tetromino_data[0] == 2:#Tミノ
                                            if Config.moving_tetromino_data[1] == 0:
                                                if Config.moving_tetromino_postion[1] + 2 == 20:#行くところの座標(height)が20だったらbreak
                                                    Config.main_window.blit(Config.p_tetromino,[295+(self.weight+1)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    for k in range(3):
                                                        Config.main_window.blit(Config.p_tetromino,[295+(self.weight+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから 
                                                    break_command == True
                                                    break
                                        elif Config.moving_tetromino_data[0] == 3:#Jミノ
                                            if Config.moving_tetromino_data[1] == 0:
                                                if Config.moving_tetromino_postion[1] + 2 == 20:#行くところの座標(height)が20だったらbreak
                                                    Config.main_window.blit(Config.b_tetromino,[295+(self.weight)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    for k in range(3):
                                                        Config.main_window.blit(Config.b_tetromino,[295+(self.weight+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    break_command == True
                                                    break
                                        elif Config.moving_tetromino_data[0] == 4:#Lミノ
                                            if Config.moving_tetromino_data[1] == 0:
                                                if Config.moving_tetromino_postion[1] + 2 == 20:#行くところの座標(height)が20だったらbreak
                                                    Config.main_window.blit(Config.o_tetromino,[295+(self.weight+2)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    for k in range(3):
                                                        Config.main_window.blit(Config.o_tetromino,[295+(self.weight+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    break_command == True
                                                    break
                                        elif Config.moving_tetromino_data[0] == 5:#Sミノ
                                            if Config.moving_tetromino_data[1] == 0:
                                                if Config.moving_tetromino_postion[1] + 2 == 20:#行くところの座標(height)が20だったらbreak
                                                    for k in range(2):
                                                        Config.main_window.blit(Config.g_tetromino,[295+(self.weight+1+k)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    for k in range(2):
                                                        Config.main_window.blit(Config.g_tetromino,[295+(self.weight+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    break_command = True
                                                    break
                                        elif Config.moving_tetromino_data[0] == 6:#Zミノ
                                            if Config.moving_tetromino_data[1] == 0:
                                                if Config.moving_tetromino_postion[1] + 2 == 20:#行くところの座標(height)が20だったらbreak
                                                    for k in range(2):
                                                        Config.main_window.blit(Config.r_tetromino,[295+(self.weight+k)*20,100+(self.height)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    for k in range(2):
                                                        Config.main_window.blit(Config.r_tetromino,[295+(self.weight+1+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                                    break_command = True
                                                    break
                                        else:
                                            pass
                                        Config.tetromino_postion[self.height][self.j] = 0#動かすために今いるところを空白にする
                                        Config.tetromino_postion[self.height+1][self.j] = Config.moving_tetromino_data#動かされるところにデータを移行。これで完全に動かされたことになる
                                        Config.moving_tetromino_postion[1] += 1#座標も変更
                                        #動かしたあとの座標はheight+1そのままweight
                                        #何ミノか確認
                                        if Config.moving_tetromino_data[0] == 0:#Iミノ
                                            for k in range(4):#Iミノはブロックが4つだから
                                                Config.main_window.blit(Config.lb_tetromino,[295+(self.weight)*20,100+(self.height+1+k)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                        elif Config.moving_tetromino_data[0] == 1:#Oミノ
                                            for k in range(2):
                                                Config.main_window.blit(Config.y_tetromino,[295+(self.weight)*20,100+(self.height+1+k)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                            for k in range(2):
                                                Config.main_window.blit(Config.y_tetromino,[295+(self.weight+1)*20,100+(self.height+1+k)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                        elif Config.moving_tetromino_data[0] == 2:#Tミノ
                                            Config.main_window.blit(Config.p_tetromino,[295+(self.weight+1)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                            for k in range(3):
                                               Config.main_window.blit(Config.p_tetromino,[295+(self.weight+k)*20,100+(self.height+2)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから 
                                        elif Config.moving_tetromino_data[0] == 3:#Jミノ
                                            Config.main_window.blit(Config.b_tetromino,[295+(self.weight)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                            for k in range(3):
                                                Config.main_window.blit(Config.b_tetromino,[295+(self.weight+k)*20,100+(self.height+2)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                        elif Config.moving_tetromino_data[0] == 4:#Lミノ
                                            Config.main_window.blit(Config.o_tetromino,[295+(self.weight+2)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                            for k in range(3):
                                                Config.main_window.blit(Config.o_tetromino,[295+(self.weight+k)*20,100+(self.height+2)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                        elif Config.moving_tetromino_data[0] == 5:#Sミノ
                                            for k in range(2):
                                                Config.main_window.blit(Config.g_tetromino,[295+(self.weight+1+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                            for k in range(2):
                                                Config.main_window.blit(Config.g_tetromino,[295+(self.weight+k)*20,100+(self.height+2)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                        elif Config.moving_tetromino_data[0] == 6:#Zミノ
                                            for k in range(2):
                                                Config.main_window.blit(Config.r_tetromino,[295+(self.weight+k)*20,100+(self.height+1)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                            for k in range(2):
                                                Config.main_window.blit(Config.r_tetromino,[295+(self.weight+1+k)*20,100+(self.height+2)*20])#weight,heightの順番なのは座標変数が[weight,height]の順番だから
                                        else:
                                            pass
                                        break_command= True
                                        break
                                    
                                else:
                                    pass
                    elif self.event_key[pygame.K_LSHIFT]:
                        pass
                    elif self.event_key[pygame.K_UP]:
                        break_command = False
                        if break_command == True:
                            break_command = False
                            return 0;
                        if Config.game_play_120_mode == True:
                            self.gamedraw.GamePlayScreen('120secconds')
                        else:
                            self.gamedraw.GamePlayScreen('endless')
                        self.height = -1#リストの順番が0,1,2...と続くため,変数に0を代入すると+1されると値が1になりリスト指定がうまくいかない
                        self.i = -1#リストの順番が0,1,2...と続くため,変数に0を代入すると+1されると値が1になりリスト指定がうまくいかない
                        self.j = -1#Jは段数のうち何個参照したか、段数が変わるとまたカウントしなおす。
                        for tetromino_line in Config.tetromino_postion:
                            if break_command == True:
                                break_command = False
                                break
                            self.height += 1
                            self.weight = -1#リストの順番が0,1,2...と続くため,変数に0を代入すると+1されると値が1になりリスト指定がうまくいかない
                            self.j = -1
                            for tetromino_block in tetromino_line:
                                self.i += 1#iは何個参照したか
                                self.j += 1#書いてあります
                                if tetromino_block != 9:
                                    self.weight += 1#weightはiと違って何個参照したかでなく壁を含めずに何個参照しているかという変数。座標と一致させやすい   
                                    if [self.weight,self.height] == Config.moving_tetromino_postion:
                                        Config.moving_tetromino_data = tetromino_line[self.j]#動かしているテトロミノブロックの情報取得
                                        if Config.moving_tetromino_data[0] == 0:
                                            if Config.moving_tetromino_data[1] == 0:#1になる処理を行う
                                                for l in range(-1,3):#移動先に何かあったらbreak
                                                    if Config.tetromino_postion[self.height+1][self.j+l] != 0:
                                                        break_command = True
                                                        break
                                                Config.tetromino_postion[self.height][self.j] = 0
                                                Config.moving_tetromino_data[1] = 1
                                                Config.tetromino_postion[self.height+1][self.j+2] = Config.moving_tetromino_data
                                                Config.moving_tetromino_postion = [self.weight+2,self.height+1]
                                                print(Config.moving_tetromino_postion)
                                                print(Config.tetromino_postion[self.height+1][self.j+2])
                                                #描画
                                                for k in range(4):
                                                    Config.main_window.blit(Config.lb_tetromino,[295+(self.weight-1+k)*20,100+(self.height+1)*20])
                                                break_command = True
                                                break
                                            elif Config.moving_tetromino_data[1] == 1:#2になる処理を行う
                                                for l in range(-1,3):
                                                    if Config.tetromino_postion[self.height+l][self.j-2] != 0:
                                                        break_command = True
                                                        break
                                                Config.tetromino_postion[self.height][self.j] = 0
                                                Config.moving_tetromino_data[1] = 2
                                                Config.tetromino_postion[self.height+2][self.j-1] = Config.moving_tetromino_data
                                                Config.moving_tetromino_postion  = [self.weight-1,self.height+2]
                                                for k in range(4):
                                                    Config.main_window.blit(Config.lb_tetromino,[295+(self.weight-1)*20,100+(self.height-1+k)*20])
                                                break_command = True
                                                break
                                            elif Config.moving_tetromino_data[1] == 2:#3になる処理を行う
                                                for l in range(-1,3):
                                                    if Config.tetromino_postion[self.height-2][self.j-1+l] != 0:
                                                        break_command = True
                                                        break
                                                Config.tetromino_postion[self.height][self.j] = 0
                                                Config.moving_tetromino_data[1] = 3
                                                Config.tetromino_postion[self.height-1][self.j-2] = Config.moving_tetromino_data
                                                Config.moving_tetromino_postion  = [self.weight-2,self.height-1]
                                                for k in range(4):
                                                    Config.main_window.blit(Config.lb_tetromino,[295+(self.weight-2+k)*20,100+(self.height-1)*20])
                                                break_command = True
                                                break
                                            elif Config.moving_tetromino_data[1] == 3:#0になる処理を行う
                                                for l in range(-1,3):#-1から2まで行う
                                                    if Config.tetromino_postion[self.height+l][self.j+1] != 0:
                                                        break_command = True
                                                        break
                                                Config.tetromino_postion[self.height][self.j] = 0
                                                Config.moving_tetromino_data[1] = 0
                                                Config.tetromino_postion[self.height-2][self.j+1] = Config.moving_tetromino_data
                                                Config.moving_tetromino_postion = [self.weight+1,self.height-2]
                                                #描画
                                                for k in range(4):
                                                    Config.main_window.blit(Config.lb_tetromino,[295+(self.weight+1)*20,100+(self.height-2+k)*20])
                                                break_command = True
                                                break 
                                                    
                                        if Config.moving_tetromino_data[0] == 1:
                                            if Config.moving_tetromino_data[1] == 0:
                                                pass
                                            elif Config.moving_tetromino_data[1] == 1:
                                                pass
                                            elif Config.moving_tetromino_data[1] == 2:
                                                pass
                                            elif Config.moving_tetromino_data[1] == 3:
                                                pass
                                        if Config.moving_tetromino_data[0] == 2:
                                            if Config.moving_tetromino_data[1] == 0:
                                                pass
                                            elif Config.moving_tetromino_data[1] == 1:
                                                pass
                                            elif Config.moving_tetromino_data[1] == 2:
                                                pass
                                            elif Config.moving_tetromino_data[1] == 3:
                                                pass
                                        if Config.moving_tetromino_data[0] == 3:
                                            if Config.moving_tetromino_data[1] == 0:
                                                pass
                                            elif Config.moving_tetromino_data[1] == 1:
                                                pass
                                            elif Config.moving_tetromino_data[1] == 2:
                                                pass
                                            elif Config.moving_tetromino_data[1] == 3:
                                                pass
                                        if Config.moving_tetromino_data[0] == 4:
                                            if Config.moving_tetromino_data[1] == 0:
                                                pass
                                            elif Config.moving_tetromino_data[1] == 1:
                                                pass
                                            elif Config.moving_tetromino_data[1] == 2:
                                                pass
                                            elif Config.moving_tetromino_data[1] == 3:
                                                pass
                                        if Config.moving_tetromino_data[0] == 5:
                                            if Config.moving_tetromino_data[1] == 0:
                                                pass
                                            elif Config.moving_tetromino_data[1] == 1:
                                                pass
                                            elif Config.moving_tetromino_data[1] == 2:
                                                pass
                                            elif Config.moving_tetromino_data[1] == 3:
                                                pass
                                        if Config.moving_tetromino_data[0] == 6:
                                            if Config.moving_tetromino_data[1] == 0:
                                                pass
                                            elif Config.moving_tetromino_data[1] == 1:
                                                pass
                                            elif Config.moving_tetromino_data[1] == 2:
                                                pass
                                            elif Config.moving_tetromino_data[1] == 3:
                                                pass
                                        
                                            
                else:
                    pass
                    
                
    def GameExit(self,):
        pygame.quit()
        Config.game_on = False
        window_for_error.destroy()
        sys.exit()
    def Settings_save(self,):
        pass

if __name__ == '__main__':
    Game = Main()