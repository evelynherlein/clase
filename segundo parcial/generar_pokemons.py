import json
import random
from pathlib import Path

#tabla de tipos
# atacante -> (super efectivo contra, poco efectivo contra, sin efecto contra)
TABLA_TIPOS = {
    "Normal":    ([], ["Roca", "Acero"], ["Fantasma"]),
    "Fuego":     (["Planta", "Hielo", "Bicho", "Acero"], ["Fuego", "Agua", "Roca", "Dragón"], []),
    "Agua":      (["Fuego", "Tierra", "Roca"], ["Agua", "Planta", "Dragón"], []),
    "Eléctrico": (["Agua", "Volador"], ["Eléctrico", "Planta", "Dragón"], ["Tierra"]),
    "Planta":    (["Agua", "Tierra", "Roca"], ["Fuego", "Planta", "Veneno", "Volador", "Bicho", "Dragón", "Acero"], []),
    "Hielo":     (["Planta", "Tierra", "Volador", "Dragón"], ["Fuego", "Agua", "Hielo", "Acero"], []),
    "Lucha":     (["Normal", "Hielo", "Roca", "Siniestro", "Acero"], ["Veneno", "Volador", "Psíquico", "Bicho", "Hada"], ["Fantasma"]),
    "Veneno":    (["Planta", "Hada"], ["Veneno", "Tierra", "Roca", "Fantasma"], ["Acero"]),
    "Tierra":    (["Fuego", "Eléctrico", "Veneno", "Roca", "Acero"], ["Planta", "Bicho"], ["Volador"]),
    "Volador":   (["Planta", "Lucha", "Bicho"], ["Eléctrico", "Roca", "Acero"], []),
    "Psíquico":  (["Lucha", "Veneno"], ["Psíquico", "Acero"], ["Siniestro"]),
    "Bicho":     (["Planta", "Psíquico", "Siniestro"], ["Fuego", "Lucha", "Veneno", "Volador", "Fantasma", "Acero", "Hada"], []),
    "Roca":      (["Fuego", "Hielo", "Volador", "Bicho"], ["Lucha", "Tierra", "Acero"], []),
    "Fantasma":  (["Psíquico", "Fantasma"], ["Siniestro"], ["Normal"]),
    "Dragón":    (["Dragón"], ["Acero"], ["Hada"]),
    "Siniestro": (["Psíquico", "Fantasma"], ["Lucha", "Siniestro", "Hada"], []),
    "Acero":     (["Hielo", "Roca", "Hada"], ["Fuego", "Agua", "Eléctrico", "Acero"], []),
    "Hada":      (["Lucha", "Dragón", "Siniestro"], ["Fuego", "Veneno", "Acero"], []),
}


def debilidades(tipos):
    """Tipos atacantes cuyo multiplicador total contra `tipos` es mayor a x1."""
    resultado = []
    for atacante, (fuerte, _debil, _inmune) in TABLA_TIPOS.items():
        mult = 1.0
        for defensor in tipos:
            _f, poco, nada = TABLA_TIPOS[atacante]
            if defensor in fuerte:
                mult *= 2
            elif defensor in poco:
                mult *= 0.5
            elif defensor in nada:
                mult *= 0
        if mult > 1:
            resultado.append(atacante)
    return resultado


