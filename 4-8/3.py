# -*- coding: utf-8 -*-

oomoji = 'boolean'.upper()#小文字を大文字に変換

shutugen = 'C02 H2o'.find("2")#２の最初の位置

shutugen2 = 'C02 H2o'.find("2", 3)#2の2番目野市

sentou = "Boolean"[0].islower()#先頭は小文字か

if sentou == False:
    sentou = "いいえ、大文字です。"
else:
    sentou = "はい、小文字です。"

henkan = "MoNDaY".lower().capitalize()#小文字にして、先頭を大文字にする。

kuhaku = " Monday".strip()



print "大文字変換すると%sです。"  %oomoji

print "最初に２がある場所は%s文字目です。" % (1 + shutugen) 

print "2番目に２がある場所は%s番文字目です。" % (1 + shutugen2) 

print "先頭文字は小文字か？%s" % sentou

print "すべて小文字にして、先頭だけ大文字にしました。%s" % henkan

print "空白削除%s" % kuhaku