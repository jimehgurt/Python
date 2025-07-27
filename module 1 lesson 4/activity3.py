math = int(input("whats your marks in math"))
english = int(input("whats your marks in english"))
urdu = int(input("whats your marks in urdu"))
history = int(input("whats your marks in history"))
sum = math+english+urdu+history
perc = (sum/400)*100
round_figure = round (perc, 2)
print (round_figure)