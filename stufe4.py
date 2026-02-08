# --- STUFE 4: ULTRA SCHWER (Experten-Level) ---
# 150 Fragen - Richtige Antworten gleichmäßig auf A, B, C, D verteilt

quiz_stufe4 = [
    # 1
    {"question": "Was ist der Hurst-Exponent und was zeigt ein Wert > 0.5?", "options": ["A) Trendpersistenz – die Zeitreihe hat ein 'Gedächtnis'", 'B) Mean Reversion', 'C) Zufällige Bewegung', 'D) Hohe Volatilität'], "answer": "A"},
    # 2
    {"question": "Was zeigt ein Hurst-Exponent < 0.5?", "options": ['A) Mean-Reversion-Verhalten', 'B) Trendpersistenz', 'C) Zufällige Bewegung', 'D) Hohe Liquidität'], "answer": "A"},
    # 3
    {"question": "Was ist ein Hurst-Exponent von exakt 0.5?", "options": ['A) Starker Trend', 'B) Mean Reversion', 'C) Hohe Volatilität', 'D) Random Walk – keine Vorhersagbarkeit'], "answer": "D"},
    # 4
    {"question": "Was ist die Fractal Dimension eines Marktes?", "options": ['A) Maß für die Komplexität und Rauheit einer Preiskurve', 'B) Fibonacci-Level', 'C) Indikator', 'D) Volumenanzeige'], "answer": "A"},
    # 5
    {"question": "Was ist ein Lévy-Flight-Modell im Kontext von Finanzmärkten?", "options": ['A) Modell mit gelegentlichen extremen Sprüngen statt Normalverteilung', 'B) Normalverteiltes Modell', 'C) Moving Average', 'D) Nur für Forex'], "answer": "A"},
    # 6
    {"question": "Was ist der Unterschied zwischen fraktaler Brownian Motion und Standard Brownian Motion?", "options": ['A) Kein Unterschied', 'B) Beide sind identisch', 'C) Standard BM hat Autokorrelation', 'D) Fraktale BM erlaubt Autokorrelation (Hurst ≠ 0.5), Standard BM nicht'], "answer": "D"},
    # 7
    {"question": "Was ist ein GARCH-Modell?", "options": ['A) Trendmodell', 'B) Volumenmodell', 'C) Ordertyp', 'D) Modell zur Vorhersage zeitvarianter Volatilität basierend auf vergangener Volatilität'], "answer": "D"},
    # 8
    {"question": "Was modelliert GARCH(1,1) konkret?", "options": ['A) Aktuelle Volatilität als Funktion des letzten Residuums und der letzten Varianz', 'B) Nur den Trend', 'C) Nur das Volumen', 'D) Den Spread'], "answer": "A"},
    # 9
    {"question": "Was ist ein Stochastic Volatility Model?", "options": ['A) Volatilität ist konstant', 'B) GARCH-Alternative ohne stochastische Komponente', 'C) Nur für Optionen', 'D) Modell, in dem Volatilität selbst ein zufälliger Prozess ist'], "answer": "D"},
    # 10
    {"question": "Was ist das Heston-Modell?", "options": ['A) Trendmodell', 'B) Volumenmodell', 'C) Chartmuster', 'D) Stochastic Volatility Modell mit Mean-Reversion der Volatilität und Korrelation zum Preis'], "answer": "D"},
    # 11
    {"question": "Was ist der SABR-Modell und wofür wird es genutzt?", "options": ['A) Aktienanalyse', 'B) Chartmuster', 'C) Stochastic Alpha Beta Rho – Modellierung der Volatility Smile bei Optionen', 'D) Forex-Modell'], "answer": "C"},
    # 12
    {"question": "Was ist die Black-Scholes-Formel und welche kritische Annahme macht sie?", "options": ['A) Optionspreismodell mit Annahme konstanter Volatilität und Normalverteilung', 'B) Futures-Modell', 'C) Forex-Modell', 'D) Modell ohne Annahmen'], "answer": "A"},
    # 13
    {"question": "Warum versagt Black-Scholes in der Praxis oft?", "options": ['A) Funktioniert perfekt', 'B) Reale Renditen sind nicht normalverteilt und Volatilität ist nicht konstant', 'C) Nur für Aktien falsch', 'D) Nur bei hohem Volumen'], "answer": "B"},
    # 14
    {"question": "Was ist ein Local Volatility Model?", "options": ['A) Globales Modell', 'B) Konstante Volatilität', 'C) Modell, in dem Volatilität eine deterministische Funktion von Preis und Zeit ist', 'D) Nur Implied Volatility'], "answer": "C"},
    # 15
    {"question": "Was ist der Dupire-Ansatz?", "options": ['A) Chartmuster', 'B) Indikator', 'C) RSI-Variante', 'D) Methode zur Berechnung lokaler Volatilität aus Optionspreisen'], "answer": "D"},
    # 16
    {"question": "Was ist ein Jump-Diffusion-Modell (Merton)?", "options": ['A) Erweiterung von Black-Scholes um plötzliche Kurssprünge (Jumps)', 'B) Nur Diffusion', 'C) Nur Jumps', 'D) Trendmodell'], "answer": "A"},
    # 17
    {"question": "Was ist Variance Risk Premium?", "options": ['A) Spread', 'B) Differenz zwischen impliziter und realisierter Varianz – oft positiv, da Hedger Prämie zahlen', 'C) Nur Volatilität', 'D) Orderkosten'], "answer": "B"},
    # 18
    {"question": "Was ist ein Variance Swap?", "options": ['A) Normaler Swap', 'B) Forex-Produkt', 'C) Derivat, das die Differenz zwischen realisierter und fixer Varianz abrechnet', 'D) Aktientausch'], "answer": "C"},
    # 19
    {"question": "Was ist ein Volatility Swap?", "options": ['A) Gleich wie Variance Swap', 'B) Forex-Swap', 'C) Aktien-Swap', 'D) Derivat auf realisierte Volatilität statt Varianz – konvexitätsbereinigt'], "answer": "D"},
    # 20
    {"question": "Was ist der VIX Term Structure und was zeigt Contango?", "options": ['A) Kurzfristige VIX-Futures teurer als langfristige', 'B) VIX-Futures steigen mit Laufzeit – Markt erwartet steigende Volatilität langfristig', 'C) VIX ist konstant', 'D) Kein Zusammenhang'], "answer": "B"},
    # 21
    {"question": "Was bedeutet Backwardation in der VIX Term Structure?", "options": ['A) Normalzustand', 'B) VIX-Futures fallen mit Laufzeit', 'C) Kurzfristige VIX-Futures teurer als langfristige – Angst im Markt', 'D) Kein Signal'], "answer": "C"},
    # 22
    {"question": "Was ist der VVIX?", "options": ['A) VIX des VIX – Volatilität der Volatilität', 'B) Doppelter VIX', 'C) Nur für Optionen', 'D) Aktienindex'], "answer": "A"},
    # 23
    {"question": "Was ist ein Cross-Gamma-Effekt?", "options": ['A) Normales Gamma', 'B) Chartmuster', 'C) Indikator', 'D) Wenn Gamma-Hedging in einem Asset Preisbewegungen in einem korrelierten Asset verursacht'], "answer": "D"},
    # 24
    {"question": "Was ist ein Vanna-Effekt?", "options": ['A) Sensitivität von Delta gegenüber Volatilität – beeinflusst Dealer-Hedging bei Vol-Änderungen', 'B) Nur Theta', 'C) Nur Gamma', 'D) Nur Vega'], "answer": "A"},
    # 25
    {"question": "Was ist Charm (Delta Bleed)?", "options": ['A) Gamma-Effekt', 'B) Änderungsrate von Delta über die Zeit – wie sich Delta mit Zeitablauf ändert', 'C) Vega-Effekt', 'D) Rho-Effekt'], "answer": "B"},
    # 26
    {"question": "Was ist Volga (Vomma)?", "options": ['A) Erste Ableitung von Vega', 'B) Theta-Effekt', 'C) Zweite Ableitung des Optionspreises nach Volatilität – Konvexität von Vega', 'D) Delta-Effekt'], "answer": "C"},
    # 27
    {"question": "Was ist ein GEX (Gamma Exposure) Flip Point?", "options": ['A) Fibonacci-Level', 'B) Moving Average', 'C) Support-Level', 'D) Preisniveau, bei dem Dealer von positivem zu negativem Gamma wechseln'], "answer": "D"},
    # 28
    {"question": "Was passiert bei negativem Dealer Gamma?", "options": ['A) Markt stabilisiert sich', 'B) Dealer müssen in Trendrichtung hedgen – verstärkt Bewegungen', 'C) Kein Effekt', 'D) Spread sinkt'], "answer": "B"},
    # 29
    {"question": "Was passiert bei positivem Dealer Gamma?", "options": ['A) Dealer hedgen gegen den Trend – dämpft Bewegungen und stabilisiert den Markt', 'B) Markt wird volatiler', 'C) Kein Effekt', 'D) Trend verstärkt sich'], "answer": "A"},
    # 30
    {"question": "Was ist ein DIX (Dark Index)?", "options": ['A) Volatilitätsindex', 'B) Aktienindex', 'C) Chartmuster', 'D) Maß für Dark Pool Kaufdruck – hoher DIX deutet auf institutionelles Kaufinteresse'], "answer": "D"},
    # 31
    {"question": "Was ist der GEX/DIX-Zusammenhang für Market Making?", "options": ['A) Kein Zusammenhang', 'B) GEX zeigt Dealer-Hedging-Dynamik, DIX zeigt institutionellen Flow – kombiniert ergibt sich Marktrichtung', 'C) Nur für Optionen', 'D) Nur für Aktien'], "answer": "B"},
    # 32
    {"question": "Was ist ein Put Wall?", "options": ['A) Call-Konzentration', 'B) Chartmuster', 'C) Strike mit höchstem Put Open Interest – wirkt als Support durch Dealer-Hedging', 'D) Fibonacci-Level'], "answer": "C"},
    # 33
    {"question": "Was ist ein Call Wall?", "options": ['A) Strike mit höchstem Call Open Interest – wirkt als Resistance durch Dealer-Hedging', 'B) Put-Konzentration', 'C) Support-Level', 'D) Indikator'], "answer": "A"},
    # 34
    {"question": "Was ist Net Gamma Exposure und wie berechnet man es?", "options": ['A) Call Gamma minus Put Gamma × Open Interest × 100 × Spot²', 'B) Nur Call Gamma', 'C) Nur Put Gamma', 'D) Volumen minus Spread'], "answer": "A"},
    # 35
    {"question": "Was ist ein Zero Gamma Level?", "options": ['A) Fibonacci 0%', 'B) Preisniveau, bei dem aggregiertes Dealer Gamma null ist – Übergang von stabilisierend zu destabilisierend', 'C) Support-Level', 'D) VPOC'], "answer": "B"},
    # 36
    {"question": "Was ist Pinning bei Optionsverfall?", "options": ['A) Trend verstärkt sich', 'B) Hohe Volatilität', 'C) Kurs tendiert dazu, sich um Strikes mit hohem Open Interest zu stabilisieren', 'D) Gap'], "answer": "C"},
    # 37
    {"question": "Was ist ein Dealer Delta-Hedge und wie beeinflusst es den Markt?", "options": ['A) Kein Effekt', 'B) Nur bei Futures', 'C) Chartmuster', 'D) Dealer kaufen/verkaufen Underlying, um deltaneutral zu bleiben – bewegt Kurse'], "answer": "D"},
    # 38
    {"question": "Was ist der Skew Index (SKEW)?", "options": ['A) Misst die Wahrscheinlichkeit extremer negativer Renditen – hoher SKEW = Tail Risk steigt', 'B) VIX-Variante', 'C) Volumenindikator', 'D) Trendindikator'], "answer": "A"},
    # 39
    {"question": "Was ist ein Dispersion Trade im Detail?", "options": ['A) Einfacher Long-Trade', 'B) Verkauf von Index-Volatilität und Kauf von Einzelaktien-Volatilität – profitiert von Korrelationsrückgang', 'C) Nur Index kaufen', 'D) Nur Einzelaktien kaufen'], "answer": "B"},
    # 40
    {"question": "Was ist Implied Correlation?", "options": ['A) Historische Korrelation', 'B) Chartmuster', 'C) Vom Optionsmarkt implizierte Korrelation zwischen Indexkomponenten', 'D) Indikator'], "answer": "C"},
    # 41
    {"question": "Was ist ein Correlation Swap?", "options": ['A) Aktientausch', 'B) Forex-Swap', 'C) Zins-Swap', 'D) Derivat, das realisierte gegen fixe Korrelation tauscht'], "answer": "D"},
    # 42
    {"question": "Was ist Microstructure Noise?", "options": ['A) Kurzfristige Preisverzerrungen durch Bid-Ask-Bounce, Latenz und diskrete Ticks', 'B) Normales Signal', 'C) Trend', 'D) Nur bei Krypto'], "answer": "A"},
    # 43
    {"question": "Was ist der Roll-Ziliak-Effekt bei hochfrequenten Daten?", "options": ['A) Klares Signal', 'B) Autokorrelation durch Bid-Ask-Bounce, die keine echte Marktinformation enthält', 'C) Volumeneffekt', 'D) Trendeffekt'], "answer": "B"},
    # 44
    {"question": "Was ist ein Realized Kernel Estimator?", "options": ['A) Trendindikator', 'B) Volumenindikator', 'C) Methode zur robusten Schätzung realisierter Volatilität trotz Microstructure Noise', 'D) Moving Average'], "answer": "C"},
    # 45
    {"question": "Was ist der Epps-Effekt?", "options": ['A) Korrelation steigt bei höherer Frequenz', 'B) Kein Effekt', 'C) Nur bei Aktien', 'D) Korrelation zwischen Assets sinkt bei höherer Messfrequenz durch asynchrones Trading'], "answer": "D"},
    # 46
    {"question": "Was ist ein Kyle-Lambda?", "options": ['A) Maß für Market Impact – wie stark eine Order den Preis bewegt', 'B) Volatilitätsmaß', 'C) Volumenmaß', 'D) Indikator'], "answer": "A"},
    # 47
    {"question": "Was ist das Kyle-Modell der Marktmikrostruktur?", "options": ['A) Chartmodell', 'B) Modell mit informiertem Trader, Noise Tradern und Market Maker – Preis enthüllt Information graduell', 'C) Nur für Aktien', 'D) Indikator'], "answer": "B"},
    # 48
    {"question": "Was ist das Glosten-Milgrom-Modell?", "options": ['A) Trendmodell', 'B) Volumenmodell', 'C) Modell: Bid-Ask-Spread entsteht durch adverse Selektion – Market Maker schützt sich vor informierten Tradern', 'D) Chartmuster'], "answer": "C"},
    # 49
    {"question": "Was ist Adverse Selection im Kontext von Market Making?", "options": ['A) Gute Selektion', 'B) Normaler Spread', 'C) Chartmuster', 'D) Risiko, gegen besser informierte Gegenpartei zu handeln'], "answer": "D"},
    # 50
    {"question": "Was ist VPIN (Volume-Synchronized Probability of Informed Trading)?", "options": ['A) Maß für die Wahrscheinlichkeit informierten Handels basierend auf Volumenserien', 'B) Volumenindikator', 'C) VIX-Variante', 'D) Chartmuster'], "answer": "A"},
    # 51
    {"question": "Was ist der Amihud Illiquidity Ratio?", "options": ['A) Liquiditätsmaß', 'B) Verhältnis von absoluter Rendite zu Handelsvolumen – höher = illiquider', 'C) Spread-Maß', 'D) Volatilitätsmaß'], "answer": "B"},
    # 52
    {"question": "Was ist ein Permanent Price Impact vs. Temporary Price Impact?", "options": ['A) Kein Unterschied', 'B) Beide sind temporär', 'C) Permanent verändert den fairen Wert (Information), temporär ist Liquiditätseffekt der sich auflöst', 'D) Beide sind permanent'], "answer": "C"},
    # 53
    {"question": "Was ist das Square-Root Law of Market Impact?", "options": ['A) Impact wächst linear', 'B) Impact wächst exponentiell', 'C) Kein Zusammenhang', 'D) Market Impact wächst proportional zur Wurzel des Ordervolumens'], "answer": "D"},
    # 54
    {"question": "Was ist Optimal Execution (Almgren-Chriss)?", "options": ['A) Framework zur Minimierung von Ausführungskosten unter Berücksichtigung von Impact und Timing-Risiko', 'B) Einfach Market Order', 'C) Limit Order immer', 'D) Nur TWAP'], "answer": "A"},
    # 55
    {"question": "Was ist der Trade-off im Almgren-Chriss-Modell?", "options": ['A) Kein Trade-off', 'B) Balance zwischen Market Impact (schnelle Ausführung) und Timing-Risiko (langsame Ausführung)', 'C) Nur Kosten', 'D) Nur Geschwindigkeit'], "answer": "B"},
    # 56
    {"question": "Was ist ein Information Ratio?", "options": ['A) Sharpe Ratio', 'B) Volatilitätsmaß', 'C) Aktive Rendite geteilt durch Tracking Error – misst Skill des Managers', 'D) Hebel-Ratio'], "answer": "C"},
    # 57
    {"question": "Was ist Tracking Error?", "options": ['A) Gesamtrendite', 'B) Spread', 'C) Volatilität', 'D) Standardabweichung der Differenz zwischen Portfolio- und Benchmark-Rendite'], "answer": "D"},
    # 58
    {"question": "Was ist Jensen's Alpha?", "options": ['A) Risikobereinigte Überrendite gegenüber dem CAPM-erwarteten Return', 'B) Beta', 'C) Sharpe Ratio', 'D) Volatilität'], "answer": "A"},
    # 59
    {"question": "Was ist das Treynor Ratio?", "options": ['A) Rendite geteilt durch systematisches Risiko (Beta)', 'B) Rendite geteilt durch Volatilität', 'C) Nur Rendite', 'D) Nur Beta'], "answer": "A"},
    # 60
    {"question": "Was ist die Omega Ratio?", "options": ['A) Sharpe-Alternative', 'B) Verhältnis der gewichteten Gewinne über einem Schwellenwert zu gewichteten Verlusten darunter', 'C) Nur Gewinne', 'D) Nur Verluste'], "answer": "B"},
    # 61
    {"question": "Was ist ein Conditional Value at Risk (CVaR)?", "options": ['A) Normaler VaR', 'B) Maximaler Gewinn', 'C) Erwarteter Verlust, wenn der VaR überschritten wird – Tail Risk Maß', 'D) Durchschnittlicher Gewinn'], "answer": "C"},
    # 62
    {"question": "Was ist der Unterschied zwischen VaR und CVaR?", "options": ['A) Kein Unterschied', 'B) Beide messen Gewinne', 'C) CVaR ist immer kleiner', 'D) VaR gibt nur das Schwellenniveau, CVaR den erwarteten Verlust darüber hinaus'], "answer": "D"},
    # 63
    {"question": "Was ist ein Coherent Risk Measure?", "options": ['A) Risikomaß, das Subadditivität, Monotonie, positive Homogenität und Translationsinvarianz erfüllt', 'B) Nur VaR', 'C) Nur Volatilität', 'D) Jedes Risikomaß'], "answer": "A"},
    # 64
    {"question": "Ist VaR ein kohärentes Risikomaß?", "options": ['A) Ja', 'B) Nein – VaR verletzt Subadditivität', 'C) Nur manchmal', 'D) Nur bei Normalverteilung'], "answer": "B"},
    # 65
    {"question": "Was ist ein Copula in der Finanzstatistik?", "options": ['A) Korrelationsmaß', 'B) Indikator', 'C) Mathematische Funktion, die marginale Verteilungen zu einer gemeinsamen Verteilung verbindet', 'D) Volatilitätsmodell'], "answer": "C"},
    # 66
    {"question": "Warum sind Copulas wichtig für Risikomodellierung?", "options": ['A) Irrelevant', 'B) Nur für Optionen', 'C) Nur akademisch', 'D) Sie modellieren Abhängigkeiten jenseits linearer Korrelation, besonders in den Tails'], "answer": "D"},
    # 67
    {"question": "Was ist eine Gaussian Copula und warum war sie in der Finanzkrise 2008 problematisch?", "options": ['A) Perfektes Modell', 'B) Unterschätzte Tail-Abhängigkeiten bei CDOs – systemisches Risiko wurde unterschätzt', 'C) Überschätzte Risiko', 'D) Nur für Forex'], "answer": "B"},
    # 68
    {"question": "Was ist ein Regime-Switching GARCH Modell?", "options": ['A) Normales GARCH', 'B) Indikator', 'C) Chartmuster', 'D) GARCH-Modell, das zwischen verschiedenen Volatilitätsregimen wechselt (z.B. ruhig vs. krisenhaft)'], "answer": "D"},
    # 69
    {"question": "Was ist ein Markov Regime-Switching Modell?", "options": ['A) Modell, das diskrete Zustände mit Übergangswahrscheinlichkeiten modelliert', 'B) Nur für Forex', 'C) Chartmuster', 'D) Indikator'], "answer": "A"},
    # 70
    {"question": "Was ist Ergodicity und warum ist es im Trading relevant?", "options": ['A) Irrelevant', 'B) Ensemble-Average ≠ Time-Average – was für die Gruppe gilt, gilt nicht für den Einzelnen', 'C) Nur Mathematik', 'D) Nur für Institutionen'], "answer": "B"},
    # 71
    {"question": "Was ist das Peters'sche Ergodizitätsproblem beim Kelly Criterion?", "options": ['A) Kelly ist immer optimal', 'B) Kein Problem', 'C) Kelly maximiert den Ensemble-Average, aber der einzelne Trader erlebt den Time-Average', 'D) Kelly ist nie nützlich'], "answer": "C"},
    # 72
    {"question": "Was ist ein Ornstein-Uhlenbeck-Prozess?", "options": ['A) Trendmodell', 'B) Random Walk', 'C) Chartmuster', 'D) Mean-Reverting stochastischer Prozess – häufig für Zinsmodellierung'], "answer": "D"},
    # 73
    {"question": "Was ist der Vasicek-Modell für Zinssätze?", "options": ['A) Aktienmodell', 'B) Ein-Faktor Mean-Reversion Zinsmodell basierend auf Ornstein-Uhlenbeck', 'C) Nur für Forex', 'D) Chartmuster'], "answer": "B"},
    # 74
    {"question": "Was ist das Cox-Ingersoll-Ross (CIR) Modell?", "options": ['A) Aktienmodell', 'B) Chartmuster', 'C) Zinsmodell wie Vasicek, aber mit Volatilität proportional zur Wurzel des Zinses (verhindert negative Zinsen)', 'D) Volumenmodell'], "answer": "C"},
    # 75
    {"question": "Was ist die Girsanov-Transformation?", "options": ['A) Chartmuster', 'B) Indikator', 'C) Wechsel von realer zu risikoneutraler Wahrscheinlichkeit zur Derivatbewertung', 'D) Moving Average'], "answer": "C"},
    # 76
    {"question": "Was ist ein Numéraire in der Finanzmathematik?", "options": ['A) Referenz-Asset, relativ zu dem andere Assets bewertet werden', 'B) Indikator', 'C) Chartmuster', 'D) Ordertyp'], "answer": "A"},
    # 77
    {"question": "Was ist der Fundamental Theorem of Asset Pricing?", "options": ['A) Markt ist immer effizient', 'B) Nur für Aktien', 'C) Chartmuster', 'D) Keine Arbitrage ⟺ Existenz eines äquivalenten Martingal-Maßes'], "answer": "D"},
    # 78
    {"question": "Was ist ein Martingal im finanzmathematischen Kontext?", "options": ['A) Trend', 'B) Prozess, bei dem der erwartete zukünftige Wert gleich dem aktuellen Wert ist', 'C) Indikator', 'D) Immer steigend'], "answer": "B"},
    # 79
    {"question": "Was ist ein Semimartingal?", "options": ['A) Halber Martingal', 'B) Indikator', 'C) Allgemeinste Klasse stochastischer Prozesse, für die Itô-Integration definiert ist', 'D) Chartmuster'], "answer": "C"},
    # 80
    {"question": "Was ist Itô's Lemma und warum ist es für Optionspricing essentiell?", "options": ['A) Chartmuster', 'B) Indikator', 'C) Kettenregel für stochastische Prozesse – ermöglicht Ableitung von Derivatpreisen', 'D) Nur für Futures'], "answer": "C"},
    # 81
    {"question": "Was ist der Unterschied zwischen Itô- und Stratonovich-Kalkül?", "options": ['A) Kein Unterschied', 'B) Itô ist nicht-antizipativ (Finanzmodellierung), Stratonovich folgt der Kettenregel (Physik)', 'C) Stratonovich ist für Finanzen', 'D) Beide sind identisch in der Praxis'], "answer": "B"},
    # 82
    {"question": "Was ist ein Feynman-Kac-Theorem?", "options": ['A) Verbindung zwischen partiellen Differentialgleichungen und stochastischen Prozessen', 'B) Nur Physik', 'C) Chartmuster', 'D) Indikator'], "answer": "A"},
    # 83
    {"question": "Was ist ein Greeks-Hedging-Paradoxon bei diskretem Hedging?", "options": ['A) Hedging funktioniert immer perfekt', 'B) Kein Paradoxon', 'C) In der Praxis verursacht diskretes Hedging Gamma-Slippage – perfektes Hedging erfordert kontinuierliches Trading', 'D) Nur bei Put-Optionen'], "answer": "C"},
    # 84
    {"question": "Was ist Pin Risk bei Optionsverfall?", "options": ['A) Kein Risiko', 'B) Normaler Trade', 'C) Indikator', 'D) Risiko für Option-Verkäufer, wenn der Kurs exakt am Strike schließt – unklar ob Assignment erfolgt'], "answer": "D"},
    # 85
    {"question": "Was ist ein Quanto-Option?", "options": ['A) Option auf ein fremdes Asset, abgerechnet in einer anderen Währung ohne FX-Risiko', 'B) Normale Option', 'C) Nur für Forex', 'D) Futures-Option'], "answer": "A"},
    # 86
    {"question": "Was ist eine Barrier Option?", "options": ['A) Normale Option', 'B) Option, die aktiviert (Knock-In) oder deaktiviert (Knock-Out) wird bei Erreichen eines bestimmten Kursniveaus', 'C) Nur für Institutionelle', 'D) Futures'], "answer": "B"},
    # 87
    {"question": "Was ist eine Asian Option?", "options": ['A) Option gehandelt in Asien', 'B) Normale Option', 'C) Option, deren Payoff vom Durchschnittskurs über eine Periode abhängt', 'D) Nur für Forex'], "answer": "C"},
    # 88
    {"question": "Was ist eine Lookback Option?", "options": ['A) Normale Option', 'B) Futures', 'C) Nur theoretisch', 'D) Option, deren Payoff vom Höchst- oder Tiefstkurs während der Laufzeit abhängt'], "answer": "D"},
    # 89
    {"question": "Was ist eine Cliquet Option?", "options": ['A) Serie von Forward-Start-Optionen mit periodischem Reset des Strikes', 'B) Normale Call-Option', 'C) Nur Put-Option', 'D) Futures'], "answer": "A"},
    # 90
    {"question": "Was ist ein Total Return Swap (TRS)?", "options": ['A) Nur Zinsen', 'B) Swap, bei dem eine Partei die Gesamtrendite eines Assets erhält und dafür einen fixen/variablen Zins zahlt', 'C) Nur Dividenden', 'D) Nur Kursgewinne'], "answer": "B"},
    # 91
    {"question": "Was ist Regulatory Arbitrage und warum nutzen Hedgefonds TRS?", "options": ['A) Illegal', 'B) Nur für Banken', 'C) TRS ermöglicht Exposure ohne Besitz – umgeht bestimmte Kapitalanforderungen und Offenlegungspflichten', 'D) Kein Vorteil'], "answer": "C"},
    # 92
    {"question": "Was ist ein Credit Default Swap (CDS)?", "options": ['A) Aktien-Swap', 'B) Forex-Swap', 'C) Zins-Swap', 'D) Versicherungsähnliches Derivat gegen Kreditausfall – Käufer zahlt Prämie, Verkäufer zahlt bei Default'], "answer": "D"},
    # 93
    {"question": "Was ist der iTraxx Index?", "options": ['A) Europäischer CDS-Index, der Kreditrisiko eines Korbes von Unternehmen misst', 'B) Aktienindex', 'C) Volatilitätsindex', 'D) Forex-Index'], "answer": "A"},
    # 94
    {"question": "Was ist ein Basis Trade im Treasury-Markt?", "options": ['A) Einfacher Long-Trade', 'B) Ausnutzung der Differenz zwischen Cash-Treasuries und Treasury-Futures', 'C) Nur für Retail', 'D) Chartmuster'], "answer": "B"},
    # 95
    {"question": "Was ist ein Cheapest-to-Deliver (CTD) bei Treasury Futures?", "options": ['A) Billigstes Asset allgemein', 'B) Forex-Konzept', 'C) Die Anleihe, die für den Futures-Verkäufer am günstigsten zu liefern ist – bestimmt den Futures-Preis', 'D) Indikator'], "answer": "C"},
    # 96
    {"question": "Was ist Convexity bei Anleihen?", "options": ['A) Nur Duration', 'B) Spread', 'C) Chartmuster', 'D) Zweite Ableitung des Anleihepreises nach Zinsen – misst Krümmung der Preis-Zins-Beziehung'], "answer": "D"},
    # 97
    {"question": "Was ist Negative Convexity?", "options": ['A) Anleihe profitiert mehr von Zinsrückgängen als sie bei Zinsanstiegen verliert', 'B) Anleihe verliert überproportional bei Zinsanstieg – typisch für MBS wegen Prepayment-Risiko', 'C) Normale Konvexität', 'D) Kein Effekt'], "answer": "B"},
    # 98
    {"question": "Was ist ein DV01 (Dollar Value of 01)?", "options": ['A) Wertänderung einer Anleihe bei 1 Basispunkt Zinsänderung', 'B) Spread', 'C) Volumen', 'D) 1 Dollar'], "answer": "A"},
    # 99
    {"question": "Was ist ein Swap Spread?", "options": ['A) Forex-Spread', 'B) Broker-Spread', 'C) Bid-Ask-Spread', 'D) Differenz zwischen Swap Rate und Treasury Yield gleicher Laufzeit'], "answer": "D"},
    # 100
    {"question": "Was bedeutet ein negativer Swap Spread?", "options": ['A) Normal', 'B) Abnormale Situation: Swap Rate unter Treasury Yield – deutet auf Marktstress oder regulatorische Verzerrungen', 'C) Positives Signal', 'D) Kein Signal'], "answer": "B"},
    # 101
    {"question": "Was ist ein Funding Squeeze?", "options": ['A) Normaler Markt', 'B) Indikator', 'C) Plötzlicher Mangel an kurzfristiger Liquidität – treibt Repo-Raten hoch', 'D) Chartmuster'], "answer": "C"},
    # 102
    {"question": "Was war die Repo-Krise September 2019?", "options": ['A) Aktiencrash', 'B) Forex-Krise', 'C) Krypto-Crash', 'D) Plötzlicher Anstieg der Repo-Raten durch Liquiditätsengpass – FED musste intervenieren'], "answer": "D"},
    # 103
    {"question": "Was ist ein Reverse Repo Facility (RRP) der FED?", "options": ['A) Instrument, mit dem die FED Liquidität aus dem System zieht – Gegenparteien parken Geld bei der FED', 'B) QE-Tool', 'C) Zinssenkung', 'D) Nur für Banken'], "answer": "A"},
    # 104
    {"question": "Was ist die FED Balance Sheet und warum beobachten Trader sie?", "options": ['A) Irrelevant', 'B) Bilanz der FED: Wachstum = Liquiditätszufuhr (bullish), Schrumpfung = Liquiditätsentzug (bearish)', 'C) Nur für Anleihen', 'D) Nur für Banken'], "answer": "B"},
    # 105
    {"question": "Was ist TGA (Treasury General Account)?", "options": ['A) Aktienindex', 'B) Forex-Konto', 'C) Konto des US-Finanzministeriums bei der FED – Änderungen beeinflussen Marktliquidität', 'D) Indikator'], "answer": "C"},
    # 106
    {"question": "Wie beeinflusst ein steigender TGA-Saldo die Märkte?", "options": ['A) Mehr Liquidität', 'B) Kein Effekt', 'C) Immer bullish', 'D) Entzieht dem Bankensystem Liquidität – potentiell bearish'], "answer": "D"},
    # 107
    {"question": "Was ist die Zusammensetzung der Netto-Liquidität (Fed Liquidity)?", "options": ['A) Fed Balance Sheet minus TGA minus RRP', 'B) Nur Balance Sheet', 'C) Nur TGA', 'D) Nur RRP'], "answer": "A"},
    # 108
    {"question": "Was ist ein Cross-Currency Basis Swap?", "options": ['A) Normaler Forex-Trade', 'B) Tausch von Zinszahlungen in verschiedenen Währungen – Basis zeigt USD-Nachfrage', 'C) Nur für Banken', 'D) Chartmuster'], "answer": "B"},
    # 109
    {"question": "Was zeigt ein sehr negativer Cross-Currency Basis?", "options": ['A) Normaler Markt', 'B) Kein Signal', 'C) Starke USD-Nachfrage und potentieller Stress im globalen Dollarsystem', 'D) USD ist schwach'], "answer": "C"},
    # 110
    {"question": "Was ist der Dollar Milkshake Theory?", "options": ['A) Forex-Indikator', 'B) Chartmuster', 'C) Volumentheorie', 'D) These, dass der USD durch globale Liquiditätsflüsse und Schuldennachfrage gestärkt wird'], "answer": "D"},
    # 111
    {"question": "Was ist ein Eurodollar (nicht EUR/USD)?", "options": ['A) US-Dollar, die außerhalb der USA gehalten werden – riesiger Offshore-Dollar-Markt', 'B) Euro-Dollar-Paar', 'C) Europäische Währung', 'D) Krypto'], "answer": "A"},
    # 112
    {"question": "Was ist SOFR und warum hat es LIBOR ersetzt?", "options": ['A) Aktienindex', 'B) Secured Overnight Financing Rate – basiert auf tatsächlichen Repo-Transaktionen statt Banker-Schätzungen', 'C) Forex-Rate', 'D) VIX-Alternative'], "answer": "B"},
    # 113
    {"question": "Was ist ein Collateral Squeeze?", "options": ['A) Normaler Markt', 'B) Indikator', 'C) Mangel an hochwertigen Sicherheiten (Treasuries) – treibt Repo-Raten und beeinflusst Liquidität', 'D) Chartmuster'], "answer": "C"},
    # 114
    {"question": "Was ist Rehypothecation?", "options": ['A) Neuer Trade', 'B) Chartmuster', 'C) Indikator', 'D) Wiederverwendung von Sicherheiten für weitere Transaktionen – erhöht systemische Hebelwirkung'], "answer": "D"},
    # 115
    {"question": "Was ist der Velocity of Money und warum sank sie trotz QE?", "options": ['A) Geschwindigkeit des Geldumlaufs – QE-Geld blieb in Reserven statt in Realwirtschaft', 'B) Immer konstant', 'C) Stieg durch QE', 'D) Nur für Krypto relevant'], "answer": "A"},
    # 116
    {"question": "Was ist ein Carry-Trade Unwind?", "options": ['A) Neuer Carry Trade', 'B) Massenhafte Auflösung von Carry Trades – kann zu extremen Währungsbewegungen führen (z.B. JPY)', 'C) Normaler Tageshandel', 'D) Chartmuster'], "answer": "B"},
    # 117
    {"question": "Was war der Yen Carry Trade Unwind 2024?", "options": ['A) Normaler Forex-Tag', 'B) Chartmuster', 'C) BOJ-Zinserhöhung löste massive Auflösung von JPY-Carry-Trades aus – globaler Sell-Off', 'D) Nur JPY betroffen'], "answer": "C"},
    # 118
    {"question": "Was ist ein Liquidity Spiral nach Brunnermeier?", "options": ['A) Aufwärtsspirale', 'B) Normaler Zyklus', 'C) Chartmuster', 'D) Selbstverstärkende Abwärtsspirale: Verluste → Margin Calls → Zwangsverkäufe → weitere Verluste'], "answer": "D"},
    # 119
    {"question": "Was ist ein Crowded Trade?", "options": ['A) Einzigartiger Trade', 'B) Position, die von vielen Marktteilnehmern gleichzeitig gehalten wird – hohes Risiko bei Auflösung', 'C) Chartmuster', 'D) Nur für Retail'], "answer": "B"},
    # 120
    {"question": "Was ist ein Factor Crowding?", "options": ['A) Normales Trading', 'B) Indikator', 'C) Zu viele Investoren nutzen dieselben Faktoren (z.B. Momentum) – reduziert Renditen und erhöht Crash-Risiko', 'D) Chartmuster'], "answer": "C"},
    # 121
    {"question": "Was ist das Grossman-Stiglitz-Paradoxon?", "options": ['A) Märkte sind perfekt effizient', 'B) Nur für Akademiker', 'C) Chartmuster', 'D) Wenn Märkte perfekt effizient wären, gäbe es keinen Anreiz Informationen zu sammeln – daher können Märkte nie perfekt effizient sein'], "answer": "D"},
    # 122
    {"question": "Was ist ein Noise Trader Risk?", "options": ['A) Kein Risiko', 'B) Irrationale Trader können Fehlbewertungen verstärken bevor sie korrigiert werden – Arbitrageure können vorher verlieren', 'C) Nur kurzfristig', 'D) Chartmuster'], "answer": "B"},
    # 123
    {"question": "Was sind die Limits of Arbitrage nach Shleifer und Vishny?", "options": ['A) Arbitrage funktioniert immer', 'B) Kein Limit', 'C) Praktische Beschränkungen (Kapital, Margin, Zeitdruck) verhindern perfekte Arbitrage', 'D) Nur theoretisch'], "answer": "C"},
    # 124
    {"question": "Was ist ein Toxic Flow im Market Making?", "options": ['A) Flow von informierten Tradern, der Market Maker systematisch Verluste verursacht', 'B) Normaler Flow', 'C) Hoher Spread', 'D) Chartmuster'], "answer": "A"},
    # 125
    {"question": "Was ist ein Heat Map im Order Flow Kontext?", "options": ['A) Chartmuster', 'B) Indikator', 'C) Nur Temperaturanzeige', 'D) Visuelle Darstellung von Limit-Order-Dichte auf verschiedenen Preisniveaus'], "answer": "D"},
    # 126
    {"question": "Was ist ein Depth of Market (DOM) Imbalance Ratio?", "options": ['A) Chartmuster', 'B) Indikator', 'C) Verhältnis von Bid- zu Ask-Volumen im Orderbuch – zeigt kurzfristigen Druck', 'D) Moving Average'], "answer": "C"},
    # 127
    {"question": "Was ist eine Iceberg Detection im Orderbuch?", "options": ['A) Erkennung versteckter Orders durch wiederholtes Auffüllen auf demselben Preisniveau', 'B) Normales Volumen', 'C) Chartmuster', 'D) Indikator'], "answer": "A"},
    # 128
    {"question": "Was ist Level 3 Marktdaten?", "options": ['A) Level 1 mit Delay', 'B) Vollständiges Orderbuch mit allen Orders, Änderungen und Cancellations – höchste Detailtiefe', 'C) Nur Bid/Ask', 'D) Nur OHLC'], "answer": "B"},
    # 129
    {"question": "Was ist ein Maker-Taker Rebate und wie beeinflusst es HFT-Strategien?", "options": ['A) Irrelevant', 'B) Chartmuster', 'C) HFT nutzt Rebates durch passives Limit-Order-Platzieren – profitiert von der Differenz', 'D) Nur für Retail'], "answer": "C"},
    # 130
    {"question": "Was ist Latency Arbitrage im HFT-Kontext?", "options": ['A) Langfristige Strategie', 'B) Chartmuster', 'C) Indikator', 'D) Ausnutzung von Mikrosekunden-Verzögerungen zwischen Börsen für risikolose Gewinne'], "answer": "D"},
    # 131
    {"question": "Was ist ein Co-Location im HFT?", "options": ['A) Remote Trading', 'B) Server direkt neben der Börse platzieren für minimale Latenz', 'C) Cloud Trading', 'D) Home Office Trading'], "answer": "B"},
    # 132
    {"question": "Was ist ein Smart Order Router (SOR)?", "options": ['A) Chartmuster', 'B) Indikator', 'C) Algorithmus, der Orders automatisch zur Börse mit bestem Preis/Liquidität leitet', 'D) Nur für Retail'], "answer": "C"},
    # 133
    {"question": "Was ist das Reg NMS (National Market System)?", "options": ['A) US-Regulierung: Orders müssen zum besten verfügbaren Preis über alle Börsen ausgeführt werden', 'B) Europäische Regulierung', 'C) Forex-Regel', 'D) Krypto-Regel'], "answer": "A"},
    # 134
    {"question": "Was ist ein Payment for Order Flow (PFOF)?", "options": ['A) Kundengebühr', 'B) Broker erhält Zahlung von Market Makern für Weiterleitung von Retail-Orders', 'C) Spread', 'D) Kommission'], "answer": "B"},
    # 135
    {"question": "Warum ist PFOF umstritten?", "options": ['A) Nicht umstritten', 'B) Immer vorteilhaft', 'C) Potentieller Interessenkonflikt: Broker leitet Orders nicht zum besten Preis, sondern zum zahlenden Market Maker', 'D) Nur in Europa'], "answer": "C"},
    # 136
    {"question": "Was ist ein Synthetic CDO?", "options": ['A) Normaler CDO', 'B) Aktien-ETF', 'C) Forex-Produkt', 'D) CDO, der Kreditrisiko durch CDS nachbildet statt echte Anleihen zu halten'], "answer": "D"},
    # 137
    {"question": "Was ist Tranching bei CDOs?", "options": ['A) Aufteilung des Kreditrisikos in Schichten (Senior, Mezzanine, Equity) mit unterschiedlichem Risiko/Rendite', 'B) Nur eine Schicht', 'C) Gleichmäßige Verteilung', 'D) Kein Risiko'], "answer": "A"},
    # 138
    {"question": "Was ist Correlation Trading bei CDO-Tranchen?", "options": ['A) Normales Trading', 'B) Handel auf die implizite Korrelation zwischen CDO-Tranchenpreisen', 'C) Nur Aktienhandel', 'D) Chartmuster'], "answer": "B"},
    # 139
    {"question": "Was ist ein Wrong-Way Risk?", "options": ['A) Kein Risiko', 'B) Normales Risiko', 'C) Wenn Exposure und Kreditrisiko der Gegenpartei positiv korreliert sind – schlimmster Fall tritt gleichzeitig ein', 'D) Nur bei Aktien'], "answer": "C"},
    # 140
    {"question": "Was ist XVA im Derivatehandel?", "options": ['A) Sammelbegriff für Bewertungsanpassungen: CVA, DVA, FVA, KVA, MVA', 'B) Nur CVA', 'C) Chartmuster', 'D) Indikator'], "answer": "A"},
    # 141
    {"question": "Was ist CVA (Credit Valuation Adjustment)?", "options": ['A) Indikator', 'B) Bewertungsanpassung für das Kontrahentenausfallrisiko bei Derivaten', 'C) Nur für Aktien', 'D) Chartmuster'], "answer": "B"},
    # 142
    {"question": "Was ist ein FVA (Funding Valuation Adjustment)?", "options": ['A) Chartmuster', 'B) Indikator', 'C) Bewertungsanpassung für Finanzierungskosten unbesicherter Derivatepositionen', 'D) Nur CVA'], "answer": "C"},
    # 143
    {"question": "Was ist ein Butterfly Spread im Zinskontext?", "options": ['A) Optionsstrategie', 'B) Forex-Trade', 'C) Chartmuster', 'D) Trade auf die Krümmung der Zinskurve – z.B. 2s5s10s Butterfly'], "answer": "D"},
    # 144
    {"question": "Was ist ein Steepener Trade?", "options": ['A) Wette auf steilere Zinskurve – z.B. Long langfristige, Short kurzfristige Anleihen', 'B) Wette auf flachere Kurve', 'C) Nur Aktien', 'D) Chartmuster'], "answer": "A"},
    # 145
    {"question": "Was ist ein Flattener Trade?", "options": ['A) Steepener', 'B) Wette auf flachere Zinskurve – z.B. Short langfristige, Long kurzfristige Anleihen', 'C) Nur Forex', 'D) Chartmuster'], "answer": "B"},
    # 146
    {"question": "Was ist der Nelson-Siegel-Modell?", "options": ['A) Aktienmodell', 'B) Chartmuster', 'C) Parametrisches Modell zur Beschreibung der Zinskurve mit Level, Slope und Curvature Faktoren', 'D) Indikator'], "answer": "C"},
    # 147
    {"question": "Was ist ein Principal Component Analysis (PCA) der Zinskurve?", "options": ['A) Chartmuster', 'B) Indikator', 'C) Volumenanalyse', 'D) Zerlegung der Zinskurve in Hauptkomponenten: Level (~90%), Slope (~8%), Curvature (~2%)'], "answer": "D"},
    # 148
    {"question": "Was ist ein Volatility Risk Premium Harvesting?", "options": ['A) Systematisches Verkaufen von Optionen, um die Prämie zwischen impliziter und realisierter Volatilität zu vereinnahmen', 'B) Nur Volatilität kaufen', 'C) Chartmuster', 'D) Indikator'], "answer": "A"},
    # 149
    {"question": "Was ist ein Tail Risk Hedging mittels OTM Puts?", "options": ['A) Nur Long-Position', 'B) Kauf günstiger Out-of-the-Money Puts als Versicherung gegen Extremereignisse', 'C) Chartmuster', 'D) Moving Average nutzen'], "answer": "B"},
    # 150
    {"question": "Was ist der Unterschied zwischen Risk Premia und Alpha?", "options": ['A) Kein Unterschied', 'B) Beide sind Alpha', 'C) Risk Premia sind systematische, erntbare Risikoentschädigungen; Alpha ist idiosynkratische Überrendite durch Skill', 'D) Beide sind Risk Premia'], "answer": "C"},
]
