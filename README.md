## Usage

```bash
# Run script
python Litho_Abbr_Dict.py


# Compiled with Pyinstaller

# Windows
pyinstaller --onefile --windowed Litho_Abbr_Dict.py
pyinstaller --onefile --windowed --add-data 'src;src' Litho_Abbr_Dict.py
pyinstaller --add-data 'src;src' -i ".\src\las.ico" --onefile --windowed Litho_Abbr_Dict.py
```

- Version: 1.0.0
- License: MIT
- Author: Mero2online
