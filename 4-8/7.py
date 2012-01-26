# -*- coding: utf-8 -*-

import media

pic = media.load_picture(media.choose_file())
media.show(pic)

for p in media.get_pixels(pic):
    media.set_red(p, 0)

media.show(pic)