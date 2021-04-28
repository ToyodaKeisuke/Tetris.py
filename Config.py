# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 18:41:30 2021

@author: keisu
"""

game_on= False
game_start_screen_on = False
game_play_mode_serect_screen_on = False
game_play_endless = False
game_play_120_mode = False
#windowの縦横比(main_window)
HEIGHT,WIDTH = 400,300
GAME_START_BACK_SCREEAN_COLOR = '#669966'
GAME_PLAY_SERECT_MODE_BACK_SCREEAN_COLOR = '#669966'
GAME_PLAY_BACK_SCREEN = '#669966'
PXMF_B_PATH = r'Fonts\PixelMplus12-Bold.ttf'
PXMF_R_PATH = r'Fonts\PixelMplus12-Regular.ttf'
KREMLINSTAR_PXCEL_ART_PATH = r'Images/Kremlinstar/OriginalKremlinStar(400x300)PixelArt.png'
OUSPENSKI_CATHEDRAL_PATH = r'Images/OuspenskiCathedral/OuspenskiCathedral(400x300)PxcelArt.png'
TITLE_PATH = r'Images/Title/Tetris.png'
ICON_PATH = r'Images/Icon/Icon.png'
PLAY_PATH = r'Images/Play/Play.png'
DQ_FONT_PATH = r'Fonts\DragonQuestFCIntact.ttf'
CAUCASUSMOUNTAINS_PXCEL_ART_PATH = r'Images\CaucasusMountains\CaucasusMountains(800x600)PxcelArt.png'
BLOCK_1_PATH = r'Images\Blocks\Block1\Block1.png'
GREEN_TETROMINO_PATH = r'Images\Blocks\Tetrominos\GreenTetromino\GreenTetromino.png'
LIGHT_BULE_TETROMINO_PATH = r'Images\Blocks\Tetrominos\LightBuleTetromino\LightBuleTetromino.png'
BULE_TETROMINO_PATH = r'Images\Blocks\Tetrominos\BuleTetromino\BuleTetromino.png'
ORANGE_TETROMINO_PATH = r'Images\Blocks\Tetrominos\OrangeTetromino\OrangeTetromino.png'
PURPLE_TETROMINO_PATH = r'Images\Blocks\Tetrominos\PurpleTetrimino\PurpleTetrimino.png'
RED_TETROMINO_PATH = r'Images\Blocks\Tetrominos\RedTetromino\RedTetromino.png'
YELLOW_TETROMINO_PATH = r'Images\Blocks\Tetrominos\YellowTetromino\YellowTetromino.png'
arrow_flashing_display = False#スタート画面時に矢印が画面上に出ているか
flame_rate = 60
next_position = 0
position = None
#
pxmf_font_32b = None
pxmf_font_20b = None
pxmf_font_34b = None
pxmf_font_38b = None
dq_font_10 = None
dq_font_12 = None
dq_font_30 = None
sys_font_32 = None
sys_font_20 = None
sys_font_34 = None
sys_font_38 = None
main_window = None
playing_window = None
ICON = None
start_screen_bg = None
title = None
start_screen_play_text = None
start_screen_record_text = None
start_screen_settings_text = None
start_screen_arrow_text = None
play_mode_serect_bg = None
play_title = None
play_mode_serect_120_seconds_mode_text = None
play_mode_serect_endless_mode_text = None
play_mode_serect_return_text = None
play_mode_serect_arrow_text = None
play_mode = None
#
"""
tetromino_postion = [0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0,
                     0,0,0,0,0,0,0,0,0,0]
"""
tetromino_postion =  [[9,0,0,0,0,0,0,0,0,0,0,9],
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
playing_bg = None
block_1 = None
playing_continuous_combo_text = None
playing_all_score_text = None
playing_continuous_combo_value = 0
playing_all_score = 0
g_tetromino = None
lb_tetromino = None
r_tetromino = None
y_tetromino = None
p_tetromino = None
b_tetromino = None
o_tetromino = None
playing_next_tetromino_text = None
moving_tetromino_postion = [0,0]
moving_tetromino_color = None
moving_tetromino_data = None
moving_tetromino_index = 0