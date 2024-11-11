# HTWG Rechnernetze WS24/25 Laboraufgaben

## Einstieg in die Socketprogrammierung
### <span style="color:gray">(1. Einleitung)</span>
### <span style="color:gray">(2. Vorbereitung)</span>
### 3. Rechenserver
Client sendet Rechnung im Format \<ID>\<Rechenoperation>\<$n$>\<$z_1$>\<$z_2$>...\<$z_n$> gesendet.
- ID ist ein <span style="color:lightgreen">u32</span>[^1] und dient als Identifikator.
- Rechenoperation sind <span style="color:lightgreen">[u8; 3]</span>, entweder "SUM", "PRO", "MIN" oder "MAX" und UTF-8 kodiert.
- $n$ ist ein <span style="color:lightgreen">u8</span> und gibt an wie viele Zahlen folgen.
- $z_1$ bis $z_n$ sind <span style="color:lightgreen">i32</span> mit welchen gerechnet wird.

Server empfängt die Nachricht, rechnet das Ergebnis aus und sendet es im Format \<ID>\<Ergebnis> zurück.
- ID ist selbiger <span style="color:lightgreen">u32</span>
- Ergebnis ist das Rechenergebnis eine <span style="color:lightgreen">i32</span>

#### 3.1 Lokale Kommunikation

#### 3.2 Netzwerk Kommunikation

#### 3.3 Unterstützung für mehrere Clients

### 4. Portscan
#### <span style="color:gray">4.1 Beschreibung</span>

#### 4.2 Versuch
##### 4.2.1 TCP Port Scanner

##### 4.2.2 UDP Port Scanner

#### 4.3 Fragen

### 5. Mail
#### 5.1 SMTP über OpenSSL

#### 5.2 SMTP über Python

[^1]: Datentypen sind, der Kürze halber und um Verwechslungen zu vermeiden, wie in Rust angegeben.