# datos
# numero|nombre|tipo1/tipo2
TABLA = """
1|Bulbasaur|Planta/Veneno
2|Ivysaur|Planta/Veneno
3|Venusaur|Planta/Veneno
4|Charmander|Fuego
5|Charmeleon|Fuego
6|Charizard|Fuego/Volador
7|Squirtle|Agua
8|Wartortle|Agua
9|Blastoise|Agua
10|Caterpie|Bicho
11|Metapod|Bicho
12|Butterfree|Bicho/Volador
13|Weedle|Bicho/Veneno
14|Kakuna|Bicho/Veneno
15|Beedrill|Bicho/Veneno
16|Pidgey|Normal/Volador
17|Pidgeotto|Normal/Volador
18|Pidgeot|Normal/Volador
19|Rattata|Normal
20|Raticate|Normal
21|Spearow|Normal/Volador
22|Fearow|Normal/Volador
23|Ekans|Veneno
24|Arbok|Veneno
25|Pikachu|Eléctrico
26|Raichu|Eléctrico
27|Sandshrew|Tierra
28|Sandslash|Tierra
29|Nidoran♀|Veneno
30|Nidorina|Veneno
31|Nidoqueen|Veneno/Tierra
32|Nidoran♂|Veneno
33|Nidorino|Veneno
34|Nidoking|Veneno/Tierra
35|Clefairy|Hada
36|Clefable|Hada
37|Vulpix|Fuego
38|Ninetales|Fuego
39|Jigglypuff|Normal/Hada
40|Wigglytuff|Normal/Hada
41|Zubat|Veneno/Volador
42|Golbat|Veneno/Volador
43|Oddish|Planta/Veneno
44|Gloom|Planta/Veneno
45|Vileplume|Planta/Veneno
46|Paras|Bicho/Planta
47|Parasect|Bicho/Planta
48|Venonat|Bicho/Veneno
49|Venomoth|Bicho/Veneno
50|Diglett|Tierra
51|Dugtrio|Tierra
52|Meowth|Normal
53|Persian|Normal
54|Psyduck|Agua
55|Golduck|Agua
56|Mankey|Lucha
57|Primeape|Lucha
58|Growlithe|Fuego
59|Arcanine|Fuego
60|Poliwag|Agua
61|Poliwhirl|Agua
62|Poliwrath|Agua/Lucha
63|Abra|Psíquico
64|Kadabra|Psíquico
65|Alakazam|Psíquico
66|Machop|Lucha
67|Machoke|Lucha
68|Machamp|Lucha
69|Bellsprout|Planta/Veneno
70|Weepinbell|Planta/Veneno
71|Victreebel|Planta/Veneno
72|Tentacool|Agua/Veneno
73|Tentacruel|Agua/Veneno
74|Geodude|Roca/Tierra
75|Graveler|Roca/Tierra
76|Golem|Roca/Tierra
77|Ponyta|Fuego
78|Rapidash|Fuego
79|Slowpoke|Agua/Psíquico
80|Slowbro|Agua/Psíquico
81|Magnemite|Eléctrico/Acero
82|Magneton|Eléctrico/Acero
83|Farfetch'd|Normal/Volador
84|Doduo|Normal/Volador
85|Dodrio|Normal/Volador
86|Seel|Agua
87|Dewgong|Agua/Hielo
88|Grimer|Veneno
89|Muk|Veneno
90|Shellder|Agua
91|Cloyster|Agua/Hielo
92|Gastly|Fantasma/Veneno
93|Haunter|Fantasma/Veneno
94|Gengar|Fantasma/Veneno
95|Onix|Roca/Tierra
96|Drowzee|Psíquico
97|Hypno|Psíquico
98|Krabby|Agua
99|Kingler|Agua
100|Voltorb|Eléctrico
101|Electrode|Eléctrico
102|Exeggcute|Planta/Psíquico
103|Exeggutor|Planta/Psíquico
104|Cubone|Tierra
105|Marowak|Tierra
106|Hitmonlee|Lucha
107|Hitmonchan|Lucha
108|Lickitung|Normal
109|Koffing|Veneno
110|Weezing|Veneno
111|Rhyhorn|Tierra/Roca
112|Rhydon|Tierra/Roca
113|Chansey|Normal
114|Tangela|Planta
115|Kangaskhan|Normal
116|Horsea|Agua
117|Seadra|Agua
118|Goldeen|Agua
119|Seaking|Agua
120|Staryu|Agua
121|Starmie|Agua/Psíquico
122|Mr. Mime|Psíquico/Hada
123|Scyther|Bicho/Volador
124|Jynx|Hielo/Psíquico
125|Electabuzz|Eléctrico
126|Magmar|Fuego
127|Pinsir|Bicho
128|Tauros|Normal
129|Magikarp|Agua
130|Gyarados|Agua/Volador
131|Lapras|Agua/Hielo
132|Ditto|Normal
133|Eevee|Normal
134|Vaporeon|Agua
135|Jolteon|Eléctrico
136|Flareon|Fuego
137|Porygon|Normal
138|Omanyte|Roca/Agua
139|Omastar|Roca/Agua
140|Kabuto|Roca/Agua
141|Kabutops|Roca/Agua
142|Aerodactyl|Roca/Volador
143|Snorlax|Normal
144|Articuno|Hielo/Volador
145|Zapdos|Eléctrico/Volador
146|Moltres|Fuego/Volador
147|Dratini|Dragón
148|Dragonair|Dragón
149|Dragonite|Dragón/Volador
150|Mewtwo|Psíquico
151|Mew|Psíquico
152|Chikorita|Planta
155|Cyndaquil|Fuego
158|Totodile|Agua
172|Pichu|Eléctrico
175|Togepi|Hada
179|Mareep|Eléctrico
181|Ampharos|Eléctrico
196|Espeon|Psíquico
197|Umbreon|Siniestro
208|Steelix|Acero/Tierra
212|Scizor|Bicho/Acero
214|Heracross|Bicho/Lucha
215|Sneasel|Siniestro/Hielo
229|Houndoom|Siniestro/Fuego
246|Larvitar|Roca/Tierra
248|Tyranitar|Roca/Siniestro
249|Lugia|Psíquico/Volador
250|Ho-Oh|Fuego/Volador
251|Celebi|Psíquico/Planta
252|Treecko|Planta
254|Sceptile|Planta
255|Torchic|Fuego
257|Blaziken|Fuego/Lucha
258|Mudkip|Agua
260|Swampert|Agua/Tierra
282|Gardevoir|Psíquico/Hada
302|Sableye|Siniestro/Fantasma
303|Mawile|Acero/Hada
306|Aggron|Acero/Roca
308|Medicham|Lucha/Psíquico
310|Manectric|Eléctrico
319|Sharpedo|Agua/Siniestro
323|Camerupt|Fuego/Tierra
334|Altaria|Dragón/Volador
354|Banette|Fantasma
359|Absol|Siniestro
362|Glalie|Hielo
373|Salamence|Dragón/Volador
376|Metagross|Acero/Psíquico
380|Latias|Dragón/Psíquico
381|Latios|Dragón/Psíquico
382|Kyogre|Agua
383|Groudon|Tierra
384|Rayquaza|Dragón/Volador
389|Torterra|Planta/Tierra
392|Infernape|Fuego/Lucha
395|Empoleon|Agua/Acero
405|Luxray|Eléctrico
428|Lopunny|Normal
445|Garchomp|Dragón/Tierra
448|Lucario|Lucha/Acero
460|Abomasnow|Planta/Hielo
470|Leafeon|Planta
471|Glaceon|Hielo
475|Gallade|Psíquico/Lucha
479|Rotom|Eléctrico/Fantasma
483|Dialga|Acero/Dragón
484|Palkia|Agua/Dragón
487|Giratina|Fantasma/Dragón
497|Serperior|Planta
500|Emboar|Fuego/Lucha
503|Samurott|Agua
530|Excadrill|Tierra/Acero
531|Audino|Normal
534|Conkeldurr|Lucha
569|Garbodor|Veneno
571|Zoroark|Siniestro
596|Galvantula|Bicho/Eléctrico
604|Eelektross|Eléctrico
609|Chandelure|Fantasma/Fuego
612|Haxorus|Dragón
635|Hydreigon|Siniestro/Dragón
637|Volcarona|Bicho/Fuego
643|Reshiram|Dragón/Fuego
644|Zekrom|Dragón/Eléctrico
652|Chesnaught|Planta/Lucha
655|Delphox|Fuego/Psíquico
658|Greninja|Agua/Siniestro
663|Talonflame|Fuego/Volador
675|Pangoro|Lucha/Siniestro
681|Aegislash|Acero/Fantasma
695|Heliolisk|Eléctrico/Normal
697|Tyrantrum|Roca/Dragón
699|Aurorus|Roca/Hielo
700|Sylveon|Hada
702|Dedenne|Eléctrico/Hada
706|Goodra|Dragón
715|Noivern|Volador/Dragón
716|Xerneas|Hada
717|Yveltal|Siniestro/Volador
719|Diancie|Roca/Hada
724|Decidueye|Planta/Fantasma
727|Incineroar|Fuego/Siniestro
730|Primarina|Agua/Hada
745|Lycanroc|Roca
748|Toxapex|Veneno/Agua
758|Salazzle|Veneno/Fuego
760|Bewear|Normal/Lucha
778|Mimikyu|Fantasma/Hada
784|Kommo-o|Dragón/Lucha
785|Tapu Koko|Eléctrico/Hada
791|Solgaleo|Psíquico/Acero
792|Lunala|Psíquico/Fantasma
809|Melmetal|Acero
812|Rillaboom|Planta
815|Cinderace|Fuego
818|Inteleon|Agua
823|Corviknight|Volador/Acero
826|Orbeetle|Bicho/Psíquico
834|Drednaw|Agua/Roca
839|Coalossal|Roca/Fuego
841|Flapple|Planta/Dragón
842|Appletun|Planta/Dragón
844|Sandaconda|Tierra
849|Toxtricity|Eléctrico/Veneno
851|Centiskorch|Fuego/Bicho
858|Hatterene|Psíquico/Hada
861|Grimmsnarl|Siniestro/Hada
869|Alcremie|Hada
879|Copperajah|Acero
884|Duraludon|Acero/Dragón
887|Dragapult|Dragón/Fantasma
888|Zacian|Hada
889|Zamazenta|Lucha
892|Urshifu|Lucha/Siniestro
906|Sprigatito|Planta
908|Meowscarada|Planta/Siniestro
909|Fuecoco|Fuego
911|Skeledirge|Fuego/Fantasma
912|Quaxly|Agua
914|Quaquaval|Agua/Lucha
923|Pawmot|Eléctrico/Lucha
936|Armarouge|Fuego/Psíquico
937|Ceruledge|Fuego/Fantasma
959|Tinkaton|Hada/Acero
979|Annihilape|Lucha/Fantasma
983|Kingambit|Siniestro/Acero
1000|Gholdengo|Acero/Fantasma
1005|Roaring Moon|Dragón/Siniestro
1006|Iron Valiant|Hada/Lucha
1007|Koraidon|Lucha/Dragón
1008|Miraidon|Eléctrico/Dragón
1025|Pecharunt|Veneno/Fantasma
"""

