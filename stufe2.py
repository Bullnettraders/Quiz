# --- STUFE 2: MITTEL (Mischung Mittel + Schwer) ---
# 150 Fragen - Richtige Antworten gleichmäßig auf A, B, C, D verteilt

quiz_stufe2 = [
    # 1
    {"question": "Was ist ein Fibonacci-Retracement?", "options": ['A) Tool zur Bestimmung von Unterstützungs-/Widerstandszonen', 'B) Chartmuster', 'C) Indikator für Volumen', 'D) Ordertyp'], "answer": "A"},
    # 2
    {"question": "Welche Fibonacci-Level werden am häufigsten genutzt?", "options": ['A) 23.6%, 38.2%, 50%, 61.8%', 'B) 10%, 20%, 30%, 40%', 'C) 25%, 50%, 75%, 100%', 'D) 33%, 50%, 66%, 100%'], "answer": "A"},
    # 3
    {"question": "Was bedeutet ein RSI über 70?", "options": ['A) Überverkauft', 'B) Neutral', 'C) Kein Signal', 'D) Überkauft – mögliches Verkaufssignal'], "answer": "D"},
    # 4
    {"question": "Was bedeutet ein RSI unter 30?", "options": ['A) Überverkauft – mögliches Kaufsignal', 'B) Neutral', 'C) Überkauft', 'D) Trendbestätigung'], "answer": "A"},
    # 5
    {"question": "Was ist eine RSI-Divergenz?", "options": ['A) RSI zeigt anderes Muster als der Kurs', 'B) RSI bestätigt den Trend', 'C) RSI ist bei 50', 'D) RSI hat keinen Wert'], "answer": "A"},
    # 6
    {"question": "Was zeigt eine bullische RSI-Divergenz?", "options": ['A) Kurs macht tiefere Tiefs, RSI macht höhere Tiefs', 'B) Kurs und RSI fallen gleich', 'C) Kurs steigt, RSI fällt', 'D) Beide steigen'], "answer": "A"},
    # 7
    {"question": "Was zeigt eine bärische RSI-Divergenz?", "options": ['A) Beide fallen', 'B) Kurs fällt, RSI steigt', 'C) Beide steigen', 'D) Kurs macht höhere Hochs, RSI macht tiefere Hochs'], "answer": "D"},
    # 8
    {"question": "Was ist der Stochastic Oscillator?", "options": ['A) Momentum-Indikator, der überkaufte/überverkaufte Bereiche zeigt', 'B) Volumenindikator', 'C) Trendindikator', 'D) Volatilitätsindikator'], "answer": "A"},
    # 9
    {"question": "Was ist der ADX-Indikator?", "options": ['A) Misst die Stärke eines Trends', 'B) Zeigt Volumen', 'C) Misst Volatilität', 'D) Zeigt Support/Resistance'], "answer": "A"},
    # 10
    {"question": "Ab welchem ADX-Wert gilt ein Trend als stark?", "options": ['A) Über 10', 'B) Über 15', 'C) Über 20', 'D) Über 25'], "answer": "D"},
    # 11
    {"question": "Was ist der ATR-Indikator?", "options": ['A) Average True Range – misst Volatilität', 'B) Trendanzeige', 'C) Volumenanzeige', 'D) RSI-Variante'], "answer": "A"},
    # 12
    {"question": "Wofür wird der ATR häufig genutzt?", "options": ['A) Stop-Loss-Berechnung basierend auf Volatilität', 'B) Trendrichtung', 'C) Einstiegssignal', 'D) Take-Profit-Signal'], "answer": "A"},
    # 13
    {"question": "Was ist der VWAP?", "options": ['A) Volumengewichteter Durchschnittspreis', 'B) Volatilitäts-Indikator', 'C) RSI-Alternative', 'D) Trendlinie'], "answer": "A"},
    # 14
    {"question": "Wer nutzt den VWAP hauptsächlich?", "options": ['A) Langfrist-Investoren', 'B) Nur Anfänger', 'C) Fundamentalanalysten', 'D) Institutionelle Trader und Daytrader'], "answer": "D"},
    # 15
    {"question": "Was ist das On-Balance Volume (OBV)?", "options": ['A) Preisindikator', 'B) Momentum-Indikator', 'C) Volumenindikator, der Kauf-/Verkaufsdruck zeigt', 'D) Volatilitätsindikator'], "answer": "C"},
    # 16
    {"question": "Was ist ein Ichimoku Cloud?", "options": ['A) Mehrteiliges Indikator-System für Trend, Support und Momentum', 'B) Einzelner Indikator', 'C) Nur Volumenanzeige', 'D) Fibonacci-Tool'], "answer": "A"},
    # 17
    {"question": "Was ist die Kumo (Wolke) im Ichimoku?", "options": ['A) Trendlinie', 'B) Moving Average', 'C) Bereich zwischen Senkou Span A und B – zeigt Support/Resistance', 'D) Volumenwolke'], "answer": "C"},
    # 18
    {"question": "Was zeigt ein Kurs über der Ichimoku-Wolke?", "options": ['A) Bärischer Trend', 'B) Seitwärtstrend', 'C) Kein Signal', 'D) Bullischer Trend'], "answer": "D"},
    # 19
    {"question": "Was ist ein Orderblock im SMC-Trading?", "options": ['A) Eine große Limit-Order', 'B) Chartmuster', 'C) Stop-Loss-Zone', 'D) Zone, wo institutionelle Trader Orders platziert haben'], "answer": "D"},
    # 20
    {"question": "Was ist eine Fair Value Gap (FVG)?", "options": ['A) Indikator', 'B) Ordertyp', 'C) Kurslücke durch Imbalance zwischen Käufern und Verkäufern', 'D) Support-Level'], "answer": "C"},
    # 21
    {"question": "Was bedeutet 'Change of Character' (ChoCh)?", "options": ['A) Trendbestätigung', 'B) Seitwärtsbewegung', 'C) Volumenänderung', 'D) Erste Anzeichen einer Trendumkehr'], "answer": "D"},
    # 22
    {"question": "Was ist der Unterschied zwischen BOS und ChoCh?", "options": ['A) Kein Unterschied', 'B) BOS ist nur für Forex', 'C) ChoCh bestätigt Trend', 'D) BOS bestätigt Trend, ChoCh zeigt mögliche Umkehr'], "answer": "D"},
    # 23
    {"question": "Was ist Liquidity im SMC-Kontext?", "options": ['A) Handelsvolumen', 'B) Spread', 'C) Ansammlung von Stop-Loss-Orders, die Smart Money anzieht', 'D) Margin'], "answer": "C"},
    # 24
    {"question": "Was bedeutet 'Liquidity Grab'?", "options": ['A) Kursbewegung, die Stop-Losses auslöst, bevor der Kurs dreht', 'B) Hoher Spread', 'C) Niedriges Volumen', 'D) Gap Fill'], "answer": "A"},
    # 25
    {"question": "Was ist ein Breaker Block?", "options": ['A) Normaler Orderblock', 'B) Fibonacci-Level', 'C) Trendlinie', 'D) Gescheiterter Orderblock, der nun als Gegensignal dient'], "answer": "D"},
    # 26
    {"question": "Was ist ein Mitigation Block?", "options": ['A) Take-Profit-Zone', 'B) Gap', 'C) Moving Average', 'D) Unmitigierter Orderblock, zu dem der Kurs zurückkehrt'], "answer": "D"},
    # 27
    {"question": "Was ist Smart Money?", "options": ['A) Retail-Trader', 'B) Anfänger', 'C) Institutionelle Marktteilnehmer mit großem Kapital', 'D) Broker'], "answer": "C"},
    # 28
    {"question": "Was ist 'Displacement' im SMC?", "options": ['A) Seitwärtsbewegung', 'B) Langsamer Trend', 'C) Volumenrückgang', 'D) Starke, impulsive Kursbewegung mit großen Kerzen'], "answer": "D"},
    # 29
    {"question": "Was ist ein Premium-Bereich im SMC?", "options": ['A) Preisbereich unter dem Equilibrium – günstig zum Kaufen', 'B) Preisbereich über dem Equilibrium – teuer', 'C) Support-Zone', 'D) Fibonacci 0%'], "answer": "B"},
    # 30
    {"question": "Was ist ein Discount-Bereich im SMC?", "options": ['A) Preisbereich über dem Gleichgewicht', 'B) Take-Profit-Zone', 'C) Preisbereich unter dem Equilibrium – günstig', 'D) Widerstandszone'], "answer": "C"},
    # 31
    {"question": "Was ist ein Swing-High?", "options": ['A) Langfristiges Allzeithoch', 'B) Lokales Hoch, umgeben von niedrigeren Hochs', 'C) Moving Average Hoch', 'D) Gap-Hoch'], "answer": "B"},
    # 32
    {"question": "Was ist ein Swing-Low?", "options": ['A) Allzeittief', 'B) Moving Average Tief', 'C) Gap-Tief', 'D) Lokales Tief, umgeben von höheren Tiefs'], "answer": "D"},
    # 33
    {"question": "Was ist ein Drawdown?", "options": ['A) Maximaler Gewinn', 'B) Seitwärtsbewegung', 'C) Rückgang vom Hoch zum Tief im Portfolio', 'D) Ordertyp'], "answer": "C"},
    # 34
    {"question": "Was ist eine Equity Curve?", "options": ['A) Grafische Darstellung des Kontostands über Zeit', 'B) Kurslinie eines Assets', 'C) Volumenkurve', 'D) RSI-Linie'], "answer": "A"},
    # 35
    {"question": "Was ist ein Backtest?", "options": ['A) Live-Trading', 'B) Demo-Trading', 'C) Paper Trading', 'D) Rückwirkende Überprüfung einer Strategie mit historischen Daten'], "answer": "D"},
    # 36
    {"question": "Was ist ein Forward Test?", "options": ['A) Backtest mit mehr Daten', 'B) Strategie in Echtzeit testen (meist Demo)', 'C) Historischer Test', 'D) Volumen-Test'], "answer": "B"},
    # 37
    {"question": "Was ist der Unterschied zwischen Backtesting und Forward Testing?", "options": ['A) Kein Unterschied', 'B) Backtest ist in Echtzeit', 'C) Backtest nutzt Vergangenheit, Forward Test nutzt Echtzeit', 'D) Forward Test nutzt nur Indikatoren'], "answer": "C"},
    # 38
    {"question": "Was ist die Winrate?", "options": ['A) Anzahl Trades', 'B) Hebel', 'C) Margin', 'D) Prozentsatz der gewonnenen Trades'], "answer": "D"},
    # 39
    {"question": "Ist eine hohe Winrate allein entscheidend für Profitabilität?", "options": ['A) Ja, immer', 'B) Nein, das Risk-Reward-Ratio ist ebenso wichtig', 'C) Ja, wenn über 50%', 'D) Winrate ist irrelevant'], "answer": "B"},
    # 40
    {"question": "Was ist ein Trading-Plan?", "options": ['A) Schriftlich festgelegte Regeln für Entry, Exit und Risk Management', 'B) Nur eine Watchlist', 'C) Broker-Empfehlung', 'D) Indikator-Sammlung'], "answer": "A"},
    # 41
    {"question": "Was ist Position Sizing?", "options": ['A) Chartgröße', 'B) Timeframe-Auswahl', 'C) Berechnung der optimalen Positionsgröße pro Trade', 'D) Spread-Berechnung'], "answer": "C"},
    # 42
    {"question": "Wie berechnet man die Positionsgröße?", "options": ['A) Zufällig', 'B) Immer 1 Lot', 'C) Immer maximaler Hebel', 'D) Risiko pro Trade / (Entfernung zum Stop-Loss × Pip-Wert)'], "answer": "D"},
    # 43
    {"question": "Was ist die 1%-Regel im Risk Management?", "options": ['A) Maximal 1% Gewinn pro Trade', 'B) Maximal 1% des Kontos pro Trade riskieren', 'C) 1% Spread zahlen', 'D) 1 Lot handeln'], "answer": "B"},
    # 44
    {"question": "Was ist ein Expectancy Value?", "options": ['A) Erwarteter Gewinn pro Trade basierend auf Winrate und RRR', 'B) Maximaler Verlust', 'C) Margin-Bedarf', 'D) Spread-Kosten'], "answer": "A"},
    # 45
    {"question": "Was bedeutet 'Scaling In'?", "options": ['A) Position auf einmal eröffnen', 'B) Schrittweises Aufbauen einer Position', 'C) Position sofort schließen', 'D) Hebel erhöhen'], "answer": "B"},
    # 46
    {"question": "Was bedeutet 'Scaling Out'?", "options": ['A) Gesamte Position auf einmal schließen', 'B) Position verdoppeln', 'C) Schrittweises Teilschließen einer Position', 'D) Stop-Loss entfernen'], "answer": "C"},
    # 47
    {"question": "Was ist ein Head and Shoulders Top?", "options": ['A) Bullisches Muster', 'B) Seitwärtsmuster', 'C) Volumenmuster', 'D) Bärisches Umkehrmuster am Ende eines Aufwärtstrends'], "answer": "D"},
    # 48
    {"question": "Was ist ein Inverse Head and Shoulders?", "options": ['A) Bullisches Umkehrmuster am Ende eines Abwärtstrends', 'B) Bärisches Muster', 'C) Seitwärtsmuster', 'D) Indikator'], "answer": "A"},
    # 49
    {"question": "Was ist ein Cup and Handle?", "options": ['A) Bärisches Muster', 'B) Bullisches Fortsetzungsmuster, U-förmig mit Henkel', 'C) Volumenanzeige', 'D) Divergenz'], "answer": "B"},
    # 50
    {"question": "Was ist ein Wedge Pattern?", "options": ['A) Keilförmiges Muster mit konvergierenden Trendlinien', 'B) Rechteck', 'C) Kreis', 'D) Dreieck ohne Spitze'], "answer": "A"},
    # 51
    {"question": "Was zeigt ein Rising Wedge?", "options": ['A) Bullisches Signal', 'B) Neutrales Signal', 'C) Bärisches Signal – oft Trendumkehr nach unten', 'D) Volumenanstieg'], "answer": "C"},
    # 52
    {"question": "Was zeigt ein Falling Wedge?", "options": ['A) Bärisches Signal', 'B) Bullisches Signal – oft Trendumkehr nach oben', 'C) Seitwärtssignal', 'D) Kein Signal'], "answer": "B"},
    # 53
    {"question": "Was ist ein symmetrisches Dreieck?", "options": ['A) Nur bullisch', 'B) Nur bärisch', 'C) Neutrales Muster – Ausbruch in beide Richtungen möglich', 'D) Trendbestätigung'], "answer": "C"},
    # 54
    {"question": "Was ist ein Measured Move?", "options": ['A) Zufällige Kursbewegung', 'B) Volumenberechnung', 'C) Spread-Anpassung', 'D) Projizierte Kursbewegung basierend auf vorheriger Impulslänge'], "answer": "D"},
    # 55
    {"question": "Was ist ein Three White Soldiers Pattern?", "options": ['A) Drei aufeinanderfolgende bullische Kerzen', 'B) Drei bärische Kerzen', 'C) Drei Dojis', 'D) Drei Gaps'], "answer": "A"},
    # 56
    {"question": "Was ist ein Three Black Crows Pattern?", "options": ['A) Drei bullische Kerzen', 'B) Drei aufeinanderfolgende bärische Kerzen', 'C) Drei Dojis', 'D) Drei Inside Bars'], "answer": "B"},
    # 57
    {"question": "Was ist ein Harami Pattern?", "options": ['A) Große Kerze gefolgt von kleiner Kerze innerhalb des Körpers', 'B) Zwei gleich große Kerzen', 'C) Gap-Muster', 'D) Nur bullisch'], "answer": "A"},
    # 58
    {"question": "Was ist ein Tweezer Top?", "options": ['A) Bullisches Muster', 'B) Volumensignal', 'C) Bärisches Umkehrmuster mit zwei Kerzen auf gleichem Hoch', 'D) Gap'], "answer": "C"},
    # 59
    {"question": "Was ist ein Tweezer Bottom?", "options": ['A) Bärisches Muster', 'B) Gap', 'C) Indikator', 'D) Bullisches Umkehrmuster mit zwei Kerzen auf gleichem Tief'], "answer": "D"},
    # 60
    {"question": "Was bedeutet Confluence im Trading?", "options": ['A) Widersprüchliche Signale', 'B) Zusammentreffen mehrerer Signale/Levels an einem Punkt', 'C) Einzelner Indikator', 'D) Gap'], "answer": "B"},
    # 61
    {"question": "Warum ist Confluence wichtig?", "options": ['A) Macht den Chart bunter', 'B) Ist irrelevant', 'C) Erhöht die Wahrscheinlichkeit eines erfolgreichen Trades', 'D) Senkt den Spread'], "answer": "C"},
    # 62
    {"question": "Was ist Multi-Timeframe-Analyse?", "options": ['A) Nur einen Timeframe nutzen', 'B) Verschiedene Timeframes analysieren für bessere Entscheidungen', 'C) Timeframes ignorieren', 'D) Nur Daily-Chart nutzen'], "answer": "B"},
    # 63
    {"question": "Welcher Timeframe gibt den übergeordneten Trend vor?", "options": ['A) M1', 'B) M5', 'C) M15', 'D) Der höhere Timeframe (z.B. H4 oder Daily)'], "answer": "D"},
    # 64
    {"question": "Was ist ein POI (Point of Interest)?", "options": ['A) Preiszone mit hoher Wahrscheinlichkeit für eine Reaktion', 'B) Zufälliger Punkt', 'C) Indikator-Signal', 'D) Volumenanzeige'], "answer": "A"},
    # 65
    {"question": "Was ist Market Structure?", "options": ['A) Broker-Aufbau', 'B) Abfolge von Hochs und Tiefs, die den Trend definieren', 'C) Nur Candlesticks', 'D) Volumenstruktur'], "answer": "B"},
    # 66
    {"question": "Wie erkennt man einen Aufwärtstrend in der Market Structure?", "options": ['A) Fallende Hochs und Tiefs', 'B) Seitwärtsbewegung', 'C) Higher Highs und Higher Lows', 'D) Nur steigende Hochs'], "answer": "C"},
    # 67
    {"question": "Wie erkennt man einen Abwärtstrend in der Market Structure?", "options": ['A) Steigende Hochs', 'B) Seitwärtsbewegung', 'C) Nur fallende Tiefs', 'D) Lower Highs und Lower Lows'], "answer": "D"},
    # 68
    {"question": "Was ist ein Supply Zone?", "options": ['A) Kaufzone', 'B) Preisbereich mit starkem Verkaufsinteresse', 'C) Support', 'D) Gap'], "answer": "B"},
    # 69
    {"question": "Was ist eine Demand Zone?", "options": ['A) Verkaufszone', 'B) Resistance', 'C) Preisbereich mit starkem Kaufinteresse', 'D) Gap'], "answer": "C"},
    # 70
    {"question": "Was ist der Unterschied zwischen Supply/Demand und Support/Resistance?", "options": ['A) Kein Unterschied', 'B) S/D basiert auf Linien, S/R auf Zonen', 'C) S/R basiert auf Orderflow-Logik', 'D) S/D basiert auf Orderflow und unmitigierten Zonen, S/R auf historischen Preisniveaus'], "answer": "D"},
    # 71
    {"question": "Was ist ein Imbalance im Chart?", "options": ['A) Gleichgewicht', 'B) Bereich, in dem Käufer oder Verkäufer stark dominiert haben', 'C) Indikator', 'D) Moving Average'], "answer": "B"},
    # 72
    {"question": "Was passiert oft bei einer Fair Value Gap?", "options": ['A) Kurs ignoriert sie', 'B) Nichts', 'C) Kurs kehrt zurück, um die Lücke zu füllen', 'D) Volumen sinkt'], "answer": "C"},
    # 73
    {"question": "Was ist Inducement im SMC?", "options": ['A) Indikator', 'B) Trendbestätigung', 'C) Ordertyp', 'D) Lockung von Retail-Tradern in die falsche Richtung'], "answer": "D"},
    # 74
    {"question": "Was ist ein Kill Zone?", "options": ['A) Zeitfenster mit hoher Aktivität (London/NY Open)', 'B) Verlustzone', 'C) Stop-Loss-Bereich', 'D) Indikator'], "answer": "A"},
    # 75
    {"question": "Wann ist die London Kill Zone (MEZ)?", "options": ['A) 6:00–8:00', 'B) 8:00–10:00', 'C) 9:00–11:00', 'D) 12:00–14:00'], "answer": "C"},
    # 76
    {"question": "Wann ist die New York Kill Zone (MEZ)?", "options": ['A) 12:00–14:00', 'B) 14:00–16:00', 'C) 16:00–18:00', 'D) 18:00–20:00'], "answer": "B"},
    # 77
    {"question": "Was ist ein Liquidity Pool?", "options": ['A) Broker-Konto', 'B) Ansammlung von Stop-Loss-Orders auf einem Preisniveau', 'C) Volumenindikator', 'D) Fibonacci-Level'], "answer": "B"},
    # 78
    {"question": "Wo liegt typischerweise Buy-Side Liquidity?", "options": ['A) Unter den Tiefs', 'B) In der Mitte des Charts', 'C) Über den Hochs (dort liegen Short-Stop-Losses)', 'D) Am VWAP'], "answer": "C"},
    # 79
    {"question": "Wo liegt typischerweise Sell-Side Liquidity?", "options": ['A) Über den Hochs', 'B) In der Mitte', 'C) Am VWAP', 'D) Unter den Tiefs (dort liegen Long-Stop-Losses)'], "answer": "D"},
    # 80
    {"question": "Was ist ein Equilibrium?", "options": ['A) 50%-Level einer Bewegung – Gleichgewichtspunkt', 'B) Höchster Punkt', 'C) Tiefster Punkt', 'D) Volumen-Level'], "answer": "A"},
    # 81
    {"question": "Was ist die Standardabweichung bei Bollinger Bändern?", "options": ['A) 1', 'B) 2', 'C) 3', 'D) 4'], "answer": "B"},
    # 82
    {"question": "Was zeigt ein Squeeze bei Bollinger Bändern?", "options": ['A) Hohe Volatilität', 'B) Trend ist vorbei', 'C) Niedrige Volatilität – bevorstehender Ausbruch möglich', 'D) Volumenrückgang'], "answer": "C"},
    # 83
    {"question": "Was ist der Parabolic SAR?", "options": ['A) Volumenindikator', 'B) Fibonacci-Tool', 'C) Ordertyp', 'D) Trend-Indikator mit Punkten über/unter dem Kurs'], "answer": "D"},
    # 84
    {"question": "Was zeigen Punkte unter dem Kurs beim Parabolic SAR?", "options": ['A) Aufwärtstrend', 'B) Abwärtstrend', 'C) Seitwärtsbewegung', 'D) Kein Signal'], "answer": "A"},
    # 85
    {"question": "Was ist der CCI (Commodity Channel Index)?", "options": ['A) Volumenanzeige', 'B) Momentum-Indikator für zyklische Trends', 'C) Trendlinie', 'D) Nur für Rohstoffe'], "answer": "B"},
    # 86
    {"question": "Was ist der Williams %R?", "options": ['A) Trendindikator', 'B) Volumenindikator', 'C) Momentum-Oscillator ähnlich dem RSI', 'D) Moving Average'], "answer": "C"},
    # 87
    {"question": "Was ist ein Renko-Chart?", "options": ['A) Zeitbasierter Chart', 'B) Volumen-Chart', 'C) Tick-Chart', 'D) Preisbasierter Chart, der nur Bewegungen ab einer bestimmten Größe zeigt'], "answer": "D"},
    # 88
    {"question": "Was ist der Vorteil von Renko-Charts?", "options": ['A) Filtern Marktrauschen und zeigen klare Trends', 'B) Zeigen mehr Details', 'C) Sind schneller', 'D) Zeigen Volumen besser'], "answer": "A"},
    # 89
    {"question": "Was ist ein Heikin-Ashi Chart?", "options": ['A) Normaler Candlestick-Chart', 'B) Modifizierter Candlestick-Chart mit geglätteten Kerzen', 'C) Bar-Chart', 'D) Linien-Chart'], "answer": "B"},
    # 90
    {"question": "Was ist ein Pivot Point?", "options": ['A) Nur ein Indikator', 'B) Berechneter Unterstützungs-/Widerstandspunkt aus dem Vortag', 'C) Moving Average', 'D) RSI-Wert'], "answer": "B"},
    # 91
    {"question": "Was ist die Neckline beim Head and Shoulders?", "options": ['A) Obere Linie', 'B) Mittlere Linie', 'C) Untere Verbindungslinie der Tiefs zwischen den Schultern', 'D) Moving Average'], "answer": "C"},
    # 92
    {"question": "Wann wird ein Head and Shoulders bestätigt?", "options": ['A) Bei der rechten Schulter', 'B) Bei der linken Schulter', 'C) Am Kopf', 'D) Beim Bruch der Neckline'], "answer": "D"},
    # 93
    {"question": "Was ist ein Channel (Kanal) im Chart?", "options": ['A) Zwei parallele Trendlinien, die den Kursverlauf eingrenzen', 'B) Einzelne Trendlinie', 'C) Volumenbereich', 'D) Indikator'], "answer": "A"},
    # 94
    {"question": "Was ist ein aufsteigender Kanal?", "options": ['A) Bärisches Signal', 'B) Kanal mit steigenden Hoch- und Tiefpunkten', 'C) Seitwärtsbewegung', 'D) Nur ein Moving Average'], "answer": "B"},
    # 95
    {"question": "Was ist ein Momentum-Indikator?", "options": ['A) Zeigt Volumen', 'B) Zeigt Spread', 'C) Zeigt die Geschwindigkeit der Kursänderung', 'D) Zeigt Support'], "answer": "C"},
    # 96
    {"question": "Was ist ein Leading Indicator?", "options": ['A) Indikator, der dem Kurs nachläuft', 'B) Volumenanzeige', 'C) Trendlinie', 'D) Indikator, der Signale vor der Kursbewegung gibt'], "answer": "D"},
    # 97
    {"question": "Was ist ein Lagging Indicator?", "options": ['A) Indikator, der dem Kurs nachläuft und Trends bestätigt', 'B) Indikator, der vorausschaut', 'C) Volumenanzeige', 'D) Ordertyp'], "answer": "A"},
    # 98
    {"question": "Ist der RSI ein Leading oder Lagging Indicator?", "options": ['A) Lagging', 'B) Leading', 'C) Keines von beiden', 'D) Beides gleichzeitig'], "answer": "B"},
    # 99
    {"question": "Ist der Moving Average ein Leading oder Lagging Indicator?", "options": ['A) Leading', 'B) Beides', 'C) Keines', 'D) Lagging'], "answer": "D"},
    # 100
    {"question": "Was ist die Dow Theory?", "options": ['A) Moderne Indikator-Theorie', 'B) Grundlage der technischen Analyse – Trends bestehen aus Phasen', 'C) Nur für Aktien', 'D) Nur für Forex'], "answer": "B"},
    # 101
    {"question": "Welche drei Trendphasen kennt die Dow Theory?", "options": ['A) Akkumulation, Partizipation, Distribution', 'B) Einstieg, Mitte, Ausstieg', 'C) Support, Resistance, Breakout', 'D) Long, Short, Flat'], "answer": "A"},
    # 102
    {"question": "Was ist eine Akkumulationsphase?", "options": ['A) Starker Aufwärtstrend', 'B) Crash', 'C) Smart Money kauft leise, bevor der Trend startet', 'D) Retail kauft massiv'], "answer": "C"},
    # 103
    {"question": "Was ist eine Distributionsphase?", "options": ['A) Smart Money verkauft in Stärke an Retail-Trader', 'B) Starker Kaufdruck', 'C) Beginn eines Trends', 'D) Konsolidierung'], "answer": "A"},
    # 104
    {"question": "Was ist die Elliott-Wellen-Theorie?", "options": ['A) Volumentheorie', 'B) RSI-Analyse', 'C) Theorie, dass Märkte in wiederkehrenden Wellenmuster verlaufen', 'D) Trendlinien-Strategie'], "answer": "C"},
    # 105
    {"question": "Wie viele Impulswellen hat ein Elliott-Wellen-Zyklus?", "options": ['A) 3', 'B) 4', 'C) 5', 'D) 8'], "answer": "C"},
    # 106
    {"question": "Wie viele Korrekturwellen hat ein Elliott-Wellen-Zyklus?", "options": ['A) 2', 'B) 3', 'C) 4', 'D) 5'], "answer": "B"},
    # 107
    {"question": "Was ist ein Fibonacci-Extension?", "options": ['A) Rücksetzungstool', 'B) Volumenanzeige', 'C) Chartmuster', 'D) Tool zur Bestimmung von Kurszielen über das letzte Hoch/Tief hinaus'], "answer": "D"},
    # 108
    {"question": "Welches Fibonacci-Extension-Level wird häufig als Kursziel genutzt?", "options": ['A) 100%', 'B) 127.2% und 161.8%', 'C) 200%', 'D) 50%'], "answer": "B"},
    # 109
    {"question": "Was ist ein harmonisches Muster?", "options": ['A) Zufälliges Chartmuster', 'B) Muster basierend auf Fibonacci-Ratios (z.B. Gartley, Bat)', 'C) Volumenanzeige', 'D) Moving Average'], "answer": "B"},
    # 110
    {"question": "Was ist ein Gartley-Pattern?", "options": ['A) Harmonisches Umkehrmuster mit spezifischen Fibonacci-Verhältnissen', 'B) Candlestick-Muster', 'C) Indikator', 'D) Gap-Muster'], "answer": "A"},
    # 111
    {"question": "Was ist 'Divergence' beim MACD?", "options": ['A) MACD bestätigt den Trend', 'B) MACD hat keinen Wert', 'C) MACD und Kurs bewegen sich in entgegengesetzte Richtungen', 'D) MACD kreuzt Nulllinie'], "answer": "C"},
    # 112
    {"question": "Was ist die MACD-Signallinie?", "options": ['A) EMA der MACD-Linie – Crossover gibt Signale', 'B) Nulllinie', 'C) Trendlinie', 'D) Volumen'], "answer": "A"},
    # 113
    {"question": "Was zeigt das MACD-Histogramm?", "options": ['A) Volumen', 'B) Spread', 'C) Differenz zwischen MACD-Linie und Signallinie', 'D) RSI-Wert'], "answer": "C"},
    # 114
    {"question": "Was ist Korrelation im Multi-Asset-Trading?", "options": ['A) Ordertyp', 'B) Statistischer Zusammenhang zwischen zwei Assets', 'C) Chartmuster', 'D) Indikator'], "answer": "B"},
    # 115
    {"question": "EUR/USD und DXY sind typischerweise wie korreliert?", "options": ['A) Positiv', 'B) Gar nicht', 'C) Zufällig', 'D) Negativ (gegenläufig)'], "answer": "D"},
    # 116
    {"question": "Was ist ein Carry Trade?", "options": ['A) Daytrading-Strategie', 'B) Scalping-Technik', 'C) Ausleihen in Niedrigzinswährung, Anlegen in Hochzinswährung', 'D) Nur für Aktien'], "answer": "C"},
    # 117
    {"question": "Was ist Swap im Forex-Handel?", "options": ['A) Spread', 'B) Kommission', 'C) Margin', 'D) Zinsdifferenz-Gebühr für das Halten einer Position über Nacht'], "answer": "D"},
    # 118
    {"question": "Was ist ein Triple Top?", "options": ['A) Bullisches Muster', 'B) Bärisches Umkehrmuster mit drei Hochs auf gleichem Level', 'C) Indikator', 'D) Fibonacci-Level'], "answer": "B"},
    # 119
    {"question": "Was ist ein Triple Bottom?", "options": ['A) Bärisches Muster', 'B) Indikator', 'C) Bullisches Umkehrmuster mit drei Tiefs auf gleichem Level', 'D) Gap'], "answer": "C"},
    # 120
    {"question": "Was ist Order Flow?", "options": ['A) Analyse der tatsächlichen Kauf- und Verkaufsorders im Markt', 'B) Indikator', 'C) Chartmuster', 'D) Moving Average'], "answer": "A"},
    # 121
    {"question": "Was ist ein Market Profile?", "options": ['A) RSI-Variante', 'B) Darstellung der Preisverteilung über Zeit und Volumen', 'C) Trendlinie', 'D) Candlestick-Muster'], "answer": "B"},
    # 122
    {"question": "Was ist der Value Area im Market Profile?", "options": ['A) Ganzer Chartbereich', 'B) Nur Hochs', 'C) Preisbereich, in dem ca. 70% des Volumens gehandelt wurde', 'D) Nur Tiefs'], "answer": "C"},
    # 123
    {"question": "Was ist ein POC (Point of Control)?", "options": ['A) Fibonacci-Level', 'B) RSI-Level', 'C) Moving Average', 'D) Preisniveau mit dem höchsten gehandelten Volumen'], "answer": "D"},
    # 124
    {"question": "Was ist Slippage und wann tritt sie auf?", "options": ['A) Preisabweichung bei hoher Volatilität oder geringer Liquidität', 'B) Immer bei Limit-Orders', 'C) Nur bei Stop-Loss', 'D) Nur beim Scalping'], "answer": "A"},
    # 125
    {"question": "Was ist ein Requote?", "options": ['A) Neue Chartansicht', 'B) Broker bietet einen neuen Preis an, weil sich der Markt bewegt hat', 'C) Stop-Loss-Änderung', 'D) Take-Profit-Änderung'], "answer": "B"},
    # 126
    {"question": "Was ist Spread Widening?", "options": ['A) Spread wird kleiner', 'B) Spread bleibt gleich', 'C) Spread wird größer, oft bei hoher Volatilität oder News', 'D) Spread verschwindet'], "answer": "C"},
    # 127
    {"question": "Was ist ein ECN-Broker?", "options": ['A) Market Maker', 'B) Demo-Broker', 'C) Nur für Krypto', 'D) Broker, der Orders direkt an den Interbankenmarkt weiterleitet'], "answer": "D"},
    # 128
    {"question": "Was ist ein Market Maker?", "options": ['A) Broker, der selbst als Gegenpartei agiert', 'B) Börsenaufsicht', 'C) Chartprogramm', 'D) Indikator'], "answer": "A"},
    # 129
    {"question": "Was ist der Unterschied zwischen ECN und Market Maker?", "options": ['A) Kein Unterschied', 'B) ECN leitet Orders weiter, Market Maker stellt eigene Kurse', 'C) Market Maker ist besser', 'D) ECN hat höhere Spreads'], "answer": "B"},
    # 130
    {"question": "Was ist ein Engulfing Bearish Pattern?", "options": ['A) Bullisches Signal', 'B) Gap', 'C) Große rote Kerze, die vorherige grüne komplett umschließt', 'D) Doji'], "answer": "C"},
    # 131
    {"question": "Was ist eine Pin Bar?", "options": ['A) Kerze mit kleinem Körper und langem Docht – Umkehrsignal', 'B) Große Trendkerze', 'C) Gap-Kerze', 'D) Inside Bar'], "answer": "A"},
    # 132
    {"question": "Was zeigt eine bullische Pin Bar?", "options": ['A) Langer oberer Docht', 'B) Langer unterer Docht – Ablehnung tieferer Preise', 'C) Kein Docht', 'D) Großer Körper'], "answer": "B"},
    # 133
    {"question": "Was ist ein Marubozu?", "options": ['A) Kerze ohne Dochte – starkes Momentum', 'B) Doji', 'C) Inside Bar', 'D) Pin Bar'], "answer": "A"},
    # 134
    {"question": "Was bedeutet 'Risk Off' Stimmung?", "options": ['A) Investoren kaufen riskante Assets', 'B) Investoren fliehen in sichere Anlagen (Gold, CHF, JPY)', 'C) Markt ist neutral', 'D) Nur Krypto betroffen'], "answer": "B"},
    # 135
    {"question": "Was bedeutet 'Risk On' Stimmung?", "options": ['A) Investoren meiden Risiko', 'B) Markt ist geschlossen', 'C) Investoren kaufen riskante Assets (Aktien, AUD)', 'D) Nur Anleihen werden gekauft'], "answer": "C"},
    # 136
    {"question": "Was ist ein sicherer Hafen (Safe Haven)?", "options": ['A) Riskantes Asset', 'B) Penny Stock', 'C) Kryptowährung', 'D) Asset, das in Krisenzeiten an Wert gewinnt (z.B. Gold, CHF)'], "answer": "D"},
    # 137
    {"question": "Was ist Intermarket-Analyse?", "options": ['A) Analyse von Zusammenhängen zwischen verschiedenen Märkten', 'B) Nur Forex-Analyse', 'C) Nur Aktien-Analyse', 'D) Indikator-Analyse'], "answer": "A"},
    # 138
    {"question": "Was ist ein Black Swan Event?", "options": ['A) Normales Marktereignis', 'B) Unvorhersehbares, extremes Ereignis mit großer Marktauswirkung', 'C) Chartmuster', 'D) Indikator-Signal'], "answer": "B"},
    # 139
    {"question": "Was ist Saisonalität im Trading?", "options": ['A) Zufallsmuster', 'B) Indikator', 'C) Wiederkehrende Muster zu bestimmten Jahreszeiten/Monaten', 'D) Charttyp'], "answer": "C"},
    # 140
    {"question": "Was ist der January Effect?", "options": ['A) Märkte fallen im Januar', 'B) Kein Effekt', 'C) Märkte sind geschlossen', 'D) Tendenz zu steigenden Kursen im Januar durch Neuinvestitionen'], "answer": "D"},
    # 141
    {"question": "Was bedeutet 'Sell in May and go away'?", "options": ['A) Historisches Muster: Mai-Oktober oft schwächer als November-April', 'B) Immer im Mai verkaufen', 'C) Märkte schließen im Mai', 'D) Nur für Aktien relevant'], "answer": "A"},
    # 142
    {"question": "Was ist ein Stop Hunt?", "options": ['A) Stop-Loss setzen', 'B) Gezielte Kursbewegung, um Stop-Losses auszulösen', 'C) Broker-Empfehlung', 'D) Take-Profit auslösen'], "answer": "B"},
    # 143
    {"question": "Was ist ein Wick Fill?", "options": ['A) Gap Fill', 'B) Indikator', 'C) Kurs kehrt zurück in den Bereich eines vorherigen Dochts', 'D) Trendlinie'], "answer": "C"},
    # 144
    {"question": "Was ist die Asian Range?", "options": ['A) Kursbewegung während der London-Session', 'B) NY-Session Range', 'C) Weekend Gap', 'D) Handelsspanne während der Asien-Session – oft als Referenz genutzt'], "answer": "D"},
    # 145
    {"question": "Was ist ein Break of the Asian Range?", "options": ['A) Ausbruch über/unter die Handelsspanne der Asien-Session', 'B) Gap in der Asien-Session', 'C) Volumenanstieg in Asien', 'D) Nur für JPY-Paare'], "answer": "A"},
    # 146
    {"question": "Was ist die Power of 3 (AMD) im SMC?", "options": ['A) Drei Indikatoren', 'B) Accumulation, Manipulation, Distribution – Phasen eines Trading-Tags', 'C) Drei Kerzen', 'D) Drei Timeframes'], "answer": "B"},
    # 147
    {"question": "Was ist ein Judas Swing?", "options": ['A) Starker Trend', 'B) Gap', 'C) Falsche Anfangsbewegung des Tages, die Trader in die falsche Richtung lockt', 'D) Indikator'], "answer": "C"},
    # 148
    {"question": "Was ist ein Optimal Trade Entry (OTE)?", "options": ['A) Zufälliger Einstieg', 'B) Market Order', 'C) Limit Order', 'D) Einstieg im 61.8%-78.6% Fibonacci-Retracement eines Swings'], "answer": "D"},
    # 149
    {"question": "Was ist Time and Price im ICT/SMC-Kontext?", "options": ['A) Nur Preis zählt', 'B) Kombination aus dem richtigen Zeitfenster und Preisniveau für Trades', 'C) Nur Zeit zählt', 'D) Indikator'], "answer": "B"},
    # 150
    {"question": "Was ist ein Silver Bullet Setup?", "options": ['A) Langfrist-Strategie', 'B) Scalping mit RSI', 'C) ICT-Setup: FVG-Entry in bestimmten Zeitfenstern (z.B. 10:00-11:00 NY)', 'D) Nur für Silber'], "answer": "C"},
]
