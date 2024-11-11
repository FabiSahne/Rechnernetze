# HTWG Rechnernetze WS24/25 Laboraufgaben

## Einstieg in die Socketprogrammierung
### ${\textsf{\color{gray}(1. Einleitung)}}$
### ${\textsf{\color{gray}(2. Vorbereitung)}}$
### 3. Rechenserver
Client sendet Rechnung im Format \<ID>\<Rechenoperation>\<$n$>\<$z_1$>\<$z_2$>...\<$z_n$> gesendet.
- ID ist ein ${\textsf{\color{lightgreen}u32}}$[^1] und dient als Identifikator.
- Rechenoperation sind ${\textsf{\color{lightgreen}[u8; 3]}}$, entweder "SUM", "PRO", "MIN" oder "MAX" und UTF-8 kodiert.
- $n$ ist ein ${\textsf{\color{lightgreen}u8}}$ und gibt an wie viele Zahlen folgen.
- $z_1$ bis $z_n$ sind ${\textsf{\color{lightgreen}i32}}$ mit welchen gerechnet wird.

Server empfängt die Nachricht, rechnet das Ergebnis aus und sendet es im Format \<ID>\<Ergebnis> zurück.
- ID ist selbiger ${\textsf{\color{lightgreen}u32}}$
- Ergebnis ist das Rechenergebnis eine ${\textsf{\color{lightgreen}i32}}$

#### 3.1 Lokale Kommunikation

#### 3.2 Netzwerk Kommunikation

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