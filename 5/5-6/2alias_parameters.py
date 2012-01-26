#encoding: utf8

def sort_and_reverse(L):
    '''ソートして逆順にしたリストを返します。'''
    L.sort()
    L.reverse()
    return L

celegans_markers = ['Emb', 'Him', 'Unc', 'lon', 'Dpy', 'Lvl']
print celegans_markers

print 'sort_and_reverse(celegans_markers)'
print sort_and_reverse(celegans_markers[:])

print '\n'
print 'celegans_markers'
print celegans_markers
