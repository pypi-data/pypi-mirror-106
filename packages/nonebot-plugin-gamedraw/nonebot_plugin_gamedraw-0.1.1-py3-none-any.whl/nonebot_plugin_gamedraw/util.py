import os
import aiohttp
import aiofiles
from .config import DRAW_PATH, TTF
import pypinyin
from PIL import Image, ImageDraw, ImageFont
from asyncio.exceptions import TimeoutError
from aiohttp.client_exceptions import InvalidURL
from typing import List, Union, Set
import asyncio
from pathlib import Path
from .config import path_dict
import base64
from io import BytesIO
import nonebot
try:
    import ujson as json
except ModuleNotFoundError:
    import json


driver: nonebot.Driver = nonebot.get_driver()


header = {'User-Agent': "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)"}


async def download_img(url: str, path: str, name: str) -> bool:
    path = path.split('_')[0]
    codename = cn2py(name)
    # print(name)
    # if not _p.exists():
    #     _p.mkdir(parents=True, exist_ok=True)
    if not os.path.exists(DRAW_PATH + f'/{path}/{codename}.png'):
        try:
            async with aiohttp.ClientSession(headers=header) as session:
                async with session.get(url, timeout=7) as response:
                    async with aiofiles.open(DRAW_PATH + f'/{path}/{codename}.png', 'wb') as f:
                        await f.write(await response.read())
                        print(f'下载 {path_dict[path]} 图片成功，名称：{name}，url：{url}')
                        return True
        except TimeoutError:
            return False
        except InvalidURL:
            return False
    else:
        # logger.info(f'{path_dict[path]} 图片 {name} 已存在')
        return False


@driver.on_startup
def _check_dir():
    for dir_name in path_dict.keys():
        _p = Path(DRAW_PATH + dir_name)
        if not _p.exists():
            _p.mkdir(parents=True, exist_ok=True)


async def generate_img(card_set: Union[Set, List], game_name: str, star_list: list, color_role_star_list: list = None) -> str:
    # try:
    img_list = []
    color_list = []
    if color_role_star_list:
        SIX_LIST = color_role_star_list[0]
        FIVE_LIST = color_role_star_list[1]
        FOUR_LIST = color_role_star_list[2]
    for name in card_set:
        if game_name == 'prts':
            if name in SIX_LIST:
                color_list.append('#FFD700')
            elif name in FIVE_LIST:
                color_list.append('#DAA520')
            elif name in FOUR_LIST:
                color_list.append('#9370D8')
            else:
                color_list.append('white')
        pyname = cn2py(name)
        img_list.append(DRAW_PATH + f'/{game_name}/{pyname}.png')
    img_len = len(img_list)
    w = 100 * 10
    if img_len <= 10:
        w = 100 * img_len
        h = 100
    elif img_len % 10 == 0:
        h = 100 * int(img_len / 10)
    else:
        h = 100 * int(img_len / 10) + 100
    card_img = await asyncio.get_event_loop().run_in_executor(None, _pst, h, img_list, game_name, color_list)
    num = 0
    for n in star_list:
        num += n
    A = CreateImg(w, h)
    A.paste(card_img)
    return A.pic2bs4()


def _pst(h: int, img_list: list, game_name: str, color_list: list):
    card_img = CreateImg(100 * 10, h, 100, 100)
    idx = 0
    for img in img_list:
        try:
            if game_name == 'prts':
                bk = CreateImg(100, 100, color=color_list[idx])
                b = CreateImg(94, 94, background=img)
                bk.paste(b, (3, 3))
                b = bk
                idx += 1
            else:
                b = CreateImg(100, 100, background=img)
        except FileNotFoundError:
            b = CreateImg(100, 100, color='black')
        card_img.paste(b)
    return card_img


def init_star_rst(star_list: list, cnlist: list, max_star_list: list, max_star_olist: list) -> str:
    rst = ''
    for i in range(len(star_list)):
        if star_list[i]:
            rst += f'[{cnlist[i]}×{star_list[i]}] '
    rst += '\n'
    for i in range(len(max_star_list)):
        rst += f'第 {max_star_olist[i]+1} 抽获取 {max_star_list[i]}\n'
    return rst


def max_card(_dict: dict):
    # print(_dict)
    _max_value = max(_dict.values())
    _max_user = list(_dict.keys())[list(_dict.values()).index(_max_value)]
    return f'抽取到最多的是{_max_user}，共抽取了{_max_value}次'


def cn2py(word) -> str:
    temp = ""
    for i in pypinyin.pinyin(word, style=pypinyin.NORMAL):
        temp += ''.join(i)
    return temp


class CreateImg:
    def __init__(self,
                 w,
                 h,
                 img_w=0,
                 img_h=0,
                 color='white',
                 image_type='RGBA',
                 font_size=10,
                 background='',
                 ttf='yz.ttf',
                 divisor=1):
        self.w = int(w)
        self.h = int(h)
        self.img_w = int(img_w)
        self.img_h = int(img_h)
        self.current_w = 0
        self.current_h = 0
        self.ttfont = ImageFont.truetype(TTF, int(font_size))
        if not background:
            self.markImg = Image.new(image_type, (self.w, self.h), color)
        else:
            if w == 0 and h == 0:
                self.markImg = Image.open(background)
                w, h = self.markImg.size
                if divisor:
                    self.w = int(divisor * w)
                    self.h = int(divisor * h)
                    self.markImg = self.markImg.resize((self.w, self.h), Image.ANTIALIAS)
                else:
                    self.w = w
                    self.h = h
            else:
                self.markImg = Image.open(background).resize((self.w, self.h), Image.ANTIALIAS)
        self.draw = ImageDraw.Draw(self.markImg)
        self.size = self.w, self.h

    # 贴图
    def paste(self, img, pos=None, alpha=False):
        if isinstance(img, CreateImg):
            img = img.markImg
        if self.current_w == self.w:
            self.current_w = 0
            self.current_h += self.img_h
        if not pos:
            pos = (self.current_w, self.current_h)
        if alpha:
            try:
                self.markImg.paste(img, pos, img)
            except ValueError:
                img = img.convert("RGBA")
                self.markImg.paste(img, pos, img)
        else:
            self.markImg.paste(img, pos)
        self.current_w += self.img_w
        return self.markImg

    # 写字
    def text(self, pos, text, fill=(0, 0, 0)):
        self.draw.text(pos, text, fill=fill, font=self.ttfont)
        return self.markImg

    # 转bs4:
    def pic2bs4(self):
        buf = BytesIO()
        self.markImg.save(buf, format='PNG')
        base64_str = base64.b64encode(buf.getvalue()).decode()
        return 'base64://' + base64_str