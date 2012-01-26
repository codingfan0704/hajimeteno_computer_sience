# -*- coding: utf-8 -*-

import media

pic = media.load_picture(media.choose_file())

for p in pic:
    c = media.get_color(p)
    c.r = c.g = c.b = (c.r + c.g + c.b) / 3
    media.set_color(p, c)

media.show(pic)