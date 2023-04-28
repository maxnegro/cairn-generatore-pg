#!/usr/bin/python

import csv
import random

# header CSV
fieldnames = ['Nome', 'FOR', 'DES', 'VOL', 'Arm', 'PF', 'PO', 'Slot1', 'Slot2', 'Slot3', 'Slot4', 'Slot5', 'Slot6', 'Slot7', 'Slot8', 'Slot9', 'Slot10', 'Note']

# tabelle
tNomeF = [
    'Agune',
    'Beatrice',
    'Breagan',
    'Bronwyn',
    'Cannora',
    'Drelil',
    'Elgile',
    'Esme',
    'Groua',
    'Henaine',
    'Lirann',
    'Lirathil',
    'Lisabeth',
    'Moralil',
    'Morgwen',
    'Sybil',
    'Theune',
    'Wenlan',
    'Ygwal',
    'Yslen'
]
tNomeM = [
    'Arwel',
    'Bevan',
    'Boroth',
    'Borrid',
    'Breagle',
    'Breglor',
    'Canhoreal',
    'Emrys',
    'Ethex',
    'Gringle',
    'Grinwit',
    'Gruwid',
    'Gruwth',
    'Gwestin',
    'Mannog',
    'Melnax',
    'Orthax',
    'Triunein',
    'Wenlan',
    'Yirmeor'
]
tCognome = [
    'Abernathy',
    'Addercap',
    'Burl',
    'Candlewick',
    'Cormick',
    'Crumwaller',
    'Dunswallow',
    'Getri',
    'Glass',
    'Harkness',
    'Harper',
    'Loomer',
    'Malksmilk',
    'Smythe',
    'Sunderman',
    'Swinney',
    'Thatcher',
    'Tolmen',
    'Weaver',
    'Wolder'
]
tBackground = [
    'Alchimista',
    'Fabbro',
    'Macellaio',
    'Scassinatore',
    'Carpentiere',
    'Chierico',
    'Scommettitore',
    'Becchino',
    'Erborista',
    'Cacciatore',
    'Mago',
    'Mercenario',
    'Mercante',
    'Minatore',
    'Fuorilegge',
    'Artista',
    'Borseggiatore',
    'Contrabbandiere',
    'Servitore',
    'Ranger'
]
tFisico = [
    'Atletico',
    'Gracile',
    'Muscoloso',
    'Corpulento',
    'Longilineo',
    'Massiccio',
    'Basso',
    'Statuario',
    'Robusto',
    'Imponente'
]
tPelle = [
    'Macchiata',
    'Scura',
    'Flaccida',
    'Butterata',
    'Rosea',
    'Morbida',
    'Liscia',
    'Abbronzata',
    'Tatuata',
    'Segnata'
]
tCapelli = [
    'Calvo',
    'Intrecciati',
    'Ricci',
    'Sporchi',
    'Crespi',
    'Lunghi',
    'Voluminosi',
    'Grassi',
    'Mossi',
    'Sparsi'
]
tFaccia = [
    'Ossuta',
    'Rotta',
    'Cesellata',
    'Allungata',
    'Pallida',
    'Perfetta',
    'da Topo',
    'Appuntita',
    'Quadrata',
    'Infossata'
]
tParlata = [
    'Schietta',
    'Profonda',
    'Misteriosa',
    'Monotona',
    'Formale',
    'Greve',
    'Precisa',
    'Stridula',
    'Balbettante',
    'Bisbigliante'
]
tVestito = [
    'Antico',
    'Insanguinato',
    'Elegante',
    'Sporco',
    'Esotico',
    'Logoro',
    'Sgargiante',
    'Livrea',
    'Fetido',
    'Sudicio'
]
tVirtu = [
    'Ambizioso',
    'Cauto',
    'Coraggioso',
    'Disciplinato',
    'Socievole',
    'Onorevole',
    'Umile',
    'Clemente',
    'Sereno',
    'Tollerante'
]
tVizio = [
    'Aggressivo',
    'Scorbutico',
    'Vile',
    'Bugiardo',
    'Avido',
    'Pigro',
    'Nervoso',
    'Rude',
    'Vanitoso',
    'Vendicativo'
]
tReputazione = [
    'Ambizioso',
    'Zotico',
    'Pericoloso',
    'Intrattenitore',
    'Onesto',
    'Fannullone',
    'Eccentrico',
    'Ripugnante',
    'Rispettato',
    'Saggio'
]
tSfortune = [
    'Abbandonato',
    'Assuefatto',
    'Ricattato',
    'Condannato',
    'Maledetto',
    'Truffato',
    'Declassato',
    'Screditato',
    'Ripudiato',
    'Esiliato'
]
tEquipaggiamento = [
    ['Sacca', 1],
    ['Antitossina', 0],
    ['Carretto (+4 slot)', 2],
    ['Catena 3m', 1],
    ['Bastone da rabdomante', 1],
    ['Olio di fuoco', 0],
    ['Rampino', 1],
    ['Sacco grande', 1],
    ['Trappola', 1],
    ['Grimaldelli', 0],
    ['Manette', 0],
    ['Piccone', 1],
    ['Asta 3m', 1],
    ['Carrucola', 0],
    ['Repellente', 0],
    ['Corda (10m)', 1],
    ['Amuleto', 0],
    ['Cannocchiale', 1],
    ['Acciarino', 0],
    ['Aconito (veleno)', 0]
]
tAttrezzi = [
    ['Soffietto', 1],
    ['Secchio', 1],
    ['Triboli', 1],
    ['Gessetto', 0],
    ['Cesello', 0],
    ['Pentole', 1], 
    ['Piede di porco', 1],
    ['Trapano (manuale)', 1],
    ['Canna da pesca', 1],
    ['Colla', 0],
    ['Grasso', 0],
    ['Martello', 0],
    ['Clessidra', 0],
    ['Lima metallica', 0],
    ['Chiodi', 0],
    ['Rete', 1],
    ['Sega', 1],
    ['Sigillante', 0],
    ['Pala', 1],
    ['Pinze', 0]
]
tChincaglierie = [
    ['Bottiglia', 1],
    ['Mazzo di carte', 0],
    ['Set di dadi', 0],
    ['Trucchi per il viso', 0],
    ['Gioielli falsi', 0], 
    ['Corno', 1],
    ['Incenso', 0],
    ['Strumento musicale', 1],
    ['Lente', 0],
    ['Biglie', 0],
    ['Specchietto', 0],
    ['Profumo', 0],
    ['Pennino e inchiostro', 0],
    ['Pacchetto di sale', 1],
    ['Campanella', 0],
    ['Sapone', 0],
    ['Spugna', 0],
    ['Vaso di pece', 1],
    ['Spago', 0],
    ['Fischietto', 0]
]
tIncantesimo = [
    'Adesione',
    'Affascinare',
    'Ancora',
    'Animare gli Spiriti',
    'Animare i Morti',
    'Animare Oggetto',
    'Antropomorfismo',
    'Aria Liquida',
    'Ascoltare i Sussurri',
    'Assordare',
    'Attrarre',
    'Avidità',
    'Bagliore',
    'Balzo',
    'Blaterare',
    'Boscaglia',
    'Bussare',
    'Camuffamento',
    'Comando',
    'Comprensione',
    'Confusione',
    'Congegno',
    'Cono di Schiuma',
    'Fermare il Tempo',
    'Controllare Piante',
    'Controllo Tempo Atmosferico',
    'Ipnotizzare',
    'Risalita',
    'Cura Ferite',
    'Lama Incantata',
    'Scambio',
    'Dislocare',
    'Legame Invisibile',
    'Scambio di Corpi',
    'Divinazione',
    'Leggere la Mente',
    'Sciame',
    'Elasticità',
    'Levitazione',
    'Scolpire Elementi',
    'Esca Bersaglio',
    'Mania delle Biglie',
    'Scudo',
    'Esca Fiore',
    'Maniero',
    'Sfera Notturna',
    'Evoca Cubo',
    'Marchio del Mago',
    'Sigillo',
    'Evoca Idolo',
    'Mascherata',
    'Smontare',
    'Fiuto',
    'Miniaturizzare',
    'Smorzatore Magico',
    'Fobia',
    'Movimento del Ragno',
    'Sonno',
    'Forma Bestiale',
    'Multibraccio',
    'Spegnimento',
    'Forma di Fumo',
    'Muro Elementale',
    'Spettacolo',
    'Forma Melmosa',
    'Nube di Nebbia',
    'Spingere/Tirare',
    'Fossa',
    'Occhio Arcano',
    'Telecinesi',
    'Frenesia',
    'Odio',
    'Telepatia',
    'Gazza',
    'Oggettivare',
    'Teletrasporto',
    'Identifica Proprietario',
    'Ordine',
    'Terremoto',
    'Illuminare',
    'Pacificare',
    'Tocco Gelido',
    'Illusione sonora',
    'Passaspecchi',
    'Velo',
    'Illusione visiva',
    'Percepire Oggetto',
    'Velocità',
    'Immagine Speculare',
    'Portale',
    'Viscido',
    'Impulso Primordiale',
    'Prigione Astrale',
    'Visione',
    'Individua il Magico',
    'Ragnatela',
    'Visione del Vero'
    'Inversione di Gravità',
    'Repulsione',
    'Vista a Raggi-X'
]
tArmatura = [
    ['Scudo (+1 Arm)', 1, 1],
    ['Elmo (+1 Arm)', 1, 1],
    ['Farsetto (1 Arm)', 1, 1],
    ['Brigantina (1 Arm, ingombrante)', 2, 1],
    ['Cotta di Maglia (2 Arm, ingombrante)', 2, 2],
    ['Corazza Piastre (3 Arm, ingombrante)', 2, 3]
]
tArmi = [
    ['Pugnale (d6 danno)', 0],
    ['Randello (d6 danno)', 1],
    ['Falcetto (d6 danno)', 1],
    ['Bastone (d6 danno)', 1],
    ['Lancia (d8 danno)', 1],
    ['Spada (d8 danno)', 1],
    ['Mazza (d8 danno)', 1],
    ['Ascia (d8 danno)', 1],
    ['Flagello (d8 danno)', 1],
    ['Alabarda (d10 danno)', 2],
    ['Martello da guerra (d10 danno)', 2],
    ['Spada lunga (d10 danno)', 2],
    ['Fionda (d4 danno)', 1],
    ['Arco (d6 danno)', 2],
    ['Balestra (d8 danno)', 2]
]

