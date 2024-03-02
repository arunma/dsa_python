import itertools
from collections import defaultdict, Counter
from typing import List


class AnalyzeUserWebsiteVisitPattern:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        graph = defaultdict(list)
        for user, time, web in sorted(zip(username, timestamp, website)):
            graph[user].append(web)

        print(graph)

        # print(graph)
        counter = Counter()
        for u, routes in graph.items():
            for pattern in set(itertools.combinations(routes, 3)):
                counter[pattern] += 1

        print(counter)

        top_pattern = None
        top_count = 0
        for pattern, count in counter.items():
            if count > top_count:
                top_pattern = pattern
                top_count = count
            elif top_count == count and top_pattern > pattern:
                top_pattern = pattern
            # print(f"top pattern: {top_pattern}, top_count: {top_count}")
        return top_pattern

    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        graph = defaultdict(list)
        for u, t, w in sorted(zip(username, timestamp, website)):
            graph[u].append(w)

        print(graph)
        counter = Counter()
        for u, routes in graph.items():
            for triple in set(itertools.combinations(routes, 3)):
                counter[triple] += 1

        print(counter)

        max_patt, max_count = None, 0
        for pat, count in counter.items():
            if count > max_count:
                max_patt = pat
                max_count = count
            elif count == max_count and max_patt > pat:
                max_patt = pat

        return max_patt

    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        graph = defaultdict(list)
        for u, t, w in sorted(zip(username, timestamp, website)):
            graph[u].append(w)

        counter = Counter()

        for user, usage in graph.items():
            for patt in set(itertools.combinations(usage, 3)):
                counter[patt] += 1

        max_patt = ""
        max_count = 0
        for pat, count in counter.items():
            if count > max_count:
                max_patt = pat
        return max_patt


if __name__ == "__main__":
    init = AnalyzeUserWebsiteVisitPattern()
    print(init.mostVisitedPattern(username=["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"],
                                  timestamp=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                                  website=["home", "about", "career", "home", "cart", "maps", "home", "home", "about",
                                           "career"]))  # ["home","about","career"]

    # print(init.mostVisitedPattern(["ua", "ua", "ua", "ub", "ub", "ub"],
    #                               [1, 2, 3, 4, 5, 6],
    #                               ["a", "b", "a", "a", "b", "c"]))  # ["a","b","a"]
    # print(init.mostVisitedPattern(["dowg", "dowg", "dowg"],
    #                               [158931262, 562600350, 148438945],
    #                               ["y", "loedo", "y"]))  # ["y","y","loedo"]
    print(init.mostVisitedPattern(["h", "eiy", "cq", "h", "cq", "txldsscx", "cq", "txldsscx", "h", "cq", "cq"],
                                  [527896567, 334462937, 517687281, 134127993, 859112386, 159548699, 51100299, 444082139, 926837079, 317455832,
                                   411747930],
                                  ["hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi", "hibympufi",
                                   "yljmntrclw", "hibympufi", "yljmntrclw"]))  # ["hibympufi","hibympufi","yljmntrclw"]
