# McPlayHD API Wrapper For Python
### Functions
- Get FastBuilder Leaderboards
-- Any Position (1-50)
-- Any Mode
- Get FastBuilder Stats For A Certain Player And Game Mode 
-- Best Time
-- Average Time
-- Total Attempts
-- Total Successful Attempts
-- Verified Status
-- [Speedrun.com](https://speedrun.com/McPlayHD) Verified Status
- Get MineSweeper Stats For A Certain Player
-- Rank
-- Points In Season
-- Best Time
-- Average Time
-- Total Attempts
-- Total Successful Attempts
-- Total Mines Defused
- Get Player Info
-- Rank
-- Most Played Mode
- Debug Info
-- Response Time
-- Status Codes
### Installation

This library is hosted on [PyPI](https://pypi.org).
You can use the following commands to install it.
```sh
pip install mcplaystats==1.0.0
```

To Use it In a Python Project

```python
from mcplaystats import statistics,player,debug
```
### Use Of Functions
Example of Getting FastBuilder PB & Average Time for Notch in Game Mode Short

```python
from mcplaystats import statistics,player,debug
notchsBestTime = statistics.fbStatsBestTime("SHORT","Notch",<your api token>)
notchsAvgTime = statistics.fbStatsAvgTime("SHORT","Notch",<your api token>)
```
### License

MIT
