import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

# Define grid size (4x4 grid)
GRID_SIZE = 4

# Define initial dirt locations using (row, column) format
dirt_locations = {(0, 2), (1, 1), (1, 3), (2, 0), (2, 2), (3, 0), (3, 2), (0, 3), (3, 1)}

# Initialize the grid (1 = dirt, 0 = clean)
grid = np.zeros((GRID_SIZE, GRID_SIZE))
for loc in dirt_locations:
    grid[loc] = 1  # Mark dirty spots

# Initial vacuum state
position = [0, 0]  # Vacuum starts at top-left
energy = 100       # Initial energy points
bag_capacity = 0   # Dirt collection capacity
bag_limit = 10     # Maximum dirt capacity
path = []          # Track movement path
visit_count = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)  # Track visit frequency

# Movement directions: {direction: (row_change, col_change)}
directions = {
    "North": (-1, 0), "South": (1, 0),
    "West": (0, -1), "East": (0, 1)
}

def bfs(start, target):
    """Find the shortest path using BFS"""
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (current, path) = queue.popleft()
        if current == target:
            return path  # Return shortest path
        
        if current in visited:
            continue
        visited.add(current)

        for direction, (dr, dc) in directions.items():
            new_pos = (current[0] + dr, current[1] + dc)
            if 0 <= new_pos[0] < GRID_SIZE and 0 <= new_pos[1] < GRID_SIZE:
                queue.append((new_pos, path + [direction]))

    return []

def move_to_target(target):
    """Move vacuum step-by-step towards the target position"""
    global position, energy

    path_to_target = bfs(tuple(position), target)
    for step in path_to_target:
        if energy <= 0:
            print("❌ Out of energy! Stopping movement.")
            return

        move(step)

def move(direction):
    """Move the vacuum in the specified direction."""
    global position, energy
    if energy <= 0:
        return
    
    new_row = position[0] + directions[direction][0]
    new_col = position[1] + directions[direction][1]

    # Ensure movement remains within the grid
    if 0 <= new_row < GRID_SIZE and 0 <= new_col < GRID_SIZE:
        position[0], position[1] = new_row, new_col
        energy -= 1  # Reduce energy per move
        path.append(tuple(position))
        visit_count[new_row, new_col] += 1
        print(f"🔄 Moved {direction} → New position: {position}, Energy left: {energy}")

def suck():
    """Vacuum cleans dirt at the current position."""
    global grid, bag_capacity, energy, dirt_locations
    pos_tuple = tuple(position)
    
    if pos_tuple in dirt_locations:
        grid[pos_tuple] = 0  # Mark as clean
        dirt_locations.remove(pos_tuple)
        bag_capacity += 1  # Increase dirt collection
        energy -= 1  # Reduce energy for cleaning
        print(f"✅ Sucked dirt at {position}, Bag: {bag_capacity}/{bag_limit}, Energy left: {energy}")

def navigate_home():
    """Guide the vacuum back to the home position (0,0) when bag is full."""
    move_to_target((0, 0))
    empty_bag()

def empty_bag():
    """Empty the vacuum bag at home location (0,0)."""
    global bag_capacity
    if tuple(position) == (0, 0):
        print("🗑️ Emptied bag at home!")
        bag_capacity = 0  # Reset bag capacity

def find_nearest_dirt():
    """Find the closest dirt spot to optimize movement."""
    if not dirt_locations:
        return None
    return min(dirt_locations, key=lambda dirt: abs(dirt[0] - position[0]) + abs(dirt[1] - position[1]))

def clean_environment():
    """Main function to clean all dirt spots efficiently."""
    global bag_capacity

    while energy > 0 and dirt_locations:
        target = find_nearest_dirt()
        if target:
            move_to_target(target)
            suck()

        # If bag reaches max capacity, return home to empty it
        if bag_capacity >= bag_limit:
            navigate_home()

    print("🎉 Cleaning Complete!")
    navigate_home()

# Start cleaning process
clean_environment()

# Visualization using Matplotlib
fig, ax = plt.subplots()

def update(frame):
    """Update function for live animation visualization."""
    ax.clear()
    display_grid = np.copy(grid)

    # Live update of path colors
    for i in range(frame + 1):
        r, c = path[i]
        display_grid[r, c] = 0.3 + (0.1 * visit_count[r, c])  # Change color after revisiting
    
    # Mark vacuum position uniquely
    if tuple(position) == (0, 0):
        display_grid[position[0], position[1]] = 0.9  # Home position in a distinct color
    else:
        display_grid[position[0], position[1]] = 0.75  # Vacuum marker

    ax.imshow(display_grid, cmap="coolwarm", vmin=0, vmax=1)
    ax.set_xticks(range(GRID_SIZE))
    ax.set_yticks(range(GRID_SIZE))
    ax.set_xticklabels(['A', 'B', 'C', 'D'])
    ax.set_yticklabels(['1', '2', '3', '4'])
    ax.set_title(f'Vacuum Position: {position}, Energy: {energy}, Bag: {bag_capacity}/{bag_limit}')

# Animate movement
anim = animation.FuncAnimation(fig, update, frames=len(path), repeat=False)

# Save animation before displaying
anim.save("vacuum_simulation.gif", writer="pillow")

# Show animation
plt.show()
