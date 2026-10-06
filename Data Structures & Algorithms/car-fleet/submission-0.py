class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        fleet = []

        for i in range(len(position)):
            cars.append((position[i], (target-position[i])/speed[i]))
        
        cars.sort(reverse=True)

        for i in range(len(cars)):
            time = cars[i][1]

            if not fleet:
                fleet.append(time)
            if time > fleet[-1]:
                fleet.append(time)
        return len(fleet)





        