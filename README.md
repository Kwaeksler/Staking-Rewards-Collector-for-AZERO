<a name="English"/><br />
# Staking-Rewards-Collector for Aleph Zero
Go to german installation guide: [GER](#German)  
### Inhaltsverzeichnis
1. [Description](#Description)  
2. [Requirements](#Requirements)
3. [Installation](#InstallationEN)
4. [Configuration](#Configuration)
5. [Execution](#Execution)
6. [Implementation in MS Excel (Office365)](#ExcelImplementation)
7. [Refresh Data](#RefreshData)

 
<a name="Description"/><br />

## Description
The Staking-Rewards-Collector creates a report (JSON file) with all staking rewards information for Aleph Zero. Information is retrieved via the API from Subscan.io. Optionally, prices can be included in the JSON file, which are queried via the API from CoinGecko.com. The goal is to integrate the JSON file into Microsoft Excel.

![grafik](https://user-images.githubusercontent.com/22911401/173590784-0434f89d-3959-423e-8e5a-971885fac5dd.png)

<a name="Requirements"/><br />

## Requirements

#### Python - Installation
The Staking-Rewards-Collector is written in Pyhton. Phyton must be installed on the end device to run:
`https://www.python.org/downloads`

#### Python - Packages
For the HTTP/HTTPS queries the Pyhton package "Requests" is additionally required, installation under Windows:
```
WIN + R
cmd.exe
pip install requests
```
<a name="InstallationEN"/><br />

## Installation of the Staking-Rewards-Collector
#### Manuel installation
Download the current GitHub repository at: <br /> `https://github.com/Kwaeksler/Staking-Rewards-Collector-for-AZERO` > `Code` > `Download ZIP`
<br /><br />
Unzip the ZIP file and save it to a desired location.

#### Installation via Git
```
git clone https://github.com/Kwaeksler/Staking-Rewards-Collector-for-AZERO.git
```

<a name="Configuration"/><br />

## Configuration
In the file `StakingAzero.py` in the area `Configuration` the program must be configured. For this the values of the variables must be adjusted (*The file can be opened with any editor*):

Variable | Required | Explanation
--- | --- | ---
API_Key | `Optional` | *The API key for Subscan.io can/should be entered here. Depending on the frequency of the query, an API key is required (key can be requested under `https://support.subscan.io`).*
Wallet_Address | `Required` | *Account/Wallet address where the rewards will be paid out to.*

<br />

Additionally, the functionality of the program can be changed:
Variable | Possible configuration | Explanation
--- | --- | ---
File_Name | ` ... ` | *Specification of any string for the file name, without file extension! Default: `Rewards`*
Prices | `'Fast'` <br /> `'Accurate'` <br /> `'No'` | *`'Fast':` "Inaccurate" daily prices are included in the file (*fast*)<br />`'Accurate':` "More accurate" prices are included in the file - average value of prices +-2h before/after event time (*slow*) <br />`'No':` No prices are included (*fastest*)*
Only_Updates | `True` <br /> `False` | *`True:` Existing file will be read. Only missing rewards will be added<br />`False:`Complete reward history will be updated*
Debug | `True` <br /> `False` | *`True:` The terminal window remains open after the script is finished to view the history and any errors that occur<br />`False:`The terminal window will be closed after the script is finished*

(*The free API of CoinGecko.com allows only about 50 queries per minute. If the variable `Prices` is set to `Accurate`, the program will be interrupted more often, because much more information is retrieved there.*)

(*By using the `Only_Updates` mode the prices can be adjusted manually in the JSON file if the prices should be too inaccurate. The manual changes will not be overwritten in this mode when run again.*)

<a name="Execution"/><br />

## Execution
The program can be executed by double-clicking on the file `StakingAzero.py`. 
<br />
Alternatively via command line: `py StakingAzero.py`

<a name="ExcelImplementation"/><br />

## Implementation in Microsoft Excel (Office 365)
It is recommended to insert a new spreadsheet for implementation and implement the JSON file there:
<br />
`Data` > `Get Data` > `From File` > `From JSON` > `Select *.JSON-File` > `Import`
<br /><br />
Transform the Rewards `to Table`:
- Select or enter delimiter: `None`
- How to handle extra columns: `Show as errors`

#### Customize column names, columns & order:
![grafik](https://user-images.githubusercontent.com/22911401/172082397-94196be0-ae65-415b-87af-88a120317a54.png)
- Via the symbol next to "Column1" the original column names can be shown (left picture)
- Here you have to uncheck 'Use original column name as prefix' (middle image)
- Columns that are not needed can be hidden (middle image)
- By right-clicking on a column header, individual columns can be moved in the order (right image)

The dialog can be closed by clicking the `Close & Load` button. Afterwards a dynmaic table should appear on the spreadsheet, which can be formatted.

<a name="RefreshData"/><br />

## Refresh data
Running the `StakingAzero.py` file will update the .JSON file. 
<br />
Then, in Microsoft Excel, the previously inserted table can be updated via `Data` > `Update all`.

<br />
<hr style="border:2px solid gray">
<br /><br /><br /><br />
<a name="German"/><br />

# Staking-Rewards-Collector für Aleph Zero
Go to english installation guide: [ENG](#English)  
### Inhaltsverzeichnis
1. [Beschreibung](#Beschreibung)  
2. [Voraussetzungen](#Voraussetzungen)
3. [Installation](#Installation)
4. [Konfiguration](#Konfiguration)
5. [Ausführung](#Ausführung)
6. [Implementierung in MS Excel (Office365)](#ExcelImplementierung)
7. [Daten aktualisieren](#DatenAktualisieren)

 
<a name="Beschreibung"/><br />

## Beschreibung
Der Staking-Rewards-Collector erstellt ein Report (JSON-Datei) mit allen Staking-Reward-Informationen für Aleph Zero. Informationen werden über die API von Subscan.io abgefragt. Optional können Preise mit in die JSON-Datei aufgenommen werden, welche über die API von CoinGecko.com abgefragt werden. Ziel ist die Einbindung der JSON-Datei in Microsoft Excel, um dort einen Steuerbericht zu erstellen.

![grafik](https://user-images.githubusercontent.com/22911401/173590854-4cc92d73-8ffd-4654-8437-ad55a4a125e5.png)

<a name="Voraussetzungen"/><br />

## Voraussetzungen

#### Python - Installation
Der Staking-Rewards-Collector ist in Pyhton programmiert, Phyton muss zur Ausführung auf dem Endgerät installiert sein:
`https://www.python.org/downloads`

#### Python - Packages
Für die HTTP/HTTPS-Abfragen wird zusätzlich das Pyhton-Paket "Requests" benötigt, Installation unter Windows:
```
WIN + R
cmd.exe
pip install requests
```
<a name="Installation"/><br />

## Installation des Staking-Rewards-Collectors
#### Manuelle Installation
Download des aktuellen GitHub Repositories unter: <br /> `https://github.com/Kwaeksler/Staking-Rewards-Collector-for-AZERO` > `Code` > `Download ZIP`
<br /><br />
Die ZIP-Datei entpacken und an einen gewünschten Ort abspeichern.

#### Installation via Git
```
git clone https://github.com/Kwaeksler/Staking-Rewards-Collector-for-AZERO.git
```

<a name="Konfiguration"/><br />

## Konfiguration
In der Datei `StakingAzero.py` im Bereich `Configuration` muss das Programm konfiguriert werden, dazu müssen die Werte der Variablen angepasst werden (*Die Datei kann mit jedem beliebigen Editor geöffnet werden*):

Variable | Notwendigkeit | Erläuterung
--- | --- | ---
API_Key | `Optional` | *Hier kann/sollte der API-Key für Subscan.io eingetragen werden. Je nach Häufigkeit der Abfrage wird ein API-Key benötigt (Key kann unter `https://support.subscan.io` beantragt werden).*
Wallet_Address | `Erforderlich` | *Account/Wallet-Adresse, auf der die Rewards ausgezahlt werden*

<br />

Zusätzlich kann die Funktionalität des Programmes verändert werden:
Variable | Mögliche Konfiguration | Erläuterung
--- | --- | ---
File_Name | ` ... ` | *Angabe einer beliebigen Zeichenkette für den Dateinamen, ohne Dateiendung! Default: `Rewards`*
Prices | `'Fast'` <br /> `'Accurate'` <br /> `'No'` | *`'Fast':` "Ungenauere" Tagespreise werden in die Datei mit aufgenommen (*schnell*)<br />`'Accurate':` "Genauere" Preise werden in die Datei mit aufgenommen - Durchschnittswert der Preise +-2h vor/nach Event-Zeitpunkt (*langsam*) <br />`'No':` Keine Preise werden mit aufgenommen (*am schnellsten*)*
Only_Updates | `True` <br /> `False` | *`True:` Bestehende Datei wird ausgelesen, nur fehlende Rewards werden hinzugefügt<br />`False:`Kompletter Reward-Verlauf wird neu aktualisiert*
Debug | `True` <br /> `False` | *`True:` Das Terminal-Fenster bleibt nach Beendigung des Skriptes geöffnet, um den Verlauf und auftretende Fehler einzusehen<br />`False:`Das Terminal-Fenster wird nach Beendigung des Skriptes geschlossen*

(*Die freie API von CoinGecko.com erlaubt nur ca. 50 Abfragen pro Minute. Wird die Variable `Prices` auf `Accurate` gesetzt, wird das Programm öfter untebrochen, da dort wesentlich mehr Informationen abgerufen werden.*)

(*Durch den `Only_Updates`-Modus können die Preise manuell in der JSON-Datei angepasst werden, falls die Preise zu ungenau sein sollten. Die manuellen Änderungen werden in diesem Modus bei erneuter Ausführung nicht überschrieben.*)

<a name="Ausführung"/><br />

## Ausführung
Das Programm kann durch einen Doppelklick auf die Datei `StakingAzero.py` ausgeführt werden. 
<br />
Alternativ über die Kommandozeile: `py StakingAzero.py`

<a name="ExcelImplementierung"/><br />

## Implementierung in Microsoft Excel (Office 365)
Es ist empfehlenswert ein neues Tabellenblatt für die Implementierung einzufügen und dort die JSON-Datei zu implementieren:
<br />
`Daten` > `Daten abrufen` > `Aus Datei` > `Von JSON` > `*.JSON-Datei auswählen` > `Importieren`
<br /><br />
Im geöffneten Listentool die Rewards `Zu Tabelle` konvertieren:
- Trennzeichen eingeben oder auswählen: `Keine`
- Behandlung zusätzlicher Spalten: `Als Fehler anzeigen`

#### Spaltennamen, Spalten & Reihenfolge anpassen:
![grafik](https://user-images.githubusercontent.com/22911401/172082397-94196be0-ae65-415b-87af-88a120317a54.png)
- Über das Symbol neben "Column1" lassen sich die originalen Spaltennamen einblenden (linkes Bild)
- Hier muss der Haken bei `Ursprünglichen Spaltennamen als Präfix verwenden` entfernt werden (mittleres Bild)
- Nicht benötigte Spalten können ausgeblendet werden (mittleres Bild)
- Durch einen Rechtsklick auf eine Spaltenüberschrift lassen sich einzelne Spalten in der Reihenfolge verschieben (rechtes Bild)

Der Dialog kann durch Klick auf die Schaltfläche `Schließen & laden` beendet werden. Anschließend sollte eine dynmaische Tabelle auf dem Tabellenblatt erscheinen, welche formatiert werden kann.

<a name="DatenAktualisieren"/><br />

## Daten aktualisieren
Durch das Ausführen der `StakingAzero.py`-Datei wird die .JSON-Datei aktualisiert. 
<br />
Anschließend kann in Microsoft Excel die vorher eingefügte Tabelle über `Daten` > `Alle Aktualisieren` aktualisiert werden.

