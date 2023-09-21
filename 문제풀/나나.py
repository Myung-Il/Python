import heapq as h,sys
input=lambda:sys.stdin.readline().rstrip()
inf=float('inf')

def dik(start):
    q = []
    h.heappush(q,[0, start])
    dis_l[start] = 0
    while q:
        dis,exp_node=h.heappop(q)
        if dis_l[exp_node]<dis:
            continue
        for n_exp_node,n_dis in graph[exp_node]:
            dis_plus=dis+n_dis
            if dis_plus<dis_l[n_exp_node]:
                dis_l[n_exp_node]=dis_plus
                h.heappush(q,[dis_plus,n_exp_node])


n,m,g=map(int,input().split())
graph = [[]for _ in range(n+1)]
for _ in range(m):
    a,b,w=map(int,input().split())
    graph[a].append([b,w])

dis_l = [inf]*(n+1)
dik(g)

ans=dis_l[:]
dis_l = [inf]*(n+1)
for node in range(1,n+1):
    if node!=g:
        dik(node)
        ans[node]+=dis_l[g]
        dis_l = [inf]*(n+1)

print(max(ans[1:]))