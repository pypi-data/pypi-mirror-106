# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fmod_tool']

package_data = \
{'': ['*']}

install_requires = \
['click-pathlib>=2020.3.13,<2021.0.0',
 'click>=8.0.0,<9.0.0',
 'numpy>=1.20.3,<2.0.0',
 'openpyxl>=3.0.7,<4.0.0',
 'pandas>=1.2.4,<2.0.0',
 'tabulate>=0.8.9,<0.9.0',
 'xlrd>=2.0.1,<3.0.0']

entry_points = \
{'console_scripts': ['tool = fmod_tool.tool:tools']}

setup_kwargs = {
    'name': 'fmod-tool',
    'version': '0.1.0',
    'description': 'A simple tool made to help keep track when correcting exercises for the course "Formale Modellierung"',
    'long_description': '# FMOD Verbesserungstool\n\n## Installation\n\nDieses git repo klonen und `pip install -r requirements.txt` ausführen. Nun kann man mit `python tool.py` in jedem Ordner arbeiten (bitte tool.py in den Arbeitsordner kopieren).\n\n## Nutzung\n\n### Setup\n\nDas Tool benötigt 2 Ordner: `done`, `not_done`. Im `not_done` bitte sämtliche PDFs legen. Die xlsx wo die Punkte hineingehören einfach in den selben Ordner wie `tool.py` legen.\n\nDer Ordner sollte so aussehen:\n\n```\ntool.py\nueXPunkte.xlsx\ndone\nnot_done/\n    3128481VornameNachname.pdf\n    3128481VornameNachname.pdf\n    3128481VornameNachname.pdf\n    3128481VornameNachname.pdf\n    ...\n```\n\n`tool.py` öffnen und die Aufgaben richtig in das `max_p` dictionary eintragen. Die Schlüssel sind die Aufgaben Nummer und der Wert sind die maximalen Punkte.\n\nAnschließend einmal `python tool.py extract` ausführen um die Datei `names.txt` zu generieren wo deine Bewertungen zwischengespeichert werden bevor sie zum Schluss in die Excel-Datei kopiert werden! Falls du manuell etwas ändern musst, kannst du das in der `names.txt` machen!\n\n## Nutzung\n\nMit `python tool.py show` kann man sich die noch nicht fertigen Abgaben anzeigen lassen. Wenn man `python tool.py show -d` macht, sieht man welche schon Abgaben schon fertig sind.\n\nUm den Verbesserungsvorgang zu starten ruft man `python tool.py correct MATNR` auf. Als Ausgabe bekommt man die schon erledigten Abgaben und anschließend die derzeitige Zeile der aktuellen. Das Tool wartet nun auf eine Bewertung für die erste Aufgabe. Hier ist es nun möglich die Abgabe des/der Studenten/in in einem PDF-Editor zu annotieren und nach Verbesserung des ersten Beispiels die Punkte im Tool einzugeben:\n\n```\nMAX POINTS FOR 1 : 3\nEnter Points:2\n```\n\nUnd Enter drücken um die Aufforderung für das nächste Beispiel zu bekommen. Nach jeder Eingabe bekommt man auch die Übersicht der aktuellen Abgabe immer wieder ausgegeben. Falls die Aufgabe mit vollen Punkten gelöst wurde, genügt es auch einfach nur Enter zu drücken ohne eine Zahl einzugeben, es wird die maximale Punkteanzahl eingetragen.\n\nNachdem alle Beispiele verbessert wurden wird die Summe ausgegeben. Diese bitte in die Abgabe annotieren. Das Tool wartet nun auf eine Eingabe. Bevor diese Eingabe passiert, ist es aber nötig die PDF zu speichern und zu schließen, da das Tool als nächstes die PDF laut Schema (also mit _copy.pdf) in den done Ordner verschieben möchte.\n\nZum Schluss werden alle noch nicht verbesserten Abgaben ausgegeben, von denen man sich eine Matrikelnummer für die nächste Verbesserung nehmen kann.\n\nFalls ein Fehler beim korrigieren passiert, kann man das Programm mit Ctrl+C einfach unterbrechen und mit der Abgabe von vorne anfangen.\n\nNachdem alle Abgaben verbessert wurden, nimmt `python tool.py to_xlsx EXCELDATEIPFAD TUTORNAME` die names.txt und trägt alle Ergebnisse *in eine Kopie der Excel Datei* die mit `_done.xlsx` endet ein. Diese liegt im selben Ordner. Es werden noch einmal alle Abgaben ausgegeben als auch ganz rechts deren Summen.\n\nNun ist es nur mehr nötig zu checken ob in der `ueXPunkte_done.xlsx` alles passt, diese umbenennen, in den `done` Ordner zu packen und den ganzen `done` Ordner per Lieblingsprogramm hochzuladen.',
    'author': 'Hurbean Alexander',
    'author_email': 'alexander.hurbean@tuwien.ac.at',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hurbeana/fmod_tool',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
