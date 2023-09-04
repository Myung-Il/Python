import heapq
from sys import stdin
input=stdin.readline

def dijkstra(graph, start):
    st_dis={node:float('inf')for node in graph}
    st_dis[start]=0
    qu=[]
    heapq.heappush(qu,[st_dis[start],start])

    while qu:
        dis,exp_node=heapq.heappop(qu)

        if st_dis[exp_node]<dis:
            continue

        for new_exp_node, new_dis in graph[exp_node].items():
            sum_dis=new_dis+dis
            if sum_dis<st_dis[new_exp_node]:
                st_dis[new_exp_node]=sum_dis
                heapq.heappush(qu,[sum_dis,new_exp_node])
    return st_dis



n,line=map(int,input().split())
start=int(input())
rt={i:{} for i in range(1,n+1)}

for _ in range(line):
    go,arrival,cost=map(int,input().split())
    if arrival in rt[go]:
        rt[go][arrival]=min(rt[go][arrival],cost)
    else:
        rt[go][arrival]=cost

for v in dijkstra(rt,start).values():
    print(v if v!=float('inf')else 'INF')