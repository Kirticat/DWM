def pagerank(G, alpha=0.85, personalization=None, max_iter=100, tol=1.0e-6, nstart=None, weight='weight', dangling=None): 
    if len(G) == 0: 
        return {} 
    if not G.is_directed(): 
        D = G.to_directed() 
    else: 
        D = G
    
    # Create a copy in (right) stochastic form 
    W = nx.stochastic_graph(D, weight=weight) 
    N = W.number_of_nodes() 

    # Choose fixed starting vector if not given 
    if nstart is None: 
        x = dict.fromkeys(W, 1.0 / N) 
    else: 
        # Normalized nstart vector 
        s = float(sum(nstart.values())) 
        x = dict((k, v / s) for k, v in nstart.items()) 
    if personalization is None: 
        # Assign uniform personalization vector if not given 
        p = dict.fromkeys(W, 1.0 / N) 
    else: 
        missing = set(G) - set(personalization) 
        if missing: 
            raise NetworkXError('Personalization dictionary must have a value for every node. Missing nodes %s' % missing) 
        s = float(sum(personalization.values())) 
        p = dict((k, v / s) for k, v in personalization.items())
    if dangling is None: 
        # Use personalization vector if dangling vector not specified 
        dangling_weights = p 
    else: 
        missing = set(G) - set(dangling) 
        if missing: 
            raise NetworkXError('Dangling node dictionary must have a value for every node. Missing nodes %s' % missing) 
        s = float(sum(dangling.values()))
        dangling_weights = dict((k, v/s) for k, v in dangling.items()) 
    dangling_nodes = [n for n in W if W.out_degree(n, weight=weight) == 0.0] 
    for _ in range(max_iter): 
        xlast = x 
        x = dict.fromkeys(xlast.keys(), 0) 
        danglesum = alpha * sum(xlast[n] for n in dangling_nodes) 
        for n in x: 
        # this matrix multiply looks odd because it is 
        # doing a left multiply x^T=xlast^T*W 
            for nbr in W[n]: 
                x[nbr] += alpha * xlast[n] * W[n][nbr][weight] 
            x[n] += danglesum * dangling_weights[n] + (1.0 - alpha) * p[n] 
        # check convergence, l1 norm 
        err = sum([abs(x[n] - xlast[n]) for n in x]) 
        if err < N*tol: 
            return x 
            raise NetworkXError('pagerank: power iteration failed to converge ' 'in %d iterations.' % max_iter) 

import networkx as nx 
import matplotlib.pyplot as plt 
#n = 40 i.e no of nodes to be created 
#m = 15 i.e Number of edges to attach from a new node to existing nodes 
G=nx.barabasi_albert_graph(40,15)   
plt.title("Graph Created") 
nx.draw(G, with_labels=True) 
plt.show() 
pr=pagerank(G) 
print("--------------------page ranks--------------------") 
print(pr)
