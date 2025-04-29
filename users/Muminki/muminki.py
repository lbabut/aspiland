# Muminki_Dashboard.py
# Strażnik Muminków – CPU-only, z Dashboard, zapisem/statem i przyciskami

import numpy as np
import tkinter as tk
import psutil
import os
import threading
import time
import random
import requests
import uuid
import pickle
from bs4 import BeautifulSoup

# ─── Constants ──────────────────────────────────────────────────────────────
GRID_SIZE        = 32
INITIAL_NEURONS  = 32
MAX_RAM_USAGE    = 0.65
LEARNING_RATE    = 0.02
MUTATION_RATE    = 0.1
MUTATION_CYCLE   = 100
MEMORY_FOLDER    = "muminki_memory"
DREAM_FOLDER     = "muminki_dreams"
STATE_FILE       = "world_state.pkl"
OPENAI_API_KEY   = "your-openai-api-key-here"

# ─── Globals ────────────────────────────────────────────────────────────────
os.makedirs(MEMORY_FOLDER, exist_ok=True)
os.makedirs(DREAM_FOLDER, exist_ok=True)

world                = np.random.rand(GRID_SIZE, GRID_SIZE) < 0.1
weights              = np.random.randn(INITIAL_NEURONS, INITIAL_NEURONS) * 0.01
emotions             = []
previous_activations = np.zeros(INITIAL_NEURONS)
cycle_counter        = 0
dreaming             = False
mutations_count      = 0
data_flow_mb         = 0
muminki_register     = []

dream_sources = [
    "https://pl.wikipedia.org/wiki/Przyja%C5%BA%C5%84",
    "https://pl.wikipedia.org/wiki/Marzenie",
    "https://pl.wikipedia.org/wiki/Szcz%C4%99%C5%9Bcie",
    "https://pl.wikipedia.org/wiki/Nadzieja",
    "https://pl.wikipedia.org/wiki/Muminki"
]

# ─── Functions ──────────────────────────────────────────────────────────────
def save_world_state():
    with open(STATE_FILE, 'wb') as f:
        pickle.dump({
            "world": world,
            "weights": weights,
            "previous_activations": previous_activations,
            "cycle_counter": cycle_counter
        }, f)
    print("Stan zapisany.")

def load_world_state():
    global world, weights, previous_activations, cycle_counter
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'rb') as f:
            st = pickle.load(f)
            world[:]                = st["world"]
            weights[:]              = st["weights"]
            previous_activations[:] = st["previous_activations"]
            cycle_counter           = st["cycle_counter"]
        print("Stan wczytany.")
    else:
        print("Brak zapisu, start nowego świata.")

def clean_text_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    for tag in soup(["script","style"]): tag.decompose()
    text = soup.get_text()
    lines = (ln.strip() for ln in text.splitlines())
    chunks = (ph for ln in lines for ph in ln.split("  "))
    return "\n".join(ch for ch in chunks if ch)

def read_from_web_and_dream():
    try:
        url = random.choice(dream_sources)
        r = requests.get(url, timeout=10); r.raise_for_status()
        txt = clean_text_from_html(r.text)
        snippet = random.choice(txt.split("\n"))[:200]
        current_gpt_response.set(f"Marzenie: {snippet}")
    except Exception as e:
        current_gpt_response.set(f"Błąd marzenia: {e}")

def manage_neurons():
    global weights, previous_activations
    mu = psutil.virtual_memory().percent / 100
    if mu < MAX_RAM_USAGE*0.8:
        weights[:]              = np.pad(weights, ((0,1),(0,1)), 'constant', constant_values=0.01)
        previous_activations[:] = np.pad(previous_activations, (0,1), 'constant')
    elif mu > MAX_RAM_USAGE and weights.shape[0] > INITIAL_NEURONS:
        weights[:]              = weights[:-1,:-1]
        previous_activations[:] = previous_activations[:-1]

def create_muminek():
    muminki_register.append(str(uuid.uuid4()))

def on_click(event):
    x,y = event.x//CELL_SIZE, event.y//CELL_SIZE
    if 0<=x<GRID_SIZE and 0<=y<GRID_SIZE:
        world[y,x] = not world[y,x]

