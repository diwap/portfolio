import timeago, datetime

print(
    timeago.format(datetime.date(2018, 3, 20), datetime.datetime.now())
)