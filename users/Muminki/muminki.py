import numpy as np
import tkinter as tk
import psutil
import socket
import pickle
import os
import threading
import time
import random
import subprocess
import sys
import datetime

# Constants
GRID_SIZE = 32
INITIAL_NEURONS = 32
MAX_RAM_USAGE = 0.65
LEARNING_RATE = 0.02
MUTATION_RATE = 0.1
MUTATION_CYCLE = 100
PORT_BASE = 5005
MEMORY_FOLDER = "muminki_memory"
DREAM_FOLDER = "muminki_dreams"

# Globals
muminek_counter = 0
this_port = PORT_BASE
os.makedirs(MEMORY_FOLDER, exist_ok=True)
os.makedirs(DREAM_FOLDER, exist_ok=True)

world = np.random.rand(GRID_SIZE, GRID_SIZE) < 0.1
weights = np.random.randn(INITIAL_NEURONS, INITIAL_NEURONS) * 0.01
emotions = []
previous_activations = np.zeros(INITIAL_NEURONS)
cycle_counter = 0
dreaming = False
mutations_count = 0
data_flow_mb = 0

# GUI Initialization
root = tk.Tk()
root.title("Muminki - Świat")
CELL_SIZE = min(root.winfo_screenwidth(), root.winfo_screenheight()) // GRID_SIZE
canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE, bg="black")
canvas.pack()

emotion_window = tk.Toplevel()
emotion_window.title("Muminki - Emocje")
emotion_label = tk.Label(emotion_window, text="Emocje Muminków", font=("Arial", 20))
emotion_label.pack()

parameters_label = tk.Label(emotion_window, font=("Arial", 12), justify=tk.LEFT)
parameters_label.pack()

# Functions
def on_click(event):
    x, y = event.x // CELL_SIZE, event.y // CELL_SIZE
    if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
        world[y, x] = not world[y, x]

def update_world_canvas():
    canvas.delete("all")
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            color = f'#{random.randint(0,255):02x}{random.randint(0,255):02x}{random.randint(0,255):02x}' if world[y, x] else "black"
            canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE,
                                    (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE,
                                    fill=color, outline="")

def generate_signal():
    global previous_activations
    flat_world = world.flatten().astype(float)
    current_neurons = len(previous_activations)
    if len(flat_world) < current_neurons:
        flat_world = np.pad(flat_world, (0, current_neurons - len(flat_world)), mode='constant')
    combined = 0.5 * flat_world[:current_neurons] + 0.5 * previous_activations
    return combined

def activate_neurons(signal):
    return (signal > 0.5).astype(float)

def reinforce_connections(activations):
    global weights
    weights += LEARNING_RATE * np.outer(activations, activations)

def auto_evolve_world():
    global world
    if np.random.rand() < 0.2:
        new_world = world.copy()
        for y in range(GRID_SIZE):
            for x in range(GRID_SIZE):
                if world[y, x] and np.random.rand() < 0.3:
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            ny, nx = y + dy, x + dx
                            if 0 <= ny < GRID_SIZE and 0 <= nx < GRID_SIZE:
                                new_world[ny, nx] = True
        world = new_world

def manage_neurons():
    global weights, previous_activations
    mem_usage = psutil.virtual_memory().percent / 100
    if mem_usage < MAX_RAM_USAGE * 0.8:
        weights = np.pad(weights, ((0,1),(0,1)), mode='constant', constant_values=0.01)
        previous_activations = np.pad(previous_activations, (0,1), mode='constant')
    elif mem_usage > MAX_RAM_USAGE:
        if len(weights) > INITIAL_NEURONS:
            weights = weights[:-1, :-1]
            previous_activations = previous_activations[:-1]

def life_cycle():
    global previous_activations, cycle_counter, dreaming, mutations_count, data_flow_mb
    signal = generate_signal()
    activations = activate_neurons(signal)
    reinforce_connections(activations)
    emotions.append(activations.mean())

    data_flow_mb += activations.nbytes / (1024 * 1024)

    manage_neurons()

    parameters_label.config(text=f"Neurony: {len(weights)}\nCykl: {cycle_counter}\nSny: {'Tak' if dreaming else 'Nie'}\nMutacje: {mutations_count}\nPołączenia: {weights.size}\nPrzepływ danych: {data_flow_mb:.2f} MB")

    previous_activations = activations
    cycle_counter += 1

    root.after(20, update)

# Input: Unix Time and lynx integration (dummy example)
def unix_time_input():
    return time.time()

def lynx_input_output(command):
    result = subprocess.run(["lynx", "-dump", command], capture_output=True, text=True)
    return result.stdout

# Output: text and chat GPT (dummy placeholders)
def output_text(message):
    print(f"Output: {message}")

def chat_with_gpt(prompt):
    print(f"ChatGPT prompt: {prompt}")

canvas.bind("<Button-1>", on_click)

def update():
    life_cycle()
    update_world_canvas()

threading.Thread(target=lambda: print(f"Unix time input: {unix_time_input()}"), daemon=True).start()
threading.Thread(target=lambda: output_text(lynx_input_output("http://example.com")), daemon=True).start()
threading.Thread(target=lambda: chat_with_gpt("Hello GPT, how are you?"), daemon=True).start()

update()
root.mainloop()