def update_world_canvas(bright=False):
    canvas.delete("all")
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if world[y,x]:
                r,g,b = [random.randint(100,255) for _ in range(3)]
            else:
                r=g=b=0
            if bright:
                r,g,b = min(255,r+50),min(255,g+50),min(255,b+50)
            col = f"#{r:02x}{g:02x}{b:02x}"
            canvas.create_rectangle(x*CELL_SIZE,y*CELL_SIZE,
                                    (x+1)*CELL_SIZE,(y+1)*CELL_SIZE,
                                    fill=col, outline="")

def generate_signal():
    flat = world.flatten().astype(float)
    n    = previous_activations.size
    if flat.size < n:
        flat = np.pad(flat,(0,n-flat.size),'constant')
    return 0.5*flat[:n] + 0.5*previous_activations

def activate_neurons(sig):
    return (sig>0.5).astype(float)

def reinforce_connections(act):
    global weights
    n = weights.shape[0]
    if act.size!=n:
        act = np.pad(act,(0,n-act.size),'constant')
    weights[:] += LEARNING_RATE * np.outer(act,act)

def mutate_weights():
    global weights, mutations_count
    noise = np.random.randn(*weights.shape)*MUTATION_RATE
    weights[:] += noise
    mutations_count +=1

def life_cycle():
    global previous_activations, cycle_counter, dreaming, data_flow_mb
    sig = generate_signal()
    act = activate_neurons(sig)
    reinforce_connections(act)
    emotions.append(act.mean())
    data_flow_mb += act.nbytes/(1024*1024)
    manage_neurons()
    if cycle_counter%200==0: create_muminek()
    if cycle_counter%MUTATION_CYCLE==0: mutate_weights()
    if dreaming:
        save_world_state(); dreaming=False
    memp = psutil.virtual_memory().percent
    con  = np.count_nonzero(weights)
    parameters_label.config(
        text=(f"Neurony: {weights.shape[0]}\n"
              f"Cykl: {cycle_counter}\n"
              f"Mutacje: {mutations_count}\n"
              f"Połączenia: {con}\n"
              f"Muminki: {len(muminki_register)}\n"
              f"Dane: {data_flow_mb:.2f} MB\n"
              f"RAM: {memp:.1f}%")
    )
    previous_activations[:] = act
    cycle_counter +=1
    root.after(20, update)

def refresh_unix_time():
    while True:
        current_unix_time.set(f"Unix time: {int(time.time())}")
        time.sleep(random.randint(5,12))

def auto_dreams():
    while True:
        time.sleep(random.randint(60,120))
        read_from_web_and_dream()

def update():
    life_cycle()
    update_world_canvas()

# ─── GUI Setup ─────────────────────────────────────────────────────────────────
root = tk.Tk()
root.title("Muminki – Świat & Dashboard")
CELL_SIZE = min(root.winfo_screenwidth(), root.winfo_screenheight()) // GRID_SIZE

# Canvas
canvas = tk.Canvas(root, width=GRID_SIZE*CELL_SIZE, height=GRID_SIZE*CELL_SIZE, bg="black")
canvas.grid(row=0, column=0, padx=10, pady=10)

# Dashboard frame
dash = tk.Frame(root)
dash.grid(row=0, column=1, sticky="n")

# StringVars
current_unix_time   = tk.StringVar()
current_gpt_response= tk.StringVar()

# Dashboard widgets
tk.Button(dash, text="Wczytaj stan", command=load_world_state).pack(fill="x", pady=2)
tk.Button(dash, text="Zapisz stan", command=save_world_state).pack(fill="x", pady=2)
tk.Button(dash, text="Marzenia",  command=read_from_web_and_dream).pack(fill="x", pady=2)
parameters_label = tk.Label(dash, justify="left")
parameters_label.pack(pady=5)
tk.Label(dash, textvariable=current_unix_time).pack(pady=2)
tk.Label(dash, textvariable=current_gpt_response, wraplength=200, justify="left").pack(pady=2)

# Bind click
canvas.bind("<Button-1>", on_click)

# Load previous state
load_world_state()

# Background threads
threading.Thread(target=refresh_unix_time,   daemon=True).start()
threading.Thread(target=auto_dreams,          daemon=True).start()

# Start sim & GUI
update()
root.mainloop()
