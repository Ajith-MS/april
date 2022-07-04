#
master_string="abbcddeghgggt"
chk_word="egg"
res=""
wc={}
for ch in master_string:
    if ch in wc:
        wc[ch]+=1
    else:
        wc[ch]=1

for ch in chk_word:
    if ch in wc:
        curcount=wc.get(ch)
        if curcount>0:
            res+=ch
            wc[ch]-=1
        else:
            break
print(res==chk_word)
