# pdb_test.copy
"""Testing built-in debugger"""


import pdb

counter = 1

while counter <= 5:
    print(counter)
    pdb.set_trace()
    counter += 1
