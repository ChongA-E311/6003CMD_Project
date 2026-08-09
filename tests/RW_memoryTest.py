def update_map(memory, position, observation):
    x, y = position

    directions = {
        "Front": (0, 1),
        "Left": (-1, 0),
        "Right": (1, 0)
    }

    for direction, (dx, dy) in directions.items():
        tile = observation[direction]
        new_pos = (x + dx, y + dy)
        memory[new_pos] = tile

    # also mark current tile
    memory[position] = "empty"

def save_memory(memory, filename="map_memory.txt"):
    with open(filename, "w") as f:
        for (x, y), tile in memory.items():
            f.write(f"{x},{y},{tile}\n")
            
def load_memory(filename="map_memory.txt"):
    memory = {}

    try:
        with open(filename, "r") as f:
            for line in f:
                x, y, tile = line.strip().split(",")
                memory[(int(x), int(y))] = tile
    except FileNotFoundError:
        pass  # start fresh if no file exists

    return memory

def print_map(memory, agent_position):
    if not memory:
        print("No map data")
        return

    xs = [pos[0] for pos in memory.keys()]
    ys = [pos[1] for pos in memory.keys()]

    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)

    for y in range(max_y, min_y - 1, -1):
        row = ""
        for x in range(min_x, max_x + 1):
            pos = (x, y)

            if pos == agent_position:
                row += " A "
            elif pos in memory:
                if memory[pos] == "wall":
                    row += " # "
                elif memory[pos] == "empty":
                    row += " . "
                else:
                    row += " ? "
            else:
                row += " ? "

        print(row)
        
map_memory = load_memory()
agent_position = (0, 0)

# simulate step
observation = {
    "Left": "wall",
    "Front": "empty",
    "Right": "wall"
}

update_map(map_memory, agent_position, observation)

print_map(map_memory, agent_position)

save_memory(map_memory)