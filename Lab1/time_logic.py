totalseconds=int(input("Enter a large seconds:"))
hours=totalseconds // 3600
remainingseconds=totalseconds % 3600
minutes=remainingseconds // 60
seconds=remainingseconds % 60
print(totalseconds, "seconds is", hours, "hours,", minutes, "minutes, and", seconds, "seconds.")


