import math
from unittest import result


#Minimax Decision Function 
def minimax_decision(state):
    good_score = -math.inf
    good_act = None
    alpha = -math.inf
    beta = math.inf
    
    for action in actions(state):
        value = minimum_value(result(state, action, 'X'), alpha, beta)
        if value > good_score:
            good_score = value
            good_act = action
        alpha = max(alpha, good_score)
            
    return good_act

#Maximum Value Function
def maximum_value(state, alpha, beta):
    if terminal(state):
        return utility(state)
    
    v = -math.inf
    for action in actions(state):
        v = max(v, minimum_value(result(state, action, 'X'), alpha , beta))
        
        if v >= beta:
            return v
        alpha = max(alpha,v)
    return v


#Minimum Value Function
def minimum_value(state):
    if terminal(state):
        return utility(state)
    
    v = math.inf
    for action in actions(state):
        v = min(v,minimum_value(result(state,action,'O'), alpha, beta))
        
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v
        