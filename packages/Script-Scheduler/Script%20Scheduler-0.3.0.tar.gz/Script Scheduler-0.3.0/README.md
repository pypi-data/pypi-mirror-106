# Script Scheduler

Script Scheduler is a package created for managing long running python files which is bound by some time interval like developer wants to run script for 3 hours in first half and 5 hours in second half a day. Here Script Scheduler comes into picture where you can just specify script path, start time and end time, these would be list.

## Steps

- Specify list of python files
- Specify list of start times for all the scripts
- Specify list of end time for all the scripts

## Installation

Script Scheduler requires [python3](https://www.python.org/downloads/) to run.

```sh
pip3 install scriptScheduler
```
## Usage

> Schedule Script

```python
from scriptScheduler import scriptScheduler

fileList = ['path_to_file1.py', 'path_to_file2.py', 'path_to_file3.py']
startTimeList = ['12:00', '14:00', '16:00']
stopTimeList = ['13:00', '15:00', '17:00']

scriptScheduler(fileList, startTimeList, stopTimeList)
```

> Remove Script From Timeline

```python
from scriptScheduler import scriptRemove

scriptId = id # you can get this from logs
scriptRemove(scriptId)
```

> Bring Back Script To Timeline

```python
from scriptScheduler import scriptAdd

scriptId = id # you can get this from logs
scriptAdd(scriptId)
```

> Update Timeline -- Development Inprogress

```python
# It will there in next release
```