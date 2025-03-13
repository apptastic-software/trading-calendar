Trading Calendar
================
[![Build](https://github.com/apptastic-software/trading-calendar/actions/workflows/build.yml/badge.svg)](https://github.com/apptastic-software/trading-calendar/actions/workflows/build.yml)
[![codecov](https://codecov.io/github/apptastic-software/trading-calendar/graph/badge.svg?token=75QZNYMEOI)](https://codecov.io/github/apptastic-software/trading-calendar)
[![Docker Image Version](https://img.shields.io/docker/v/apptasticsoftware/trading-calendar?logo=Docker&logoColor=ffffff)](https://hub.docker.com/r/apptasticsoftware/trading-calendar/tags)
[![API Doc](https://img.shields.io/github/v/release/apptastic-software/trading-calendar?display_name=release&label=api%20doc)](https://apptastic-software.github.io/trading-calendar/api-doc/latest)
[![License](https://img.shields.io/:license-MIT-blue.svg?style=flat-round)](https://apptastic-software.mit-license.org)

Free trading calendar REST API with holiday, late open, and early close. Over [50 unique exchange calendars](#calendars) for global equity and futures markets.

Data includes:

* All holidays, including: trading holidays and partial days
* Support for timezones and daylight savings time transitions
* Definitions for weekends for each market
* Open and close time for each market
* Current market status (open or closed based on static schedule).

## Running it locally

### Pull image

Pull image from [Docker Hub repository][1]:
```
docker pull apptasticsoftware/trading-calendar:latest
```
Or pull image from [GitHub Container Registry (GHCR)][2]:
```
docker pull ghcr.io/apptastic-software/trading-calendar:latest
```

### Start the container
Run a container based on the image from Docker Hub:
```
docker run -d --name trading-calendar -p 8000:80 apptasticsoftware/trading-calendar
```

Run a container based on the image from GHCR:
```
docker run -d --name trading-calendar -p 8000:80 ghcr.io/apptastic-software/trading-calendar
```

It will take around one minute for the container to start and accept requests.

### Test it
Test that the container is working:
```
 http://127.0.0.1:8000/api/v1/markets?mic=XNYS
```

### Swagger UI
UI with interactive exploration, call and test API directly from the browser:
```
http://127.0.0.1:8000/docs
```

### ReDoc UI
Alternative API documentation with ReDoc:
```
http://127.0.0.1:8000/redoc
```

### OpenAPI
OpenAPI 3.1 specification:
```
http://127.0.0.1:8000/api/v1/openapi.json
```

## Calendars

| Exchange                        | MIC      | Country          | Exchange Website                                               |
| ------------------------------- | -------- | ---------------- | -------------------------------------------------------------- |
| New York Stock Exchange         | XNYS     | 🇺🇸 USA            | https://www.nyse.com/index                                    |
| CBOE Futures                    | XCBF     | 🇺🇸 USA            | https://markets.cboe.com/us/futures/overview                  |
| Chicago Mercantile Exchange     | CMES     | 🇺🇸 USA            | https://www.cmegroup.com                                      |
| ICE US                          | IEPA     | 🇺🇸 USA            | https://www.theice.com/index                                  |
| Toronto Stock Exchange          | XTSE     | 🇨🇦 Canada         | https://www.tsx.com                                           |
| B3 S.A. - Brasil Bolsa Balcao   | BVMF     | 🇧🇷 Brazil         | https://www.b3.com.br/en_us                                   |
| London Stock Exchange           | XLON     | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 England        | https://www.londonstockexchange.com/home/homepage.htm         |
| Euronext Amsterdam              | XAMS     | 🇳🇱 Netherlands    | https://www.euronext.com/en/regulation/amsterdam              |
| Euronext Brussels               | XBRU     | 🇧🇪 Belgium        | https://www.euronext.com/en/regulation/brussels               |
| Luxembourg Stock Exchange       | XLUX     | 🇱🇺 Luxembourg     | https://www.luxse.com                                         |
| Euronext Lisbon                 | XLIS     | 🇵🇹 Portugal       | https://www.euronext.com/en/regulation/lisbon                 |
| Euronext Paris                  | XPAR     | 🇫🇷 France         | https://www.euronext.com/en/regulation/paris                  |
| Frankfurt Stock Exchange        | XFRA     | 🇩🇪 Germany        | https://en.boerse-frankfurt.de                                |
| Deutsche Börse Xetra            | XETR     | 🇩🇪 Germany        | https://www.xetra.com/xetra-en                                |
| European Energy Exchange        | XEEE     | 🇩🇪 Germany        | https://www.eex.com                                           |
| Hamburg Stock Exchange          | XHAM     | 🇩🇪 Germany        | https://www.boerse-hamburg.de                                 |
| Duesseldorf Stock Exchange      | XDUS     | 🇩🇪 Germany        | https://www.boerse-duesseldorf.de                             |
| SIX Swiss Exchange              | XSWX     | 🇨🇭 Switzerland    | https://www.six-group.com/exchanges/index.html                |
| Tokyo Stock Exchange            | XTKS     | 🇯🇵 Japan          | https://www.jpx.co.jp/english                                 |
| Austrialian Securities Exchange | XASX     | 🇦🇺 Australia      | https://www.asx.com.au                                        |
| Bolsa de Madrid                 | XMAD     | 🇪🇸 Spain          | https://www.bolsamadrid.es/ing/aspx/Portada/Portada.aspx      |
| Borsa Italiana                  | XMIL     | 🇮🇹 Italy          | https://www.borsaitaliana.it/homepage/homepage.en.htm         |
| New Zealand Exchange            | XNZE     | 🇳🇿 New Zealand    | https://www.nzx.com                                           |
| Wiener Borse                    | XWBO     | 🇦🇹 Austria        | https://www.wienerborse.at/en                                 |
| Hong Kong Stock Exchange        | XHKG     | 🇭🇰 Hong Kong      | https://www.hkex.com.hk/?sc_lang=en                           |
| Copenhagen Stock Exchange       | XCSE     | 🇩🇰 Denmark        | https://www.nasdaqomxnordic.com                               |
| Helsinki Stock Exchange         | XHEL     | 🇫🇮 Finland        | https://www.nasdaqomxnordic.com                               |
| Stockholm Stock Exchange        | XSTO     | 🇸🇪 Sweden         | https://www.nasdaqomxnordic.com                               |
| Oslo Stock Exchange             | XOSL     | 🇳🇴 Norway         | https://www.oslobors.no/ob_eng                                |
| Irish Stock Exchange            | XDUB     | 🇮🇪 Ireland        | https://www.euronext.com/en/markets/dublin                    |
| Bombay Stock Exchange           | XBOM     | 🇮🇳 India          | https://www.bseindia.com                                      |
| Singapore Exchange              | XSES     | 🇸🇬 Singapore      | https://www.sgx.com                                           |
| Shanghai Stock Exchange         | XSHG     | 🇨🇳 China          | https://english.sse.com.cn                                    |
| Korea Exchange                  | XKRX     | 🇰🇷 South Korea    | https://global.krx.co.kr                                      |
| Iceland Stock Exchange          | XICE     | 🇮🇸 Iceland        | https://www.nasdaqomxnordic.com                               |
| Poland Stock Exchange           | XWAR     | 🇵🇱 Poland         | https://www.gpw.pl                                            |
| Santiago Stock Exchange         | XSGO     | 🇨🇱 Chile          | https://inter.bolsadesantiago.com/sitios/en/Paginas/home.aspx |
| Colombia Securities Exchange    | XBOG     | 🇨🇴 Colombia       | https://www.bvc.com.co/nueva/index_en.html                    |
| Mexican Stock Exchange          | XMEX     | 🇲🇽 Mexico         | https://www.bmv.com.mx                                        |
| Lima Stock Exchange             | XLIM     | 🇵🇪 Peru           | https://www.bvl.com.pe                                        |
| Prague Stock Exchange           | XPRA     | 🇨🇿 Czech Republic | https://www.pse.cz/en                                         |
| Budapest Stock Exchange         | XBUD     | 🇭🇺 Hungary        | https://bse.hu                                                |
| Athens Stock Exchange           | ASEX     | 🇬🇷 Greece         | https://www.athexgroup.gr                                     |
| Istanbul Stock Exchange         | XIST     | 🇹🇷 Turkey         | https://www.borsaistanbul.com/en                              |
| Tel Aviv Stock Exchange         | XTAE     | 🇮🇱 Israel         | https://www.tase.co.il/Eng/Pages/Homepage.aspx                |
| Johannesburg Stock Exchange     | XJSE     | 🇿🇦 South Africa   | https://www.jse.co.za/z                                       |
| Malaysia Stock Exchange         | XKLS     | 🇲🇾 Malaysia       | https://www.bursamalaysia.com                                 |
| Moscow Exchange                 | XMOS     | 🇷🇺 Russia         | https://www.moex.com/en                                       |
| Philippine Stock Exchange       | XPHS     | 🇵🇭 Philippines    | https://www.pse.com.ph/stockMarket/home.html                  |
| Stock Exchange of Thailand      | XBKK     | 🇹🇭 Thailand       | https://www.set.or.th/set/mainpage.do?language=en&country=US  |
| Indonesia Stock Exchange        | XIDX     | 🇮🇩 Indonesia      | https://www.idx.co.id                                         |
| Taiwan Stock Exchange Corp.     | XTAI     | 🇹🇼 Taiwan         | https://www.twse.com.tw/en                                    |
| Buenos Aires Stock Exchange     | XBUE     | 🇦🇷 Argentina      | https://www.bcba.sba.com.ar                                   |
| Pakistan Stock Exchange         | XKAR     | 🇵🇰 Pakistan       | https://www.psx.com.pk                                        |
| Saudi Stock Exchange            | XSAU     | 🇸🇦 Saudi Arabia   | https://www.saudiexchange.sa                                  |
| Astana International Exchange   | AIXK     | 🇰🇿 Kazakhstan     | https://www.aix.kz                                            |
| Bucharest Stock Exchange        | XBSE     | 🇷🇴 Romania        | https://www.bvb.ro                                            |

> Note that exchange calendars are defined by their [ISO-10383](https://www.iso20022.org/10383/iso-10383-market-identifier-codes) market identifier code (MIC).

License
-------

    MIT License
    
    Copyright (c) 2024, Apptastic Software
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.

[1]: https://hub.docker.com/r/apptasticsoftware/trading-calendar
[2]: https://github.com/apptastic-software/trading-calendar/pkgs/container/trading-calendar
