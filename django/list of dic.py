results = [
    {"district":"tvm","win": 98, "A+": 45000},
    {"district":"ktm","win": 95, "A+": 44000},
    {"district":"apy","win": 97, "A+": 47000},
    {"district":"idk","win": 90, "A+": 38000},
    {"district":"ekm","win": 99, "A+": 56000},
    {"district":"pta","win": 99, "A+": 58000},
    {"district":"tsr","win": 98, "A+": 57000},
    {"district":"kzd","win": 99, "A+": 58000},
    {"district":"pkd","win" :95, "A+": 50000},
    {"district":"mpm","win": 90, "A+": 4500},

]

# win % of tvm
tvm_win=[res for res in results if res["district"]=='tvm']
print("win % of tvm=",tvm_win)

#district with highest win %
print("Highest win %=",max(results,key=lambda res:res["win"]))

#district with lowest win%
print("Lowest win %=",min(results,key=lambda res:res["win"]))

#district with highest A+
print("District with highest A+=",max(results,key=lambda re:re["A+"]))

#district with lowest A+
print("District with lowest A+=",min(results,key=lambda  res:res["A+"]))

#Total number of A+
print("Total number of A+=",sum([res["A+"] for res in results]))

#Total win %
print("Total win % =",sum([res["win"] for res in results]))

#sort districts wrt win %
results.sort(key=lambda res:res["win"],reverse=True)
print(results)