
`pip install pynput` to get keyboard capable interface

`pip install PyQt5` to get Qt5 with python bindings

`pip install pyqt5-tools` to allow for gui creation under:
...\Python36\Lib\site-packages\pyqt5-tools\designer\designer.exe
"C:\Users\~\AppData\Local\Programs\Python\Python36\Lib\site-packages\pyqt5-tools\designer.exe"

` pyuic5 -x *.ui -o *.py` having created your first .ui file

If we apply horizontal/vertical layouts then the gui will scale if we drag it
If we just place the items, they won't move or scale as the window resizes (which we view to be a bad thing)