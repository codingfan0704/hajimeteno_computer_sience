#encoding: utf8

def print_table():
    '''1から5までの掛け算九九の表を出力します。'''
    numbers = [1, 2, 3, 4, 5]
    
    for i in numbers:
        print '\t' + str(i),
        
    print # ヘッダ行を終了(改行)
        
        # 行番号と表の内容の出力
    for i in numbers:
        print i,
        for j in numbers:
            print '\t' + str(i * j),
        print #現在行を終了（改行）