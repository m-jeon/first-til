# 미세먼지

dust = 111


if dust > 150:
    print('매우 나쁨')
elif dust > 80:  ## dust > 80 and dust <= 150:  #  80 <dust <= 150:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')
    print('밖으로~')