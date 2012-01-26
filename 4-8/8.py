# -*- coding: utf-8 -*-

import media

pic = media.load_picture(media.choose_file())
media.show(pic)

for p in media.get_pixels(pic):
    new_green = int(0.5 * media.get_green(p))
    media.set_green(p, new_green)

media.show(pic)