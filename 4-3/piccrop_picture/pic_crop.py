#encoding: utf8

import media

f = media.choose_file()
pic = media.load_picture(f)

media.crop_picture(pic, 50, 50, 200, 200)
media.show(pic)
media.save_as(pic, 'pic207cropped.jpg')