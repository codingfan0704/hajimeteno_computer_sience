#encoding: utf8

velocities = [0.0, 9.81, 19.62, 29.43]

for v in velocities:
    print "メートル法：", v, "m/秒",
    print "ヤードポンド法：", v * 3.28, "ft/秒"