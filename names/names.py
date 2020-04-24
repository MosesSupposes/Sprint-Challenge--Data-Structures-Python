import time
from bst import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# -------------- Time complexity: O(n^2) -----------------

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

bst = BinarySearchTree("a")
names_1.sort()
# first_tenth = names_1[0:1000]
# second_tenth = names_1[1000:2000]
# third_tenth = names_1[2000:3000]
# fourth_tenth = names_1[3000:4000]
# fifth_tenth = names_1[4000:5000]
# sixth_tenth = names_1[5000:6000]
# seventh_tenth = names_1[6000:7000]
# eighth_tenth = names_1[7000:8000]
# ninth_tenth = names_1[8000:9000]
# tenth_tenth = names_1[9000:10001]
# first_twentieth = names_1[0:500]
# second_twentieth = names_1[500:1000]
# third_twentieth = names_1[1000:1500]
# fourth_twentieth = names_1[1500:2000]
# fifth_twentieth = names_1[2000:2500]
# sixth_twentieth = names_1[2500:3000]
# seventh_twentieth = names_1[3000:3500]
# eighth_twentieth = names_1[3500:4000]
# ninth_twentieth = names_1[4000:4500]
# tenth_twentieth = names_1[4500:5000]
# eleventh_twentieth = names_1[5000:5500]
# twelveth_twentieth = names_1[5500:6000]
# thirteenth_twentieth = names_1[6000:6500]
# fourteenth_twentieth = names_1[6500:7000]
# fifteenth_twentieth = names_1[7000:7500]
# sixteenth_twentieth = names_1[7500:8000]
# seventeenth_twentieth = names_1[8000:8500]
# eighteenth_twentieth = names_1[8500:9000]
# nineteenth_twentieth = names_1[9000:9500]
# twentieth_twentieth = names_1[9500:10001]
# first_fourtieth = names_1[0:250]
# second_fourtieth = names_1[250:500]
# third_fourtieth = names_1[500:750]
# fourth_fourtieth = names_1[750:1000]
# fifth_fourtieth = names_1[1000:1250]
# sixth_fourtieth = names_1[1250:1500]
# seventh_fourtieth = names_1[1500:1750]
# eighth_fourtieth = names_1[1750: 2000]
# ninth_fourtieth = names_1[2000:2250]
# tenth_fourtieth = names_1[2250:2500]
# eleventh_fourtieth = names_1[2500:2750]
# twelveth_fourtieth = names_1[2750:3000]
# thirteenth_fourtieth = names_1[3000:3250]
# fourteenth_fourtieth = names_1[3250:3500]
# fifteenth_fourtieth = names_1[3500:3750]
# sixteenth_fourtieth = names_1[3750:4000]
# seventeenth_fourtieth = names_1[4000:4250]
# eighteenth_fourtieth = names_1[4250:4500]
# nineteenth_fourtieth = names_1[4500:4750]
# twentieth_fourtieth = names_1[4750:5000]
# twenty_first_fourtieth = names_1[5000:5250]
# twenty_second_fourtieth = names_1[5250:5500]
# twenty_third_fourtieth = names_1[5500:5750]
# twenty_fourth_fourtieth = names_1[5750:6000]
# twenty_fifth_fourtieth = names_1[6000:6250]
# twenty_sixth_fourtieth = names_1[6250:6500]
# twenty_seventh_fourtieth = names_1[6500:6750]
# twenty_eighth_fourtieth = names_1[6750:7000]
# twenty_ninth_fourtieth = names_1[7000:7250]
# thirtieth_fourtieth = names_1[7250:7500]
# thirty_first_fourtieth = names_1[7500:7750]
# thirty_second_fourtieth = names_1[7750:8000]
# thirty_third_fourtieth = names_1[8000:8250]
# thirty_fourth_fourtieth = names_1[8250:8500]
# thirty_fifth_fourtieth = names_1[8500:8750]
# thirty_sixth_fourtieth = names_1[8750:9000]
# thirty_seventh_fourtieth = names_1[9000:9250]
# thirty_eighth_fourtieth = names_1[9250:9500]
# thirty_ninth_fourtieth = names_1[9500:9750]
# fourtieth_fourtieth = names_1[9750:10001]

# all_names = [
#     first_fourtieth, second_fourtieth, third_fourtieth, fourteenth_fourtieth,
#     fifth_fourtieth, sixth_fourtieth, seventh_fourtieth, eighth_fourtieth, ninth_fourtieth, 
#     tenth_fourtieth, eleventh_fourtieth, twelveth_fourtieth, thirteenth_fourtieth, 
#     fourteenth_fourtieth, fifteenth_fourtieth, sixteenth_fourtieth, seventeenth_fourtieth,
#     eighteenth_fourtieth, nineteenth_fourtieth, twentieth_fourtieth, twenty_first_fourtieth,
#     twenty_second_fourtieth, twenty_third_fourtieth, twenty_fourth_fourtieth, twenty_fifth_fourtieth,
#     twenty_sixth_fourtieth, twenty_seventh_fourtieth, twenty_eighth_fourtieth, twenty_ninth_fourtieth,
#     thirtieth_fourtieth, thirty_first_fourtieth, thirty_second_fourtieth, thirty_third_fourtieth,
#     thirty_fourth_fourtieth, thirty_fifth_fourtieth, thirty_sixth_fourtieth, thirty_seventh_fourtieth,
#     thirty_eighth_fourtieth, thirty_ninth_fourtieth, fourtieth_fourtieth 
# ]

# for names in all_names:
#     for name in names:
#         bst.insert(name)

for name in names_1:
    bst.iterative_insert(name)


for name in names_2:
    if bst.iterative_contains(name):
        duplicates.append(name)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
