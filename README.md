# Logger 


## Description

This script takes a logfile as input and can output 1 of 3 things

1. Total requests aggregated by day 
2. Top 3 user agents over time 
3. Ratio of GETS/POSTS over time  



### Prerequisites
Python 2.7 

Modules: 
import collections
import datetime
import re
import sys
import argparse



###  Usage 

```
usage: log_parser.py [-h] --file FILE
                     {get_daily_requests,get_user_agents,get_ratio} ...
```

###  Arguments:
```
get_daily_requests  Get total daily requests
get_user_agents     Get top 3 user agents
get_ratio           Get ratio of GETS/POSTS
```

###  Optional arguments:
  
   -h, --help            show this help message and exit
  --file FILE, -f FILE   Enter a filename 

### Example 
```
python log_parser.py -f sample.log get_daily_requests
```

###  Acknowledgments

* Thanks for the opportunity to work on this ! 
