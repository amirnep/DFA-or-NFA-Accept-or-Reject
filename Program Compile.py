#Program Compile for Example:

"""

Which one do you want?  
1.DFA 
2.NFA 
3.Exit
--> 1

Enter number of states: 4

Enter States by space: 
0 1 2 3

Enter Transitions by space: 
a b

Enter state that connect with state 0 by path a: 
1

Enter state that connect with state 0 by path b: 
3


Enter state that connect with state 1 by path a: 
1

Enter state that connect with state 1 by path b: 
2


Enter state that connect with state 2 by path a: 
3

Enter state that connect with state 2 by path b: 
2


Enter state that connect with state 3 by path a: 
3

Enter state that connect with state 3 by path b: 
3


Your Automata Table is:
--------------------------
     0    1    2    3
a  [1]  [1]  [3]  [3]
b  [3]  [2]  [2]  [3]
--------------------------

Enter Finall states: 
2

Enter Walk of transitions or type "Exit": 
aaaab
Accepted.

Enter Walk of transitions or type "Exit": 
aaaaaaaaaaaaaaaabbbbbbbbbbbbb
Accepted.

Enter Walk of transitions or type "Exit": 
bababababababab
Rejected.

Enter Walk of transitions or type "Exit": 
aaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbaaaaaaaaaaaaaaabbbbbbbbbb
Rejected.

Enter Walk of transitions or type "Exit": 
abababab
Rejected.

Enter Walk of transitions or type "Exit": 
Exit

"""
