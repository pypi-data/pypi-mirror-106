# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fmod_tool']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0',
 'click-pathlib>=2020.3.13,<2021.0.0',
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
    'version': '0.1.9',
    'description': 'A simple tool made to help keep track when correcting exercises for the course "Formale Modellierung"',
    'long_description': '# FMOD Verbesserungstool\n\n## Installation\n\nDas tool lässt sich über pip für Python >3.7.1<=3.9 mit `pip install fmod_tool` installieren.\n\n### DEV\n\nDieses git repo klonen und `poetry install` ausführen (poetry nötig). Nun kann man mit `tool` in jedem Ordner arbeiten\nund weiter am Projekt arbeiten.\n\n## Nutzung\n\n### Setup\n\nDas Tool benötigt 2 Ordner: `done`, `not_done`. Im `not_done` bitte sämtliche PDFs legen. Die Excel Datei sollte nicht\nim `not_done` Ordner sein, verursacht aber keine Probleme.\n\nDer Ordner sollte so aussehen:\n\n```\nueXPunkte.xlsx\ndone\nnot_done/\n    3128481VornameNachname.pdf\n    3128481VornameNachname.pdf\n    3128481VornameNachname.pdf\n    3128481VornameNachname.pdf\n    ...\n```\n\nNach dem ersten mal ausführen von `tool` wird eine `settings.yml` erstellt. Diese bitte öffnen und bearbeiten\n(Punkte eintragen und Präfenz für Abschluss nach Korrektur festlegen).\n\nAnschließend einmal `tool extract` ausführen um die Datei `names.txt` zu generieren wo deine Bewertungen\nzwischengespeichert werden bevor sie zum Schluss in die Excel-Datei kopiert werden! Falls du manuell etwas ändern musst,\nkannst du das in der `names.txt` machen!\n\n## Nutzung\n\nMit `tool show` kann man sich die noch nicht fertigen Abgaben anzeigen lassen. Wenn man `tool show -d` macht, sieht man\nwelche schon Abgaben schon fertig sind.\n\nUm den Verbesserungsvorgang zu starten ruft man `tool correct MATNR` auf. Als Ausgabe bekommt man die schon erledigten\nAbgaben und anschließend die derzeitige Zeile der aktuellen. Das Tool wartet nun auf eine Bewertung für die erste\nAufgabe. Hier ist es nun möglich die Abgabe des/der Studenten/in in einem PDF-Editor zu annotieren und nach Verbesserung\ndes ersten Beispiels die Punkte im Tool einzugeben:\n\n```\nMAX POINTS FOR 1 : 3\nEnter Points:2\n```\n\nUnd Enter drücken um die Aufforderung für das nächste Beispiel zu bekommen. Nach jeder Eingabe bekommt man auch die\nÜbersicht der aktuellen Abgabe immer wieder ausgegeben. Falls die Aufgabe mit vollen Punkten gelöst wurde, genügt es\nauch einfach nur Enter zu drücken ohne eine Zahl einzugeben, es wird die maximale Punkteanzahl eingetragen.\n\nNachdem alle Beispiele verbessert wurden wird die Summe ausgegeben. Diese bitte in die Abgabe annotieren und die PDF\nspeichern (oder eine Kopie in `done` speichern). Das Tool wartet nun auf eine Eingabe. Nachdem Eingabe gedrückt wird,\ngeschieht jetzt das was in `settings.yml` gewählt wurde:\n\n- "NOTHING": Die Original PDF bleibt im `not_done` Ordner (schlecht, da das `show` command damit durcheinander kommt)\n- "REMOVE": Die Original PDF wird aus dem `not_done` Ordner gelöscht (standard, somit wird `show` richtig berechnet).\n  Diese Option nutzen, falls man die PDF nicht in-place editiert und stattdessen die Kopie selbst in `done` speichert.\n- "RENAME": Die Original PDF wird aus `not_done` nach `done` verschoben und ein `_copy.pdf` wird angehangen\n  Diese Option nutzen, falls man die PDF in-place verändert und das Original nun die Annotationen hat.\n\nZum Schluss werden alle noch nicht verbesserten Abgaben ausgegeben, von denen man sich eine Matrikelnummer für die\nnächste Verbesserung nehmen kann.\n\nFalls ein Fehler beim korrigieren passiert, kann man das Programm mit Ctrl+C einfach unterbrechen und mit der Abgabe von\nvorne anfangen.\n\nNachdem alle Abgaben verbessert wurden, nimmt `tool to_xlsx EXCELDATEIPFAD TUTORNAME` die names.txt und trägt\nalle Ergebnisse *in eine Kopie der Excel Datei* die mit `_done.xlsx` endet ein. Diese liegt im selben Ordner. Es werden\nnoch einmal alle Abgaben ausgegeben als auch ganz rechts deren Summen.\n\nNun ist es nur mehr nötig zu checken ob in der `ueXPunkte_done.xlsx` alles passt, diese umbenennen, in den `done` Ordner\nzu packen und den ganzen `done` Ordner per Lieblingsprogramm hochzuladen.\n\n### Anmerkungen\n\nFür jedes Kommando gibt es eine kurze Help die man mit sich anzeigen lassen kann indem man `--help` anhängt.\n\nJede/r ist eingeladen am Projekt zu helfen indem er/sie das Projekt auf Github forked und Vorschläge auf dem Fork macht.\nAnschließend per Pull Request diese Änderungen vorschlagen! Danke vielmals für jegliche Hilfe.\n\nBei Fragen oder Bugs im Repo ein Ticket öffnen oder mir eine Email schreiben!',
    'author': 'Hurbean Alexander',
    'author_email': 'alexander.hurbean@tuwien.ac.at',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hurbeana/fmod_tool',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7.1',
}


setup(**setup_kwargs)
