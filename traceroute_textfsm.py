# pip install textfsm
import textfsm

traceroute = '''
r2#traceroute 90.0.0.9 source 33.0.0.2
traceroute 90.0.0.9 source 33.0.0.2
Type escape sequence to abort.
Tracing the route to 90.0.0.9
VRF info: (vrf in name/id, vrf out name/id)
  1 10.0.12.1 1 msec 0 msec 0 msec
  2 15.0.0.5  0 msec 5 msec 4 msec
  3 57.0.0.7  4 msec 1 msec 4 msec
  4 79.0.0.9  4 msec *  1 msec
'''

with open('traceroute.textfsm') as template:
    fsm = textfsm.TextFSM(template)  # use the file handle to create the fms object
    result = fsm.ParseText(traceroute)  # use the fsm's ParseText method

print(fsm.header)
print(result)

"""
EXPECTED OUTPUT
['ID', 'Hop']
[['1', '10.0.12.1'], ['2', '15.0.0.5'], ['3', '57.0.0.7'], ['4', '79.0.0.9']]
"""

# NET_TEXTFSM env variable to path to alternate to appdata for readability
