# Muminki

Muminki is an experimental Python desktop simulation with a Tkinter dashboard, a mutable neuron matrix, local state persistence and short text fragments fetched from selected Wikipedia pages.

## Entry point

```bash
python muminki.py
```

## Requirements

- Python 3.10 or newer
- Tkinter available in the Python installation
- Packages listed in `requirements.txt`

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

## Local data

The application creates local runtime data:

- `world_state.pkl`
- `muminki_memory/`
- `muminki_dreams/`

These paths are ignored by Git and should not be committed.

`world_state.pkl` uses Python pickle. Load only a state file that you created and trust; pickle is not a safe interchange format for untrusted data.

## Network access

The dream function makes outbound HTTP requests to a fixed list of Polish Wikipedia pages. No OpenAI API call is currently implemented, and no API key is required.

## Building an executable

`muminki.spec` is a PyInstaller configuration. Build output under `build/` and `dist/` is generated and must not be committed.

```bash
python -m pip install pyinstaller
pyinstaller muminki.spec
```

## Status

Experimental. The simulation is not a scientific model of consciousness, cognition or biological neurons.
