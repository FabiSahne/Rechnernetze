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

### 4. Portscan
#### ${\textsf{\color{gray}4.1 Beschreibung}}$

#### 4.2 Versuch
##### 4.2.1 TCP Port Scanner

##### 4.2.2 UDP Port Scanner

#### 4.3 Fragen

### 5. Mail
#### 5.1 SMTP über OpenSSL

#### 5.2 SMTP über Python

[^1]: Datentypen sind, der Kürze halber und um Verwechslungen zu vermeiden, wie in Rust angegeben.
