# AI_Vacuum_Cleaner_Agent
This repository contains an AI-based Vacuum Cleaner Agent implementation using Python. The project is structured around the PEAS (Performance, Environment, Actuators, Sensors) framework and simulates an intelligent agent operating in a 4x4 grid environment.


## Part A: PEAS for the Vacuum Cleaner Agent

**1. Performance Measures:**

- Complete Cleaning: The agent must clean all dirt in the environment.
- Minimized Actions: The agent should use the least number of moves and actions.
- Energy Optimization: The agent starts with 100 energy points and must manage consumption efficiently.
- Bag Management: The dust bag has a maximum capacity of 10 dirt units and must be emptied before reaching this limit.
- Return to Base: After cleaning, the agent must return to the starting position A 0r (0,0) to complete its task.

**2. Environment:**

- Grid Layout: The environment is a 4x4 grid, where each location is represented using (row, column) format (e.g., A = (0,0), P = (3,3)).
- Dirt Distribution: Some cells contain dirt while others are clean.
- Agent Start Position: The vacuum begins at location A or (0,0) – top-left corner.
- Movement Restrictions: The agent can only move North, South, East, or West (no diagonal movement).
- Action Cost: Each movement or dirt collection reduces energy by 1 point.
- Bag Capacity: The vacuum can hold up to 10 dirt units before needing to empty at A or (0,0).

**3. Actuators:**

- Move: The agent moves in one of the four directions (North, South, East, West).
- Suck: The agent removes dirt from the current location.
- Empty: The agent empties its dust bag when at home (Location A).

**4. Sensors:**

- Dirt Sensor: Detects whether the current location is dirty or clean.
- Location Sensor: Identifies the vacuum's (agent’s) current location.
- Bag Capacity Sensor: Determines if the bag is full (10 units max).
- Energy Sensor: Monitors the remaining energy level to ensure efficiency.


## Part B: Pseudo-Code Implementation with Visualization

**Python Code Output:**


🔄 Moved South → New position: [1, 0], Energy left: 99

🔄 Moved South → New position: [2, 0], Energy left: 98

✅ Sucked dirt at [2, 0], Bag: 1/10, Energy left: 97

🔄 Moved South → New position: [3, 0], Energy left: 96

✅ Sucked dirt at [3, 0], Bag: 2/10, Energy left: 95

🔄 Moved East → New position: [3, 1], Energy left: 94

🔄 Moved East → New position: [3, 2], Energy left: 93

✅ Sucked dirt at [3, 2], Bag: 3/10, Energy left: 92

🔄 Moved North → New position: [2, 2], Energy left: 91

✅ Sucked dirt at [2, 2], Bag: 4/10, Energy left: 90

🔄 Moved North → New position: [1, 2], Energy left: 89

🔄 Moved North → New position: [0, 2], Energy left: 88

✅ Sucked dirt at [0, 2], Bag: 5/10, Energy left: 87

🔄 Moved South → New position: [1, 2], Energy left: 86

🔄 Moved West → New position: [1, 1], Energy left: 85

✅ Sucked dirt at [1, 1], Bag: 6/10, Energy left: 84

🔄 Moved East → New position: [1, 2], Energy left: 83

🔄 Moved East → New position: [1, 3], Energy left: 82

✅ Sucked dirt at [1, 3], Bag: 7/10, Energy left: 81

🎉 Cleaning Complete!

🔄 Moved North → New position: [0, 3], Energy left: 80

🔄 Moved West → New position: [0, 2], Energy left: 79

🔄 Moved West → New position: [0, 1], Energy left: 78

🔄 Moved West → New position: [0, 0], Energy left: 77

🗑️ Emptied bag at home!

![vacuum_simulation](https://github.com/user-attachments/assets/bbf1f83d-5700-4a96-b472-9b75e0fdd47f)


## Part C: Summary

**Lessons Learned**

Developing this vacuum cleaner agent was an insightful process into AI-driven automation and optimization. The biggest challenge was ensuring an **efficient path** for cleaning while managing **energy** and **bag capacity** constraints.

**Energy Considerations**

With a **100-energy point** limit, the vacuum can clean and return home, but an **optimized path** is essential. Implementing smarter algorithms like A search* can further enhance efficiency by reducing unnecessary movements.

**Scaling to Larger Environments**

- Implementing a bigger grid (e.g., 8x8) will require a graph-based search algorithm.
- Using machine learning to predict the dirtiest areas first can improve efficiency.

**Handling Real-World Obstacles**

- Adding obstacle detection sensors.
- Introducing real-time path recalculations.
- Using LiDAR or vision-based navigation for better adaptability.
