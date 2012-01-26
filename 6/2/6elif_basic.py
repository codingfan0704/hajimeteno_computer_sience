#encoding: utf8
ph = float(raw_input())

if ph < 7.0:
    print "%sはさん性です。 "  %  (ph)

elif ph > 7.0:
    print "%sはアルカリ性です。" % (ph)