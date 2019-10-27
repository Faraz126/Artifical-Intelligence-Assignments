import math
def sigmoid(x):
    return round(1/(1 + (math.e**(-x))), 4)
def df_sigmoid(x):
    return round(sigmoid(x) * (1 - sigmoid(x)), 4)

def w_sum(x, w):
    sum = 0
    for i in range(len(x)):
        sum += x[i] * w[i]
    return round(sum,4)

def error(actual, pred):
    return round((actual-pred)*(pred)*(1-pred),4)

def weighted_error(weight, error_at_forward_node, value):
    return round(weight * error_at_forward_node * df_sigmoid(value),4)

def new_weight(old_w, learning_rate, output_at_start, delta_at_end):
    return round(old_w + (learning_rate * output_at_start * delta_at_end),4)



w14=0.35
w24=0.15
w25=-0.10
w34=-0.20
w35=0.20
w46=0.40
w56=0.25
node1, node2, node3 = (0.5, 0.3, 0.9)
actual6 = 0.8

node4 = w_sum((node1,node2,node3),(w14, w24, w34))
o_node4 = sigmoid(node4)
print("input at node 4", node4)
print("output at node 4", o_node4)
node5 = w_sum((node2,node3),(w25,w35))
o_node5 = sigmoid(node5)
print("input at node 5", node5)
print("output at node 5", o_node5)
node6 = w_sum((o_node4, o_node5),(w46, w56))
o_node6 = sigmoid(node6)
print("input at node 6", node6)
print("output at node 6", o_node6)

error6 = error(actual6, o_node6)
print("Error at Node 6", error6)

error4 = weighted_error(w46,error6, o_node4)
print("Error at Node 4", error4)

error5 = weighted_error(w56,error6, o_node5)
print("Error at Node 5", error5)

nw46 = new_weight(w46, 0.8, o_node4, error6)
nw56 = new_weight(w56, 0.8, o_node5, error6)
nw14 = new_weight(w14, 0.8, node1, error4)
nw24 = new_weight(w24, 0.8, node2, error4)
nw34 = new_weight(w34, 0.8, node3, error4)
nw25 = new_weight(w25, 0.8, node2, error5)
nw35 = new_weight(w35, 0.8, node3, error5)
print("new weight 46", nw46)
print("new weight 56", nw56)
print("new weight 14", nw14)
print("new weight 24", nw24)
print("new weight 34", nw34)
print("new weight 25", nw25)
print("new weight 35", nw35)

 
