class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Create a list of tuples (position, speed) and sort it by position in descending order
        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        
        # Initialize variables
        fleets = 0
        time_to_reach_target = 0
        
        # Iterate through the sorted list
        for pos, spd in cars:
            # Calculate the time it takes for this car to reach the target
            time = (target - pos) / spd
            
            # If this car takes more time than the previous car in the current fleet, it forms a new fleet
            if time > time_to_reach_target:
                fleets += 1
                time_to_reach_target = time
        
        return fleets