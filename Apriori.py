import apyori 
transactions = [ 
['Milk', 'Bread', 'Saffron'], 
['Milk', 'Saffron'], 
['Bread', 'Saffron', 'Water'], 
['Bread','Water'] 
] 
rules = list(apyori.apriori(transactions, min_support = 0.5, min_confidence = 0.5))
for i in range(len(rules)): 
    LHS = list(rules[i][2][0][0]) 
    RHS = list(rules[i][2][0][1]) 
    support = rules [i][1] 
    confidence = rules [i][2][0][3] 
    lift = rules[i][2][0][3] 
    print("LHS:",LHS,"--","RHS:",RHS) 
    print("Support:",support) 
    print("Confidence:",confidence) 
    print("Lift:",lift) 
    print(10*"----") 
