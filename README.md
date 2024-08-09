# Game of Life
Zero-player game, aka cellural automation. That means, game plays itself, without interaction by player and simulates very simple "evolution".

# Features
* Simulate evolution of cells
* Create own cells to start evolution
* Fill board with cells by random
* Start/Stop game
* Iterate through stopped game step-by-step

# Requirements
* **Python 3.12** (probably can be lower, but not tested)
* **Poetry**
* ***GNU Make*** (optional)

# Installation
1. Clone the repository:

```bash
git clone https://github.com/KreenGG/game-of-life.git
cd game-of-life
```
2. Install python requerements via poetry:

```bash
poetry install
```
3. Start game:

```bash
# With GNU Make installed
make run

# or simply run
python src/main.py
``` 

## Config
You can modify `config.py` for changing, for example, density of random cells on start.