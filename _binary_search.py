from collections import deque


def binary_search_algorithm(array,item):
    if not type(array) is list:
        raise TypeError
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        if array[mid] > item:
            low = mid + 1
        if array[mid] < item:
            high = mid
        if array[mid] == item:
            return mid
    return None


def quick_sort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    left_array = [x for x in array[1:] if x < pivot]
    right_array = [x for x in array[1:] if x > pivot]
    return quick_sort(left_array) + [pivot] + quick_sort(right_array)

graph = {}
graph["me"] = ["Bob", "Claire", "Alice"]
graph["Bob"] = ["Peggy", "Anuj"]
graph["Claire"] = ["Jonny", "Thom"]
graph["Alice"] = ["Peggy"]
graph["Anuj"] = []
graph["Peggy"] = []
graph["Jonny"] = []
graph["Thom"] = []

node_gap = {}
node_gap["Book"] = {}
node_gap["Book"]["LP"] = 5
node_gap["Book"]["Poster"] = 0
node_gap["LP"]= {}
node_gap["LP"]["Bass"] = 15
node_gap["LP"]["Drums"] = 20
node_gap["Poster"] = {}
node_gap["Poster"]["Drums"] = 35
node_gap["Poster"]["Bass"] = 30
node_gap["Bass"] = {}
node_gap["Drums"] = {}
node_gap["Bass"]["Piano"] = 20
node_gap["Drums"]["Piano"] = 10


d_graph = {}
d_graph["start"] = {}
d_graph["start"]["a"] = 6
d_graph["start"]["b"] = 2
d_graph["a"] = {}
d_graph["a"]["fin"] = 1
d_graph["b"] = {}
d_graph["b"]["a"] = 3
d_graph["b"]["fin"] = 5
# fin node has no neighbors
d_graph["fin"] = {}

parents = dict()
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

costs = {}
infinity = float("inf")
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

processed = []


def find_lowest_cost_node(cost):
    lowest_cost = infinity
    lowest_cost_node = None
    for k in cost:
        if cost[k] < lowest_cost and k not in processed:
            lowest_cost = cost[k]
            lowest_cost_node = k
    return lowest_cost_node


def graph_algorithm(g):
    if type(g) is not dict:
        raise TypeError
    searched = []
    search_deque = deque(g.get('me'))
    while search_deque:
        person = deque.popleft(search_deque)
        if person not in searched:
            if str(person)[-1] == 'm':
                print('%s is a mongo seller' % person)
                return True
            else:
                searched.append(person)
                search_deque += graph.get(person)


if __name__ == '__main__':
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = d_graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if new_cost < costs[n]:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)

    print(parents)

