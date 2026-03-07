import cv2
import numpy as np
import heapq

# --- A* ALGORITHM FUNCTIONS ---

def heuristic(a, b):
    # Euclidean distance (allows diagonal movement)
    return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

def astar(array, start, goal):
    # Neighbors: Up, Down, Left, Right, and Diagonals
    neighbors = [(0,1), (0,-1), (1,0), (-1,0), 
                 (1,1), (1,-1), (-1,1), (-1,-1)]
    
    close_set = set()
    came_from = {}
    gscore = {start: 0}
    fscore = {start: heuristic(start, goal)}
    oheap = []

    heapq.heappush(oheap, (fscore[start], start))

    while oheap:
        current = heapq.heappop(oheap)[1]

        if current == goal:
            data = []
            while current in came_from:
                data.append(current)
                current = came_from[current]
            return data[::-1] # Return reversed path

        close_set.add(current)
        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + heuristic((0,0), (i,j))

            # Bounds check
            if 0 <= neighbor[0] < array.shape[0]:
                if 0 <= neighbor[1] < array.shape[1]:
                    if array[neighbor[0]][neighbor[1]] == 1: # 1 is Obstacle (Black)
                        continue
                else:
                    # Array bound y walls
                    continue
            else:
                # Array bound x walls
                continue

            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue

            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(oheap, (fscore[neighbor], neighbor))

    return False

# --- MOUSE CLICK HANDLER ---
points = []
def get_points(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((y, x)) # Store as (Row, Col)
        print(f"Point selected: {y}, {x}")
        cv2.circle(display_img, (x, y), 5, (0, 0, 255), -1) # Draw Red Dot
        cv2.imshow("Map", display_img)

# --- MAIN EXECUTION ---

# 1. Load the CLEANED map
# Make sure to use the one where buildings are painted BLACK!
image_path = 'cleaned_map.png' 
img = cv2.imread(image_path, 0) # Load as grayscale

if img is None:
    print("Error: Could not load image. Make sure 'cleaned_map.png' exists.")
    exit()

# 2. Process Map for A*
# Resize to make calculations faster (Optional, but recommended for large images)
# scale_percent = 50 
# width = int(img.shape[1] * scale_percent / 100)
# height = int(img.shape[0] * scale_percent / 100)
# img = cv2.resize(img, (width, height))

# Convert to Binary Matrix (0 = Free Road, 1 = Obstacle)
# In your image: White(255) is Road, Black(0) is Obstacle.
# We invert this because usually 0 is empty and 1 is occupied in arrays, 
# but for visualization 255 is white.
# Let's stick to: Road pixels > 128 are "Walkable".
ret, binary_map = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# Create the Grid: 0 = Walkable, 1 = Wall
# Invert: White (255) becomes 0 (Walkable), Black (0) becomes 1 (Wall)
grid = (255 - binary_map) / 255 

# 3. User Interface
display_img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
cv2.namedWindow("Map")
cv2.setMouseCallback("Map", get_points)

print("--- INSTRUCTIONS ---")
print("1. Click the START point on the white road.")
print("2. Click the GOAL point on the white road.")
print("3. Press any key to run A*.")

cv2.imshow("Map", display_img)
cv2.waitKey(0)

if len(points) >= 2:
    start = points[0]
    goal = points[1]
    
    print("Running A*... (This might take a second)")
    path = astar(grid, start, goal)

    if path:
        print("Path Found!")
        # Draw the path
        for coordinate in path:
            # coordinate is (y, x) -> (row, col)
            # opencv draws (x, y)
            display_img[coordinate[0], coordinate[1]] = (0, 255, 0) # Green Path

        # Draw Start/End again for visibility
        cv2.circle(display_img, (start[1], start[0]), 5, (0, 0, 255), -1)
        cv2.circle(display_img, (goal[1], goal[0]), 5, (255, 0, 0), -1)

        cv2.imshow("Result", display_img)
        cv2.imwrite("final_path.png", display_img)
        print("Path saved as 'final_path.png'")
        cv2.waitKey(0)
    else:
        print("No path found! (Did you click on a black wall?)")

cv2.destroyAllWindows()