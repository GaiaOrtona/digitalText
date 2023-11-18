placeList = [{'Urbino': 'Urbino'}, {'Europa': 'Europe'}, {'Genova': 'Genoa'}, {'Nemours': 'Nemours'}, {'Grecia': 'Greece'}, {'Venezia': 'Venice'}, {'Napoli': 'Naples'}, {'Bologna': 'Bologna'}, {'Museo Civico Medievale di Bologna': 'MCMBologna'}, {'Uffizi': 'Uffizi'}, {'basilica di San Petronio': 'BSanPetronio'}, {'Egitto': 'Egypt'}, {'Palazzo Bolognini Amorini': 'palazzo-salina-amorini'}, {'Italia': 'Italy'}, {'Cremona': 'Cremona'}, {'National Gallery': 'NGLondon'}, {'Roma': 'Rome'}, {'Musei Vaticani': 'VaticanMuseums'}, {'Madrid': 'Madrid'}, {'Museo del Prado': 'PradoMuseum'}, {'Palermo': 'Palermo'}, {'Sicilia': 'Sicily'}, {'Isola di Capri': 'Capri'}, {'monastero della Santissima Annunziata': 'Annunziata-Paternò'}, {'Imola': 'Imola'}, {'Parigi': 'Paris'}, {'Francia': 'France'}, {'Pisa': 'Pisa'}, {'Firenze': 'Florence'}, {'Hampton Court': 'HCourt'}, {'chiesa di San Lorenzo in Fonte': 'sanlinfonte'}, {'Accademia nazionale di San Luca': 'accademia-san-luca-roma'}, {'basilica di San Domenico': 'san-domenico-bologna'}, {'Milano': 'Milan'}, {'Ascoli': 'Ascoli'}, {'Spagna': 'Spain'}, {'AccaAccademia Nazionale dei Lincei': 'accademia-lincei'}, {'Toscana': 'Tuscany'}, {'Torino': 'Turin'}, {'Coira': 'Coira'}, {'Accademia di belle arti di Firenze': 'accademia-belle-arti-firenze'}, {'Londra': 'London'}, {'Royal Academy of Arts': 'royal-academy-of-arts'}, {'Loreto': 'Loreto'}, {'chiesa di Santa Maria di Loreto': 'santa-casa-di-maria'}, {'via Sistina': 'via-sistina'}, {'Russia': 'Russia'}, {"basilica di Sant'Andrea delle Fratte": 'chiesa-andrea-fratte'}, {'Pantheon': 'pantheon'}, {'Palazzo dell’Archiginnasio': 'archiginnasio'}, {'Gran Bretagna': 'GreatBritain'}, {'Frogmore House': 'FrogmoreHouse'}, {'castello di Windsor': 'WindsorCastle'}, {'reggia di Versailles': 'PalaceofVersailles'}, {'Bordeaux': 'Bordeaux'}, {'Museo del Louvre': 'LouvreMuseum'}, {'By': 'By'}, {'Batignolles': 'Batignolles'}, {'Passy': 'Passy'}, {'America': 'America'}, {'Pittsburgh': 'Pittsburgh'}, {'Hudson': 'HudsonRiver'}, {'Senna': 'Seine'}, {'Boulevard des Capucins': 'BoulevarddesCapucins'}, {'New York': 'NewYorkCity'}, {'Washington': 'Washington'}, {'Filadelfia': 'Philadelphia'}, {'Boston': 'Boston'}, {'Montparnasse': 'Montparnasse '}, {'Hôpital Ville-évrard': 'Villeevrard'}, {'Inghilterra': 'England'}, {'Regno Unito': 'UK'}, {"Stati Uniti d'America": 'USA'}, {'Sud Amreica': 'SouthAmreica'}, {'Rue Cortot': 'RueCortot'}, {'San Pietroburgo': 'SaintPetersburg'}, {'Lago di Garda': 'LakeGarda'}, {'Vittoriale degli Italiani': 'Vittoriale'}, {'Brescia': 'Brescia'}, {'Parma': 'Parma'}, {'Cuernavaca': 'Cuernavaca'}, {'Messico': 'Mexico'}, {'Polonia': 'Poland'}, {'Unione Sovietica': 'SovietUnion'}, {'Kazan': 'Kazan'}, {'Odessa': 'Odessa'}, {'Kaunas': 'Kaunas'}, {'Finlandia': 'Finland'}, {'Germania': 'Germany'}, {'Austria': 'Austria'}, {'Svizzera': 'Switzerland'}, {'Karlsruhe': 'Karlsruhe'}, {'Boulevard Malesherbes': 'BoulevardMalesherbes'}, {'Champs Elysées': 'ChampsElysees'}, {'Mosca': 'Moscow'}, {'Colonia': 'Cologne'}, {'Indocina': 'Indochina'}, {'Asia': 'Asia'}, {'Cadaqués': 'Cadaqués'}, {'Girona': 'Girona'}, {'Castello di Púbol': 'CastleofPubol'}, {'Coyoacán': 'Coyoacan'}, {'Rockefeller Center': 'RockefellerCenter'}, {'San Francisco': 'SanFrancisco'}, {'Mexico City': 'MexicoCity'}, {'Friuli Venezia-Giulia': 'FriuliVeneziaGiulia'}, {'Berlino': 'Berlin'}, {'Los Angeles': 'LosAngeles'}, {'Villa Borghese': 'Villaborghese'}, {'Etna': 'Etna'}, {'Carso': 'Carso'}, {'Piave': 'Piave'}, {'Palazzo delle Poste': 'Palazzodellepostepalermo'}, {'Lituania': 'Lithuania'}, {'Pescolanciano': 'Pescolanciano'}, {'Isernia': 'Isernia'}, {'Castel di Sangro': 'Casteldisangro'}, {'Lucera': 'Lucera'}, {"Galleria dell'Obelisco": 'Gallerialobelisco'}, {'Mura Aureliane': 'Muraaureliane'}, {'piazzale Fiume': 'Piazzafiume'}, {'Porta Pia': 'Portapia'}, {'Bronx': 'Bronx'}, {'Galleria La Tartaruga': 'Gallerialatartaruga'}, {'Klagenfurt': 'Klagenfurt'}, {'Saint-Germain': 'Saintgermain'}, {'Trapani': 'Trapani'}, {'Erice': 'Erice'}, {'Monte San Giuliano': 'Montesangiuliano'}, {'convento di San Marco': 'Conventodisanmarco'}, {'via Flaminia': 'Viaflaminia'}, {'piazza del Popolo': 'Piazzadelpopolo'}, {'via del Babuino': 'Viadelbabuino'}, {'Salone del Palazzo del Podestà': 'Salonedelpalazzodelpodestà'}, {'Ungheria': 'Hungary'}, {'castello di Rivoli': 'Castellodirivoli'}, {'Brenta': 'Brenta'}, {'chiesa dei Gesuati': 'Chiesadeigesuati'}, {'Gorizia': 'Gorizia'}, {'Monza': 'Monza'}, {'Barcellona': 'Barcelona'}, {'Lido di Venezia': 'Venicelido'}, {'via San Nicolò da Tolentino': 'Viasannicolodatolentino'}, {'Caffè Aragno': 'Caffearagno'}, {'Ulassai': 'Ulassai'}, {'Ogliastra': 'Ogliastra'}, {'provincia di Nuoro': 'Nuoroprovince'}, {'Sardegna': 'Sardinia'}, {'Verona': 'Verona'}, {'Accademia di Belle Arti': 'Accademiadibelleartiverona'}, {'porto di Napoli': 'Portofnaples'}, {'Cagliari': 'Cagliari'}, {'Galleria Schneider': 'Galleriaschneider'}, {'monte Gedili': 'Montegedili'}, {'Galleria Diaframma di Milano': 'Galleriadiaframmamilan'}, {'Cappella Bardi': 'Cappellabardi'}, {'Santa Croce': 'Santacroce'}, {'rue des Grands-Augustins': 'Ruedesgrandsaugustins'}, {'Guernica': 'Guernica'}, {'Les Deux Magots': 'Cafelesdeuxmagots'}, {'Bosnia ed Erzegovina': 'Bosniaandherzegovina'}, {'Buenos Aires': 'Buenosaires'}, {'École de la Photographie de la Ville de Paris': 'Ecoledelaphotographiedelavilledeparis'}, {'Washington': 'Washingtonstate'}, {'New Mexico': 'Newmexico'}, {'Manhattan': 'Manhattan'}, {'Teachers College': 'Teacherscollege'}, {'Columbia University': 'Columbiauniversity'}, {'ponte di Brooklyn': 'Brooklynbridge'}, {'East River': 'Eastrivernewyork'}, {'Greenwich Village': 'Greenwichvillage'}, {'Bellevue Hospital Center': 'Bellevuehospital'}, {'Coenties Slip': 'Coentiesslip'}, {'Bowery Street': 'Bowerystreetnewyork'}, {'SoHo': 'Soho'}, {'Taos': 'Taos'}, {'Arco della Pace': 'Arcodellapace'}, {'Porta Palazzo': 'Portapalazzo'}, {'Arsenali di Amalfi': 'Arsenaliamalfi'}, {'L’Attico': 'Gallerialattico'}, {'Fregene': 'Fregene'}, {'Ciampino': 'Ciampino'}, {'Neuilly-sur-Seine': 'Neuillysurseine'}, {'Moderna Museet': 'Modernamuseet'}, {'Stoccolma': 'Stockholm'}, {'Ginevra': 'Geneva'}, {'Gerusalemme': 'Jerusalem'}, {'parco Güell': 'Parcguell'}, {'Garavicchio': 'Garavicchio'}, {'Maremma': 'Maremma'}, {'Centro Georges Pompidou': 'Centrepompidou'}, {'Palazzo delle Esposizioni': 'Palazzodelleesposizioni'}, {'Villa Borghese': 'Villaborghese'}, {'via Beccaria': 'Viabeccariarome'}, {'ex chiesa di S. Lucia': 'Chiesadisantaluciabologna'}, {'Rhode Island School of Design': 'Rhodeislandschoolofdesign'}, {'Galleria Ugo Ferranti': 'Galleriaugoferranti'}, {'Club 82 di Lower Manhattan': 'Club82newyork'}, {'Hubert’s Museum': 'Hubertsmuseum'}, {'Times Square': 'Timessquare'}, {'50th West': '50thwest'}, {'Avenue of the Americas': '6thavenue'}, {'Digione': 'Dijon'}, {'Bussola': 'Bussolaturin'}, {'Institute of Contemporary Art (Boston)': 'Instituteofcontemporaryartboston'}, {'Stedelijk Museum': 'Stedelijkmuseumamsterdam'}, {'Amburgo': 'Hamburg'}, {'Olanda': 'Netherlands'}, {'Ruhr': 'Ruhr'}, {'Camden Arts Centre': 'Camdenartscentre'}, {'Guggenheim Bilbao': 'Guggenheimmuseumbilbao'}, {'MAXXI - Museo nazionale delle arti del XXI secolo': 'Maxxirome'}, {'provincia di Udine': 'Udineprovince'}, {'Biella': 'Biella'}, {'Trani': 'Trani'}, {'Puglia': 'Apulia'}, {'Calabria': 'Calabria'}, {'Vesuvio': 'Vesuvius'}, {'Politecnico di Milano': 'Politecnicomilan'}, {'Ivrea': 'Ivrea'}, {'Brera': 'Brera'}, {'Teatro Mediterraneo': 'Teatromediterraneonaples'}, {'Teatro Alla Scala': 'Teatroallascalamilan'}, {'Teatro Argentina': 'Teatroargentinarome'}, {'Palazzo Grassi': 'Palazzograssi'}, {'piazza Dante': 'PiazzaDanteNapoli'}, {'Museo Archeologico': 'Museoarcheologiconaples'}, {'piazzale Luigi Cadorna': 'Piazzalecadornamilan'}, {'Montmartre': 'Montmartre'}]
