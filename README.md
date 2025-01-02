# HTWG Rechnernetze WS24/25 Laboraufgaben

## Einstieg in die Socketprogrammierung

### ${\textsf{\color{gray}(1. Einleitung)}}$
### ${\textsf{\color{gray}(2. Vorbereitung)}}$
### 3. Rechenserver
Client sendet Rechnung im Format \<ID>\<Rechenoperation>\< $n$ >\< $z_1$ >\< $z_2$ >...\< $z_n$ > gesendet.
- ID ist ein ${\textsf{\color{lightgreen}u32}}$[^1] und dient als Identifikator.
- Rechenoperation sind ${\textsf{\color{lightgreen}[u8; 3]}}$, entweder "SUM", "PRO", "MIN" oder "MAX" und UTF-8 kodiert.
- $n$ ist ein ${\textsf{\color{lightgreen}u8}}$ und gibt an wie viele Zahlen folgen.
- $z_1$ bis $z_n$ sind ${\textsf{\color{lightgreen}i32}}$ mit welchen gerechnet wird.

Server empfängt die Nachricht, rechnet das Ergebnis aus und sendet es im Format \<ID>\<Ergebnis> zurück.
- ID ist selbiger ${\textsf{\color{lightgreen}u32}}$
- Ergebnis ist das Rechenergebnis eine ${\textsf{\color{lightgreen}i32}}$

#### 3.1 Lokale Kommunikation
|Time     |Scr Prt|Dst Port|Info      |Script|Befehl   |blockierender Befehl|
|:--------|:------|:-------|:---------|:-----|:--------|:-------------------|
|4.066763 |55048  |12345   |[SYN]     |Client|`connect`|`accept`            |
|4.066797 |12345  |55048   |[SYN][ACK]|Server|`accept` |`connect`           |
|4.066815 |55048  |12345   |[ACK]     |Client|         |                    |
|11.182750|55048  |12345   |[PSH][ACK]|Client|`send`   |`recv`              |
|11.182788|12345  |55048   |[ACK]     |Server|         |                    |
|11.183160|12345  |55048   |[PSH][ACK]|Server|`send`   |`recv`              |
|11.183179|55048  |12345   |[ACK]     |Client|         |                    |
|11.183204|12345  |55048   |[FIN][ACK]|Server|`close`  |                    |
|11.183215|55048  |12345   |[ACK]     |Client|         |                    |
|11.194491|55048  |12345   |[FIN][ACK]|Client|`close`  |                    |
|11.194567|12345  |55048   |[ACK]     |Server|         |                    |


#### 3.2 Netzwerk Kommunikation
1. Wie können Sie im Client Skript die IP-Adresse und Port-Nummer des verwendeten lokalen Sockets bestimmen?
    - `(addr, port) = socket.getaddrinfo()`
2. Wann und woher erhält ein Client seine IP-Adresse und Port-Nummer?
    - `socket.connect((IP, PORT))`
    - Vom Betriebsystem
3. Wie können Sie im Client Skript die IP-Adresse und Port-Nummer bestimmen?
    - Des Clients gar nicht.
    - Die IP und den Port zum zu verbindenden Server mit `socket.connect((IP, PORT))`
4. Warum müssen Sie Timeouts verwenden und wie funktioniert `try except`? Mit welchem Befehl können Sie einen gemeinsamen Timeout für alle Sockets setzen?
    - Man muss keine Timeouts benutzen, der Server hängt dann nur leider für immer, falls nie eine Verbindung kommt.
    - `try` führt Code aus, und falls dieser fehlschlägt wird der Code im `except` Block ausgefürt.
    - `socket.setdefaulttimeout(time)`
5. Kann man einen Server betreiben, der ECHO-Anfragen auf dem gleichen Port für UDP und TCP beantwortet?
    - Nein, es folgt der Fehler: "`OSError: [WinError 10048] Only one usage of each socket address (protocol/network address/port) is normally permitted`"

#### 3.3 Unterstützung für mehrere Clients
Siehe `rechenserver-multithreaded.py`.

### 4. Portscan
#### ${\textsf{\color{gray}4.1 Beschreibung}}$

#### 4.2 Versuch
##### 4.2.1 TCP Port Scanner und 4.2.2 UDP Port Scanner
Siehe `port-scanner.py`.

#### 4.3 Fragen
Fragen
##### 1. Geben Sie die Liste der offenen Ports an.
|Port|TCP        |UDP        |
|---:|:----------|:----------|
|1   |no response|no response|
|2   |no response|no response|
|3   |no response|no response|
|4   |no response|no response|
|5   |no response|no response|
|6   |no response|no response|
|7   |open       |open       |
|8   |no response|no response|
|9   |open       |no response|
|10  |no response|no response|
|11  |no response|no response|
|12  |no response|no response|
|13  |open       |open       |
|14  |no response|no response|
|15  |no response|no response|
|16  |no response|no response|
|17  |open       |open       |
|18  |no response|no response|
|19  |open       |no response|
|20  |no response|no response|
|21  |no response|no response|
|22  |no response|no response|
|23  |no response|no response|
|24  |no response|no response|
|25  |no response|no response|
|26  |no response|no response|
|27  |no response|no response|
|28  |no response|no response|
|29  |no response|no response|
|30  |no response|no response|
|31  |no response|no response|
|32  |no response|no response|
|33  |no response|no response|
|34  |no response|no response|
|35  |no response|no response|
|36  |no response|no response|
|37  |no response|no response|
|38  |no response|no response|
|39  |no response|no response|
|40  |no response|no response|
|41  |no response|no response|
|42  |no response|no response|
|43  |no response|no response|
|44  |no response|no response|
|45  |no response|no response|
|46  |no response|no response|
|47  |no response|no response|
|48  |no response|no response|
|49  |no response|no response|
|50  |no response|no response|

##### 2. Wählen Sie für TCP und UDP jeweils einen offenen und einen geschlossenen Port und erklären Sie die entsprechende Paketsequenz, die Sie in Wireshark aufgezeichnet haben.
Client sendet SYN
Server antwortet mit SYN-ACK
Client sendet ACK
Verbindung etabliert

TCP geschlossen (z.B. Port 8):

Client sendet SYN
Server antwortet mit RST-ACK
Verbindungsaufbau abgebrochen

UDP offen (Port 7):

Client sendet UDP-Datagramm
Server antwortet mit UDP-Datagramm

UDP geschlossen (die meisten anderen Ports):

Client sendet UDP-Datagramm
Keine Antwort (Timeout)

##### 3. Auf Port 7 des Servers läuft ein Echo-Dienst. Testen Sie ihr Client-Skript mit dem Echo-Server. Versuchen Sie das TCP und das UDP Skript.
=== TCP ECHO Test ===
Verbindungsaufbau zu 141.37.168.26:7 (TCP)...
Verbindung hergestellt!
Sende Nachricht: Hello ECHO Server!
Empfangene Antwort: Hello ECHO Server!

=== UDP ECHO Test ===
Sende Nachricht an 141.37.168.26:7 (UDP): Hello ECHO Server!
Empfangene Antwort von ('141.37.168.26', 7): Hello ECHO Server!
### 5. Mail
#### 5.1 SMTP über OpenSSL
Das Folgen der Anleitung hat super funktioniert, habe sowohl Emails normal an mich selbst als auch von einer "fake email" an mich selbst senden können.
#### 5.2 SMTP über Python
Implementierung siehe `smtp.py`.

[^1]: Datentypen sind, der Kürze halber und um Verwechslungen zu vermeiden, wie in Rust angegeben.
