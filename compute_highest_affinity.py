import operator


class HighestWebPagesAffinity:
    def highest_affinity(self, site_list, user_list, time_list):
        user_set = set(user_list)
        data_dict = {}
        for i in range(len(site_list)):
            p = site_list[i]
            for j in range(1, len(site_list)):
                q = site_list[j]
                if p is not q:
                    if (p, q) not in data_dict and (q, p) not in data_dict:
                        count_of_users_for_pair = 0
                        for user in user_set:
                            indices = [i for i, x in enumerate(user_list) if x == user]
                            a = [site_list[i] for i in indices]
                            if p in a and q in a:
                                count_of_users_for_pair += 1
                                data_dict.__setitem__((p, q), count_of_users_for_pair)
        return max(data_dict.items(), key=operator.itemgetter(1))[0]


if __name__ == '__main__':
    highestWebPagesAffinity = HighestWebPagesAffinity()
    site_list = ["a.com", "b.com", "a.com", "b.com", "a.com", "c.com"]
    user_list = ["andy", "andy", "bob", "bob", "charlie", "charlie"]
    time_list = [1238972321, 1238972456, 1238972618, 1238972899, 1248472489, 1258861829]
    output = highestWebPagesAffinity.highest_affinity(site_list, user_list, time_list)
    print(output)
