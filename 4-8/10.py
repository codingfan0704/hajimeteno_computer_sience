# -*- coding: utf-8 -*-

import media

pic = media.load_picture(media.choose_file())

for p in media.get_pixels(pic):
    new_red = int(2 * media.get_red(p))
    media.set_red(p, new_red)

media.show(pic)