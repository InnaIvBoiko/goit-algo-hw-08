import heapq
from typing import List, Sequence, Tuple, TypeVar

T = TypeVar("T")


def merge_k_lists(lists: Sequence[Sequence[T]]) -> List[T]:
    """
    Merge k sorted lists into one sorted list using a min heap.
    
    Args:
        lists (list): List of sorted lists to merge
        
    Returns:
        list: A single sorted list containing all elements from input lists
    """
    # Initialize min heap and result list
    heap: List[Tuple[T, int, int]] = []
    merged_list: List[T] = []
    
    # Add the first element of each non-empty list to the heap
    # Format: (value, list_index, element_index)
    for i, lst in enumerate(lists):
        if lst:  # Check if list is not empty
            heapq.heappush(heap, (lst[0], i, 0))
    
    # Process heap until empty
    while heap:
        # Get the smallest element from heap
        value, list_index, element_index = heapq.heappop(heap)
        
        # Add the smallest value to result
        merged_list.append(value)
        
        # If there are more elements in the same list, add next element to heap
        if element_index + 1 < len(lists[list_index]):
            next_value = lists[list_index][element_index + 1]
            heapq.heappush(heap, (next_value, list_index, element_index + 1))
    
    return merged_list


# Example usage
if __name__ == "__main__":
    example_lists: List[List[int]] = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(example_lists)
    print("Sorted list:", merged_list)