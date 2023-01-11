class Solution:
    from collections import Counter
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = []
        count = Counter()
        
        for cpdom in cpdomains:
            num, dom = cpdom.split()
            num, dom = int(num), dom.split('.')
            
            for i in reversed(range(len(dom))):
                count['.'.join(dom[i:])] += num
                print(count)
                
        return [str(amount) + ' ' + domain for domain, amount in count.items()]