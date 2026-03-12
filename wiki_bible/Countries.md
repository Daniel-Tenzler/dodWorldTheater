---
title: Countries
category: other
tags: [country, reference]
source: Victoria 2 Wiki
url: https://vic2.paradoxwikis.com/Countries
---

## Quick Reference

**What Are Country Tags?**
3-letter uppercase codes (e.g., ENG, FRA, GER) used to identify countries in modding and console commands.

**Key Files:**
- `common/countries/TAG - Name.txt` - Country definition (color, unit names)
- `history/countries/TAG - Name.txt` - Country starting data
- `common/countries.txt` - TAG to filename mapping
- `common/country_colors.txt` - TAG to RGB color mapping

**Common Tasks:**
| Task | File | Effect/Command |
|------|------|----------------|
| Check country tag | Event/decision trigger | `tag = ENG` / `THIS = { tag = ENG }` |
| Check exists | Event/decision trigger | `ENG = { exists = yes }` |
| Switch country | Event effect | `change_tag = GER` |
| Annex country | Event effect | `annex = THIS` / `GER = { annex = THIS }` |
| Release country | Event effect | `release = POL` / `release_vassal = POL` |
| Check GP status | Event/decision trigger | `is_greater_power = yes` |

**Great Powers (1836 Start):**
| Country | TAG | Region |
|---------|-----|--------|
| United Kingdom | ENG | Europe |
| France | FRA | Europe |
| Prussia | PRU | Europe |
| Russia | RUS | Europe/Asia |
| Austria | AUS | Europe |
| United States | USA | North America |
| Ottoman Empire | TUR | Middle East |
| Spain | SPA | Europe |

**Secondary Powers (1836 Start):**
| Country | TAG | Region |
|---------|-----|--------|
| Belgium | BEL | Europe |
| Brazil | BRZ | South America |
| Denmark | DEN | Europe |
| Mexico | MEX | North America |
| Netherlands | NET | Europe |
| Portugal | POR | Europe |
| Sardinia-Piedmont | SAR | Europe |
| Sweden | SWE | Europe |

**Formable Countries:**
| Country | TAG | Formation Notes |
|---------|-----|-----------------|
| Germany | GER | Germanic culture group |
| Italy | ITA | Italian culture group |
| Romania | ROM | Romanian/South Slavic cultures |
| Yugoslavia | YUG | South Slavic cultures |
| Scandinavia | SCA | Nordic cultures |
| Poland | POL | Polish/other Slavic cultures |

**Common Console Commands:**
```bash
tag [TAG]          # Switch to play as country
debug fow          # Toggle fog of war
debug showid        # Show province IDs
event [ID] [TAG]    # Fire event for country
```

**Common Pitfalls:**
- **TAG not found** → Check `common/countries.txt` for exact spelling
- **Country not appearing** → Missing from `common/countries/` or `history/countries/`
- **Wrong color** → Check `common/country_colors.txt`
- **Flag missing** → Need `gfx/flags/TAG.tga` file

**See Also:**
- [QUICKSTART.md](QUICKSTART.md) - Task 3: Create a New Country
- [Country_modding.md](Country_modding.md) - Creating countries
- [PATTERNS.md](PATTERNS.md) - Patterns 1, 5, 14 (country actions)

---

Please help create and format strategy guides according to the National strategy guides. Note that nations marked with (1861–P) are able to be played at the beginning of 1861, (1861–R) are able to be released at the beginning of the 1861 start date, (V2) are specific to the original Victoria 2 game, (AHD) is specific to the A House Divided expansion, and (HOD) is specific to the Heart of Darkness expansion. Jan Mayen, besides the colonial dominions, is the only new country in Heart of Darkness. Behind the country name is its TAG used for modding and console commands.

Maps
The political situation of The Grand Campaign bookmark, January 1st, 1836.
The political situation of the A House Divided bookmark, July 1st, 1861.


Great powers
 United Kingdom (ENG)
 France (FRA)
 Prussia (PRU)
 Russia (RUS)
 Austria (AUS)
 United States of America (USA)
 Ottoman Empire (TUR)
 Spain (SPA)
Secondary powers
 Belgium (BEL)
 Brazil (BRZ)
 Denmark (DEN)
 Mexico (MEX)
 Netherlands (NET)
 Portugal (POR)
 Sardinia-Piedmont (SAR)
 Sweden (SWE)
Minor civilized powers
Europe
 Greece (GRE)
 Ionian Islands (ION)
 Krakow (KRA)
 Luxembourg (LUX)
 Moldavia (MOL)
 Montenegro (MON)
 Serbia (SER)
 Switzerland (SWI)
 Wallachia (WAL)
Germany
 Anhalt (ANH)
 Baden (BAD)
 Bavaria (BAV)
 Braunschweig (BRA)
 Bremen (BRE)
 Frankfurt am Main (FRM)
 Hamburg (HAM)
 Hannover (HAN)
 Hesse-Darmstadt (HES)
 Hesse-Kassel (HEK)
 Holstein (HOL)
 Lippe-Detmold (LIP)
 Lübeck (LUB)
 Mecklenburg (MEC)
 Nassau (NAS)
 Oldenburg (OLD)
 Saxe-Coburg-Gotha (COB)
 Saxe-Meiningen (MEI)
 Saxe-Weimar (WEI)
 Saxony (SAX)
 Württemberg (WUR)
Italy
 Lucca (LUC)
 Modena (MOD)
 The Papal States (PAP)
 Two Sicilies (SIC)
 Parma (PAR)
 Tuscany (TUS)
North America
 Haiti (HAI)
 Texas (TEX)
 United States of Central America (UCA)
