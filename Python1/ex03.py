print("*** Election ***")

election_array_round = int(input("Enter a number of voter(s) : "))
election_array = list(map(int, input("").split()))

counter = {}
max_frequency = 0

for num in election_array:
    if num >= 1 and num <= 20:
        counter[num] = counter.get(num, 0) + 1
        if counter[num] > max_frequency:
            max_frequency = counter[num]

winners = [num for num, frequency in counter.items() if frequency == max_frequency]

if winners:
    print(" ".join(map(str, winners[::-1])))
else:
    print("*** No Candidate Wins ***")
