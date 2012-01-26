#encoding: utf8

''' 温度を操作する関数を集めてあります。 '''

def to_celsius(t):
    ''' 華氏から摂氏に変換します '''
    
    return round((t - 32.0) * 5.0 / 9.0)

def above_freezing(t):
    ''' 摂氏表現の温度が氷点下以上だったらTrue、そうでなければFalseをかえします。 '''
    return t > 0