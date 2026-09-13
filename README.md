# Amino Acid Notebook Exporter

## Overview

This module is designed to save selected amino acids from the cell simulation environment into a Jupyter Notebook (`.ipynb`) file. The generated notebook acts as a biological record of the cell nucleus state at a specific moment in time.

The system automatically:

* Records the current date and time.
* Imports the selected amino acid sequence from the Ribosome module.
* Creates a valid Jupyter Notebook structure.
* Stores amino acid data for future analysis.
* Generates uniquely named notebook files using timestamps.

This allows simulation data to be archived, inspected, and analyzed later within Jupyter environments.

---

## Purpose in the Cell Simulation

Within the larger cell simulation project, the Ribosome module is responsible for amino acid selection and protein synthesis activities.

This exporter functions as a biological "memory archive" by preserving the current amino acid pool generated during simulation runtime.

The generated notebook can be viewed as a digital equivalent of recording protein-building resources available within the nucleus at a specific moment.

---

## Features

### Automatic Timestamp Generation

Each export includes:

* Date
* Time
* Unique file identifier

Example:

```text
13.09.2026 15:42:18
```

---

### Jupyter Notebook Creation

The program creates a complete `.ipynb` file compatible with:

* Jupyter Notebook
* JupyterLab
* VS Code Notebook Interface
* Google Colab

---

### Amino Acid Storage

Selected amino acids imported from the Ribosome module are stored directly inside the notebook.

Example:

```python
selected_amino_acids = ["Methionine", "Alanine", "Lysine"]
```

---

### Automatic Documentation

Each notebook contains:

1. A title page.
2. Export timestamp.
3. Amino acid data.
4. Display code for reviewing stored amino acids.

This allows exported files to remain self-contained and understandable even months later.

---

## Workflow

### Step 1

Import amino acids from the Ribosome system.

```python
from Ribosome import selected
```

### Step 2

Generate timestamp information.

### Step 3

Construct notebook structure using JSON.

### Step 4

Save notebook to disk.

### Step 5

Display exported amino acids in the terminal.

---

## Generated Notebook Structure

The notebook contains:

### Markdown Cell

```markdown
# Selected Amino Acids
Export Date and Time
```

### Data Cell

```python
selected_amino_acids = [...]
```

### Visualization Cell

```python
for amino in selected_amino_acids:
    print(amino)
```

---

## Example Use Cases

* Protein synthesis experiments
* Ribosome activity logging
* Cell-state snapshots
* Amino acid tracking
* Educational biology simulations
* Long-term simulation archives

---

## Future Improvements

Potential future developments include:

* Automatic protein generation reports
* Codon-to-amino-acid translation logs
* DNA transcription records
* Mutation tracking
* Simulation statistics
* CSV and Excel export support
* Integration with NumPy and Pandas
* Automated biological experiment reports

---

## Requirements

Python 3.9+

Standard Libraries:

* datetime
* json
* os

Project Dependency:

* Ribosome.py

No external packages are required.

---

## Author

Created as part of the Project Neuron cell simulation ecosystem.

This module serves as a persistent biological data recorder for ribosome-generated amino acid selections and simulation state tracking.
