import randomized_input
from compute_highest_affinity import HighestWebPagesAffinity

num_lines = 10000
num_users = 1000

site_list = randomized_input.randomized_site_list(num_lines)
user_list = randomized_input.randomized_user_list(num_lines, num_users)
time_list = range(0,num_lines)

highestWebPagesAffinity = HighestWebPagesAffinity()
computed_result = highestWebPagesAffinity.highest_affinity(site_list, user_list, time_list)
expected_result = ('facebook', 'google')

assert computed_result == expected_result
print("Successfully passed test2!")