import PyInstaller.__main__

PyInstaller.__main__.run([
    'Litho_Abbr_Dict.py',
    '--onefile',
    '--windowed',
    '-i', "abbr.ico",
    '--splash', "abbr.png",
])
