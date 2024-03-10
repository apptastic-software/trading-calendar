from .exchange import Exchange as Exchange
from .calendar import Calendar as Calendar
import exchange_calendars as ecals

class Exchanges:
    def __init__(self):
        print("Exchange Calendars version: {}".format(ecals.__version__))
        self.exchanges = {}
        self.mic_list = []
        pass


    def load(self):
        exchange_list = {
            'XNYS' : {
                'mic' : 'XNYS',
                'name' : 'New York Stock Exchange',
                'acronym' : 'NYSE',
                'lei' : '5493000F4ZO33MV32P92',
                'url' : 'https://www.nyse.com/index',
                'city' : 'New York',
                'country' : 'United States',
                'country_code' : 'US',
                'region' : 'North America',
                'flag' : '🇺🇸',
            },
            'XCBF' : {
                'mic' : 'XCBF',
                'name' : 'CBOE Futures',
                'acronym' : 'CFE',
                'lei' : '529900RLNSGA90UPEH54',
                'url' : 'https://markets.cboe.com/us/futures/overview/',
                'city' : 'Chicago',
                'country' : 'United States',
                'country_code' : 'US',
                'region' : 'North America',
                'flag' : '🇺🇸',
            },
            'CMES' : {
                'mic' : 'CMES',
                'name' : 'Chicago Mercantile Exchange',
                'acronym' : 'CME',
                'lei' : 'LCZ7XYGSLJUHFXXNXD88',
                'url' : 'https://www.cmegroup.com/',
                'city' : 'Chicago',
                'country' : 'United States',
                'country_code' : 'US',
                'region' : 'North America',
                'flag' : '🇺🇸',
            },
            'IEPA' : {
                'mic' : 'IEPA',
                'name' : 'ICE US',
                'acronym' : 'ICE',
                'lei' : '5493000F4ZO33MV32P92',
                'url' : 'https://www.theice.com/index',
                'city' : 'Atlanta',
                'country' : 'United States',
                'country_code' : 'US',
                'region' : 'North America',
                'flag' : '🇺🇸',
            },
            'XTSE' : {
                'mic' : 'XTSE',
                'name' : 'Toronto Stock Exchange',
                'acronym' : 'TSX',
                'lei' : '549300N65GFVKSHGJW59',
                'url' : 'https://www.tsx.com/',
                'city' : 'Toronto',
                'country' : 'Canada',
                'country_code' : 'CA',
                'region' : 'North America',
                'flag' : '🇨🇦',
            },
            'BVMF' : {
                'mic' : 'BVMF',
                'name' : 'B3',
                'acronym' : 'B3',
                'lei' : '4GTK5S46E6H318LMDS44',
                'url' : 'http://www.b3.com.br/en_us/',
                'city' : 'Sao Paulo',
                'country' : 'Brazil',
                'country_code' : 'BR',
                'region' : 'South America',
                'flag' : '🇧🇷',
            },
            'XBUE' : {
                'mic' : 'XBUE',
                'name' : 'Buenos Aires Stock Exchange',
                'acronym' : 'BCBA',
                'lei' : None,
                'url' : 'https://www.bcba.sba.com.ar/',
                'city' : 'Buenos Aires',
                'country' : 'Argentina',
                'country_code' : 'AR',
                'region' : 'South America',
                'flag' : '🇦🇷',
            },
            'XMEX' : {
                'mic' : 'XMEX',
                'name' : 'Mexican Stock Exchange',
                'acronym' : None,
                'lei' : '894500CS2D6RLGW61A19',
                'url' : 'https://www.bmv.com.mx',
                'city' : 'Mexico',
                'country' : 'Mexico',
                'country_code' : 'MX',
                'region' : 'South America',
                'flag' : '🇲🇽',
            },
            'XSGO' : {
                'mic' : 'XSGO',
                'name' : 'Santiago Stock Exchange',
                'acronym' : None,
                'lie' : None,
                'url' : 'https://www.bolsadesantiago.com/',
                'city' : 'Santiago',
                'country' : 'Chile',
                'country_code' : 'CL',
                'region' : 'South America',
                'flag' : '🇨🇱',
            },
            'XBOG' : {
                'mic' : 'XBOG',
                'name' : 'Colombia Securities Exchange',
                'acronym' : 'BVC',
                'lei' : '254900XQMHVWJ1P3FC67',
                'url' : 'https://www.bvc.com.co/nueva/index_en.html',
                'city' : 'Bogota',
                'country' : 'Colombia',
                'country_code' : 'CO',
                'region' : 'South America',
                'flag' : '🇨🇴',
            },
            'XLIM' : {
                'mic' : 'XLIM',
                'name' : 'Lima Stock Exchange',
                'acronym' : 'BVL',
                'lei' : None,
                'url' : 'https://www.bvl.com.pe',
                'city' : 'Lima',
                'country' : 'Peru',
                'country_code' : 'PE',
                'region' : 'South America',
                'flag' : '🇵🇪',
            },
            'XICE' : {
                'mic' : 'XICE',
                'name' : 'Iceland Stock Exchange',
                'acronym' : 'ICEX',
                'lei' : '5493000SYSCC8J8U5638',
                'url' : 'http://www.nasdaqomxnordic.com/',
                'city' : 'Reykjavik',
                'country' : 'Iceland',
                'country_code' : 'IS',
                'region' : 'Europe',
                'flag' : '🇮🇸',
            },
            'XOSL' : {
                'mic' : 'XOSL',
                'name' : 'Oslo Stock Exchange',
                'acronym' : None,
                'lei' : '5967007LIEEXZXHDL433',
                'url' : 'https://www.oslobors.no/ob_eng/',
                'city' : 'Oslo',
                'country' : 'Norway',
                'country_code' : 'NO',
                'region' : 'Europe',
                'flag' : '🇳🇴',
            },
            'XSTO' : {
                'mic' : 'XSTO',
                'name' : 'Stockholm Stock Exchange',
                'acronym' : None,
                'lei' : '549300KBQIVNEJEZVL96',
                'url' : 'http://www.nasdaqomxnordic.com/',
                'city' : 'Stockholm',
                'country' : 'Sweden',
                'country_code' : 'SE',
                'region' : 'Europe',
                'flag' : '🇸🇪',
            },
            'XHEL' : {
                'mic' : 'XHEL',
                'name' : 'Helsinki Stock Exchange',
                'acronym' : None,
                'lei' : '743700NAXLL4Q86IEX32',
                'url' : 'http://www.nasdaqomxnordic.com/',
                'city' : 'Helsinki',
                'country' : 'Finland',
                'country_code' : 'FI',
                'region' : 'Europe',
                'flag' : '🇫🇮',
            },
            'XCSE' : {
                'mic' : 'XCSE',
                'name' : 'Copenhagen Stock Exchange',
                'acronym' : None,
                'lei' : '549300JNYZUL5PLI8E17',
                'url' : 'http://www.nasdaqomxnordic.com/',
                'city' : 'Copenhagen',
                'country' : 'Denmark',
                'country_code' : 'DK',
                'region' : 'Europe',
                'flag' : '🇩🇰',
            },
            'XLON' : {
                'mic' : 'XLON',
                'name' : 'London Stock Exchange',
                'acronym' : 'LSE',
                'lei' : '213800D1EI4B9WTWWD28',
                'url' : 'https://www.londonstockexchange.com/home/homepage.htm',
                'city' : 'London',
                'country' : 'United Kingdom',
                'country_code' : 'GB',
                'region' : 'Europe',
                'flag' : '🇬🇧',
            },
            'XDUB' : {
                'mic' : 'XDUB',
                'name' : 'Irish Stock Exchange',
                'acronym' : 'ISE',
                'lei' : '635400DZBUIMTBCXGA12',
                'url' : 'https://www.ise.ie/',
                'city' : 'Dublin',
                'country' : 'Ireland',
                'country_code' : 'IE',
                'region' : 'Europe',
                'flag' : '🇮🇪',
            },
            'XAMS' : {
                'mic' : 'XAMS',
                'name' : 'Euronext Amsterdam',
                'acronym' : None,
                'lei' : '724500V6UOK62XEZ2L78',
                'url' : 'https://www.euronext.com/en/regulation/amsterdam',
                'city' : 'Amsterdam',
                'country' : 'Netherlands',
                'country_code' : 'NL',
                'region' : 'Europe',
                'flag' : '🇳🇱',
            },
            'XBRU' : {
                'mic' : 'XBRU',
                'name' : 'Euronext Brussels',
                'acronym' : None,
                'lei' : '5493007YLUF2KAS0TM17',
                'url' : 'https://www.euronext.com/en/regulation/brussels',
                'city' : 'Brussels',
                'country' : 'Belgium',
                'country_code' : 'BE',
                'region' : 'Europe',
                'flag' : '🇧🇪',
            },
            'XFRA' : {
                'mic' : 'XFRA',
                'name' : 'Frankfurt Stock Exchange',
                'acronym' : None,
                'lei' : '529900G3SW56SHYNPR95',
                'url' : 'https://en.boerse-frankfurt.de/',
                'city' : 'Frankfurt',
                'country' : 'Germany',
                'country_code' : 'DE',
                'region' : 'Europe',
                'flag' : '🇩🇪',
            },
            'XETR' : {
                'mic' : 'XETR',
                'name' : 'Deutsche Börse Xetra',
                'acronym' : 'XETRA',
                'lei' : '529900G3SW56SHYNPR95',
                'url' : 'https://www.xetra.com/xetra-en/',
                'city' : 'Frankfurt',
                'country' : 'Germany',
                'country_code' : 'DE',
                'region' : 'Europe',
                'flag' : '🇩🇪',
            },
            'XSWX' : {
                'mic' : 'XSWX',
                'name' : 'SIX Swiss Exchange',
                'acronym' : 'SIX',
                'lei' : '529900HQ12A6FGDMWA17',
                'url' : 'https://www.six-group.com/exchanges/index.html',
                'city' : 'Zurich',
                'country' : 'Switzerland',
                'country_code' : 'CH',
                'region' : 'Europe',
                'flag' : '🇨🇭',
            },
            'XWBO' : {
                'mic' : 'XWBO',
                'name' : 'Wiener Borse',
                'acronym' : None,
                'lei' : '315700ENWH1A81RCVZ91',
                'url' : 'https://www.wienerborse.at/en/',
                'city' : 'Vienna',
                'country' : 'Austria',
                'country_code' : 'AT',
                'region' : 'Europe',
                'flag' : '🇦🇹',
            },
            'XWAR' : {
                'mic' : 'XWAR',
                'name' : 'Warsaw Stock Exchange',
                'acronym' : 'WSE',
                'lei' : '25940039ZHD3Z37GKR71',
                'url' : 'https://www.gpw.pl/en-home',
                'city' : 'Warsaw',
                'country' : 'Poland',
                'country_code' : 'PL',
                'region' : 'Europe',
                'flag' : '🇵🇱',
            },
            'XPRA' : {
                'mic' : 'XPRA',
                'name' : 'Prague Stock Exchange',
                'acronym' : 'PSE',
                'lei' : '969500HMVSZ0TCV65D58',
                'url' : 'https://www.pse.cz/en/',
                'city' : 'Prague',
                'country' : 'Czech Republic',
                'country_code' : 'CZ',
                'region' : 'Europe',
                'flag' : '🇨🇿',
            },
            'XMOS' : {
                'mic' : 'XMOS',
                'name' : 'Moscow Exchange',
                'acronym' : 'MFB',
                'lei' : '253400RX2CP80AMV8V57',
                'url' : 'https://mse.ru/',
                'city' : 'Moscow',
                'country' : 'Russia',
                'country_code' : 'RU',
                'region' : 'Europe',
                'flag' : '🇷🇺',
            },
            'AIXK' : {
                'mic' : 'AIXK',
                'name' : 'Astana International Exchange',
                'acronym' : 'AIX',
                'lei' : '254900L6FRRJKZTLNY11',
                'url' : 'https://www.aix.kz/',
                'city' : 'Astana',
                'country' : 'Kazakhstan',
                'country_code' : 'KZ',
                'region' : 'Europe',
                'flag' : '🇰🇿',
            },
            'XLIS' : {
                'mic' : 'XLIS',
                'name' : 'Euronext Lisbon',
                'acronym' : None,
                'lei' : '529900K0OK4J5I7A5V66',
                'url' : 'https://www.euronext.com/en/regulation/lisbon',
                'city' : 'Lisbon',
                'country' : 'Portugal',
                'country_code' : 'PT',
                'region' : 'Europe',
                'flag' : '🇵🇹',
            },
            'XPAR' : {
                'mic' : 'XPAR',
                'name' : 'Euronext Paris',
                'acronym' : None,
                'lei' : '969500HMVSZ0TCV65D58',
                'url' : 'https://www.euronext.com/en/regulation/paris',
                'city' : 'Paris',
                'country' : 'France',
                'country_code' : 'FR',
                'region' : 'Europe',
                'flag' : '🇫🇷',
            },
            'XMAD' : {
                'mic' : 'XMAD',
                'name' : 'Bolsa de Madrid',
                'acronym' : None,
                'lei' : '959800UYJM40XUGVGG78',
                'url' : 'https://www.bolsamadrid.es/ing/aspx/Portada/Portada.aspx',
                'city' : 'Madrid',
                'country' : 'Spain',
                'country_code' : 'ES',
                'region' : 'Europe',
                'flag' : '🇪🇸',
            },
            'XMIL' : {
                'mic' : 'XMIL',
                'name' : 'Borsa Italiana',
                'acronym' : None,
                'lei' : '8156005391EE905D3124',
                'url' : 'https://www.borsaitaliana.it/homepage/homepage.en.htm',
                'city' : 'Milan',
                'country' : 'Italy',
                'country_code' : 'IT',
                'region' : 'Europe',
                'flag' : '🇮🇹',
            },
            'XBUD' : {
                'mic' : 'XBUD',
                'name' : 'Budapest Stock Exchange',
                'acronym' : None,
                'lei' : '54930094UMSXWVWJMT48',
                'url' : 'https://bse.hu',
                'city' : 'Budapest',
                'country' : 'Hungary',
                'country_code' : 'HU',
                'region' : 'Europe',
                'flag' : '🇭🇺',
            },
            'XBSE' : {
                'mic' : 'XBSE',
                'name' : 'Bucharest Stock Exchange',
                'acronym' : None,
                'lei' : '254900LXHEVKYGERER05',
                'url' : 'https://www.bvb.ro/',
                'city' : 'Bucharest',
                'country' : 'Romania',
                'country_code' : 'RO',
                'region' : 'Europe',
                'flag' : '🇷🇴',
            },            
            'ASEX' : {
                'mic' : 'ASEX',
                'name' : 'Athens Stock Exchange',
                'acronym' : 'ASE',
                'lei' : '549300GSRN07MNENPL97',
                'url' : 'http://www.helex.gr/',
                'city' : 'Athens',
                'country' : 'Greece',
                'country_code' : 'GR',
                'region' : 'Europe',
                'flag' : '🇬🇷',
            },
            'XIST' : {
                'mic' : 'XIST',
                'name' : 'Istanbul Stock Exchange',
                'acronym' : None,
                'lei' : None,
                'url' : 'https://www.borsaistanbul.com/en/',
                'city' : 'Istanbul',
                'country' : 'Turkey',
                'country_code' : 'TR',
                'region' : 'Europe',
                'flag' : '🇹🇷',
            },
            'XTAE' : {
                'mic' : 'XTAE',
                'name' : 'Tel Aviv Stock Exchange',
                'acronym' : 'TASE',
                'lei' : '213800WG3A9RJ78EGT48',
                'url' : 'https://www.tase.co.il/Eng/Pages/Homepage.aspx',
                'city' : 'Tel Aviv',
                'country' : 'Israel',
                'country_code' : 'IL',
                'region' : 'Europe',
                'flag' : '🇮🇱',
            },
            'XBOM' : {
                'mic' : 'XBOM',
                'name' : 'Bombay Stock Exchange',
                'acronym' : 'MSE',
                'lei' : '335800UOTLCPTZQVDA19',
                'url' : 'https://www.bseindia.com',
                'city' : 'Mumbai',
                'country' : 'India',
                'country_code' : 'IN',
                'region' : 'Asia-Pacific',
                'flag' : '🇮🇳',
            },
            'XKAR' : {
                'mic' : 'XKAR',
                'name' : 'Pakistan Stock Exchange',
                'acronym' : 'PSX',
                'lei' : None,
                'url' : 'https://www.psx.com.pk',
                'city' : 'Karachi',
                'country' : 'Pakistan',
                'country_code' : 'PK',
                'region' : 'Asia-Pacific',
                'flag' : '🇵🇰',
            },
            'XSAU' : {
                'mic' : 'XSAU',
                'name' : 'Saudi Stock Exchange',
                'acronym' : None,
                'lei' : '894500BXFAWZK686TP37',
                'url' : 'https://www.tadawul.com.sa/',
                'city' : 'Rijad',
                'country' : 'Saudi Arabia',
                'country_code' : 'SA',
                'region' : 'Middle East',
                'flag' : '🇸🇦',
            },
            'XJSE' : {
                'mic' : 'XJSE',
                'name' : 'Johannesburg Stock Exchange',
                'acronym' : 'JSE',
                'lei' : '213800MZ1VUQEBWRFO39',
                'url' : 'https://www.jse.co.za/',
                'city' : 'Johannesburg',
                'country' : 'South Africa',
                'country_code' : 'ZA',
                'region' : 'Africa',
                'flag' : '🇿🇦',
            },
            'XHKG' : {
                'mic' : 'XHKG',
                'name' : 'Hong Kong Stock Exchange',
                'acronym' : 'HKEX',
                'lei' : '213800YTVSXYQN17BW16',
                'url' : 'https://www.hkex.com.hk/?sc_lang=en',
                'city' : 'Hong Kong',
                'country' : 'Hong Kong',
                'country_code' : 'HK',
                'region' : 'Asia-Pacific',
                'flag' : '🇭🇰',
            },
            'XSES' : {
                'mic' : 'XSES',
                'name' : 'Singapore Exchange',
                'acronym' : 'SGX',
                'lei' : '549300IQ650PPXM76X03',
                'url' : 'https://www.sgx.com',
                'city' : 'Singapore',
                'country' : 'Singapore',
                'country_code' : 'SG',
                'region' : 'Asia-Pacific',
                'flag' : '🇸🇬',
            },
            'XSHG' : {
                'mic' : 'XSHG',
                'name' : 'Shanghai Stock Exchange',
                'acronym' : 'SSE',
                'lei' : '300300LRJ5FEZ23N8725',
                'url' : 'http://www.szse.cn/English/index.html',
                'city' : 'Shanghai',
                'country' : 'China',
                'country_code' : 'CN',
                'region' : 'Asia-Pacific',
                'flag' : '🇨🇳',
            },
            'XTAI' : {
                'mic' : 'XTAI',
                'name' : 'Taiwan Stock Exchange Corp.',
                'acronym' : 'TWSE',
                'lei' : '549300NH6S3EOUMY2162',
                'url' : 'https://www.twse.com.tw/en/',
                'city' : 'Taipei',
                'country' : 'Taiwan',
                'country_code' : 'TW',
                'region' : 'Asia-Pacific',
                'flag' : '🇹🇼',
            },
            'XKLS' : {
                'mic' : 'XKLS',
                'name' : 'Malaysia Stock Exchange',
                'acronym' : None,
                'lei' : '254900CXCSGW8M52ZU27',
                'url' : 'https://www.bursamalaysia.com/',
                'city' : 'Kuala Lumpur',
                'country' : 'Malaysia',
                'country_code' : 'MY',
                'region' : 'Asia-Pacific',
                'flag' : '🇲🇾',
            },
            'XIDX' : {
                'mic' : 'XIDX',
                'name' : 'Indonesia Stock Exchange',
                'acronym' : 'IDX',
                'lei' : None,
                'url' : 'https://www.idx.co.id/',
                'city' : 'Jakarta',
                'country' : 'Indonesia',
                'country_code' : 'ID',
                'region' : 'Asia-Pacific',
                'flag' : '🇮🇩',
            },
            'XBKK' : {
                'mic' : 'XBKK',
                'name' : 'Stock Exchange of Thailand',
                'acronym' : 'SET',
                'lei' : '254900R211PTUP8K9M82',
                'url' : 'https://www.set.or.th/set/mainpage.do?language=en&country=US',
                'city' : 'Bangkok',
                'country' : 'Thailand',
                'country_code' : 'TH',
                'region' : 'Asia-Pacific',
                'flag' : '🇹🇭',
            },
            'XPHS' : {
                'mic' : 'XPHS',
                'name' : 'Philippine Stock Exchange',
                'acronym' : 'PSE',
                'lei' : None,
                'url' : 'https://www.pse.com.ph/stockMarket/home.html',
                'city' : 'Pasig City',
                'country' : 'Philippines',
                'country_code' : 'PH',
                'region' : 'Asia-Pacific',
                'flag' : '🇵🇭',
            },
            'XKRX' : {
                'mic' : 'XKRX',
                'name' : 'Korea Exchange',
                'acronym' : 'KRX',
                'lei' : '549300TJ3RRV6Q1UEW14',
                'url' : 'https://global.krx.co.kr',
                'city' : 'Seoul',
                'country' : 'South Korea',
                'country_code' : 'KR',
                'region' : 'Asia-Pacific',
                'flag' : '🇰🇷',
            },
            'XTKS' : {
                'mic' : 'XTKS',
                'name' : 'Tokyo Stock Exchange',
                'acronym' : 'TSE',
                'lei' : '353800578ADEGIJTVW07',
                'url' : 'https://www.jpx.co.jp/english/',
                'city' : 'Tokyo',
                'country' : 'Japan',
                'country_code' : 'JP',
                'region' : 'Asia-Pacific',
                'flag' : '🇯🇵',
            },
            'XASX' : {
                'mic' : 'XASX',
                'name' : 'Austrialian Securities Exchange',
                'acronym' : 'ASX',
                'lei' : '549300USWUR0S7VMM868',
                'url' : 'https://www.asx.com.au/',
                'city' : 'Sydney',
                'country' : 'Australia',
                'country_code' : 'AU',
                'region' : 'Asia-Pacific',
                'flag' : '🇦🇺',
            },
            'XNZE' : {
                'mic' : 'XNZE',
                'name' : 'New Zealand Exchange',
                'acronym' : 'NZX',
                'lei' : None,
                'url' : 'https://www.nzx.com/',
                'city' : 'Wellington',
                'country' : 'New Zealand',
                'country_code' : 'NZ',
                'region' : 'Asia-Pacific',
                'flag' : '🇳🇿',
            }
        }

        count = 0
        sorted_exchange_list = dict(sorted(exchange_list.items(), key=lambda item: item[1]['name'])).values()
        for exchange in sorted_exchange_list:
            count += 1
            mic = exchange.get('mic')
            print("Loading calendar for {}... {}/{}".format(mic, count, len(sorted_exchange_list)))
            self.mic_list.append(mic)
            self.exchanges[mic] = Exchange(
                mic = mic,
                name = exchange.get('name'),
                acronym = exchange.get('acronym'),
                lei = exchange.get('lei'),
                url = exchange.get('url'),
                city = exchange.get('city'),
                country = exchange.get('country'),
                country_code = exchange.get('country_code'),
                flag = exchange.get('flag'),
                region = exchange.get('region'),
                calendar = Calendar(ecals.get_calendar(mic), exchange.get('country_code'))
            )

    def get_exchange(self, mic):
        return self.exchanges.get(mic)

    def get_exchanges(self):
        return self.exchanges.values()

    def get_mic_list(self):
        return self.mic_list
