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

| Exchange                                                                                   | MIC      | Country          | Region        |
| ------------------------------------------------------------------------------------------ | -------- | ---------------- |---------------|
| [Toronto Stock Exchange](https://www.tsx.com)                                              | XTSE     | 🇨🇦 Canada         | North America |
| [New York Stock Exchange](https://www.nyse.com/index)                                      | XNYS     | 🇺🇸 USA            | North America |
| [CBOE Futures](https://markets.cboe.com/us/futures/overview)                               | XCBF     | 🇺🇸 USA            | North America |
| [Chicago Mercantile Exchange](https://www.cmegroup.com)                                    | CMES     | 🇺🇸 USA            | North America |
| [ICE US](https://www.theice.com/index)                                                     | IEPA     | 🇺🇸 USA            | North America |
| [Bermuda Stock Exchange](https://www.bsx.com)                                              | XBDA     | 🇧🇲 Bermuda        | North America |
| [Mexican Stock Exchange](https://www.bmv.com.mx)                                           | XMEX     | 🇲🇽 Mexico         | North America |
| [B3 S.A. - Brasil Bolsa Balcao](https://www.b3.com.br/en_us)                               | BVMF     | 🇧🇷 Brazil         | South America |
| [Santiago Stock Exchange](https://inter.bolsadesantiago.com/sitios/en/Paginas/home.aspx)   | XSGO     | 🇨🇱 Chile          | South America |
| [Colombia Securities Exchange](https://www.bvc.com.co/nueva/index_en.html)                 | XBOG     | 🇨🇴 Colombia       | South America |
| [Lima Stock Exchange](https://www.bvl.com.pe)                                              | XLIM     | 🇵🇪 Peru           | South America |
| [Buenos Aires Stock Exchange](https://www.bcba.sba.com.ar)                                 | XBUE     | 🇦🇷 Argentina      | South America |
| [London Stock Exchange](https://www.londonstockexchange.com/home/homepage.htm)             | XLON     | 🏴󠁧󠁢󠁥󠁮󠁧󠁿 England        | Europe        |
| [Euronext Amsterdam](https://www.euronext.com/en/regulation/amsterdam)                     | XAMS     | 🇳🇱 Netherlands    | Europe        |
| [Euronext Brussels](https://www.euronext.com/en/regulation/brussels)                       | XBRU     | 🇧🇪 Belgium        | Europe        |
| [Luxembourg Stock Exchange](https://www.luxse.com)                                         | XLUX     | 🇱🇺 Luxembourg     | Europe        |
| [Euronext Lisbon](https://www.euronext.com/en/regulation/lisbon)                           | XLIS     | 🇵🇹 Portugal       | Europe        |
| [Euronext Paris](https://www.euronext.com/en/regulation/paris)                             | XPAR     | 🇫🇷 France         | Europe        |
| [Frankfurt Stock Exchange](https://en.boerse-frankfurt.de)                                 | XFRA     | 🇩🇪 Germany        | Europe        |
| [Deutsche Börse Xetra](https://www.xetra.com/xetra-en)                                     | XETR     | 🇩🇪 Germany        | Europe        |
| [European Energy Exchange](https://www.eex.com)                                            | XEEE     | 🇩🇪 Germany        | Europe        |
| [Hamburg Stock Exchange](https://www.boerse-hamburg.de)                                    | XHAM     | 🇩🇪 Germany        | Europe        |
| [Duesseldorf Stock Exchange](https://www.boerse-duesseldorf.de)                            | XDUS     | 🇩🇪 Germany        | Europe        |
| [SIX Swiss Exchange](https://www.six-group.com/exchanges/index.html)                       | XSWX     | 🇨🇭 Switzerland    | Europe        |
| [Bolsa de Madrid](https://www.bolsamadrid.es/ing/aspx/Portada/Portada.aspx)                | XMAD     | 🇪🇸 Spain          | Europe        |
| [Borsa Italiana](https://www.borsaitaliana.it/homepage/homepage.en.htm)                    | XMIL     | 🇮🇹 Italy          | Europe        |
| [Wiener Borse](https://www.wienerborse.at/en)                                              | XWBO     | 🇦🇹 Austria        | Europe        |
| [Copenhagen Stock Exchange](https://www.nasdaqomxnordic.com)                               | XCSE     | 🇩🇰 Denmark        | Europe        |
| [Helsinki Stock Exchange](https://www.nasdaqomxnordic.com)                                 | XHEL     | 🇫🇮 Finland        | Europe        |
| [Stockholm Stock Exchange](https://www.nasdaqomxnordic.com)                                | XSTO     | 🇸🇪 Sweden         | Europe        |
| [Iceland Stock Exchange](https://www.nasdaqomxnordic.com)                                  | XICE     | 🇮🇸 Iceland        | Europe        |
| [Oslo Stock Exchange](https://www.oslobors.no/ob_eng)                                      | XOSL     | 🇳🇴 Norway         | Europe        |
| [Irish Stock Exchange](https://www.euronext.com/en/markets/dublin)                         | XDUB     | 🇮🇪 Ireland        | Europe        |
| [Tallinn Stock Exchange](https://nasdaqbaltic.com)                                         | XTAL     | 🇪🇪 Estonia        | Europe        |
| [Riga Stock Exchange](https://nasdaqbaltic.com)                                            | XRIS     | 🇱🇻 Latvia         | Europe        |
| [Vilnius Stock Exchange](https://nasdaqbaltic.com)                                         | XLIT     | 🇱🇹 Lithuania      | Europe        |
| [Poland Stock Exchange](https://www.gpw.pl)                                                | XWAR     | 🇵🇱 Poland         | Europe        |
| [Prague Stock Exchange](https://www.pse.cz/en)                                             | XPRA     | 🇨🇿 Czech Republic | Europe        |
| [Bucharest Stock Exchange](https://www.bvb.ro)                                             | XBSE     | 🇷🇴 Romania        | Europe        |
| [Zagreb Stock Exchange](https://www.zse.hr/en)                                             | XZAG     | 🇭🇷 Croatia        | Europe        |
| [Budapest Stock Exchange](https://bse.hu)                                                  | XBUD     | 🇭🇺 Hungary        | Europe        |
| [Moscow Exchange](https://www.moex.com/en)                                                 | XMOS     | 🇷🇺 Russia         | Europe        |
| [Astana International Exchange](https://www.aix.kz)                                        | AIXK     | 🇰🇿 Kazakhstan     | Europe        |
| [Athens Stock Exchange](https://www.athexgroup.gr)                                         | ASEX     | 🇬🇷 Greece         | Europe        |
| [Cyprus Stock Exchange](https://www.cse.com.cy/en-GB/home)                                 | XCYS     | 🇨🇾 Cyprus         | Europe        |
| [Istanbul Stock Exchange](https://www.borsaistanbul.com/en)                                | XIST     | 🇹🇷 Turkey         | Europe        |
| [Austrialian Securities Exchange](https://www.asx.com.au)                                  | XASX     | 🇦🇺 Australia      | Asia-Pacific  |
| [New Zealand Exchange](https://www.nzx.com)                                                | XNZE     | 🇳🇿 New Zealand    | Asia-Pacific  |
| [Singapore Exchange](https://www.sgx.com)                                                  | XSES     | 🇸🇬 Singapore      | Asia-Pacific  |
| [Shanghai Stock Exchange](https://english.sse.com.cn)                                      | XSHG     | 🇨🇳 China          | Asia-Pacific  |
| [Hong Kong Stock Exchange](https://www.hkex.com.hk/?sc_lang=en)                            | XHKG     | 🇭🇰 Hong Kong      | Asia-Pacific  |
| [Taiwan Stock Exchange Corp.](https://www.twse.com.tw/en)                                  | XTAI     | 🇹🇼 Taiwan         | Asia-Pacific  |
| [Tokyo Stock Exchange](https://www.jpx.co.jp/english)                                      | XTKS     | 🇯🇵 Japan          | Asia-Pacific  |
| [Korea Exchange](https://global.krx.co.kr)                                                 | XKRX     | 🇰🇷 South Korea    | Asia-Pacific  |
| [Malaysia Stock Exchange](https://www.bursamalaysia.com)                                   | XKLS     | 🇲🇾 Malaysia       | Asia-Pacific  |
| [Philippine Stock Exchange](https://www.pse.com.ph/stockMarket/home.html)                  | XPHS     | 🇵🇭 Philippines    | Asia-Pacific  |
| [Stock Exchange of Thailand](https://www.set.or.th/set/mainpage.do?language=en&country=US) | XBKK     | 🇹🇭 Thailand       | Asia-Pacific  |
| [Indonesia Stock Exchange](https://www.idx.co.id)                                          | XIDX     | 🇮🇩 Indonesia      | Asia-Pacific  |
| [Bombay Stock Exchange](https://www.bseindia.com)                                          | XBOM     | 🇮🇳 India          | Asia-Pacific  |
| [Pakistan Stock Exchange](https://www.psx.com.pk)                                          | XKAR     | 🇵🇰 Pakistan       | Asia-Pacific  |
| [Tel Aviv Stock Exchange](https://www.tase.co.il/Eng/Pages/Homepage.aspx)                  | XTAE     | 🇮🇱 Israel         | Middle East   |
| [Saudi Stock Exchange](https://www.saudiexchange.sa)                                       | XSAU     | 🇸🇦 Saudi Arabia   | Middle East   |
| [Johannesburg Stock Exchange](https://www.jse.co.za/z)                                     | XJSE     | 🇿🇦 South Africa   | Africa        |

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