South America
 Argentina (ARG)
 Bolivia (BOL)
 Chile (CHL)
 Colombia (CLM)
 Ecuador (ECU)
 Paraguay (PRG)
 Peru (PEU)
 Uruguay (URU)
 Venezuela (VNZ)
Africa
 Oranje (ORA)
 South African Republic/Transvaal (TRN)
Releasable or formable civilized nations
Europe
Releasable
 Albania (ALB)
 Armenia (ARM)
 Azerbaijan (AZB)
 Belarus (BYE)
 Bosnia-Herzegovina (BOS)
 Bohemia-Moravia (BOH)
 Bulgaria (BUL)
 Catalonia (CAT)
 Crete (CRE)
 Croatia (CRO)
 Danzig (DZG)
 Estonia (EST)
 Finland (FIN)
 Flanders (FLA)
 Georgia (GEO)
 Hungary (HUN)
 Iceland (ICL)
 Ireland (IRE)
 Jan Mayen (JAN) HOD
 Latvia (LAT)
 Lithuania (LIT)
 Lombardia (LOM)
 Norway (NOR)
 Ruthenia (RUT)
 Schleswig (SCH)
 Scotland (SCO)
 Siebenbürgen (SIE)
 Slovakia (SLV)
 Slovenia (SLO)
 Trieste (TRE)
 Ukraine (UKR)
 Wallonia (WLL)
 Venice (VEN)
Formable countries (some are releasable as well)
 Austria-Hungary (KUK)
 Byzantine Empire (BYZ)
 Czechoslovakia (CZH)
 Germany (GER)
 Italy (ITA)
 Poland (POL)
 Poland-Lithuania (PLC) (1861–R)
 Romania (ROM)
 Scandinavia (SCA)
 South German Federation (SGF)
 United Baltic Nations (UBD)
 Yugoslavia (YUG)
North America
 Californian Republic (CAL)
 Canada (CAN)
 Columbia (COL)
 Confederate States of America (CSA)
 Costa Rica (COS)
 Cuba (CUB)
 Deseret (DES)
 Dominican Republic (DOM) (1861–P)
 El Salvador (ELS) (1861–P)
 Guatemala (GUA) (1861–P)
 Honduras (HON) (1861–P)
 Manhattan Commune (MAN)
 Metis Confederacy (MTC) (1861–R)
 New England (NEN)
 Newfoundland (NEW)
 Nicaragua (NIC) (1861–P)
 Quebec (QUE)
South America
Releasable
 Panama (PNM)
Formable countries (some are releasable as well)
 Gran Colombia (GCO) AHD
Africa
 South Africa (SAF)
 Southern Rhodesia (RHO)
Asia
Releasable
 Cyprus (CYP)
 Israel (ISR)
 Philippines (PHI)
Formable countries (some are releasable as well)
 Arabia (ARA)
 Babylon (BAB)
 India (HND)
Oceania
 Australia (AST)
 New Zealand (NZL)
Uncivilized nations
North America
 Hawaii (HAW)
Africa
 Aldjazair (ALD) V2
 Algeria (ALD) AHD
 Egypt (EGY)
 Ethiopia (ETH)
 Liberia (LIB)
 Madagascar (MAD)
 Morocco (MOR)
 Sokoto (SOK)
 Tripoli (TRI)
 Tunis (TUN)
 Zulu (ZUL)
Asia
 Abu Dhabi (ABU)
 Afghanistan (AFG)
 Atjeh (ATJ)
 Bali (BAL)
 Bhutan (BHU)
 Brunei (BRU)
 Bukkhara (BUK)
 Burma (BUR)
 Cambodia (CAM)
 China (CHI)
 Dai Nam (DAI)
 Hedjaz (HDJ)
 Japan (JAP)
 Johore (JOH)
 Kalat (KAL)
 Khiva (KHI)
 Kokand (KOK)
 Korea (KOR)
 Luang Prabang (LUA)
 Makran (MAK)
 Nejd (NEJ)
 Nepal (NEP)
 Oman (OMA)
 Persia (PER)
 Siam (SIA)
 Sikkim (SIK)
 Tibet (TIB)
 Yemen (YEM)
India
 Awadh (AWA)
 Bastar (BAS)
 Beroda (BER)
 Bikaner (BIK)
 Bhopal (BHO)
 Bundelkhand (BUN)
 Gwalior (GWA)
 Hyderabad (HYD)
 Indore (IND)
 Jaisalmer (JAS)
 Jaipur (JAI)
 Jodhpur (JOD)
 Kutch (KUT)
 Mewar (MEW)
 Mysore (MYS)
 Nagpur (NAG)
 Orissa (ORI)
 Panjab (PAN)
 Sindh (SIN)
 Travancore (TRA)
Chinese substates
 Guangxi (GXI) AHD
 Manchuria (MCK) AHD
 Mongolia (MGL)
 Qinghai (XBI) AHD
 Xinjiang (XIN) AHD
 Yunnan (YNN) AHD
Releasable uncivilized nations
Europe
 Crimea (CRI)
North America
 Cherokee (CHE)
Africa
 Congo (or Congo Free State) (CNG)
 Natalia (NAL)
 Zanzibar (ZAN)
Asia
 Heavenly Kingdom (TPG)
 Iraq (IRQ)
 Java (JAV)
 Kashmir (KAS) (1861–P)
 Ladakh (LAD)
 Mughalistan (MUG)
 Shimla (SHI)
 Wiang Chhan (WIA)
China (only Vanilla)
 Guangxi Clique (GXI) V2
 Manchukuo (MCK) V2
 Shanxi Clique (SXI) V2
 Xibei San Ma (XBI) V2
 Xinjiang Clique (XIN) V2
 Yunnan Clique (YNN) V2
