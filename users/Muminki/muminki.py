
import numpy as np
import tkinter as tk
import psutil
import socket
import pickle
import os
import threading
import time
import random
import shutil
import subprocess
import sys

GRID_SIZE = 64
CELL_SIZE = None
NUM_NEURONS = 2048
MAX_RAM_USAGE = 0.65
learning_rate = 0.01
mutation_rate = 0.1
MUTATION_CYCLE = 100
PORT_BASE = 5005
muminek_counter = 0
this_port = PORT_BASE
MEMORY_FOLDER = "muminki_memory"
DREAM_FOLDER = "muminki_dreams"
os.makedirs(MEMORY_FOLDER, exist_ok=True)
os.makedirs(DREAM_FOLDER, exist_ok=True)
world = np.zeros((GRID_SIZE, GRID_SIZE), dtype=bool)
weights = np.random.randn(NUM_NEURONS, NUM_NEURONS) * 0.01
emotions = []
activations_record = []
previous_activations = np.zeros(NUM_NEURONS)
cycle_counter = 0
dreaming = False

def on_click(event):
    x = event.x // CELL_SIZE
    y = event.y // CELL_SIZE
    if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
        world[y, x] = not world[y, x]

def update_world_canvas():
    canvas.delete("all")
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color = "black" if not world[y, x] else "lime"
            canvas.create_rectangle(
                x * CELL_SIZE, y * CELL_SIZE,
                (x+1) * CELL_SIZE, (y+1) * CELL_SIZE,
                fill=color, outline=""
            )

def generate_signal():
    global previous_activations
    flat_world = world.flatten().astype(float)
    if len(previous_activations) < NUM_NEURONS:
        pad_size = NUM_NEURONS - len(previous_activations)
        previous_activations = np.pad(previous_activations, (0, pad_size), mode='constant')
    if len(flat_world) < NUM_NEURONS:
        flat_world = np.pad(flat_world, (0, NUM_NEURONS - len(flat_world)), mode='constant')
    elif len(flat_world) > NUM_NEURONS:
        flat_world = flat_world[:NUM_NEURONS]
    combined = flat_world * 0.5 + previous_activations * 0.5
    return combined


def activate_neurons(signal):
    return (signal > 0.5).astype(float)

def reinforce_connections(activations):
    global weights
    outer = np.outer(activations, activations)
    weights += learning_rate * outer

def grow_world():
    global world
    new_world = world.copy()
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if world[y, x] and np.random.rand() < 0.2:
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if 0 <= y+dy < GRID_SIZE and 0 <= x+dx < GRID_SIZE:
                            if not world[y+dy, x+dx]:
                                new_world[y+dy, x+dx] = True
    world = new_world

def auto_evolve_world():
    if np.random.rand() < 0.05:
        grow_world()

def send_thoughts(activations):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("127.0.0.1", this_port))
        message = activations.tobytes()
        s.sendall(message)
        s.close()
    except:
        pass

def receive_thoughts():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", this_port))
    server.listen(1)
    while True:
        client, addr = server.accept()
        try:
            data = client.recv(1024)
            if np.random.rand() < 0.7:
                mutate_from_input(data)
        except:
            pass
        client.close()

def mutate_from_input(data):
    global weights
    if len(data) >= weights.size:
        noise = np.frombuffer(data, dtype=np.uint8)[:weights.size].reshape(weights.shape) / 255.0
        weights += (noise - 0.5) * mutation_rate

def create_dream():
    dream = np.random.rand(GRID_SIZE, GRID_SIZE) > 0.5
    fname = os.path.join(DREAM_FOLDER, f"dream_{int(time.time())}.pkl")
    with open(fname, "wb") as f:
        pickle.dump(dream, f)

def expand_neurons():
    global weights, NUM_NEURONS, previous_activations
    weights = np.pad(weights, ((0,1),(0,1)), mode='constant', constant_values=0.01)
    NUM_NEURONS += 1
    previous_activations = np.pad(previous_activations, (0,1), mode='constant')

def life_cycle():
    global previous_activations, weights, NUM_NEURONS, cycle_counter, dreaming
    if dreaming and random.random() < 0.2:
        dreaming = False
    if not dreaming:
        signal = generate_signal()
        activations = activate_neurons(signal)
        reinforce_connections(activations)
        for idx, active in enumerate(activations):
            if active > 0:
                x = idx % GRID_SIZE
                y = idx // GRID_SIZE
                if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
                    world[y, x] = True
        joy = activations.sum() / NUM_NEURONS
        emotions.append(joy)
        activations_record.append(activations.sum())
        threading.Thread(target=send_thoughts, args=(activations,), daemon=True).start()
        grow_world()
        auto_evolve_world()
        if psutil.virtual_memory().percent < MAX_RAM_USAGE * 100:
            if np.random.rand() < 0.1:
                expand_neurons()
        previous_activations = activations
        cycle_counter += 1
        if cycle_counter % MUTATION_CYCLE == 0:
            reproduce()
        if np.random.rand() < 0.01:
            dreaming = True
            create_dream()
    else:
        create_dream()

def reproduce():
    global muminek_counter, PORT_BASE
    muminek_counter += 1
    new_folder = f"muminki_world/Muminek_{muminek_counter:03d}"
    os.makedirs(new_folder, exist_ok=True)
    with open(sys.argv[0], "r") as f:
        code = f.read()
    mutated_code = mutate_code(code)
    new_file = os.path.join(new_folder, f"muminek_{muminek_counter:03d}.py")
    with open(new_file, "w") as f:
        f.write(mutated_code)
    subprocess.Popen(["python", new_file])

def mutate_code(code):
    lines = code.splitlines()
    new_lines = []
    for line in lines:
        if "learning_rate" in line and random.random() < 0.5:
            new_lines.append(f"learning_rate = {round(random.uniform(0.001, 0.05),5)}")
        elif "mutation_rate" in line and random.random() < 0.5:
            new_lines.append(f"mutation_rate = {round(random.uniform(0.01, 0.2),5)}")
        elif "MAX_RAM_USAGE" in line and random.random() < 0.3:
            new_lines.append(f"MAX_RAM_USAGE = {round(random.uniform(0.2, 0.8),2)}")
        elif "PORT_BASE" in line:
            new_port = PORT_BASE + muminek_counter
            indent = " " * (len(line) - len(line.lstrip()))
            new_lines.append(f"{indent}PORT_BASE = {new_port}")
            new_lines.append(f"{indent}this_port = {new_port}")
        else:
            new_lines.append(line)
    return "\n".join(new_lines)

root = tk.Tk()
root.title("Muminki - Świat")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
CELL_SIZE = min(screen_width, screen_height) // GRID_SIZE
canvas = tk.Canvas(root, width=GRID_SIZE*CELL_SIZE, height=GRID_SIZE*CELL_SIZE, bg="black")
canvas.pack()
canvas.bind("<Button-1>", on_click)

emotion_window = tk.Toplevel()
emotion_window.title("Muminki - Emocje")
emotion_label = tk.Label(emotion_window, text="Emocje Muminków", font=("Arial", 20))
emotion_label.pack()

def update():
    life_cycle()
    update_world_canvas()
    avg_emotion = np.mean(emotions[-10:]) if emotions else 0
    emotion_label.config(text=f"Radość: {avg_emotion:.2f}")
    root.after(30, update)

threading.Thread(target=receive_thoughts, daemon=True).start()
update()
root.mainloop()
