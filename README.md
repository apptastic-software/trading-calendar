Trading Calendar
================

Market calendar RESTful API with holiday, late open and early close. Over 50+ unique exchange calendars for global equity and futures markets.

## Running it locally

# Pull the Docker Image

Pull pre-built image from [Docker Hub repository][1]:
```
docker pull apptasticsoftware/trading-calendar:latest
```

# Start the Docker Container
Run a container based on the image:
```
docker run -d --name trading-calendar -p 8000:80 apptasticsoftware/trading-calendar
```

# Test it
You should be able to test it in your Docker container's URL, for example:
```
 http://127.0.0.1:8000/api/v1/markets?mic=XNYS
```

# Interactive API docs
For automatic interactive API documentation (OpenAPI, previously known as the Swagger):
```
http://127.0.0.1:8000/docs
```


## Calendar Support

| Exchange                        | MIC      | Country        | Exchange Website                                             |
| ------------------------------- | -------- | -------------- | ------------------------------------------------------------ |
| New York Stock Exchange         | XNYS     | USA            | https://www.nyse.com/index                                   |
| CBOE Futures                    | XCBF     | USA            | https://markets.cboe.com/us/futures/overview/                |
| Chicago Mercantile Exchange     | CMES     | USA            | https://www.cmegroup.com/                                    |
| ICE US                          | IEPA     | USA            | https://www.theice.com/index                                 |
| Toronto Stock Exchange          | XTSE     | Canada         | https://www.tsx.com/                                         |
| BMF Bovespa                     | BVMF     | Brazil         | http://www.b3.com.br/en_us/                                  |
| London Stock Exchange           | XLON     | England        | https://www.londonstockexchange.com/home/homepage.htm        |
| Euronext Amsterdam              | XAMS     | Netherlands    | https://www.euronext.com/en/regulation/amsterdam             |
| Euronext Brussels               | XBRU     | Belgium        | https://www.euronext.com/en/regulation/brussels              |
| Euronext Lisbon                 | XLIS     | Portugal       | https://www.euronext.com/en/regulation/lisbon                |
| Euronext Paris                  | XPAR     | France         | https://www.euronext.com/en/regulation/paris                 |
| Frankfurt Stock Exchange        | XFRA     | Germany        | http://en.boerse-frankfurt.de/                               |
| Deutsche Börse Xetra            | XETR     | Germany        | https://www.xetra.com/xetra-en/                              |
| SIX Swiss Exchange              | XSWX     | Switzerland    | https://www.six-group.com/exchanges/index.html               |
| Tokyo Stock Exchange            | XTKS     | Japan          | https://www.jpx.co.jp/english/                               |
| Austrialian Securities Exchange | XASX     | Australia      | https://www.asx.com.au/                                      |
| Bolsa de Madrid                 | XMAD     | Spain          | http://www.bolsamadrid.es/ing/aspx/Portada/Portada.aspx      |
| Borsa Italiana                  | XMIL     | Italy          | https://www.borsaitaliana.it/homepage/homepage.en.htm        |
| New Zealand Exchange            | XNZE     | New Zealand    | https://www.nzx.com/                                         |
| Wiener Borse                    | XWBO     | Austria        | https://www.wienerborse.at/en/                               |
| Hong Kong Stock Exchange        | XHKG     | Hong Kong      | https://www.hkex.com.hk/?sc_lang=en                          |
| Copenhagen Stock Exchange       | XCSE     | Denmark        | http://www.nasdaqomxnordic.com/                              |
| Helsinki Stock Exchange         | XHEL     | Finland        | http://www.nasdaqomxnordic.com/                              |
| Stockholm Stock Exchange        | XSTO     | Sweden         | http://www.nasdaqomxnordic.com/                              |
| Oslo Stock Exchange             | XOSL     | Norway         | https://www.oslobors.no/ob_eng/                              |
| Irish Stock Exchange            | XDUB     | Ireland        | http://www.ise.ie/                                           |
| Bombay Stock Exchange           | XBOM     | India          | https://www.bseindia.com                                     |
| Singapore Exchange              | XSES     | Singapore      | https://www.sgx.com                                          |
| Shanghai Stock Exchange         | XSHG     | China          | http://english.sse.com.cn                                    |
| Korea Exchange                  | XKRX     | South Korea    | http://global.krx.co.kr                                      |
| Iceland Stock Exchange          | XICE     | Iceland        | http://www.nasdaqomxnordic.com/                              |
| Poland Stock Exchange           | XWAR     | Poland         | http://www.gpw.pl                                            |
| Santiago Stock Exchange         | XSGO     | Chile          | http://inter.bolsadesantiago.com/sitios/en/Paginas/home.aspx |
| Colombia Securities Exchange    | XBOG     | Colombia       | https://www.bvc.com.co/nueva/index_en.html                   |
| Mexican Stock Exchange          | XMEX     | Mexico         | https://www.bmv.com.mx                                       |
| Lima Stock Exchange             | XLIM     | Peru           | https://www.bvl.com.pe                                       |
| Prague Stock Exchange           | XPRA     | Czech Republic | https://www.pse.cz/en/                                       |
| Budapest Stock Exchange         | XBUD     | Hungary        | https://bse.hu/                                              |
| Athens Stock Exchange           | ASEX     | Greece         | http://www.helex.gr/                                         |
| Istanbul Stock Exchange         | XIST     | Turkey         | https://www.borsaistanbul.com/en/                            |
| Tel Aviv Stock Exchange         | XTAE     | Israel         | https://www.tase.co.il/Eng/Pages/Homepage.aspx               |
| Johannesburg Stock Exchange     | XJSE     | South Africa   | https://www.jse.co.za/z                                      |
| Malaysia Stock Exchange         | XKLS     | Malaysia       | http://www.bursamalaysia.com/market/                         |
| Moscow Exchange                 | XMOS     | Russia         | https://www.moex.com/en/                                     |
| Philippine Stock Exchange       | XPHS     | Philippines    | https://www.pse.com.ph/stockMarket/home.html                 |
| Stock Exchange of Thailand      | XBKK     | Thailand       | https://www.set.or.th/set/mainpage.do?language=en&country=US |
| Indonesia Stock Exchange        | XIDX     | Indonesia      | https://www.idx.co.id/                                       |
| Taiwan Stock Exchange Corp.     | XTAI     | Taiwan         | https://www.twse.com.tw/en/                                  |
| Buenos Aires Stock Exchange     | XBUE     | Argentina      | https://www.bcba.sba.com.ar/                                 |
| Pakistan Stock Exchange         | XKAR     | Pakistan       | https://www.psx.com.pk/                                      |
| Astana International Exchange   | AIXK     | Kazakhstan     | https://www.aix.kz/                                          |
| Bucharest Stock Exchange        | XBSE     | Romania        | https://www.bvb.ro/                                          |

> Note that exchange calendars are defined by their [ISO-10383](https://www.iso20022.org/10383/iso-10383-market-identifier-codes) market identifier code (MIC).

[1]: https://hub.docker.com/repository/docker/apptasticsoftware/trading-calendar
