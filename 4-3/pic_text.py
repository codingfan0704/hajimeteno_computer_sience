import media

f = media.choose_file()
pic = media.load_picture(f)
media.add_text(pic, 115, 40, 'Medeleine', media.magenta)
media.show(pic)
