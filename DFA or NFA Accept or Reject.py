import pandas as p

automata = {}

def input_dfa_nfa(n):
    global automata

    print("\nEnter States by space: ")

    states = [x for x in input().split()]

    print("\nEnter Transitions by space: ")

    trans = [x for x in input().split()]

    print()
    for state in states:
        automata[state] = {}
        
        for path in trans:
            print("Enter state that connect with state %s by path %s: "%(state,path))
            final_states = [x for x in input().split()]
            automata[state][path] = final_states
            print()
        print()
            
    return automata

def accept_reject(automata,final_states):
    print("\nEnter Walk of transitions or type \"Exit\": ")

    string = [x for x in input()]

    if string[-1] == 't':
        exit(0)
        
    state = []
    start = automata['0'][string[0]][0]
    state.append(start)

    j = 0
    for i in string[1::]:
        s = automata[state[j]][i][0]
        state.append(s)
        j += 1

    end_state = state.pop()

    if end_state in final_states:
        return True
    return False

print("Which one do you want? ","\n1.DFA","\n2.NFA","\n3.Exit")

menu = int(input("--> "))

if menu == 1 or menu == 2:
    print()
    states_no = int(input("Enter number of states: "))

    automata = input_dfa_nfa(states_no)

    automata_table = p.DataFrame(automata)

    print("Your Automata Table is:")
    print("--------------------------")
    print(automata_table)
    print("--------------------------\n")
    
    print("Enter Finall states: ")
    
    final_states = [x for x in input()]
    while(True):
        if accept_reject(automata,final_states) is True:
            print("Accepted.")
        else:
            print("Rejected.")
    
else:
    exit(0)
