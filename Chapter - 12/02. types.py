from typing import List, Tuple, Dict, Union
name : str = "Krishna"

def sum(a : int, b : int) -> int:
    return a+b

# list of intigers
numbers : List[int] = [1, 2, 3, 4, 5]

# tuples of a string and an intiger
person : Tuple[str, int] = ("Krishna", 13)

# Dictionary of strings and intigers value
scores : Dict[str, int] = {"krishna" : 99, "Rife" : 95}

# Union types in varibles that can hold multiple values
Identifier : Union[str, int] = "ID201240"
Identifier = 201240 #also valaid
n : int = 5


