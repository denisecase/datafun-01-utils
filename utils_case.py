"""My Python Utils"""

import math
import statistics

mname: str = "Denise"
course_count: int = 6
is_experienced: bool = True
hours_invested: float = 2.5
numbers: list = [7, 6, 5, 8, 8, 4, 5, 7, 8, 6]

course_count_string: str = f"{name=}"
is_experienced_string: str = f"{is_experienced}"
hours_invested_string: str = f"{hours_invested}"
numbers_string: str = f"{numbers=}"

radius: float = 6.0
area: float = math.pi * radius**2
radius_area_string: str = f"Math: Given {radius=}, {area=}"

# stats
count: int = len(numbers)
smallest: int = min(numbers)
largest: int = max(numbers)
mode: float = statistics.mode(numbers)
median: float = statistics.median(numbers)
mean: float = statistics.mean(numbers)
stdev: float = statistics.stdev(numbers)

my_stats_string: str = f"""
Recent Daily Water Counts
-------------------------
{count=}
{smallest=}
{largest=}
{mode=}
{median=}
{mean=}
{stdev=}
"""

# display the information
print(course_count_string)
print(is_experienced_string)
print(hours_invested_string)
print(numbers_string)
print(radius_area_string)
print(my_stats_string)
