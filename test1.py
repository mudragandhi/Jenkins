from compute_highest_affinity import HighestWebPagesAffinity

site_list = ["a.com", "b.com", "a.com", "b.com", "a.com", "c.com"]
user_list = ["andy", "andy", "bob", "bob", "charlie", "charlie"]
time_list = [1238972321, 1238972456, 1238972618, 1238972899, 1248472489, 1258861829] 

highestWebPageAffinity = HighestWebPagesAffinity()
computed_result = highestWebPageAffinity.highest_affinity(site_list, user_list, time_list)
expected_result = ('a.com', 'b.com')

assert computed_result == expected_result
print("Successfully passed test1!")