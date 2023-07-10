def num_grid(lst):
    for i in range(5):
      for j in range(5):
        if lst[i][j] == "-":
          bomb = 0
          try:
            if lst[i][j+1] == "#" and i >= 0 and j+1 >=0:

              bomb +=1
          except:
            pass

          try:
            if lst[i][j-1] == "#" and i >= 0 and j-1 >=0:

              bomb +=1
          except:
            pass

          try:
            if lst[i+1][j] == "#"and i+1 >= 0 and j >=0:

              bomb +=1
          except:
            pass

          try:
            if lst[i-1][j] == "#" and i-1 >= 0 and j >=0:

              bomb +=1
          except:
            pass

          try:
            if lst[i-1][j-1] == "#" and i-1 >= 0 and j-1 >=0:

              bomb +=1
          except:
            pass

          try:
            if lst[i-1][j+1] == "#" and i-1 >= 0 and j+1 >=0:
              bomb +=1
          except:
            pass

          try:
            if lst[i+1][j-1] == "#" and i+1 >= 0 and j-1 >=0:
              bomb +=1
          except:
            pass

          try:
            if lst[i+1][j+1] == "#" and i+1 >= 0 and j+1 >=0:
              bomb +=1
          except:
            pass
          lst[i][j] = bomb
          bomb = 0
          
    for i in range(5):
      for j in range(5):
        if lst[i][j] == "-":
          lst[i][j] = 0
        if lst[i][j] != "-":
          lst[i][j] = str(lst[i][j])
    return lst
'''lst_input = [
    ["-","-","-","-","-"],
    ["-","-","-","-","-"],
    ["-","-","#","-","-"],
    ["-","-","-","-","-"],
    ["-","-","-","-","-"]
]'''
print("*** Minesweeper ***")
print("Enter input(5x5) : ",end="")
lst_input = []
input_list = input().split(",")
for e in input_list:
  lst_input.append([i for i in e.split()])
print("\n",*lst_input,sep = "\n")

print("\n",*num_grid(lst_input),sep = "\n")