# --- STUFE 1: EINFACH (Mischung Einfach + Mittel) ---
# 150 Fragen - Richtige Antworten gleichmäßig auf A, B, C, D verteilt

quiz_stufe1 = [
    # 1
    {"question": "Was ist ein 'Stop-Loss'?", "options": ['A) Verlustbegrenzung', 'B) Candlestick-Muster', 'C) Gewinnziel', 'D) Ordertyp'], "answer": "A"},
    # 2
    {"question": "Was zeigt ein grüner Candlestick?", "options": ['A) Kurs steigt', 'B) Kurs fällt', 'C) Markt ist geschlossen', 'D) Keine Aussage'], "answer": "A"},
    # 3
    {"question": "Was bedeutet 'Buy Low, Sell High'?", "options": ['A) Leerverkauf', 'B) Markt meiden', 'C) Nur kaufen bei Ausbruch', 'D) Günstig kaufen, teuer verkaufen'], "answer": "D"},
    # 4
    {"question": "Was ist ein Markttrend?", "options": ['A) Langfristige Kursrichtung', 'B) Zufallsbewegung', 'C) Volumensignal', 'D) Ordertyp'], "answer": "A"},
    # 5
    {"question": "Was ist ein Broker?", "options": ['A) Analyseprogramm', 'B) Chart', 'C) Kerze', 'D) Vermittler für Börsengeschäfte'], "answer": "D"},
    # 6
    {"question": "Was ist ein Candlestick?", "options": ['A) Grafische Darstellung des Preisverlaufs', 'B) Order', 'C) Indikator', 'D) Trading-Strategie'], "answer": "A"},
    # 7
    {"question": "Was ist ein Spread?", "options": ['A) Unterschied zwischen Kauf- und Verkaufspreis', 'B) Verlust', 'C) Trend', 'D) Gewinn'], "answer": "A"},
    # 8
    {"question": "Was ist eine Long-Position?", "options": ['A) Wette auf steigende Kurse', 'B) Leerverkauf', 'C) Wette auf fallende Kurse', 'D) Sicherheit'], "answer": "A"},
    # 9
    {"question": "Was ist eine Short-Position?", "options": ['A) Kauf', 'B) Breakout', 'C) Wette auf steigende Kurse', 'D) Wette auf fallende Kurse'], "answer": "D"},
    # 10
    {"question": "Was bedeutet Volumen im Trading?", "options": ['A) Anzahl gehandelter Einheiten', 'B) Geräuschpegel', 'C) Kursverlauf', 'D) Gewinn'], "answer": "A"},
    # 11
    {"question": "Was ist eine Unterstützung (Support)?", "options": ['A) Preiszone, in der Nachfrage steigt', 'B) Trading-Stil', 'C) Verkaufsbereich', 'D) Broker'], "answer": "A"},
    # 12
    {"question": "Was ist ein Widerstand (Resistance)?", "options": ['A) Preiszone, an der Verkaufsdruck zunimmt', 'B) Indikator', 'C) Kursgrenze nach unten', 'D) News'], "answer": "A"},
    # 13
    {"question": "Was bedeutet Take-Profit?", "options": ['A) Verlustgrenze', 'B) Kauf-Order', 'C) Risiko', 'D) Gewinnmitnahme'], "answer": "D"},
    # 14
    {"question": "Was ist ein Demo-Konto?", "options": ['A) Übungskonto mit virtuellem Geld', 'B) Konto mit Echtgeld', 'C) Broker-Konto', 'D) Depot'], "answer": "A"},
    # 15
    {"question": "Was ist ein Hebel (Leverage)?", "options": ['A) Multiplikator für Gewinne und Verluste', 'B) Chartmuster', 'C) Kursanzeige', 'D) Stop-Loss'], "answer": "A"},
    # 16
    {"question": "Was bedeutet Liquidität?", "options": ['A) Verkaufsmenge', 'B) Verlustzone', 'C) Gewinnquote', 'D) Wie leicht ein Asset gehandelt werden kann'], "answer": "D"},
    # 17
    {"question": "Was ist ein Indikator?", "options": ['A) Mathematisches Analysewerkzeug', 'B) Kursbewegung', 'C) Ordertyp', 'D) Chart'], "answer": "A"},
    # 18
    {"question": "Was bedeutet FOMO?", "options": ['A) Angst, einen Trade zu verpassen', 'B) Indikator', 'C) Trading-Strategie', 'D) Hebelwirkung'], "answer": "A"},
    # 19
    {"question": "Was ist ein Portfolio?", "options": ['A) Gesamtheit aller gehaltenen Investitionen', 'B) Eine einzelne Aktie', 'C) Nur Futures', 'D) Kontoauszug'], "answer": "A"},
    # 20
    {"question": "Was ist Scalping?", "options": ['A) Langfristiger Handel', 'B) Fundamentalstrategie', 'C) Trading-Analyse', 'D) Kurzfristiger Handel mit kleinen Gewinnen'], "answer": "D"},
    # 21
    {"question": "Was ist ein Pip?", "options": ['A) Kleinste Preisänderung im Forex-Markt', 'B) Ordertyp', 'C) Chartmuster', 'D) Trendfolge-Signal'], "answer": "A"},
    # 22
    {"question": "Was ist ein Lot im Forex-Handel?", "options": ['A) Standardisierte Handelseinheit', 'B) Gewinnziel', 'C) Risikobegrenzung', 'D) Spread'], "answer": "A"},
    # 23
    {"question": "Was bedeutet 'Bullish'?", "options": ['A) Steigende Kurse erwartet', 'B) Seitwärtsbewegung', 'C) Fallende Kurse', 'D) Markt geschlossen'], "answer": "A"},
    # 24
    {"question": "Was bedeutet 'Bearish'?", "options": ['A) Steigende Kurse', 'B) Seitwärtsbewegung', 'C) Markt offen', 'D) Fallende Kurse erwartet'], "answer": "D"},
    # 25
    {"question": "Was ist eine Limit-Order?", "options": ['A) Order zum aktuellen Marktpreis', 'B) Automatischer Verkauf', 'C) Stop-Loss', 'D) Order zu einem bestimmten Wunschpreis'], "answer": "D"},
    # 26
    {"question": "Was ist eine Market-Order?", "options": ['A) Order zum bestmöglichen aktuellen Preis', 'B) Order mit Zeitverzögerung', 'C) Limit-Order', 'D) Pending Order'], "answer": "A"},
    # 27
    {"question": "Was ist ein Aufwärtstrend?", "options": ['A) Fallende Hochs und Tiefs', 'B) Steigende Hochs und steigende Tiefs', 'C) Seitwärtsbewegung', 'D) Nur steigende Hochs'], "answer": "B"},
    # 28
    {"question": "Was ist ein Abwärtstrend?", "options": ['A) Steigende Hochs', 'B) Seitwärtsbewegung', 'C) Nur fallende Tiefs', 'D) Fallende Hochs und fallende Tiefs'], "answer": "D"},
    # 29
    {"question": "Was ist der Eröffnungskurs?", "options": ['A) Höchster Kurs des Tages', 'B) Tiefster Kurs des Tages', 'C) Schlusskurs', 'D) Erster gehandelter Kurs einer Periode'], "answer": "D"},
    # 30
    {"question": "Was ist der Schlusskurs?", "options": ['A) Letzter gehandelter Kurs einer Periode', 'B) Höchster Kurs', 'C) Tiefster Kurs', 'D) Durchschnittskurs'], "answer": "A"},
    # 31
    {"question": "Welche Farbe hat typischerweise ein fallender Candlestick?", "options": ['A) Grün', 'B) Blau', 'C) Gelb', 'D) Rot'], "answer": "D"},
    # 32
    {"question": "Was ist ein Chart?", "options": ['A) Ordertyp', 'B) Grafische Darstellung von Kursbewegungen', 'C) Indikator', 'D) Broker'], "answer": "B"},
    # 33
    {"question": "Was bedeutet Daytrading?", "options": ['A) Handel über Wochen', 'B) Handel über Monate', 'C) Langfristiges Investieren', 'D) Kauf und Verkauf innerhalb eines Tages'], "answer": "D"},
    # 34
    {"question": "Was ist Swing-Trading?", "options": ['A) Handel im Sekundentakt', 'B) Halten von Positionen über mehrere Tage bis Wochen', 'C) Nur Verkaufen', 'D) Nur Long-Positionen'], "answer": "B"},
    # 35
    {"question": "Was ist ein ETF?", "options": ['A) Einzelne Aktie', 'B) Kryptowährung', 'C) Broker', 'D) Börsengehandelter Fonds'], "answer": "D"},
    # 36
    {"question": "Was ist eine Aktie?", "options": ['A) Anteil an einem Unternehmen', 'B) Schuldschein', 'C) Währungspaar', 'D) Rohstoff'], "answer": "A"},
    # 37
    {"question": "Was ist Forex?", "options": ['A) Aktienhandel', 'B) Rohstoffhandel', 'C) Kryptohandel', 'D) Devisenhandel'], "answer": "D"},
    # 38
    {"question": "Was ist eine Dividende?", "options": ['A) Kursgewinn', 'B) Gewinnausschüttung an Aktionäre', 'C) Handelsgebühr', 'D) Spread'], "answer": "B"},
    # 39
    {"question": "Was ist Volatilität?", "options": ['A) Kursstabilität', 'B) Handelsvolumen', 'C) Trend', 'D) Schwankungsbreite eines Kurses'], "answer": "D"},
    # 40
    {"question": "Was ist ein Index?", "options": ['A) Zusammenfassung mehrerer Wertpapiere', 'B) Einzelne Aktie', 'C) Ordertyp', 'D) Indikator'], "answer": "A"},
    # 41
    {"question": "Was ist der DAX?", "options": ['A) US-Index', 'B) Japanischer Index', 'C) Französischer Index', 'D) Deutscher Aktienindex'], "answer": "D"},
    # 42
    {"question": "Was ist der S&P 500?", "options": ['A) Deutscher Index', 'B) Index der 500 größten US-Unternehmen', 'C) Kryptowährung', 'D) Rohstoff-Index'], "answer": "B"},
    # 43
    {"question": "Was ist ein Zeitrahmen (Timeframe)?", "options": ['A) Handelszeit des Brokers', 'B) Dauer eines Trades', 'C) Marktöffnungszeit', 'D) Zeitspanne, die ein Candlestick darstellt'], "answer": "D"},
    # 44
    {"question": "Was bedeutet H1 als Timeframe?", "options": ['A) 1-Stunden-Chart', 'B) 1-Tages-Chart', 'C) 1-Wochen-Chart', 'D) 1-Minuten-Chart'], "answer": "A"},
    # 45
    {"question": "Was bedeutet M15 als Timeframe?", "options": ['A) 15 Stunden', 'B) 15 Tage', 'C) 15 Sekunden', 'D) 15 Minuten'], "answer": "D"},
    # 46
    {"question": "Was ist ein Docht (Wick) beim Candlestick?", "options": ['A) Der Kerzenkörper', 'B) Die dünne Linie über/unter dem Körper', 'C) Der Schlusskurs', 'D) Das Volumen'], "answer": "B"},
    # 47
    {"question": "Was zeigt der Körper eines Candlesticks?", "options": ['A) Höchst- und Tiefstkurs', 'B) Volumen', 'C) Trend', 'D) Spanne zwischen Eröffnungs- und Schlusskurs'], "answer": "D"},
    # 48
    {"question": "Was ist Margin?", "options": ['A) Sicherheitsleistung beim gehebelten Handel', 'B) Gewinn', 'C) Verlust', 'D) Spread'], "answer": "A"},
    # 49
    {"question": "Was passiert bei einem Margin Call?", "options": ['A) Man bekommt Gewinn ausgezahlt', 'B) Der Broker ruft an', 'C) Man erhält einen Bonus', 'D) Man muss Kapital nachschießen oder Positionen werden geschlossen'], "answer": "D"},
    # 50
    {"question": "Was ist ein Gap im Chart?", "options": ['A) Ein Trend', 'B) Eine Kurslücke', 'C) Ein Indikator', 'D) Ein Ordertyp'], "answer": "B"},
    # 51
    {"question": "Was bedeutet Slippage?", "options": ['A) Gewinn', 'B) Chartmuster', 'C) Spread', 'D) Abweichung zwischen gewünschtem und tatsächlichem Ausführungspreis'], "answer": "D"},
    # 52
    {"question": "Was ist eine Pending Order?", "options": ['A) Sofort ausgeführte Order', 'B) Stornierte Order', 'C) Abgelaufene Order', 'D) Ausstehende Order, die bei einem bestimmten Preis ausgelöst wird'], "answer": "D"},
    # 53
    {"question": "Was ist eine Buy-Stop Order?", "options": ['A) Kauforder über dem aktuellen Preis', 'B) Kauforder unter dem aktuellen Preis', 'C) Verkaufsorder', 'D) Stop-Loss'], "answer": "A"},
    # 54
    {"question": "Was ist eine Sell-Limit Order?", "options": ['A) Verkauf unter dem aktuellen Preis', 'B) Verkauf zum aktuellen Preis', 'C) Kauforder', 'D) Verkauf über dem aktuellen Preis'], "answer": "D"},
    # 55
    {"question": "Was ist eine Buy-Limit Order?", "options": ['A) Kauforder über dem aktuellen Preis', 'B) Kauforder unter dem aktuellen Preis', 'C) Verkaufsorder', 'D) Market Order'], "answer": "B"},
    # 56
    {"question": "Was ist ein Trailing Stop?", "options": ['A) Fixer Stop-Loss', 'B) Limit-Order', 'C) Take-Profit', 'D) Stop-Loss, der dem Kurs automatisch nachzieht'], "answer": "D"},
    # 57
    {"question": "Was ist ein Breakeven?", "options": ['A) Großer Gewinn', 'B) Großer Verlust', 'C) Chartmuster', 'D) Der Punkt, an dem weder Gewinn noch Verlust entsteht'], "answer": "D"},
    # 58
    {"question": "Was ist die Nachbörse?", "options": ['A) Handel vor Marktöffnung', 'B) Handel während der Haupthandelszeit', 'C) Mittagspause', 'D) Handel nach offiziellem Börsenschluss'], "answer": "D"},
    # 59
    {"question": "Was ist die Vorbörse?", "options": ['A) Handel vor offiziellem Marktstart', 'B) Handel nach Börsenschluss', 'C) Wochenendhandel', 'D) Mittagspause'], "answer": "A"},
    # 60
    {"question": "Was ist ein Orderbook?", "options": ['A) Trading-Tagebuch', 'B) Liste aller offenen Kauf- und Verkaufsorders', 'C) Charttyp', 'D) Indikator'], "answer": "B"},
    # 61
    {"question": "Was bedeutet 'Ask' im Trading?", "options": ['A) Kaufpreis (Preis, zu dem man kaufen kann)', 'B) Verkaufspreis', 'C) Durchschnittspreis', 'D) Schlusskurs'], "answer": "A"},
    # 62
    {"question": "Was bedeutet 'Bid' im Trading?", "options": ['A) Kaufpreis', 'B) Höchstpreis', 'C) Verkaufspreis (Preis, zu dem man verkaufen kann)', 'D) Eröffnungskurs'], "answer": "C"},
    # 63
    {"question": "Was ist ein Währungspaar?", "options": ['A) Zwei Aktien', 'B) Zwei Indizes', 'C) Verhältnis von zwei Rohstoffen', 'D) Verhältnis zweier Währungen zueinander'], "answer": "D"},
    # 64
    {"question": "Was ist die Basiswährung bei EUR/USD?", "options": ['A) USD', 'B) EUR', 'C) Beide gleich', 'D) Keine'], "answer": "B"},
    # 65
    {"question": "Was ist die Kurswährung bei EUR/USD?", "options": ['A) EUR', 'B) Beide', 'C) USD', 'D) Keine'], "answer": "C"},
    # 66
    {"question": "Wann öffnet die Londoner Börse (MEZ)?", "options": ['A) 6:00 Uhr', 'B) 7:00 Uhr', 'C) 9:00 Uhr', 'D) 9:00 Uhr'], "answer": "C"},
    # 67
    {"question": "Wann öffnet die New Yorker Börse (MEZ)?", "options": ['A) 12:00 Uhr', 'B) 13:30 Uhr', 'C) 15:30 Uhr', 'D) 17:00 Uhr'], "answer": "C"},
    # 68
    {"question": "Was ist ein Bullenmarkt?", "options": ['A) Markt mit fallenden Kursen', 'B) Seitwärtsmarkt', 'C) Markt mit steigenden Kursen', 'D) Geschlossener Markt'], "answer": "C"},
    # 69
    {"question": "Was ist ein Bärenmarkt?", "options": ['A) Markt mit steigenden Kursen', 'B) Seitwärtsmarkt', 'C) Geschlossener Markt', 'D) Markt mit fallenden Kursen'], "answer": "D"},
    # 70
    {"question": "Was ist ein Hammer-Candlestick?", "options": ['A) Umkehrkerze mit langem unteren Docht', 'B) Trendkerze', 'C) Volumenkerze', 'D) Doji'], "answer": "A"},
    # 71
    {"question": "Was ist eine Doji-Kerze?", "options": ['A) Starke Trendkerze', 'B) Kerze mit großem Körper', 'C) Kerze, bei der Eröffnung und Schluss fast gleich sind', 'D) Gap-Kerze'], "answer": "C"},
    # 72
    {"question": "Was ist ein Engulfing Pattern?", "options": ['A) Eine kleine Kerze', 'B) Eine Kerze, die die vorherige komplett umschließt', 'C) Ein Gap', 'D) Ein Indikator'], "answer": "B"},
    # 73
    {"question": "Was ist Fundamentalanalyse?", "options": ['A) Chartanalyse', 'B) Volumenanalyse', 'C) Bewertung eines Assets anhand wirtschaftlicher Daten', 'D) Indikator-Analyse'], "answer": "C"},
    # 74
    {"question": "Was ist Technische Analyse?", "options": ['A) Analyse von Unternehmensbilanzen', 'B) Analyse von Charts und Kursmustern', 'C) Analyse von Nachrichten', 'D) Analyse von Zinsen'], "answer": "B"},
    # 75
    {"question": "Was ist ein Moving Average?", "options": ['A) Durchschnitt des Volumens', 'B) Durchschnitt der Spreads', 'C) Gleitender Durchschnitt der Kurse', 'D) Durchschnitt der Trades'], "answer": "C"},
    # 76
    {"question": "Was ist der SMA?", "options": ['A) Schneller Moving Average', 'B) Simple Moving Average', 'C) Short Market Analysis', 'D) Stop Moving Alert'], "answer": "B"},
    # 77
    {"question": "Was ist der EMA?", "options": ['A) Extra Market Alert', 'B) Einfacher Mittelwert', 'C) Exit Market Analysis', 'D) Exponential Moving Average'], "answer": "D"},
    # 78
    {"question": "Was passiert, wenn der EMA den SMA von unten nach oben kreuzt?", "options": ['A) Kaufsignal (Golden Cross)', 'B) Verkaufssignal', 'C) Keine Bedeutung', 'D) Seitwärtssignal'], "answer": "A"},
    # 79
    {"question": "Was ist ein Golden Cross?", "options": ['A) Verkaufssignal', 'B) Seitwärtssignal', 'C) Kurzfristiger MA kreuzt langfristigen MA von unten nach oben', 'D) Chartmuster'], "answer": "C"},
    # 80
    {"question": "Was ist ein Death Cross?", "options": ['A) Kaufsignal', 'B) Trendbestätigung', 'C) Indikator-Reset', 'D) Kurzfristiger MA kreuzt langfristigen MA von oben nach unten'], "answer": "D"},
    # 81
    {"question": "Was zeigt hohes Volumen bei einem Ausbruch?", "options": ['A) Schwacher Ausbruch', 'B) Bestätigung des Ausbruchs', 'C) Fakeout', 'D) Seitwärtsbewegung'], "answer": "B"},
    # 82
    {"question": "Was ist ein Fakeout?", "options": ['A) Echter Ausbruch', 'B) Trendbestätigung', 'C) Fehlausbruch, der schnell zurückkehrt', 'D) Volumensignal'], "answer": "C"},
    # 83
    {"question": "Was ist eine Konsolidierung?", "options": ['A) Starker Trend', 'B) Phase, in der sich der Kurs seitwärts bewegt', 'C) Crash', 'D) Ausbruch'], "answer": "B"},
    # 84
    {"question": "Was ist eine Trendlinie?", "options": ['A) Linie, die Hochs oder Tiefs verbindet', 'B) Moving Average', 'C) Indikator', 'D) Fibonacci-Level'], "answer": "A"},
    # 85
    {"question": "Was bedeutet 'Flat' im Trading?", "options": ['A) Long-Position', 'B) Short-Position', 'C) Keine offene Position', 'D) Großer Gewinn'], "answer": "C"},
    # 86
    {"question": "Was ist ein Lot im Forex?", "options": ['A) 1.000 Einheiten', 'B) 10.000 Einheiten', 'C) 100.000 Einheiten der Basiswährung', 'D) 1.000.000 Einheiten'], "answer": "C"},
    # 87
    {"question": "Was ist ein Mini-Lot?", "options": ['A) 1.000 Einheiten', 'B) 10.000 Einheiten', 'C) 50.000 Einheiten', 'D) 100.000 Einheiten'], "answer": "B"},
    # 88
    {"question": "Was ist ein Micro-Lot?", "options": ['A) 1.000 Einheiten', 'B) 100 Einheiten', 'C) 10.000 Einheiten', 'D) 500 Einheiten'], "answer": "A"},
    # 89
    {"question": "Was ist der Unterschied zwischen SMA und EMA?", "options": ['A) Kein Unterschied', 'B) SMA ist schneller', 'C) EMA reagiert schneller auf aktuelle Kurse', 'D) SMA nutzt Volumen'], "answer": "C"},
    # 90
    {"question": "Was ist ein Retracement?", "options": ['A) Neuer Trend', 'B) Kurzer Rücksetzer im bestehenden Trend', 'C) Trendwende', 'D) Ausbruch'], "answer": "B"},
    # 91
    {"question": "Was bedeutet 'Risk Management'?", "options": ['A) Maximalen Hebel nutzen', 'B) Nur gewinnen', 'C) Kontrollierter Umgang mit dem Verlustrisiko', 'D) Nie handeln'], "answer": "C"},
    # 92
    {"question": "Was ist eine Korrelation im Trading?", "options": ['A) Ordertyp', 'B) Chartmuster', 'C) Indikator', 'D) Zusammenhang zwischen zwei Märkten'], "answer": "D"},
    # 93
    {"question": "Gold und USD sind typischerweise wie korreliert?", "options": ['A) Positiv', 'B) Negativ (gegenläufig)', 'C) Gar nicht', 'D) Zufällig'], "answer": "B"},
    # 94
    {"question": "Was ist ein Pip bei EUR/USD wert (1 Standard-Lot)?", "options": ['A) 1 Dollar', 'B) 5 Dollar', 'C) 10 Dollar', 'D) 100 Dollar'], "answer": "C"},
    # 95
    {"question": "Was ist eine Session im Trading?", "options": ['A) Ein einzelner Trade', 'B) Bestimmte Handelszeit einer Börsenregion', 'C) Chartmuster', 'D) Indikator'], "answer": "B"},
    # 96
    {"question": "Welche Session gilt als die volatilste?", "options": ['A) Asien-Session', 'B) Australien-Session', 'C) London-New York Overlap', 'D) Nachtsession'], "answer": "C"},
    # 97
    {"question": "Was ist ein Economic Calendar?", "options": ['A) Privater Kalender', 'B) Urlaubsplaner', 'C) Trading-Tagebuch', 'D) Kalender mit wichtigen Wirtschaftsnachrichten'], "answer": "D"},
    # 98
    {"question": "Was bedeutet NFP?", "options": ['A) Non-Farm Payrolls (US-Arbeitsmarktdaten)', 'B) New Forex Platform', 'C) Net Financial Profit', 'D) National Fund Program'], "answer": "A"},
    # 99
    {"question": "Was passiert typischerweise bei NFP-Veröffentlichung?", "options": ['A) Markt schließt', 'B) Hohe Volatilität', 'C) Keine Auswirkung', 'D) Nur Aktien betroffen'], "answer": "B"},
    # 100
    {"question": "Was ist CPI?", "options": ['A) Company Price Index', 'B) Consumer Price Index (Verbraucherpreisindex)', 'C) Current Pip Indicator', 'D) Central Payment Interest'], "answer": "B"},
    # 101
    {"question": "Was misst der CPI?", "options": ['A) Aktienkurse', 'B) Zinsen', 'C) Inflation der Verbraucherpreise', 'D) Arbeitslosigkeit'], "answer": "C"},
    # 102
    {"question": "Was ist die FED?", "options": ['A) Europäische Zentralbank', 'B) Japanische Zentralbank', 'C) US-amerikanische Zentralbank', 'D) Schweizer Nationalbank'], "answer": "C"},
    # 103
    {"question": "Was ist die EZB?", "options": ['A) US-Zentralbank', 'B) Europäische Zentralbank', 'C) Britische Zentralbank', 'D) Weltbank'], "answer": "B"},
    # 104
    {"question": "Was passiert typischerweise wenn Zinsen steigen?", "options": ['A) Währung wird schwächer', 'B) Keine Auswirkung', 'C) Aktien steigen immer', 'D) Währung wird tendenziell stärker'], "answer": "D"},
    # 105
    {"question": "Was ist ein Linien-Chart?", "options": ['A) Zeigt nur Schlusskurse als Linie', 'B) Zeigt Candlesticks', 'C) Zeigt Volumen', 'D) Zeigt Order Flow'], "answer": "A"},
    # 106
    {"question": "Was zeigt ein Bar-Chart?", "options": ['A) Nur Schlusskurse', 'B) Open, High, Low, Close als Balken', 'C) Nur Volumen', 'D) Nur Trends'], "answer": "B"},
    # 107
    {"question": "Welcher Charttyp zeigt die meisten Informationen?", "options": ['A) Linien-Chart', 'B) Punkt-Chart', 'C) Candlestick-Chart', 'D) Alle gleich'], "answer": "C"},
    # 108
    {"question": "Was ist XAUUSD?", "options": ['A) Euro gegen Dollar', 'B) Silber gegen Dollar', 'C) Öl gegen Dollar', 'D) Gold gegen US-Dollar'], "answer": "D"},
    # 109
    {"question": "Was ist EURUSD?", "options": ['A) Euro gegen Schweizer Franken', 'B) Euro gegen US-Dollar', 'C) Euro gegen Pfund', 'D) Euro gegen Yen'], "answer": "B"},
    # 110
    {"question": "Was bedeutet 'Sell Stop'?", "options": ['A) Verkauf über dem aktuellen Preis', 'B) Kauf unter dem aktuellen Preis', 'C) Verkauf unter dem aktuellen Preis', 'D) Kauf über dem aktuellen Preis'], "answer": "C"},
    # 111
    {"question": "Was ist ein Rohstoff?", "options": ['A) Nur Gold', 'B) Nur Öl', 'C) Natürliche Ressource, die gehandelt wird', 'D) Aktie'], "answer": "C"},
    # 112
    {"question": "Welcher dieser Werte ist KEIN Rohstoff?", "options": ['A) Gold', 'B) Silber', 'C) Tesla-Aktie', 'D) Rohöl'], "answer": "C"},
    # 113
    {"question": "Was ist ein CFD?", "options": ['A) Aktientyp', 'B) Differenzkontrakt (Contract for Difference)', 'C) Kryptowährung', 'D) Fond'], "answer": "B"},
    # 114
    {"question": "Was ist ein Kerzenschatten?", "options": ['A) Anderes Wort für den Kerzenkörper', 'B) Anderes Wort für den Docht/Wick', 'C) Volumen', 'D) Spread'], "answer": "B"},
    # 115
    {"question": "Was ist ein Inside Bar?", "options": ['A) Kerze, die größer ist als die vorherige', 'B) Gap-Kerze', 'C) Kerze, die komplett innerhalb der vorherigen Kerze liegt', 'D) Doji'], "answer": "C"},
    # 116
    {"question": "Was ist ein Outside Bar?", "options": ['A) Kerze, die die vorherige komplett umschließt', 'B) Kleine Kerze', 'C) Doji', 'D) Gap'], "answer": "A"},
    # 117
    {"question": "Was ist ein Shooting Star?", "options": ['A) Bullische Umkehrkerze', 'B) Trendkerze', 'C) Bärische Umkehrkerze mit langem oberen Docht', 'D) Doji'], "answer": "C"},
    # 118
    {"question": "Was ist ein Morning Star Pattern?", "options": ['A) Bärisches Signal', 'B) Bullisches Umkehrmuster aus drei Kerzen', 'C) Einzelne Kerze', 'D) Indikator'], "answer": "B"},
    # 119
    {"question": "Was ist ein Evening Star Pattern?", "options": ['A) Bullisches Signal', 'B) Einzelne Kerze', 'C) Indikator', 'D) Bärisches Umkehrmuster aus drei Kerzen'], "answer": "D"},
    # 120
    {"question": "Was ist Backtesting?", "options": ['A) Live-Handel', 'B) Strategie mit historischen Daten testen', 'C) Demo-Handel', 'D) Paper Trading'], "answer": "B"},
    # 121
    {"question": "Was ist Paper Trading?", "options": ['A) Echter Handel', 'B) Handel mit Papieraktien', 'C) Simulierter Handel ohne echtes Geld', 'D) Briefhandel'], "answer": "C"},
    # 122
    {"question": "Was ist eine Watchlist?", "options": ['A) Liste gehandelter Positionen', 'B) Verlustliste', 'C) Liste von beobachteten Assets', 'D) Orderbuch'], "answer": "C"},
    # 123
    {"question": "Was ist der DXY?", "options": ['A) US-Dollar Index', 'B) Deutscher Index', 'C) Japanischer Index', 'D) Volatilitätsindex'], "answer": "A"},
    # 124
    {"question": "Was ist der VIX?", "options": ['A) Aktienindex', 'B) Währungsindex', 'C) Angstindex / Volatilitätsindex', 'D) Rohstoffindex'], "answer": "C"},
    # 125
    {"question": "Was bedeutet 'Position schließen'?", "options": ['A) Neue Position eröffnen', 'B) Hebel erhöhen', 'C) Timeframe wechseln', 'D) Den offenen Trade beenden'], "answer": "D"},
    # 126
    {"question": "Was ist eine Kommission?", "options": ['A) Spread', 'B) Gebühr, die der Broker pro Trade berechnet', 'C) Gewinn', 'D) Margin'], "answer": "B"},
    # 127
    {"question": "Was bedeutet 'Break of Structure' (BOS)?", "options": ['A) Chartfehler', 'B) Wenn der Kurs ein wichtiges Hoch/Tief durchbricht', 'C) Indikator-Signal', 'D) Gap im Chart'], "answer": "B"},
    # 128
    {"question": "Was ist Liquidation?", "options": ['A) Gewinnmitnahme', 'B) Neue Order', 'C) Zwangsschließung einer Position durch den Broker', 'D) Stop-Loss'], "answer": "C"},
    # 129
    {"question": "Was ist ein Trend?", "options": ['A) Zufällige Bewegung', 'B) Seitwärtsbewegung', 'C) Nachhaltige Kursbewegung in eine Richtung', 'D) Gap'], "answer": "C"},
    # 130
    {"question": "Was bedeutet 'overtrading'?", "options": ['A) Zu viele Trades ohne klare Strategie', 'B) Sehr profitable Trades', 'C) Nur ein Trade pro Tag', 'D) Automatischer Handel'], "answer": "A"},
    # 131
    {"question": "Was ist eine Bollinger Band?", "options": ['A) Volumenanzeige', 'B) Band um einen Moving Average, das Volatilität zeigt', 'C) Trendlinie', 'D) Fibonacci-Tool'], "answer": "B"},
    # 132
    {"question": "Was zeigt der RSI an?", "options": ['A) Volumen', 'B) Trend', 'C) Ob ein Asset überkauft oder überverkauft ist', 'D) Spread'], "answer": "C"},
    # 133
    {"question": "Ab welchem RSI-Wert gilt ein Asset als überkauft?", "options": ['A) Über 50', 'B) Über 60', 'C) Über 70', 'D) Über 90'], "answer": "C"},
    # 134
    {"question": "Ab welchem RSI-Wert gilt ein Asset als überverkauft?", "options": ['A) Unter 40', 'B) Unter 30', 'C) Unter 20', 'D) Unter 10'], "answer": "B"},
    # 135
    {"question": "Was ist der MACD?", "options": ['A) Moving Average Convergence Divergence', 'B) Market Average Chart Display', 'C) Multiple Asset Currency Detector', 'D) Main Analysis Chart Data'], "answer": "A"},
    # 136
    {"question": "Was zeigt ein MACD-Crossover?", "options": ['A) Volumenänderung', 'B) Spread-Änderung', 'C) Mögliche Trendwende', 'D) Gap'], "answer": "C"},
    # 137
    {"question": "Was ist ein Double Bottom?", "options": ['A) Fortsetzungsmuster', 'B) Bullisches Umkehrmuster mit zwei Tiefs', 'C) Bärisches Signal', 'D) Indikator'], "answer": "B"},
    # 138
    {"question": "Was ist ein Double Top?", "options": ['A) Bullisches Signal', 'B) Fortsetzungsmuster', 'C) Bärisches Umkehrmuster mit zwei Hochs', 'D) Indikator'], "answer": "C"},
    # 139
    {"question": "Was ist ein Head and Shoulders Pattern?", "options": ['A) Fortsetzungsmuster', 'B) Nur bullisches Signal', 'C) Umkehrmuster mit drei Hochs', 'D) Candlestick'], "answer": "C"},
    # 140
    {"question": "Was ist eine Flagge im Chart?", "options": ['A) Umkehrmuster', 'B) Konsolidierung im Trend (Fortsetzungsmuster)', 'C) Gap', 'D) Indikator'], "answer": "B"},
    # 141
    {"question": "Was ist ein Wimpel (Pennant)?", "options": ['A) Dreieckige Konsolidierung im Trend', 'B) Umkehrmuster', 'C) Volumenanzeige', 'D) Moving Average'], "answer": "A"},
    # 142
    {"question": "Was ist ein Dreieck (Triangle) im Chart?", "options": ['A) Indikator', 'B) Konsolidierungsmuster mit enger werdender Spanne', 'C) Volumenanzeige', 'D) Gap'], "answer": "B"},
    # 143
    {"question": "Was ist ein aufsteigendes Dreieck?", "options": ['A) Bärisches Signal', 'B) Seitwärtssignal', 'C) Eher bullisches Muster mit flacher Oberseite und steigenden Tiefs', 'D) Umkehrmuster'], "answer": "C"},
    # 144
    {"question": "Was ist ein absteigendes Dreieck?", "options": ['A) Bullisches Signal', 'B) Seitwärtssignal', 'C) Umkehrmuster', 'D) Eher bärisches Muster mit flacher Unterseite und fallenden Hochs'], "answer": "D"},
    # 145
    {"question": "Was ist ein Pullback?", "options": ['A) Neuer Trend', 'B) Kurzer Rücklauf nach einem Ausbruch', 'C) Trendwende', 'D) Gap'], "answer": "B"},
    # 146
    {"question": "Was ist eine Range?", "options": ['A) Trend', 'B) Ausbruch', 'C) Seitwärtsphase zwischen Support und Resistance', 'D) Indikator'], "answer": "C"},
    # 147
    {"question": "Was bedeutet 'Break Even setzen'?", "options": ['A) Stop-Loss auf Einstiegspreis setzen', 'B) Take-Profit entfernen', 'C) Position verdoppeln', 'D) Neuen Trade eröffnen'], "answer": "A"},
    # 148
    {"question": "Was ist ein Risk-Reward-Ratio?", "options": ['A) Gewinnquote', 'B) Verlustrate', 'C) Verhältnis von Risiko zu potenziellem Gewinn', 'D) Hebel'], "answer": "C"},
    # 149
    {"question": "Was ist ein gutes Mindest-RRR für Anfänger?", "options": ['A) 1:0.5', 'B) 1:1', 'C) Mindestens 1:2', 'D) 1:10'], "answer": "C"},
    # 150
    {"question": "Was bedeutet 'den Markt lesen'?", "options": ['A) Nachrichten lesen', 'B) Charts und Price Action interpretieren', 'C) Bücher über Trading lesen', 'D) Social Media checken'], "answer": "B"},
]