# Megaevoluciones clásicas (XY / ORAS / Sol y Luna), por número de Pokédex.
MEGA = {
    3, 6, 9, 15, 18, 65, 80, 94, 115, 127, 130, 142, 150, 181, 208, 212, 214,
    229, 248, 254, 257, 260, 282, 302, 303, 306, 308, 310, 319, 323, 334, 354,
    359, 362, 373, 376, 380, 381, 384, 428, 445, 448, 460, 475, 531, 719,
}

# Formas Gigamax (Espada y Escudo).
GIGAMAX = {
    3, 6, 9, 12, 25, 52, 68, 94, 99, 131, 133, 143, 569, 809, 812, 815, 818,
    823, 826, 834, 839, 841, 842, 844, 849, 851, 858, 861, 869, 879, 884, 892,
}


def construir():
    pokemons = []
    for linea in TABLA.strip().splitlines():
        numero, nombre, tipos = linea.split("|")
        numero = int(numero)
        tipos = tipos.split("/")
        pokemons.append({
            "nombre": nombre,
            "numero": numero,
            "tipos": tipos,
            "debilidades": debilidades(tipos),
            "mega_evolucion": numero in MEGA,
            "gigamax": numero in GIGAMAX,
        })
    random.Random(2026).shuffle(pokemons)  # carga "aleatoria", pero reproducible
    return pokemons


if __name__ == "__main__":
    datos = construir()
    destino = Path(__file__).with_name("pokemons.json")
    destino.write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{len(datos)} Pokémon escritos en {destino.name}")
