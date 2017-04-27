#!/usr/bin/env python

import os, sys
import json

with open(sys.argv[1], 'r') as f:
    account_data = json.loads(f.read())

script = '''#!/bin/bash

node /src/bin/testrpc'''

accounts = account_data['accounts']
for a in accounts:
    script += ' --account=\"{},{}\"'.format(accounts[a]['key'], accounts[a]['balance'])
    print 'Added account with address:\t' + a

with open(sys.argv[2], 'w') as f:
    f.write(script + '\n')
