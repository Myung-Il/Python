def fail(s):
    table=[0]*len(s)
    patten=0
    for s_idx in range(1,len(s)):
        while patten>0 and s[s_idx]!=s[patten]:
            patten=table[patten-1]

        if s[s_idx]==s[patten]:
            patten+=1
            table[s_idx]=patten

    print(*s)
    print(*table)
    print()

fail('abcababc')
fail('ababab')
fail('aaaa')
fail('abcbbacabcb')