# Extrahieren bestimmter Seiten aus einer PDF-Datei
Das Python Skript `PDF_sep_pages.py` extrahiert aus einer vorhandenen PDF-Datei definierte Seiten und speichert diese in einer neuen PDF Datei.

## Abhängigkeiten
Bei der Ausführung des Skripts werden folgende Module genutzt, die auf dem Rechner vorab installiert sein müssen
- PyPDF2
- os
- sys

Die Module <i>os</i> und <i>sys</i> kommen mit Python standardmäßig, das Modul <i>PyPDF2</i> kann mit dem Befehl 
```
pip install PyPDF2  
```
installiert werden.

## Aufruf über die Konsole
Das Skript kann über die Konsole aufgerufen werden.
Der Befehl heirfür ist in folgender Form aufgebaut:
```
python PDF_sep_pages.py <start_page> <end_page>
```
Die Angabe der Argumente <start_page> und <end_page> ist optional. Wenn nur ein Argument <start_page> übergeben wird, dann wird nur die angegebene Seite extrahiert.<br>
Wenn das Argument <start_page> nicht übergeben wird, dann wird es im Skript mit dem Wert 1 angenommen und nur die erste Seite des Dokuments extrahiert und abgespeichert.

## Dateiname der neuen Datei
Das Python Skript speichert die neue Datei automatisch, wobei sich der Dateiname aus dem Namen der vorhandenen Datei und den zu extrahierenden Seiten zusammensetzt.<br>
```
<Dateiname>_p<start_page>_to_<end_page>
```
Wenn für das Argument <end_page> nichts übergeben wird, dann ergibt sich der neue Dateiname zu
```
<Dateiname>_p<start_page>
```

## Beispiel
Aus dem Dokument <b>example.pdf</b> sollen die Seiten 1 bis 2 extrahiert und in einer neuen PDF-Datei gespeichert werden.
Der Befehl hierfür lautet:
```
python PDF_sep_pages.py example.pdf 1 2
```
Das Skript speichert im Verzeichnis der Originaldatei eine neue Datei mit dem Dateinamen <b>example_p1_to_2.pdf</b>, die die extrahierten Seiten enthält.<br>

## Fragen, Probleme und Weiterentwicklung
Das Skript kann auf Anfrage gerne weiterentwickelt werden. Bitte kontaktieren Sie mich dazu über GitHub.
