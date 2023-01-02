class Solution:
    import collections
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
#         winner = []
#         loser = []
#         allWin = []
#         both = []
#         oneLose = []
#         for i in range(len(matches)):
#             winner.append(matches[i][0])
#             loser.append(matches[i][1])
#         winner = list(dict.fromkeys(winner))
#         print(winner)
#         print(loser)
#         for i in winner:
#             if i not in loser:
#                 allWin.append(i)
#         allWin = sorted(allWin)
#         c = Counter(loser)

#         for i in c:
#             if c[i] == 1:
#                 oneLose.append(i)
#         oneLose = sorted(oneLose)
#         both.append(allWin)
#         both.append(oneLose)

#         return both

        
        loser = collections.defaultdict(int)
        players = set()
        
        for a, b in matches:
            loser[b] += 1
            players.add(a)
            players.add(b)
        print(players)
        # for i in range(2):
        #     for x in sorted(players):
        #         if loser[x] == i:
                    # return [[x]]
        return [[x for x in sorted(players) if loser[x] == i] for i in range(2)]
    
    
    