import PyInstaller.__main__

PyInstaller.__main__.run([
    'Litho_Abbr_Dict.py',
    '--onefile',
    '--windowed',
    '--add-data', 'src;src',
    '-i', ".\src\\abbr.ico",
    '--splash', ".\src\\abbr.png",
])
