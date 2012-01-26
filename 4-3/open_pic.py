#encoding: utf8

import media

f = media.choose_file()
pic = media.load_picture(f)
media.show(pic)

w = pic.get_width()
h = pic.get_height()
t = pic.title

print(w)
print(h)
print(t)
