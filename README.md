Trading Calendar
================
[![Build](https://github.com/apptastic-software/trading-calendar/actions/workflows/build.yml/badge.svg)](https://github.com/apptastic-software/trading-calendar/actions/workflows/build.yml)
[![codecov](https://codecov.io/github/apptastic-software/trading-calendar/graph/badge.svg?token=75QZNYMEOI)](https://codecov.io/github/apptastic-software/trading-calendar)
[![Docker Image Version](https://img.shields.io/docker/v/apptasticsoftware/trading-calendar?logo=Docker&logoColor=ffffff)](https://hub.docker.com/r/apptasticsoftware/trading-calendar/tags)
[![API Doc](https://img.shields.io/github/v/release/apptastic-software/trading-calendar?display_name=release&label=api%20doc)](https://apptastic-software.github.io/trading-calendar/api-doc/latest)
[![License](https://img.shields.io/:license-MIT-blue.svg?style=flat-round)](https://apptastic-software.mit-license.org)

Free trading calendar REST API with holiday, late open, and early close. Over [60 unique exchange calendars](#calendars) for global equity and futures markets.

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

| Exchange                                                                                   | MIC      | Country          |
| ------------------------------------------------------------------------------------------ | -------- | ---------------- |
| [New York Stock Exchange](https://www.nyse.com/index)                                      | XNYS     | 🇺🇸 USA            |
| [CBOE Futures](https://markets.cboe.com/us/futures/overview)                               | XCBF     | 🇺🇸 USA            |
| [Chicago Mercantile Exchange](https://www.cmegroup.com)                                    | CMES     | 🇺🇸 USA            |
| [ICE US](https://www.theice.com/index)                                                     | IEPA     | 🇺🇸 USA            |
| [Toronto Stock Exchange](https://www.tsx.com)                                              | XTSE     | 🇨🇦 Canada         |
| [London Stock Exchange](https://www.londonstockexchange.com/home/homepage.htm)             | XLON     | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 England        |
| [Euronext Amsterdam](https://www.euronext.com/en/regulation/amsterdam)                     | XAMS     | 🇳🇱 Netherlands    |
| [Euronext Brussels](https://www.euronext.com/en/regulation/brussels)                       | XBRU     | 🇧🇪 Belgium        |
| [Luxembourg Stock Exchange](https://www.luxse.com)                                         | XLUX     | 🇱🇺 Luxembourg     |
| [Euronext Lisbon](https://www.euronext.com/en/regulation/lisbon)                           | XLIS     | 🇵🇹 Portugal       |
| [Euronext Paris](https://www.euronext.com/en/regulation/paris)                             | XPAR     | 🇫🇷 France         |
| [Frankfurt Stock Exchange](https://en.boerse-frankfurt.de)                                 | XFRA     | 🇩🇪 Germany        |
| [Deutsche Börse Xetra](https://www.xetra.com/xetra-en)                                     | XETR     | 🇩🇪 Germany        |
| [European Energy Exchange](https://www.eex.com)                                            | XEEE     | 🇩🇪 Germany        |
| [Hamburg Stock Exchange](https://www.boerse-hamburg.de)                                    | XHAM     | 🇩🇪 Germany        |
| [Duesseldorf Stock Exchange](https://www.boerse-duesseldorf.de)                            | XDUS     | 🇩🇪 Germany        |
| [SIX Swiss Exchange](https://www.six-group.com/exchanges/index.html)                       | XSWX     | 🇨🇭 Switzerland    |
| [Bolsa de Madrid](https://www.bolsamadrid.es/ing/aspx/Portada/Portada.aspx)                | XMAD     | 🇪🇸 Spain          |
| [Borsa Italiana](https://www.borsaitaliana.it/homepage/homepage.en.htm)                    | XMIL     | 🇮🇹 Italy          |
| [Wiener Borse](https://www.wienerborse.at/en)                                              | XWBO     | 🇦🇹 Austria        |
| [Copenhagen Stock Exchange](https://www.nasdaqomxnordic.com)                               | XCSE     | 🇩🇰 Denmark        |
| [Helsinki Stock Exchange](https://www.nasdaqomxnordic.com)                                 | XHEL     | 🇫🇮 Finland        |
| [Stockholm Stock Exchange](https://www.nasdaqomxnordic.com)                                | XSTO     | 🇸🇪 Sweden         |
| [Iceland Stock Exchange](https://www.nasdaqomxnordic.com)                                  | XICE     | 🇮🇸 Iceland        |
| [Oslo Stock Exchange](https://www.oslobors.no/ob_eng)                                      | XOSL     | 🇳🇴 Norway         |
| [Irish Stock Exchange](https://www.euronext.com/en/markets/dublin)                         | XDUB     | 🇮🇪 Ireland        |
| [Tallinn Stock Exchange](https://nasdaqbaltic.com)                                         | XTAL     | 🇪🇪 Estonia        |
| [Riga Stock Exchange](https://nasdaqbaltic.com)                                            | XRIS     | 🇱🇻 Latvia         |
| [Vilnius Stock Exchange](https://nasdaqbaltic.com)                                         | XLIT     | 🇱🇹 Lithuania      |
| [Poland Stock Exchange](https://www.gpw.pl)                                                | XWAR     | 🇵🇱 Poland         |
| [Prague Stock Exchange](https://www.pse.cz/en)                                             | XPRA     | 🇨🇿 Czech Republic |
| [Bucharest Stock Exchange](https://www.bvb.ro)                                             | XBSE     | 🇷🇴 Romania        |
| [Zagreb Stock Exchange](https://www.zse.hr/en)                                             | XZAG     | 🇭🇷 Croatia        |
| [Budapest Stock Exchange](https://bse.hu)                                                  | XBUD     | 🇭🇺 Hungary        |
| [Moscow Exchange](https://www.moex.com/en)                                                 | XMOS     | 🇷🇺 Russia         |
| [Astana International Exchange](https://www.aix.kz)                                        | AIXK     | 🇰🇿 Kazakhstan     |
| [Athens Stock Exchange](https://www.athexgroup.gr)                                         | ASEX     | 🇬🇷 Greece         |
| [Cyprus Stock Exchange](https://www.cse.com.cy/en-GB/home)                                 | XCYS     | 🇨🇾 Cyprus         |
| [Istanbul Stock Exchange](https://www.borsaistanbul.com/en)                                | XIST     | 🇹🇷 Turkey         |
| [Tel Aviv Stock Exchange](https://www.tase.co.il/Eng/Pages/Homepage.aspx)                  | XTAE     | 🇮🇱 Israel         |
| [Bombay Stock Exchange](https://www.bseindia.com)                                          | XBOM     | 🇮🇳 India          |
| [Austrialian Securities Exchange](https://www.asx.com.au)                                  | XASX     | 🇦🇺 Australia      |
| [New Zealand Exchange](https://www.nzx.com)                                                | XNZE     | 🇳🇿 New Zealand    |
| [Bermuda Stock Exchange](https://www.bsx.com)                                              | XBDA     | 🇧🇲 Bermuda        |
| [Singapore Exchange](https://www.sgx.com)                                                  | XSES     | 🇸🇬 Singapore      |
| [Shanghai Stock Exchange](https://english.sse.com.cn)                                      | XSHG     | 🇨🇳 China          |
| [Hong Kong Stock Exchange](https://www.hkex.com.hk/?sc_lang=en)                            | XHKG     | 🇭🇰 Hong Kong      |
| [Taiwan Stock Exchange Corp.](https://www.twse.com.tw/en)                                  | XTAI     | 🇹🇼 Taiwan         |
| [Tokyo Stock Exchange](https://www.jpx.co.jp/english)                                      | XTKS     | 🇯🇵 Japan          |
| [Korea Exchange](https://global.krx.co.kr)                                                 | XKRX     | 🇰🇷 South Korea    |
| [Malaysia Stock Exchange](https://www.bursamalaysia.com)                                   | XKLS     | 🇲🇾 Malaysia       |
| [Philippine Stock Exchange](https://www.pse.com.ph/stockMarket/home.html)                  | XPHS     | 🇵🇭 Philippines    |
| [Stock Exchange of Thailand](https://www.set.or.th/set/mainpage.do?language=en&country=US) | XBKK     | 🇹🇭 Thailand       |
| [Indonesia Stock Exchange](https://www.idx.co.id)                                          | XIDX     | 🇮🇩 Indonesia      |
| [B3 S.A. - Brasil Bolsa Balcao](https://www.b3.com.br/en_us)                               | BVMF     | 🇧🇷 Brazil         |
| [Santiago Stock Exchange](https://inter.bolsadesantiago.com/sitios/en/Paginas/home.aspx)   | XSGO     | 🇨🇱 Chile          |
| [Colombia Securities Exchange](https://www.bvc.com.co/nueva/index_en.html)                 | XBOG     | 🇨🇴 Colombia       |
| [Mexican Stock Exchange](https://www.bmv.com.mx)                                           | XMEX     | 🇲🇽 Mexico         |
| [Lima Stock Exchange](https://www.bvl.com.pe)                                              | XLIM     | 🇵🇪 Peru           |
| [Buenos Aires Stock Exchange](https://www.bcba.sba.com.ar)                                 | XBUE     | 🇦🇷 Argentina      |
| [Johannesburg Stock Exchange](https://www.jse.co.za/z)                                     | XJSE     | 🇿🇦 South Africa   |
| [Pakistan Stock Exchange](https://www.psx.com.pk)                                          | XKAR     | 🇵🇰 Pakistan       |
| [Saudi Stock Exchange](https://www.saudiexchange.sa)                                       | XSAU     | 🇸🇦 Saudi Arabia   |

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
