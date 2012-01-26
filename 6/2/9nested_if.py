#encoding: utf8

input = raw_input()

if len(input) > 0:
    ph = float(input)
    if ph < 7.0:
            print "%sはさん性です。"  %  (ph)
    elif ph > 7.0:
            print "%sはアルカリ性です。" % (ph)
    else:
            print "%sは中性です。" % (ph)
else:
    print "pH値が与えられていません。!"