from compute_highest_affinity import HighestWebPagesAffinity

a = "a"
b = "b"
c = "c"
d = "d"
e = "e"
f = "f"
g = "g"
h = "h"

A = "A"
B = "B"
C = "C"
D = "D"
E = "E"
F = "F"
G = "G"
H = "H"


site_list = [a,a,a,a,b,b,b,b,c,c,c,d,d,d,d,d]
user_list = [B,D,E,F,A,B,C,F,B,D,E,A,B,C,D,F]

time_list = range(0,16)

highestWebPagesAffinity = HighestWebPagesAffinity()
computed_result = highestWebPagesAffinity.highest_affinity(site_list, user_list, time_list)
expected_result = (b, d)

assert computed_result == expected_result

print("Successfully passed test4!")
