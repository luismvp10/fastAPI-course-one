from typing import List


def process_items(items: List[str]):
    for item in items:
        print(item.title())


print(process_items(['Item1', 'Item2', 'Item3', 'Item4', 'Item5']))
