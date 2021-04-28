# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 20:36:22 2021

@author: keisuke
"""

import pygame
import threading
import Tetris
import Config

class Main(Tetris.Main):
    def __init__(self,):
        #super().__init__()
        #pygame初期化
        pygame.init()
        #フォント
        try:#フォントの読み込みができなければ
            Config.pxmf_font_32b = pygame.font.Font(Config.PXMF_B_PATH,32)
            Config.pxmf_font_20b = pygame.font.Font(Config.PXMF_B_PATH,20)
            Config.pxmf_font_34b = pygame.font.Font(Config.PXMF_B_PATH,34)
            Config.pxmf_font_38b = pygame.font.Font(Config.PXMF_B_PATH,38)
            Config.pxmf_font_34r = pygame.font.Font(Config.PXMF_R_PATH,34)
            Config.dq_font_30 = pygame.font.Font(Config.DQ_FONT_PATH,30)
            Config.dq_font_12 = pygame.font.Font(Config.DQ_FONT_PATH,12)
            Config.dq_font_10 = pygame.font.Font(Config.DQ_FONT_PATH,10)
        except:#pxmfフォントの代わりとしてpygameに備わっているフォントを使う(変数名はそのままにしないとプログラムを大幅に書き換えなければいけなくなる)
            Config.pxmf_font_32b = pygame.font.SysFont(None,32)#システムフォント pygame.font.SysFont(name, size, bold=False, italic=False)
            Config.pxmf_font_20b = pygame.font.SysFont(None,20)
            Config.pxmf_font_34b = pygame.font.SysFont(None,34)
            Config.pxmf_font_38b = pygame.font.SysFont(None,38)
            Config.pxmf_font_34r = pygame.font.SysFont(None,34)
            Config.dq_font_30 = pygame.font.SysFont(None,30)
            Config.dq_font_12 = pygame.font.SysFont(None,12)
            Config.dq_font_10 = pygame.font.SysFont(None,10)
        Config.sys_font_32 = pygame.font.SysFont(None,32)
        Config.sys_font_20 = pygame.font.SysFont(None,16)
        Config.sys_font_34 = pygame.font.SysFont(None,34)
        Config.sys_font_38 = pygame.font.SysFont(None,38)
        #メインウィンドウ作成
        Config.main_window = pygame.display.set_mode((Config.HEIGHT,Config.WIDTH))
        #アイコン作成
        Config.ICON = pygame.image.load(Config.ICON_PATH)
        #ウィンドウのタイトルとタスクバーのアイコン
        pygame.display.set_caption("TETRIS",Config.ICON_PATH)
        #ウィンドウのアイコン
        pygame.display.set_icon(Config.ICON)
        #Config.arrow_position = 0
    def GameStartScreen(self,is_game_start_screen_first_time=None):#最初に描画する時以外は引数いらない
        #
        self.is_game_start_screen_first_time = is_game_start_screen_first_time
        if self.is_game_start_screen_first_time == 'first_time':
            #最初の画面
            Config.main_window.fill(Config.GAME_START_BACK_SCREEAN_COLOR)#緑の画面で塗りつぶし
            #背景を作成
            Config.start_screen_bg = pygame.image.load(Config.KREMLINSTAR_PXCEL_ART_PATH).convert_alpha()#convertするとfpsが3倍になるらしい
            #title作成
            Config.title = pygame.image.load(Config.TITLE_PATH).convert_alpha()
            #テキストオブジェクト作成
            #play作成
            # (テキスト, アンチエイリアス, カラー)を指定
            Config.start_screen_play_text = Config.pxmf_font_38b.render('Play',False,(255,255,255))
            #Record作成
            Config.start_screen_record_text = Config.pxmf_font_38b.render('Record',False,(255,255,255))
            #Settings作成
            Config.start_screen_settings_text = Config.pxmf_font_38b.render('Settings',False,(255,255,255))
            #矢印作成
            Config.start_screen_arrow_text = Config.pxmf_font_38b.render('▶',False,(255,255,255))#描画はしない
            ###描画###
            Config.main_window.blit(Config.start_screen_bg,(0,0))#貼り付け
            Config.main_window.blit(Config.title,(0,0))
            #bilt:第一引数=テキストオブジェクト(self.textのような)第二引数=座標
            Config.main_window.blit(Config.start_screen_play_text,[160,100])
            Config.main_window.blit(Config.start_screen_record_text,[140,150])
            Config.main_window.blit(Config.start_screen_settings_text,[120,200])
            ###メソッド初期化###
            self.GameArrow(None)
        else:#最初に描画する時以外は
            ###描画###
            Config.main_window.fill(Config.GAME_START_BACK_SCREEAN_COLOR)#緑の画面で塗りつぶし
            Config.main_window.blit(Config.start_screen_bg,(0,0))#貼り付け
            Config.main_window.blit(Config.title,(0,0))
            #bilt:第一引数=テキストオブジェクト(self.textのような)第二引数=座標
            Config.main_window.blit(Config.start_screen_play_text,[160,100])
            Config.main_window.blit(Config.start_screen_record_text,[140,150])
            Config.main_window.blit(Config.start_screen_settings_text,[120,200])
    def GameArrow(self,is_initialize = 0):
        self.is_initialize = is_initialize
        #0 = Play 1 = Record 2 = Settings
        #
        if is_initialize == None:#最初に初期化したときConfig.is_initializenはNone
            Config.next_position = 0
            Config.position = Config.next_position
        else:
            if 0 <= Config.position <= 2:#0から2までしかConfig.position(矢印)は移動できない(Play,Record,Settingsしか選択肢ないし...)
                pass
            else:
                if Config.position < 0:
                    Config.position += 1
                elif 2 < Config.position:
                    Config.position -= 1
                else:
                    error = Tetris.VariableError()
                    error.Error('GameDraw.py/Main/GameArrow.position')
        if Config.game_start_screen_on:#もしgame_start_screenを表示していたら
            if Config.next_position == 0:
                Config.position = Config.next_position
                self.GameStartScreen()#矢印なしの画面を出して...
                Config.main_window.blit(Config.start_screen_arrow_text,[125,100])#矢印を表示
            elif Config.next_position == 1:
                Config.position = Config.next_position
                self.GameStartScreen()
                Config.main_window.blit(Config.start_screen_arrow_text,[105,150])
            elif Config.next_position == 2:
                Config.position = Config.next_position
                self.GameStartScreen()
                Config.main_window.blit(Config.start_screen_arrow_text,[85,200])
        elif Config.game_play_mode_serect_screen_on:
            if Config.next_position == 0:
                Config.position = Config.next_position
                self.GamePlayModeSerect()
                Config.main_window.blit(Config.play_mode_serect_arrow_text,[35,100])
            elif Config.next_position == 1:
                Config.position = Config.next_position
                self.GamePlayModeSerect()
                Config.main_window.blit(Config.play_mode_serect_arrow_text,[75,150])
            elif Config.next_position == 2:
                Config.position = Config.next_position
                self.GamePlayModeSerect()
                Config.main_window.blit(Config.play_mode_serect_arrow_text,[105,200])
        else:
            pass
    def GamePlayModeSerect(self,is_game_play_mode_first_time=None):
        #
        #
        self.is_game_play_mode_first_time = is_game_play_mode_first_time
        if self.is_game_play_mode_first_time == 'first_time':
            #
            Config.main_window.fill(Config.GAME_PLAY_SERECT_MODE_BACK_SCREEAN_COLOR)#緑の画面で塗りつぶし
            #Playタイトル追加
            Config.play_title = pygame.image.load(Config.PLAY_PATH).convert_alpha()
            #背景追加
            Config.play_mode_serect_bg = pygame.image.load(Config.OUSPENSKI_CATHEDRAL_PATH).convert_alpha()#convertするとfpsが3倍になるらしい
            #テキスト追加
            #120秒モード
            Config.play_mode_serect_120_seconds_mode_text = Config.pxmf_font_38b.render('120SecondsMode',False,(255,255,255))
            #エンドレスモード
            Config.play_mode_serect_endless_mode_text = Config.pxmf_font_38b.render('EndlessMode',False,(255,255,255))
            #戻るtext
            Config.play_mode_serect_return_text = Config.pxmf_font_38b.render('Return',False,(255,255,255))
            #矢印作成
            Config.play_mode_serect_arrow_text = Config.pxmf_font_38b.render('▶',False,(255,255,255))#描画はしない
            #表示させる
            #
            Config.main_window.blit(Config.play_mode_serect_bg,[0,0])#背景表示
            Config.main_window.blit(Config.play_title,[0,0])
            #テキスト表示
            Config.main_window.blit(Config.play_mode_serect_120_seconds_mode_text,[70,100])#120秒モード
            Config.main_window.blit(Config.play_mode_serect_endless_mode_text,[110,150])#エンドレスモード
            Config.main_window.blit(Config.play_mode_serect_return_text,[140,200])#戻るtext
            ###メソッド初期化###
            self.GameArrow(None)
            #
        else:
            #表示させる
            #
            Config.main_window.blit(Config.play_mode_serect_bg,[0,0])#背景表示
            Config.main_window.blit(Config.play_title,[0,0])
            #テキスト表示
            Config.main_window.blit(Config.play_mode_serect_120_seconds_mode_text,[70,100])#120秒モード
            Config.main_window.blit(Config.play_mode_serect_endless_mode_text,[110,150])#エンドレスモード
            Config.main_window.blit(Config.play_mode_serect_return_text,[140,200])#戻るtext
    def GamePlayScreen(self,play_mode,is_game_play_screen_first_time=None):
        Config.play_mode = play_mode
        #
        #playmode = '120secconds','endless'
        #
        self.is_game_play_screen_first_time = is_game_play_screen_first_time
        if self.is_game_play_screen_first_time == 'first_time':
            if Config.play_mode == '120secconds':
                #
                self.th = threading.Thread(target=self.OneHundredTwentySeccondsTimer,daemon=True)
                self.th.start()
                #
                Config.game_on= True
                Config.game_start_screen_on = False
                Config.game_play_mode_serect_screen_on = False
                Config.game_play_endless = False
                Config.game_play_120_mode = True
            elif Config.play_mode == 'endless':
                Config.game_on= True
                Config.game_start_screen_on = False
                Config.game_play_mode_serect_screen_on = False
                Config.game_play_120_mode = False
                Config.game_play_endless = True
            else:
                error = Tetris.VariableError()
                error.Error('GameDraw.py/Main/GameArrow.play_mode')
            ###テトリミノの位置を初期化
            Config.tetromino_postion =  [[9,[0,0],0,0,0,0,0,0,0,0,0,9],
                                         [9,0,0,0,0,0,0,0,0,0,0,9],
                                         [9,0,0,0,0,0,0,0,0,0,0,9],
                                         [9,0,0,0,0,0,0,0,0,0,0,9],
                                         [9,0,0,0,0,0,0,0,0,0,0,9],
                                         [9,0,0,0,0,0,0,0,0,0,0,9],
                                         [9,0,0,0,0,0,0,0,0,0,0,9],
                                         [9,0,0,0,0,0,0,0,0,0,0,9],
                                         [9,0,0,0,0,0,0,0,0,0,0,9],
                                         [9,0,0,0,0,0,0,0,0,0,0,9],
                                         [9,0,0,0,0,0,0,0,0,0,0,9],
                                         [9,0,0,0,0,0,0,0,0,0,0,9],
                                         [9,0,0,0,0,0,0,0,0,0,0,9],
                                         [9,0,0,0,0,0,0,0,0,0,0,9],
                                         [9,0,0,0,0,0,0,0,0,0,0,9],
                                         [9,0,0,0,0,0,0,0,0,0,0,9],
                                         [9,0,0,0,0,0,0,0,0,0,0,9],
                                         [9,0,0,0,0,0,0,0,0,0,0,9],
                                         [9,0,0,0,0,0,0,0,0,0,0,9],
                                         [9,0,0,0,0,0,0,0,0,0,0,9],
                                         [9,0,0,0,0,0,0,0,0,0,0,9],
                                         [9,9,9,9,9,9,9,9,9,9,9,9]]
            #Iミノ=0,0ミノ=1,Tミノ=2,Jミノ=3,Lミノ=4,Sミノ=5,Zミノ=6
            #
            ###メソッド初期化###
            self.GameArrow(None)
            #
            #pygame.display.iconify()#window最小化,戻すにはpygame.display.get_active()
            Config.playing_window = pygame.display.set_mode((Config.HEIGHT*2,Config.WIDTH*2))
            #写真追加
            Config.playing_bg = pygame.image.load(Config.CAUCASUSMOUNTAINS_PXCEL_ART_PATH).convert_alpha()
            #ブロック1
            Config.block_1 = pygame.image.load(Config.BLOCK_1_PATH).convert_alpha()
            #テトロミノ
            #緑テトリミノ
            Config.g_tetromino = pygame.image.load(Config.GREEN_TETROMINO_PATH).convert_alpha()
            #水色
            Config.lb_tetromino = pygame.image.load(Config.LIGHT_BULE_TETROMINO_PATH).convert_alpha()
            #赤
            Config.r_tetromino = pygame.image.load(Config.RED_TETROMINO_PATH).convert_alpha()
            #黄
            Config.y_tetromino = pygame.image.load(Config.YELLOW_TETROMINO_PATH).convert_alpha()
            #紫
            Config.p_tetromino = pygame.image.load(Config.PURPLE_TETROMINO_PATH).convert_alpha()
            #青
            Config.b_tetromino = pygame.image.load(Config.BULE_TETROMINO_PATH).convert_alpha()
            #オレンジ
            Config.o_tetromino = pygame.image.load(Config.ORANGE_TETROMINO_PATH).convert_alpha()
            #スコアテキスト
            Config.playing_all_score_text = Config.pxmf_font_34r.render('ALL SCORE:00000',False,(255,255,255))#すべて
            Config.playing_continuous_combo_text = Config.pxmf_font_34r.render('NUNBER OF CONTINUOUS COMBO:00000',False,(255,255,255))#連続コンボ数
            #NEXT TETROMINO表示
            Config.playing_next_tetromino_text = Config.pxmf_font_34r.render('NEXT TETROMINO',False,(255,255,255))
            #画面表示
            Config.main_window.blit(Config.playing_bg,[0,0])
            for i in range(12):#ブロック表示(テトリミノ表示の枠)
                Config.main_window.blit(Config.block_1,[275+i*20,80])
            for i in range(20):
                Config.main_window.blit(Config.block_1,[275,100+i*20])
            for i in range(12):
                Config.main_window.blit(Config.block_1,[275+i*20,500])
            for i in range(20):
                Config.main_window.blit(Config.block_1,[495,100+i*20])
            for i in range(4):
                Config.main_window.blit(Config.block_1,[195+i*20,80])
            for i in range(4):
                Config.main_window.blit(Config.block_1,[195,100+i*20])
            for i in range(4):
                Config.main_window.blit(Config.block_1,[195+i*20,180])
            for i in range(5):
                Config.main_window.blit(Config.block_1,[600+i*20,80])
            for i in range(15):
               Config.main_window.blit(Config.block_1,[600,100+i*20])
            for i in range(15):
                Config.main_window.blit(Config.block_1,[680,100+i*20])
            for i in range(3):
                Config.main_window.blit(Config.block_1,[620+i*20,180])
            for i in range(3):
                Config.main_window.blit(Config.block_1,[620+i*20,280])
            for i in range(3):
                Config.main_window.blit(Config.block_1,[620+i*20,380])
            Config.main_window.blit(Config.playing_continuous_combo_text,[0,0])#テキスト表示
            Config.main_window.blit(Config.playing_all_score_text,[0,35])
            Config.main_window.blit(Config.playing_next_tetromino_text,[540,35])
            #
            #Config.main_window.blit(Config.o_tetromino,[295,100])
            Config.moving_tetromino_postion = [0,0]#[weight,height]
        else:
            #画面表示
            Config.main_window.blit(Config.playing_bg,[0,0])
            for i in range(12):#ブロック表示(テトリミノ表示の枠)
                Config.main_window.blit(Config.block_1,[275+i*20,80])
            for i in range(20):
                Config.main_window.blit(Config.block_1,[275,100+i*20])
            for i in range(12):
                Config.main_window.blit(Config.block_1,[275+i*20,500])
            for i in range(20):
                Config.main_window.blit(Config.block_1,[495,100+i*20])
            for i in range(4):
                Config.main_window.blit(Config.block_1,[195+i*20,80])
            for i in range(4):
                Config.main_window.blit(Config.block_1,[195,100+i*20])
            for i in range(4):
                Config.main_window.blit(Config.block_1,[195+i*20,180])
            for i in range(5):
                Config.main_window.blit(Config.block_1,[600+i*20,80])
            for i in range(15):
               Config.main_window.blit(Config.block_1,[600,100+i*20])
            for i in range(15):
                Config.main_window.blit(Config.block_1,[680,100+i*20])
            for i in range(3):
                Config.main_window.blit(Config.block_1,[620+i*20,180])
            for i in range(3):
                Config.main_window.blit(Config.block_1,[620+i*20,280])
            for i in range(3):
                Config.main_window.blit(Config.block_1,[620+i*20,380])
            Config.main_window.blit(Config.playing_continuous_combo_text,[0,0])#テキスト表示
            Config.main_window.blit(Config.playing_all_score_text,[0,35])
            Config.main_window.blit(Config.playing_next_tetromino_text,[540,35])
    def OneHundredTwentySeccondsTimer(self,):
        pygame.time.delay(120000)#120秒タイマー
if __name__ == '__main__':
    pass