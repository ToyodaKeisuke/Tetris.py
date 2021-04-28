# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 20:36:22 2021

@author: keisuke
"""

import pygame
import threading
from Tetris import *

class Main(Main):
    def __init__(self,):
        super().__init__()
        #pygame初期化
        pygame.init()
        #フォント
        try:#フォントの読み込みができなければ
            self.pxmf_font_32b = pygame.font.Font(self.PXMF_B_PATH,32)
            self.pxmf_font_20b = pygame.font.Font(self.PXMF_B_PATH,20)
            self.pxmf_font_34b = pygame.font.Font(self.PXMF_B_PATH,34)
            self.pxmf_font_38b = pygame.font.Font(self.PXMF_B_PATH,38)
        except:#pxmfフォントの代わりとしてpygameに備わっているフォントを使う(変数名はそのままにしないとプログラムを大幅に書き換えなければいけなくなる)
            self.pxmf_font_32b = pygame.font.SysFont(None,32)#システムフォント pygame.font.SysFont(name, size, bold=False, italic=False)
            self.pxmf_font_20b = pygame.font.SysFont(None,20)
            self.pxmf_font_34b = pygame.font.SysFont(None,34)
            self.pxmf_font_38b = pygame.font.SysFont(None,38)
        self.sys_font_32 = pygame.font.SysFont(None,32)
        self.sys_font_20 = pygame.font.SysFont(None,16)
        self.sys_font_34 = pygame.font.SysFont(None,34)
        self.sys_font_38 = pygame.font.SysFont(None,38)
        #メインウィンドウ作成
        self.main_window = pygame.display.set_mode((self.HEIGHT,self.WIDTH))
        #アイコン作成
        self.ICON = pygame.image.load(self.ICON_PATH)
        #ウィンドウのタイトルとタスクバーのアイコン
        pygame.display.set_caption("TETRIS",self.ICON_PATH)
        #ウィンドウのアイコン
        pygame.display.set_icon(self.ICON)
        self.arrow_position = 0
    def GameStartScreen(self,game_start_screen_is_first_time=None):#最初に描画する時以外は引数いらない
        #
        self.game_start_screen_is_first_time = game_start_screen_is_first_time
        if self.game_start_screen_is_first_time == 'first_time':
            #最初の画面
            self.main_window.fill(self.GAME_START_BACK_SCREEAN_COLOR)#緑の画面で塗りつぶし
            #背景を作成
            self.start_screen_bg = pygame.image.load(self.KREMLINSTAR_PXCEL_ART_PATH).convert_alpha()#convertするとfpsが3倍になるらしい
            #title作成
            self.title = pygame.image.load(self.TITLE_PATH).convert_alpha()
            #テキストオブジェクト作成
            #play作成
            # (テキスト, アンチエイリアス, カラー)を指定
            self.start_screen_play_text = self.pxmf_font_38b.render('Play',False,(255,255,255))
            #Record作成
            self.start_screen_record_text = self.pxmf_font_38b.render('Record',False,(255,255,255))
            #Settings作成
            self.start_screen_settings_text = self.pxmf_font_38b.render('Settings',False,(255,255,255))
            #矢印作成
            self.start_screen_arrow_text = self.pxmf_font_38b.render('▶',False,(255,255,255))#描画はしない
            ###描画###
            self.main_window.blit(self.start_screen_bg,(0,0))#貼り付け
            self.main_window.blit(self.title,(0,0))
            #bilt:第一引数=テキストオブジェクト(self.textのような)第二引数=座標
            self.main_window.blit(self.start_screen_play_text,[160,100])
            self.main_window.blit(self.start_screen_record_text,[140,150])
            self.main_window.blit(self.start_screen_settings_text,[120,200])
            ###メソッド初期化?###
            self.GameArrow()
        else:#最初に描画する時以外は
            ###描画###
            self.main_window.fill(self.GAME_START_BACK_SCREEAN_COLOR)#緑の画面で塗りつぶし
            self.main_window.blit(self.start_screen_bg,(0,0))#貼り付け
            self.main_window.blit(self.title,(0,0))
            #bilt:第一引数=テキストオブジェクト(self.textのような)第二引数=座標
            self.main_window.blit(self.start_screen_play_text,[160,100])
            self.main_window.blit(self.start_screen_record_text,[140,150])
            self.main_window.blit(self.start_screen_settings_text,[120,200])
    def GameArrow(self,arrow_flashing_display=False,position=None,on_display=None):
        #position
        #0 = Play 1 = Record 2 = Settings
        self.position = position
        self.arrow_flashing_display = arrow_flashing_display
        #display game_start_screen,game_play_mode_serect
        self.on_display = on_display
        #
        if self.position == None:#最初に初期化したときself.positionはNone
            self.position = 0
        else:
            if 0 <= self.position <= 2:#0から2までしかself.position(矢印)は移動できない(Play,Record,Settingsしか選択肢ないし...)
                pass
            else:
                if self.position < 0:
                    self.position += 1
                elif 2 < self.position:
                    self.position -= 1
                else:
                    error = VariableError()
                    error.Error('GameDraw.py/Main/GameArrow.position')
        if self.arrow_flashing_display == True:#もし矢印を出して良かったら
            if self.on_display == 'game_start_screen':#もしgame_start_screenを表示していたら
                if self.position == 0:
                    self.GameStartScreen()#矢印なしの画面を出して...
                    self.main_window.blit(self.start_screen_arrow_text,[125,100])#矢印を表示
                elif self.position == 1:
                    self.GameStartScreen()
                    self.main_window.blit(self.start_screen_arrow_text,[105,150])
                elif self.position == 2:
                    self.GameStartScreen()
                    self.main_window.blit(self.start_screen_arrow_text,[85,200])
            elif self.on_display == 'game_play_mode_serect':
                if self.position == 0:
                    self.GamePlayModeSerect()
                    self.main_window.blit(self.play_mode_serect_arrow_text,[35,100])
                elif self.position == 1:
                    self.GamePlayModeSerect()
                    self.main_window.blit(self.play_mode_serect_arrow_text,[75,150])
                elif self.position == 2:
                    self.GamePlayModeSerect()
                    self.main_window.blit(self.play_mode_serect_arrow_text,[105,200])
            else:
                pass
        else:
            pass
    def GamePlayModeSerect(self,is_game_play_mode_first_time=None):
        #
        #
        self.is_game_play_mode_first_time = is_game_play_mode_first_time
        if self.is_game_play_mode_first_time == 'first_time':
            #
            self.main_window.fill(self.GAME_START_BACK_SCREEAN_COLOR)#緑の画面で塗りつぶし
            #Playタイトル追加
            
            #背景追加
            self.play_mode_serect_bg = pygame.image.load(self.OUSPENSKI_CATHEDRAL_PATH).convert_alpha()#convertするとfpsが3倍になるらしい
            #テキスト追加
            #120秒モード
            self.play_mode_serect_120_seconds_mode_text = self.pxmf_font_38b.render('120SecondsMode',False,(255,255,255))
            #エンドレスモード
            self.play_mode_serect_endless_mode_text = self.pxmf_font_38b.render('EndlessMode',False,(255,255,255))
            #戻るtext
            self.play_mode_serect_return_text = self.pxmf_font_38b.render('Return',False,(255,255,255))
            #矢印作成
            self.play_mode_serect_arrow_text = self.pxmf_font_38b.render('▶',False,(255,255,255))#描画はしない
            #表示させる
            #
            self.main_window.blit(self.play_mode_serect_bg,[0,0])#背景表示
            #テキスト表示
            self.main_window.blit(self.play_mode_serect_120_seconds_mode_text,[70,100])#120秒モード
            self.main_window.blit(self.play_mode_serect_endless_mode_text,[110,150])#エンドレスモード
            self.main_window.blit(self.play_mode_serect_return_text,[140,200])#戻るtext
            ###メソッド初期化?###
            self.GameArrow()
            #
            self.th = threading.Thread(target=self.OneHundredTwentySeccondsTimer)
            self.th.start()
        else:
            #表示させる
            #
            self.main_window.blit(self.play_mode_serect_bg,[0,0])#背景表示
            #テキスト表示
            self.main_window.blit(self.play_mode_serect_120_seconds_mode_text,[70,100])#120秒モード
            self.main_window.blit(self.play_mode_serect_endless_mode_text,[110,150])#エンドレスモード
            self.main_window.blit(self.play_mode_serect_return_text,[140,200])#戻るtext
    def GameDrawVariableSharing(self,variables):
        #まずlocalできたvariablesを解凍
        #items()で辞書の中の変数の名前と、変数を取り出すため、forの代入する変数は二つ(変数名,値)
        for self.variable_name , self.value in variables:
            self.variable_name = self.variable_name[self.variable_name]#わざわざリストにすることで変数名に代入することができる
            self.variable_name[0] = self.value
        #localsでこのメソッド内にある変数名と内容を取得
        #items()で辞書の中の変数の名前と、変数を取り出すため、forの代入する変数は二つ(変数名,値)
        for self.variable_name , self.value in locals().items():
            if self.variable_name != 'self':#変数名がselfでなければ
                self.variable_name = [self.variable_name]#わざわざリストにすることで変数名に代入することができる
                self.variable_name[0] = self.value
    def OneHundredTwentySeccondsTimer(self,):
        pygame.time.delay(12000)#120秒タイマー
        if self.game_start_screen_on != True:
            pass
        else:
            print('a')
if __name__ == '__main__':
    pass