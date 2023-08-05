# jyp

![image failed to load](banner.png "jyp banner")

Pocket converter for **Korean to Canadian currency**
* Pull from **live-time conversion rate trends**
* Receive **automatic daily updates**

## Usage

```
from jyp import communicate, reminder

# Send an immediate update
communicate()

# Set repeating updates
reminder("8am")
```

## Install

```
pip install jyp
```

## How to run tests

In the root directory run
```
python -m tests.test
```
