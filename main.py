import heapq
from typing import Sequence


def minimize_connection_cost(cables: Sequence[float]) -> float:
    """
    Calculate the minimum cost to connect all network cables.
    
    This function uses a greedy approach with heap queue to always connect
    the two shortest cables first, which minimizes the total cost.
    
    Args:
        cables (Sequence): Sequence of cable lengths (integers or floats)
        
    Returns:
        float: Minimum total cost to connect all cables
    """
    # Handle edge cases
    if not cables:
        return 0.0
    if len(cables) == 1:
        return 0.0
    
    # Create a min heap from the cable lengths
    heap = list(cables)
    heapq.heapify(heap)
    
    total_cost = 0.0
    
    print(f"Cable lengths heap: {heap}")
    print('»»»')
    
    # Connect cables until only one remains
    while len(heap) > 1:
        # Get the two shortest cables
        first_cable = heapq.heappop(heap)
        second_cable = heapq.heappop(heap)
        
        # Calculate connection cost
        connection_cost = first_cable + second_cable
        total_cost += connection_cost
        
        # Push the combined cable back to heap
        heapq.heappush(heap, connection_cost)
        
        # Print intermediate results
        print(
            f"Connecting cables of lengths {first_cable} and {second_cable} with costs {connection_cost}. Total costs: {total_cost}"
        )
        print(f"Current heap state: {heap}")

    return total_cost


# Test the function with example data
if __name__ == "__main__":
    cables = [4, 3, 2, 6, 20, 7]
    
    print(f"Initial cable lengths: {cables}")
    print('»»»')
    
    result = minimize_connection_cost(cables)
    
    print('»»»')
    print(f"Minimum connection cost: {result}")
    print()
    
    