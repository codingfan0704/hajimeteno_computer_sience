# -*- coding: utf-8 -*-

import calendar

start = 2000
end = 2050

uruudosi = calendar.leapdays(start, end) #閏年が何回あるか
youbi = calendar.weekday(2016, 7, 29)

if youbi == 0:
    youbi = "月"
elif youbi == 1:
    youbi = "火"
elif youbi == 2:
    youbi = "水"
elif youbi == 3:
    youbi = "木"
elif youbi == 4:
    youbi = "金"
elif youbi == 5:
    youbi = "土"
elif youbi == 6:
    youbi = "日"
else:
    youbi = "エラーです。"
 

print "%s年から%s年までの閏年は全部で %s回です。"  % (start, end, uruudosi)

print "%s曜日です." % youbi