def tiraCaratteristica():
    lanci = []
    for i in range(4) :
        lanci.append(random.randrange(1,7))
    print (lanci)
    lanci.sort(reverse=True)
    print (lanci)
    return sum(lanci[0:3])

def creaPG():
    pg = {}
    if (random.random() < .5) :
        pg['Nome'] = random.choice(tNomeM) + ' ' + random.choice(tCognome) + ' \u2642'
    else:
        pg['Nome'] = random.choice(tNomeF) + ' ' + random.choice(tCognome) + ' \u2640'

    pg['Note']  = 'Background: ' + random.choice(tBackground) + '\n'
    pg['Note'] += 'Fisico: ' + random.choice(tFisico) + '\n'
    pg['Note'] += 'Pelle: ' + random.choice(tPelle) + '\n'
    pg['Note'] += 'Capelli: ' + random.choice(tCapelli) + '\n'
    pg['Note'] += 'Faccia: ' + random.choice(tFaccia) + '\n'
    pg['Note'] += 'Parlata: ' + random.choice(tParlata) + '\n'
    pg['Note'] += 'Vestito: ' + random.choice(tVestito) + '\n'
    pg['Note'] += 'Virtù: ' + random.choice(tVirtu) + '\n'
    pg['Note'] += 'Vizio: ' + random.choice(tVizio) + '\n'
    pg['Note'] += 'Reputazione: ' + random.choice(tReputazione) + '\n'
    pg['Note'] += 'Sfortune: ' + random.choice(tSfortune) + '\n'
    pg['Note'] += 'Età: ' + str(random.randrange(1,20) + random.randrange(1,20) + 10) + '\n'

    pg['FOR'] = tiraCaratteristica()
    pg['DES'] = tiraCaratteristica()
    pg['VOL'] = tiraCaratteristica()

    pg['PF'] = 6
    pg['Arm'] = 0
    pg['PO'] = tiraCaratteristica()

    pg['Slot1'] = '3gg razioni'
    pg['Slot2'] = 'Torcia'

    match random.randrange(1,21) :
        #case 1 | 2 | 3:
        #    # Nothing
        case 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 :
            pg['Slot3'] = 'Brigantina (+1 Arm, ingombrante)'
            pg['Arm'] += 1
        case 15 | 16 | 17 | 18 | 19 :
            pg["Slot3"] = 'Cotta di maglia (+2 Arm, ingombrante)'
            pg['Arm'] += 2
        case 20 :
            pg['Slot3'] = 'Corazza Piastre (+3 Arm, ingombrante)'

    match random.randrange(1,21) :
        case 14 | 15 | 16 :
            pg['Slot4'] = 'Elmo (+1 Arm)'
            pg['Arm'] += 1
        case 17 | 18 | 19 :
            pg["Slot4"] = 'Scudo (+1 Arm)'
            pg['Arm'] += 1
        case 20 :
            pg['Slot4'] = 'Elmo (+1 Arm)'
            pg['Slot5'] = 'Scudo (+1 Arm)'
            pg['Arm'] += 2

    match random.randrange(1,21) :
        case 1 | 2 | 3 | 4 | 5 :
            pg['Slot6'] = 'Pugnale (d6 danno)'
        case 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 :
            pg["Slot6"] = 'Spada (d8 danno)'
        case 15 | 16 | 17 | 18 | 19 :
            pg['Slot6'] = 'Balestra (d8 danno)'
        case 20 : 
            pg['Slot6'] = 'Martello da Guerra (d10 danno)'

    pg['Slot7'] = random.choice(tEquipaggiamento)[0]
    pg['Slot8'] = random.choice(tAttrezzi)[0]
    pg['Slot9'] = random.choice(tChincaglierie)[0]

    match random.randrange(1,21) :
        case 1 | 2 | 3 | 4 | 5 :
            if (random.random() < .5) :
                pg['Slot10'] = random.choice(tAttrezzi)[0]
            else :
                pg['Slot10'] = random.choice(tChincaglierie)[0]
        case 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 :
            pg['Slot10'] = random.choice(tEquipaggiamento)[0]
        case 14 | 15 | 16 | 17 :
            if (random.random() < .5) :
                pg['Slot10'] = random.choice(tArmatura)[0]
            else :
                pg['Slot10'] = random.choice(tArmi)[0]
        case 18 | 19 | 20 :
            pg['Slot10'] = 'Inc: ' + random.choice(tIncantesimo)
    print (pg)
    return (pg)

outdata = []
for x in range(30) :
    outdata.append(creaPG())

f = open('pg-generati.csv', 'w')
writer = csv.DictWriter(f, fieldnames=fieldnames)
writer.writeheader()
writer.writerows(outdata)

f.close