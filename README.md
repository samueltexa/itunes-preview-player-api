# itunes-preview-player-api
A Python script to search for songs on iTunes and play 30-second previews using VLC

---

## Requirements

- Python 3.x
- requests library
- vlc library
- VLC media player

## Installation

1. **Python**: Install Python 3.x from [python.org](https://www.python.org/).

2. **Libraries**: Install the required Python libraries using pip:
   ```bash
   pip install requests python-vlc
   ```

3. **VLC Media Player**: Ensure VLC media player is installed on your system. You can download it from [videolan.org](https://www.videolan.org/).

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/samueltexa/itunes-preview-player-api.git
   ```

2. Navigate into the repository directory:
   ```bash
   cd itunes-preview-player-api
   ```

3. Run the script with the search term as an argument:
   ```bash
   python randoms.py <search_term>
   ```

   Replace `<search_term>` with the term you want to search for on iTunes.

   Example:
   ```bash
   python ituneApi.py Gomezi
   ```

## Features

- Searches iTunes for songs based on the provided search term.
- Plays 30-second preview clips of the found songs using VLC media player.
- Simple command-line interface for easy interaction.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
