print("*** Election ***")
election_array_round = int(input("Enter the number of voter(s): "))
election_sum = 0
election_array = list(map(int, input("").split()))

for i in range(len(election_array) - 1):
    if election_array[i] == election_array[i + 1]:
        election_sum += 0
    else:
        election_sum += 1

print(election_sum)