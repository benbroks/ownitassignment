import math 

from maxFlow import FlowNetwork, Edge

FILEPATH = "sampleOwnIt.csv"
NUM_PREFERENCES = 5
EARLY_BIRD_VALUES = [19,17,15,13,11]
REGULAR_VALUES = [18,16,14,12,10]
MAX_USER_FLOW = max(EARLY_BIRD_VALUES)

def read_in_csv(fp):
    rooms = set()
    num_people = 0
    g = FlowNetwork()
    g.AddVertex('s')
    g.AddVertex('t')

    with open(fp,'r') as f:
        for line in f:
            line = line.strip()
            entries = line.split(',')
            if entries[0] != 'Name':
                name = entries[0]
                status = entries[1]
                g.AddVertex(name)
                g.AddEdge('s',name,1)
                if status == 'Early Bird':
                    for _, room in zip(EARLY_BIRD_VALUES,entries[-1*NUM_PREFERENCES:]):
                        g.AddVertex(room)
                        rooms.add(room)
                        g.AddEdge(name,room,1)
                else:
                    for _, room in zip(REGULAR_VALUES,entries[-1*NUM_PREFERENCES:]):
                        g.AddVertex(room)
                        rooms.add(room)
                        g.AddEdge(name,room,1)
                num_people += 1
    
    room_capacity = math.ceil(num_people / len(rooms))
    for room in rooms:
        g.AddEdge(room,'t',room_capacity)
    
    print(g.MaxFlow('s','t'))

if __name__ == "__main__":
    read_in_csv(FILEPATH)

    