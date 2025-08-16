class Solution(object):
    def subdomainVisits(self, c):
        hash_map = {}
        lists = []

        for i in c:
            count_str, domain = i.split(" ")
            count = int(count_str)
            subdomain = domain.split(".")

            for i in range(len(subdomain)):
                s = ".".join(subdomain[i:])
                hash_map[s] = hash_map.get(s, 0) + count

        for domain, count in hash_map.items():
            lists.append("{} {}".format(count, domain))

        return lists