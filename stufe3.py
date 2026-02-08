# --- STUFE 3: SCHWER (Mischung Schwer + Ultra Schwer) ---
# 150 Fragen - Richtige Antworten gleichmäßig auf A, B, C, D verteilt

quiz_stufe3 = [
    # 1
    {"question": "Was ist ein Wyckoff-Akkumulationsschema?", "options": ['A) Verkaufsstrategie', 'B) Chartmuster ohne Bedeutung', 'C) Modell, das zeigt wie Smart Money in Seitwärtsphasen Positionen aufbaut', 'D) Indikator'], "answer": "C"},
    # 2
    {"question": "Welche Phase im Wyckoff-Schema ist der 'Spring'?", "options": ['A) Falsche Bewegung unter Support, die Schwäche vortäuscht', 'B) Starker Aufwärtstrend', 'C) Distributionsphase', 'D) Markup-Phase'], "answer": "A"},
    # 3
    {"question": "Was ist ein Wyckoff-Distributionsschema?", "options": ['A) Kaufsignal', 'B) Akkumulation', 'C) Trendbestätigung', 'D) Modell, das zeigt wie Smart Money in Stärke verkauft'], "answer": "D"},
    # 4
    {"question": "Was ist der UTAD (Upthrust After Distribution)?", "options": ['A) Falsche Aufwärtsbewegung über Resistance in der Distribution', 'B) Starkes Kaufsignal', 'C) Trendfortsetzung', 'D) Volumenanstieg'], "answer": "A"},
    # 5
    {"question": "Was sind die 5 Phasen im Wyckoff-Akkumulationsschema?", "options": ['A) A, B, C, D, E – von Selling Climax bis Markup', 'B) 1, 2, 3, 4, 5', 'C) Entry, Stop, Target, Exit, Review', 'D) Nur 3 Phasen'], "answer": "A"},
    # 6
    {"question": "Was ist ein Selling Climax (SC) im Wyckoff?", "options": ['A) Beginn eines Aufwärtstrends', 'B) Normaler Verkauf', 'C) Panikverkauf mit hohem Volumen, der den Abwärtstrend beendet', 'D) Take-Profit-Level'], "answer": "C"},
    # 7
    {"question": "Was ist ein Automatic Rally (AR) im Wyckoff?", "options": ['A) Geplanter Kursanstieg', 'B) Indikator-Signal', 'C) Trendfortsetzung', 'D) Natürliche Gegenbewegung nach dem Selling Climax'], "answer": "D"},
    # 8
    {"question": "Was ist der Secondary Test (ST) im Wyckoff?", "options": ['A) Erneuter Test des SC-Bereichs mit weniger Volumen', 'B) Zweiter Indikator-Test', 'C) Backtest einer Trendlinie', 'D) Moving Average Test'], "answer": "A"},
    # 9
    {"question": "Was ist ein Sign of Strength (SOS) im Wyckoff?", "options": ['A) Starke Aufwärtsbewegung mit hohem Volumen nach dem Spring', 'B) Schwaches Signal', 'C) Verkaufssignal', 'D) Seitwärtsbewegung'], "answer": "A"},
    # 10
    {"question": "Was ist ein Last Point of Support (LPS) im Wyckoff?", "options": ['A) Letzter Rücksetzer vor dem Markup, bestätigt Akkumulation', 'B) Tiefster Punkt', 'C) Höchster Punkt', 'D) Indikator-Level'], "answer": "A"},
    # 11
    {"question": "Was ist der Composite Man im Wyckoff-Kontext?", "options": ['A) Ein einzelner Trader', 'B) Ein Indikator', 'C) Chartmuster', 'D) Konzept: Smart Money als eine koordiniert handelnde Einheit'], "answer": "D"},
    # 12
    {"question": "Was ist Volume Spread Analysis (VSA)?", "options": ['A) Analyse der Beziehung zwischen Volumen, Spread und Schlusskurs', 'B) Nur Volumenanzeige', 'C) Nur Spread-Analyse', 'D) Moving Average'], "answer": "A"},
    # 13
    {"question": "Was zeigt ein No Demand Bar in der VSA?", "options": ['A) Starke Nachfrage', 'B) Hoher Kaufdruck', 'C) Enge Kerze mit niedrigem Volumen – Aufwärtsbewegung hat keine Unterstützung', 'D) Gap'], "answer": "C"},
    # 14
    {"question": "Was zeigt ein No Supply Bar in der VSA?", "options": ['A) Enge Kerze mit niedrigem Volumen auf Abwärtsbewegung – Verkäufer erschöpft', 'B) Starkes Angebot', 'C) Hoher Verkaufsdruck', 'D) Volumenanstieg'], "answer": "A"},
    # 15
    {"question": "Was ist ein Stopping Volume?", "options": ['A) Niedriges Volumen', 'B) Normales Volumen', 'C) Indikator', 'D) Extrem hohes Volumen, das eine Trendbewegung stoppt'], "answer": "D"},
    # 16
    {"question": "Was ist ein Effort vs. Result Prinzip?", "options": ['A) Volumen (Effort) sollte zum Kursergebnis (Result) passen', 'B) Nur Preis zählt', 'C) Nur Volumen zählt', 'D) Indikator-Konzept'], "answer": "A"},
    # 17
    {"question": "Was bedeutet es, wenn hohes Volumen wenig Kursbewegung erzeugt?", "options": ['A) Absorption – eine Seite absorbiert die andere', 'B) Starker Trend', 'C) Normales Verhalten', 'D) Kein Signal'], "answer": "A"},
    # 18
    {"question": "Was ist ein Delta im Order Flow?", "options": ['A) Spread', 'B) Volumen insgesamt', 'C) Differenz zwischen aggressiven Käufern und Verkäufern', 'D) Moving Average'], "answer": "C"},
    # 19
    {"question": "Was zeigt ein positives Cumulative Delta?", "options": ['A) Mehr aggressive Verkäufer', 'B) Gleichgewicht', 'C) Kein Signal', 'D) Mehr aggressive Käufer dominieren'], "answer": "D"},
    # 20
    {"question": "Was ist ein Footprint Chart?", "options": ['A) Chart, der Volumen auf jedem Preisniveau innerhalb einer Kerze zeigt', 'B) Normaler Candlestick-Chart', 'C) Linien-Chart', 'D) Renko-Chart'], "answer": "A"},
    # 21
    {"question": "Was zeigt ein Volume Profile?", "options": ['A) Nur Zeitvolumen', 'B) Nur Ticks', 'C) Verteilung des Volumens über verschiedene Preisniveaus', 'D) Nur Order Flow'], "answer": "C"},
    # 22
    {"question": "Was ist das VPOC im Volume Profile?", "options": ['A) Volume Point of Control – Preisniveau mit höchstem Volumen', 'B) Tiefster Punkt', 'C) Höchster Punkt', 'D) Fibonacci-Level'], "answer": "A"},
    # 23
    {"question": "Was ist eine High Volume Node (HVN)?", "options": ['A) Niedriges Volumen', 'B) Gap', 'C) Indikator', 'D) Preisbereich mit überdurchschnittlich hohem Volumen – wirkt als Magnet'], "answer": "D"},
    # 24
    {"question": "Was ist eine Low Volume Node (LVN)?", "options": ['A) Preisbereich mit wenig Volumen – Kurs bewegt sich schnell hindurch', 'B) Hoher Volumensbereich', 'C) VPOC', 'D) Fibonacci-Level'], "answer": "A"},
    # 25
    {"question": "Was ist ein Initial Balance?", "options": ['A) Kontoeröffnungsbetrag', 'B) Margin', 'C) Handelsspanne der ersten Stunde – Referenz für Daytrader', 'D) Stop-Loss'], "answer": "C"},
    # 26
    {"question": "Was zeigt ein Bruch der Initial Balance nach oben?", "options": ['A) Bärisches Signal', 'B) Kein Signal', 'C) Seitwärtsbewegung', 'D) Mögliche bullische Tagesrichtung'], "answer": "D"},
    # 27
    {"question": "Was ist Gamma Exposure im Optionshandel?", "options": ['A) Maß dafür, wie Market Maker ihre Hedges anpassen und dadurch Kurse beeinflussen', 'B) Optionspreis', 'C) Spread', 'D) Volumen'], "answer": "A"},
    # 28
    {"question": "Was ist ein Options Expiry und warum ist es relevant?", "options": ['A) Irrelevant', 'B) Großes Volumen an auslaufenden Optionen kann Kursbewegungen erzwingen', 'C) Nur für Optionshändler relevant', 'D) Betrifft nur US-Märkte'], "answer": "B"},
    # 29
    {"question": "Was ist Max Pain im Optionshandel?", "options": ['A) Maximaler Gewinn', 'B) Preisniveau, bei dem die meisten Optionen wertlos verfallen', 'C) Stop-Loss-Level', 'D) Indikator'], "answer": "B"},
    # 30
    {"question": "Was ist Dealer Positioning?", "options": ['A) Retail-Positionierung', 'B) Chartmuster', 'C) Wie Market Maker positioniert sind und wie das den Markt beeinflusst', 'D) Volumenanzeige'], "answer": "C"},
    # 31
    {"question": "Was ist ein Dark Pool?", "options": ['A) Öffentliche Börse', 'B) Charttyp', 'C) Indikator', 'D) Private Handelsplattform für institutionelle Orders außerhalb der öffentlichen Börse'], "answer": "D"},
    # 32
    {"question": "Was ist ein Iceberg Order?", "options": ['A) Normale Market Order', 'B) Stop-Loss', 'C) Große Order, die nur in kleinen Teilen sichtbar ist', 'D) Limit Order'], "answer": "C"},
    # 33
    {"question": "Was ist Spoofing?", "options": ['A) Legale Handelsstrategie', 'B) Platzieren von Fake-Orders, um andere Trader zu täuschen (illegal)', 'C) Scalping-Technik', 'D) Chartmuster'], "answer": "B"},
    # 34
    {"question": "Was ist Front Running?", "options": ['A) Schnelles Scalping', 'B) Daytrading-Technik', 'C) Chartmuster', 'D) Handeln vor einer bekannten großen Order (oft illegal)'], "answer": "D"},
    # 35
    {"question": "Was ist ein TWAP-Algorithmus?", "options": ['A) Time-Weighted Average Price – verteilt Orders gleichmäßig über Zeit', 'B) Trendindikator', 'C) Volumenindikator', 'D) Chartmuster'], "answer": "A"},
    # 36
    {"question": "Was ist ein VWAP-Algorithmus im institutionellen Handel?", "options": ['A) Chartanzeige', 'B) Algorithmus, der Orders am VWAP orientiert ausführt', 'C) Indikator', 'D) Nur für Retail'], "answer": "B"},
    # 37
    {"question": "Was ist Latency Arbitrage?", "options": ['A) Langfristige Strategie', 'B) Ausnutzung minimaler Geschwindigkeitsvorteile bei der Orderausführung', 'C) Chartmuster', 'D) Fundamental-Strategie'], "answer": "B"},
    # 38
    {"question": "Was ist Mean Reversion?", "options": ['A) Trend folgen', 'B) Nur kaufen', 'C) Strategie, die darauf setzt, dass Kurse zum Mittelwert zurückkehren', 'D) Nur verkaufen'], "answer": "C"},
    # 39
    {"question": "Was ist ein Z-Score im statistischen Trading?", "options": ['A) Chartmuster', 'B) Indikator', 'C) Volumenanzeige', 'D) Maß für die Abweichung eines Wertes vom Mittelwert in Standardabweichungen'], "answer": "D"},
    # 40
    {"question": "Was ist ein Sharpe Ratio?", "options": ['A) Risikobereinigte Rendite: Rendite minus risikoloser Zins geteilt durch Volatilität', 'B) Nur Rendite', 'C) Nur Risiko', 'D) Hebel-Ratio'], "answer": "A"},
    # 41
    {"question": "Was ist ein guter Sharpe Ratio?", "options": ['A) Unter 0', 'B) Über 1 gilt als gut, über 2 als sehr gut', 'C) Genau 0.5', 'D) Über 10'], "answer": "B"},
    # 42
    {"question": "Was ist der Sortino Ratio?", "options": ['A) Gleich wie Sharpe', 'B) Volumen-Ratio', 'C) Wie Sharpe, aber berücksichtigt nur Downside-Volatilität', 'D) Margin-Ratio'], "answer": "C"},
    # 43
    {"question": "Was ist der Maximum Drawdown?", "options": ['A) Maximaler Gewinn', 'B) Durchschnittlicher Verlust', 'C) Täglicher Verlust', 'D) Größter Rückgang vom Hoch zum Tief im Portfolio'], "answer": "D"},
    # 44
    {"question": "Was ist der Calmar Ratio?", "options": ['A) Rendite geteilt durch Maximum Drawdown', 'B) Volumen-Ratio', 'C) Spread-Ratio', 'D) Hebel-Ratio'], "answer": "A"},
    # 45
    {"question": "Was ist ein Monte-Carlo-Simulation im Trading?", "options": ['A) Casino-Strategie', 'B) Simulation vieler zufälliger Trade-Sequenzen zur Risikobewertung', 'C) Chartmuster', 'D) Indikator'], "answer": "B"},
    # 46
    {"question": "Was testet man mit Monte-Carlo-Simulationen?", "options": ['A) Nur Gewinne', 'B) Nur Verluste', 'C) Robustheit einer Strategie unter verschiedenen Szenarien', 'D) Spread-Kosten'], "answer": "C"},
    # 47
    {"question": "Was ist Curve Fitting beim Backtesting?", "options": ['A) Gute Strategie-Entwicklung', 'B) Robustes System', 'C) Zukunftssicher', 'D) Überoptimierung auf historische Daten, die in der Zukunft versagt'], "answer": "D"},
    # 48
    {"question": "Was ist Walk-Forward-Analyse?", "options": ['A) Backtest mit allen Daten', 'B) Methode: Optimieren auf Teilperiode, testen auf nächster Periode, wiederholen', 'C) Forward Test', 'D) Demo-Trading'], "answer": "B"},
    # 49
    {"question": "Was ist Out-of-Sample Testing?", "options": ['A) Test mit denselben Daten wie Optimierung', 'B) Kein Test', 'C) Test mit Daten, die nicht für die Optimierung verwendet wurden', 'D) Live-Trading'], "answer": "C"},
    # 50
    {"question": "Was ist der Profit Factor?", "options": ['A) Nur Gewinn', 'B) Nur Verlust', 'C) Margin', 'D) Bruttogewinne geteilt durch Bruttoverluste'], "answer": "D"},
    # 51
    {"question": "Was ist ein guter Profit Factor?", "options": ['A) Unter 1', 'B) Genau 1', 'C) Über 1.5 gilt als gut', 'D) Über 100'], "answer": "C"},
    # 52
    {"question": "Was ist die Kelly Criterion?", "options": ['A) Formel zur Berechnung der optimalen Positionsgröße basierend auf Winrate und Payoff', 'B) Nur für Poker', 'C) Indikator', 'D) Chartmuster'], "answer": "A"},
    # 53
    {"question": "Warum nutzen viele Trader nur einen Bruchteil der Kelly Criterion?", "options": ['A) Kelly ist immer falsch', 'B) Volle Kelly ist zu aggressiv und führt zu hohen Drawdowns', 'C) Broker erlauben es nicht', 'D) Hat keinen Grund'], "answer": "B"},
    # 54
    {"question": "Was ist Regime Detection?", "options": ['A) Politische Analyse', 'B) Nur Nachrichtenhandel', 'C) Erkennung verschiedener Marktphasen (Trend, Range, Volatilität)', 'D) Indikator'], "answer": "C"},
    # 55
    {"question": "Was ist ein Hidden Markov Model (HMM) im Trading?", "options": ['A) Chartmuster', 'B) Candlestick', 'C) Volumenindikator', 'D) Statistisches Modell zur Erkennung versteckter Marktzustände'], "answer": "D"},
    # 56
    {"question": "Was ist Autocorrelation in Kursreihen?", "options": ['A) Zufällige Bewegung', 'B) Korrelation einer Kursreihe mit sich selbst in der Vergangenheit', 'C) Korrelation zwischen zwei Assets', 'D) Indikator'], "answer": "B"},
    # 57
    {"question": "Was ist ein Volatility Smile?", "options": ['A) Muster bei impliziter Volatilität: höher für ITM/OTM-Optionen als für ATM', 'B) Chartmuster', 'C) Candlestick', 'D) Trendlinie'], "answer": "A"},
    # 58
    {"question": "Was ist Implied Volatility?", "options": ['A) Historische Volatilität', 'B) Vom Markt erwartete zukünftige Volatilität, eingepreist in Optionen', 'C) Realisierte Volatilität', 'D) ATR'], "answer": "B"},
    # 59
    {"question": "Was ist der Unterschied zwischen Implied und Realized Volatility?", "options": ['A) Kein Unterschied', 'B) Beide zeigen die Vergangenheit', 'C) Implied ist Erwartung, Realized ist tatsächlich eingetretene Volatilität', 'D) Beide zeigen die Zukunft'], "answer": "C"},
    # 60
    {"question": "Was ist ein Volatility Crush?", "options": ['A) Anstieg der Volatilität', 'B) Normaler Zustand', 'C) Indikator', 'D) Starker Rückgang der impliziten Volatilität nach einem Event (z.B. Earnings)'], "answer": "D"},
    # 61
    {"question": "Was ist die Volatilitäts-Oberfläche (Vol Surface)?", "options": ['A) 3D-Darstellung der Implied Volatility über verschiedene Strikes und Laufzeiten', 'B) Nur ein Chart', 'C) Indikator', 'D) Candlestick-Muster'], "answer": "A"},
    # 62
    {"question": "Was ist ein Straddle im Optionshandel?", "options": ['A) Nur Call kaufen', 'B) Gleichzeitiger Kauf von Call und Put mit gleichem Strike und Verfall', 'C) Nur Put kaufen', 'D) Verkauf beider'], "answer": "B"},
    # 63
    {"question": "Wann profitiert ein Straddle?", "options": ['A) Nur bei steigenden Kursen', 'B) Nur bei fallenden Kursen', 'C) Bei starker Bewegung in eine Richtung – egal welche', 'D) Nur bei Seitwärtsbewegung'], "answer": "C"},
    # 64
    {"question": "Was ist ein Strangle?", "options": ['A) Wie Straddle, aber Call und Put haben verschiedene Strikes', 'B) Gleich wie Straddle', 'C) Nur Calls', 'D) Nur Puts'], "answer": "A"},
    # 65
    {"question": "Was ist ein Iron Condor?", "options": ['A) Einzelner Trade', 'B) Chartmuster', 'C) Indikator', 'D) Optionsstrategie: Verkauf von Call/Put-Spreads für Seitwärtsmärkte'], "answer": "D"},
    # 66
    {"question": "Was ist Theta Decay bei Optionen?", "options": ['A) Kursgewinn', 'B) Zeitwertverlust – Optionen verlieren mit der Zeit an Wert', 'C) Volumenrückgang', 'D) Spread-Änderung'], "answer": "B"},
    # 67
    {"question": "Was ist Delta bei Optionen?", "options": ['A) Zeitwert', 'B) Volatilität', 'C) Sensitivität des Optionspreises gegenüber Kursänderung des Underlyings', 'D) Spread'], "answer": "C"},
    # 68
    {"question": "Was ist Gamma bei Optionen?", "options": ['A) Rate der Änderung von Delta bei Kursänderung', 'B) Zeitwert', 'C) Volatilität', 'D) Volumen'], "answer": "A"},
    # 69
    {"question": "Was ist Vega bei Optionen?", "options": ['A) Zeitwert', 'B) Delta-Änderung', 'C) Kursrichtung', 'D) Sensitivität des Optionspreises gegenüber Volatilitätsänderung'], "answer": "D"},
    # 70
    {"question": "Was ist ein COT-Report?", "options": ['A) Chartmuster', 'B) Commitment of Traders – zeigt Positionierung von Commercials, Large Specs und Retail', 'C) Indikator', 'D) Volumenanzeige'], "answer": "B"},
    # 71
    {"question": "Wer sind 'Commercials' im COT-Report?", "options": ['A) Retail-Trader', 'B) Spekulanten', 'C) Hedger – Unternehmen, die sich gegen Preisrisiken absichern', 'D) Broker'], "answer": "C"},
    # 72
    {"question": "Warum sind extreme COT-Positionen relevant?", "options": ['A) Irrelevant', 'B) Nur für Rohstoffe', 'C) Nur für Forex', 'D) Können bevorstehende Trendwenden signalisieren'], "answer": "D"},
    # 73
    {"question": "Was ist Open Interest?", "options": ['A) Gesamtzahl der ausstehenden Kontrakte', 'B) Handelsvolumen', 'C) Spread', 'D) Margin'], "answer": "A"},
    # 74
    {"question": "Was bedeutet steigendes Open Interest bei steigenden Kursen?", "options": ['A) Schwacher Trend', 'B) Neues Geld fließt in den Markt – Trend wird bestätigt', 'C) Trendende', 'D) Kein Signal'], "answer": "B"},
    # 75
    {"question": "Was ist die Yield Curve?", "options": ['A) Aktienchart', 'B) Forex-Indikator', 'C) Zinskurve – Verhältnis von Zinssätzen verschiedener Laufzeiten', 'D) Volumenanzeige'], "answer": "C"},
    # 76
    {"question": "Was signalisiert eine invertierte Yield Curve?", "options": ['A) Wirtschaftsboom', 'B) Steigende Aktien', 'C) Höhere Zinsen', 'D) Mögliche Rezession – kurzfristige Zinsen höher als langfristige'], "answer": "D"},
    # 77
    {"question": "Was ist Quantitative Easing (QE)?", "options": ['A) Zentralbank kauft Anleihen, um Geld in den Markt zu pumpen', 'B) Zinsen erhöhen', 'C) Geld aus dem Markt nehmen', 'D) Steuerpolitik'], "answer": "A"},
    # 78
    {"question": "Was ist Quantitative Tightening (QT)?", "options": ['A) Geld drucken', 'B) Zentralbank reduziert ihre Bilanz – Liquidität wird entzogen', 'C) Zinsen senken', 'D) Steuern senken'], "answer": "B"},
    # 79
    {"question": "Was ist der Fed Funds Rate?", "options": ['A) Aktienindex', 'B) Spread', 'C) US-Leitzins, den Banken für Übernacht-Kredite zahlen', 'D) Forex-Paar'], "answer": "C"},
    # 80
    {"question": "Was ist Forward Guidance?", "options": ['A) Chartmuster', 'B) Indikator', 'C) Backtesting', 'D) Kommunikation der Zentralbank über zukünftige Geldpolitik'], "answer": "D"},
    # 81
    {"question": "Was ist der Dot Plot der FED?", "options": ['A) Grafische Darstellung der Zinserwartungen einzelner FED-Mitglieder', 'B) Aktienchart', 'C) Volumenanzeige', 'D) Forex-Chart'], "answer": "A"},
    # 82
    {"question": "Was ist die Rolle von Treasury Yields für den Aktienmarkt?", "options": ['A) Keine Rolle', 'B) Steigende Yields konkurrieren mit Aktien und können Druck erzeugen', 'C) Steigende Yields sind immer bullisch', 'D) Nur für Anleihen relevant'], "answer": "B"},
    # 83
    {"question": "Was ist ein Credit Spread im makroökonomischen Kontext?", "options": ['A) Optionsstrategie', 'B) Forex-Spread', 'C) Differenz zwischen Unternehmensanleihen- und Staatsanleihen-Zinsen', 'D) Broker-Gebühr'], "answer": "C"},
    # 84
    {"question": "Was zeigt ein sich weitender Credit Spread?", "options": ['A) Optimismus', 'B) Stabilität', 'C) Normaler Zustand', 'D) Zunehmende Risikoaversion und Stress im Finanzsystem'], "answer": "D"},
    # 85
    {"question": "Was ist die DXY-Korrelation zu Emerging Market Assets?", "options": ['A) Positive Korrelation', 'B) Starker Dollar belastet oft Emerging Markets (negative Korrelation)', 'C) Keine Korrelation', 'D) Nur für Gold relevant'], "answer": "B"},
    # 86
    {"question": "Was ist ein Liquidity Void im SMC?", "options": ['A) Hohe Liquidität', 'B) Indikator', 'C) Bereich ohne nennenswerte Handelsaktivität – Kurs bewegt sich schnell hindurch', 'D) Support-Level'], "answer": "C"},
    # 87
    {"question": "Was ist ein Propulsion Block?", "options": ['A) Orderblock, der nach einem BOS entsteht und starkes Momentum zeigt', 'B) Normaler Support', 'C) Fibonacci-Level', 'D) Moving Average'], "answer": "A"},
    # 88
    {"question": "Was ist ein Reclaimed Orderblock?", "options": ['A) Neuer Orderblock', 'B) Orderblock, der gebrochen wurde und dann zurückerobert wird', 'C) Fibonacci-Zone', 'D) Gap'], "answer": "B"},
    # 89
    {"question": "Was ist Institutional Order Flow Entry Drill (IOFED)?", "options": ['A) Indikator', 'B) Chartmuster', 'C) ICT-Konzept: Sequenz aus Displacement, FVG und Orderblock für Entries', 'D) Ordertyp'], "answer": "C"},
    # 90
    {"question": "Was ist ein Turtle Soup Setup?", "options": ['A) Trendfolge-Setup', 'B) RSI-Strategie', 'C) MACD-Setup', 'D) Fading eines Breakouts: Einstieg gegen den Ausbruch bei Fehlausbrüchen'], "answer": "D"},
    # 91
    {"question": "Was ist das 2022 ICT Model?", "options": ['A) Altes Modell', 'B) Entry-Modell: Liquidity Sweep + Market Structure Shift + FVG Entry', 'C) Nur Fibonacci', 'D) Nur Volumen'], "answer": "B"},
    # 92
    {"question": "Was ist ein Market Structure Shift (MSS)?", "options": ['A) Seitwärtsbewegung', 'B) Trendfortsetzung', 'C) Erste Änderung der Marktstruktur, die einen ChoCh bestätigt', 'D) Gap'], "answer": "C"},
    # 93
    {"question": "Was ist ein Premium/Discount Array im ICT?", "options": ['A) Fibonacci allein', 'B) Indikator', 'C) Moving Average', 'D) Einteilung von Orderblocks/FVGs in Premium- oder Discount-Bereiche'], "answer": "D"},
    # 94
    {"question": "Was ist ein Re-Distribution Schematic nach Wyckoff?", "options": ['A) Akkumulation nach Abwärtstrend', 'B) Distributionsmuster, das innerhalb eines Abwärtstrends auftritt und Fortsetzung signalisiert', 'C) Markup-Phase', 'D) Spring'], "answer": "B"},
    # 95
    {"question": "Was ist Re-Accumulation nach Wyckoff?", "options": ['A) Akkumulationsmuster innerhalb eines Aufwärtstrends – Trendfortsetzung', 'B) Distribution', 'C) Trendwende', 'D) Selling Climax'], "answer": "A"},
    # 96
    {"question": "Was ist ein Absorption Pattern im Order Flow?", "options": ['A) Starker Trend', 'B) Gap', 'C) Indikator-Signal', 'D) Große Orders absorbieren Gegenseite ohne Kursbewegung – Vorbote einer Wende'], "answer": "D"},
    # 97
    {"question": "Was ist Tape Reading?", "options": ['A) Chartanalyse', 'B) Lesen des Time & Sales – Analyse einzelner Transaktionen in Echtzeit', 'C) Indikator nutzen', 'D) Nur für Aktien'], "answer": "B"},
    # 98
    {"question": "Was ist ein Imbalance im Footprint Chart?", "options": ['A) Gleichgewicht', 'B) Indikator', 'C) Deutliches Übergewicht von Käufern oder Verkäufern auf einem Preisniveau', 'D) Gap'], "answer": "C"},
    # 99
    {"question": "Was ist der POC Shift (Migration)?", "options": ['A) POC bleibt gleich', 'B) Indikator-Signal', 'C) Fibonacci-Anpassung', 'D) Verschiebung des Point of Control in Richtung des neuen Wertebereichs'], "answer": "D"},
    # 100
    {"question": "Was ist die Auction Market Theory?", "options": ['A) Märkte suchen durch Auktionsprozesse nach dem fairen Preis', 'B) Nur für Auktionshäuser', 'C) Indikator', 'D) Chartmuster'], "answer": "A"},
    # 101
    {"question": "Was ist ein Single Print im Market Profile?", "options": ['A) Hoher Volumensbereich', 'B) TPO, das nur einmal auf einem Preisniveau erscheint – zeigt schnelle Bewegung', 'C) VPOC', 'D) Fibonacci-Level'], "answer": "B"},
    # 102
    {"question": "Was ist ein Poor High/Poor Low im Market Profile?", "options": ['A) Starkes Hoch/Tief', 'B) Fibonacci-Level', 'C) Unvollständiges Hoch/Tief ohne Ablehnung – wird oft erneut getestet', 'D) Indikator'], "answer": "C"},
    # 103
    {"question": "Was ist ein Excess High/Low?", "options": ['A) Schwaches Hoch/Tief', 'B) Normales Hoch/Tief', 'C) Indikator', 'D) Starkes Hoch/Tief mit klarer Ablehnung – weniger wahrscheinlich erneut getestet'], "answer": "D"},
    # 104
    {"question": "Was ist das Konzept der 'Failed Auction'?", "options": ['A) Erfolgreicher Ausbruch', 'B) Normaler Trade', 'C) Trendfortsetzung', 'D) Markt testet ein Level, findet keine Akzeptanz und kehrt um'], "answer": "D"},
    # 105
    {"question": "Was ist Smart Money Trap?", "options": ['A) Retail-Trader profitieren', 'B) Situation, in der Smart Money absichtlich falsche Signale erzeugt', 'C) Chartmuster ohne Bedeutung', 'D) Indikator'], "answer": "B"},
    # 106
    {"question": "Was ist die Breaker-Block-Theorie?", "options": ['A) Gescheiterter Orderblock wird zur Gegenzone – z.B. bullischer OB wird bärisch', 'B) Normaler Orderblock', 'C) Gap', 'D) Moving Average'], "answer": "A"},
    # 107
    {"question": "Was ist ein Rejection Block?", "options": ['A) Orderblock', 'B) Zone, die durch lange Dochte gebildet wird – zeigt starke Ablehnung', 'C) Gap', 'D) Fibonacci-Zone'], "answer": "B"},
    # 108
    {"question": "Was ist ein Vacuum Block?", "options": ['A) Normaler Block', 'B) Trendlinie', 'C) Bereich geringer Liquidität, der als Magnet für Preisbewegungen wirkt', 'D) Indikator'], "answer": "C"},
    # 109
    {"question": "Was ist der Quarterly Theory Cycle im ICT?", "options": ['A) Jahres-Zyklus', 'B) Wochen-Zyklus', 'C) Tages-Zyklus', 'D) Quartalsweise Muster: Accumulation → Manipulation → Distribution → Decline'], "answer": "D"},
    # 110
    {"question": "Was ist Algorithmic Price Delivery?", "options": ["A) Konzept, dass institutionelle Algorithmen den Preis zu bestimmten Levels 'liefern'", 'B) Zufällige Kursbewegung', 'C) Indikator', 'D) Nur Theorie ohne Praxis'], "answer": "A"},
    # 111
    {"question": "Was ist ein NWOG/NDOG (New Week/New Day Opening Gap)?", "options": ['A) Normaler Gap', 'B) Gap zwischen dem Schlusskurs einer Periode und dem Eröffnungskurs der nächsten', 'C) Indikator', 'D) Chartmuster'], "answer": "B"},
    # 112
    {"question": "Was ist die True Day Open im ICT-Kontext?", "options": ['A) NY Midnight Open – 0:00 Uhr New Yorker Zeit als wahrer Tagesbeginn', 'B) London Open', 'C) Asia Open', 'D) Broker-abhängig'], "answer": "A"},
    # 113
    {"question": "Was ist ein Balanced Price Range?", "options": ['A) Single FVG', 'B) Fibonacci-Level', 'C) Bereich, in dem sich zwei gegenläufige FVGs überlappen', 'D) Support/Resistance'], "answer": "C"},
    # 114
    {"question": "Was ist ein Consequent Encroachment?", "options": ['A) Orderblock-Mitte', 'B) Fibonacci 50%', 'C) Moving Average', 'D) 50%-Level einer FVG, das oft als Reaktionspunkt dient'], "answer": "D"},
    # 115
    {"question": "Was ist ein Standard Deviation Move?", "options": ['A) Normaler Tagestrend', 'B) Kursbewegung, die X Standardabweichungen vom Mittelwert entfernt ist', 'C) Indikator', 'D) Fibonacci-Level'], "answer": "B"},
    # 116
    {"question": "Was bedeutet 'Delivery' im ICT/SMC-Kontext?", "options": ['A) Orderausführung', 'B) Spread', "C) Der Prozess, wie der Preis von einem Level zum nächsten 'geliefert' wird", 'D) Volumen'], "answer": "C"},
    # 117
    {"question": "Was ist ein Mitigation im SMC?", "options": ['A) Wenn der Kurs zu einem unmitigierten Orderblock zurückkehrt und dort reagiert', 'B) Gap Fill', 'C) Trendfortsetzung', 'D) Breakout'], "answer": "A"},
    # 118
    {"question": "Was ist Risk Parity?", "options": ['A) Gleiches Kapital pro Position', 'B) Portfolio-Strategie: Risikobeitrag jeder Assetklasse wird gleich gewichtet', 'C) Nur Aktien kaufen', 'D) Maximaler Hebel'], "answer": "B"},
    # 119
    {"question": "Was ist ein Correlation Breakdown?", "options": ['A) Normale Korrelation', 'B) Indikator', 'C) Wenn historische Korrelationen plötzlich nicht mehr gelten – oft in Krisen', 'D) Chartmuster'], "answer": "C"},
    # 120
    {"question": "Was ist Tail Risk?", "options": ['A) Normales Risiko', 'B) Moderates Risiko', 'C) Spread-Risiko', "D) Risiko extremer, seltener Ereignisse in den 'Rändern' der Verteilung"], "answer": "D"},
    # 121
    {"question": "Was ist ein Fat Tail in der Statistik?", "options": ['A) Normalverteilung', 'B) Verteilung mit mehr extremen Ereignissen als bei Normalverteilung erwartet', 'C) Geringe Volatilität', 'D) Gleichmäßige Verteilung'], "answer": "B"},
    # 122
    {"question": "Warum sind Fat Tails im Trading relevant?", "options": ['A) Irrelevant', 'B) Nur für Optionen', 'C) Extreme Kursbewegungen treten häufiger auf als Modelle annehmen', 'D) Nur in Krypto'], "answer": "C"},
    # 123
    {"question": "Was ist ein Regime Switch?", "options": ['A) Plötzlicher Wechsel des Marktcharakters (z.B. von Range zu Trend)', 'B) Indikator-Wechsel', 'C) Broker-Wechsel', 'D) Timeframe-Wechsel'], "answer": "A"},
    # 124
    {"question": "Was ist ein Dispersion Trade?", "options": ['A) Normaler Aktienhandel', 'B) Chartmuster', 'C) Indikator', 'D) Handel auf die Differenz zwischen Index-Volatilität und Einzelaktien-Volatilität'], "answer": "D"},
    # 125
    {"question": "Was ist Reflexivity nach Soros?", "options": ['A) Chartmuster', 'B) Markterwartungen beeinflussen die Realität, die wiederum Erwartungen beeinflusst', 'C) Indikator', 'D) Nur Theorie'], "answer": "B"},
    # 126
    {"question": "Was ist das Stock-to-Flow Modell?", "options": ['A) Forex-Modell', 'B) Aktienmodell', 'C) Verhältnis von bestehendem Bestand zur Neuproduktion – oft für Gold/Bitcoin verwendet', 'D) Indikator'], "answer": "C"},
    # 127
    {"question": "Was ist der Cantillon-Effekt?", "options": ['A) Neues Geld profitiert die Erstempfänger mehr als die Gesamtwirtschaft', 'B) Geld hat keinen Effekt', 'C) Inflation betrifft alle gleich', 'D) Nur für Krypto relevant'], "answer": "A"},
    # 128
    {"question": "Was ist ein Minsky Moment?", "options": ['A) Normaler Marktzyklus', 'B) Chartmuster', 'C) Indikator', 'D) Plötzlicher Zusammenbruch nach langer Kreditexpansion und Spekulation'], "answer": "D"},
    # 129
    {"question": "Was ist ein Flash Crash?", "options": ['A) Langsamer Abverkauf', 'B) Extremer, kurzfristiger Kurseinbruch innerhalb von Minuten/Sekunden', 'C) Normaler Pullback', 'D) Gap'], "answer": "B"},
    # 130
    {"question": "Was war der Flash Crash von 2010?", "options": ['A) Langsamer Bärenmarkt', 'B) Krypto-Crash', 'C) Dow Jones fiel innerhalb von Minuten ~1000 Punkte und erholte sich schnell', 'D) Forex-Event'], "answer": "C"},
    # 131
    {"question": "Was ist eine Volcker Rule?", "options": ['A) Trading-Strategie', 'B) Chartmuster', 'C) Indikator', 'D) Regulierung, die Eigenhandel von Banken einschränkt'], "answer": "D"},
    # 132
    {"question": "Was ist Basel III und warum ist es für Trader relevant?", "options": ['A) Bankregulierung, die Kapitalanforderungen erhöht und Marktliquidität beeinflusst', 'B) Nur für Banken', 'C) Forex-Regulierung', 'D) Krypto-Gesetz'], "answer": "A"},
    # 133
    {"question": "Was ist Repo Rate und warum wird sie beobachtet?", "options": ['A) Aktienindex', 'B) Zinssatz für kurzfristige Wertpapierleihe – zeigt Stress im Finanzsystem', 'C) Forex-Rate', 'D) Spread'], "answer": "B"},
    # 134
    {"question": "Was ist ein Convexity Trade?", "options": ['A) Linearer Trade', 'B) Indikator', 'C) Trade mit asymmetrischem Payoff – kleines Risiko, großes Potenzial', 'D) Normaler Long-Trade'], "answer": "C"},
    # 135
    {"question": "Was ist ein Asymmetric Risk Profile?", "options": ['A) Gleich viel Risiko wie Gewinn', 'B) Kein Risiko', 'C) Indikator', 'D) Setup, bei dem potenzielle Gewinne deutlich größer sind als potenzielle Verluste'], "answer": "D"},
    # 136
    {"question": "Was ist ein Barbell Strategy nach Taleb?", "options": ['A) Alles in eine Assetklasse', 'B) Gleichmäßige Verteilung', 'C) Kombination aus sehr sicheren und sehr riskanten Positionen, nichts dazwischen', 'D) Nur Anleihen'], "answer": "C"},
    # 137
    {"question": "Was ist Skewness in der Renditeverteilung?", "options": ['A) Symmetrie', 'B) Maß für die Asymmetrie einer Verteilung', 'C) Volatilität', 'D) Volumen'], "answer": "B"},
    # 138
    {"question": "Was ist Kurtosis?", "options": ['A) Volatilität', 'B) Volumen', 'C) Trend', "D) Maß für die 'Spitzheit' einer Verteilung – hohe Kurtosis = mehr Extremereignisse"], "answer": "D"},
    # 139
    {"question": "Was ist ein Pairs Trade?", "options": ['A) Long und Short auf zwei korrelierte Assets, um von der Spread-Veränderung zu profitieren', 'B) Zwei Long-Positionen', 'C) Zwei Short-Positionen', 'D) Nur für Forex'], "answer": "A"},
    # 140
    {"question": "Was ist Cointegration und warum ist sie für Pairs Trading wichtig?", "options": ['A) Gleich wie Korrelation', 'B) Langfristige stabile Beziehung zwischen zwei Zeitreihen – wichtiger als Korrelation', 'C) Indikator', 'D) Nur für Aktien'], "answer": "B"},
    # 141
    {"question": "Was ist ein Structural Break in einer Zeitreihe?", "options": ['A) Chartmuster', 'B) Indikator', 'C) Plötzliche Veränderung der statistischen Eigenschaften einer Zeitreihe', 'D) Normaler Trend'], "answer": "C"},
    # 142
    {"question": "Was ist ein Market Microstructure?", "options": ['A) Charttyp', 'B) Studium der Mechanismen und Regeln, wie Preise im Markt entstehen', 'C) Indikator', 'D) Ordertyp'], "answer": "B"},
    # 143
    {"question": "Was ist Price Discovery?", "options": ['A) Chartanalyse', 'B) Indikator', 'C) Fibonacci', 'D) Prozess, durch den der Markt den fairen Preis eines Assets findet'], "answer": "D"},
    # 144
    {"question": "Was ist ein Liquidity Provider?", "options": ['A) Retail-Trader', 'B) Chartprogramm', 'C) Marktteilnehmer, der ständig Kauf-/Verkaufsangebote stellt', 'D) Indikator'], "answer": "C"},
    # 145
    {"question": "Was ist das Maker-Taker Fee Model?", "options": ['A) Maker (Liquiditätsprovider) erhält Rabatt, Taker (Liquiditätsnehmer) zahlt Gebühr', 'B) Beide zahlen gleich', 'C) Maker zahlt mehr', 'D) Keine Gebühren'], "answer": "A"},
    # 146
    {"question": "Was ist ein Sweep im SMC/ICT-Kontext?", "options": ['A) Normaler Breakout', 'B) Kurze, schnelle Bewegung über ein Hoch/Tief, die Liquidität nimmt und sofort zurückkehrt', 'C) Trendfortsetzung', 'D) Moving Average Crossover'], "answer": "B"},
    # 147
    {"question": "Was ist die Efficient Market Hypothesis (EMH)?", "options": ['A) Märkte sind immer ineffizient', 'B) Nur für Krypto', 'C) Theorie, dass alle verfügbaren Infos bereits im Preis eingepreist sind', 'D) Chartmuster'], "answer": "C"},
    # 148
    {"question": "Was ist Behavioral Finance?", "options": ['A) Forschungsfeld: Wie psychologische Verzerrungen Marktentscheidungen beeinflussen', 'B) Nur Charttechnik', 'C) Indikator-Analyse', 'D) Fundamentalanalyse'], "answer": "A"},
    # 149
    {"question": "Was ist Anchoring Bias im Trading?", "options": ['A) Rationale Entscheidung', 'B) Übermäßige Fixierung auf eine Referenzzahl (z.B. Einstiegspreis)', 'C) Nur bei Anfängern', 'D) Chartmuster'], "answer": "B"},
    # 150
    {"question": "Was ist Confirmation Bias im Trading?", "options": ['A) Objektive Analyse', 'B) Trendfolge', 'C) Indikator-basiert', 'D) Nur Informationen suchen und wahrnehmen, die die eigene Meinung bestätigen'], "answer": "D"},
]
