import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Conquista

Conquista.objects.all().delete()

conquistas = [
    (2022, 'Mitelli', 'toxictrippin', 'Persuasión'),
    (2021, 'Vitelli', 'Yami · JulianCapone', 'Persuasión'),
    (2021, 'Stalino', 'Jordan999! · -NestorC', 'Persuasión'),
    (2021, 'Corleone Old House', 'Vivacamilo10', 'Persuasión'),
    (2021, 'Galeano / N.O.S', 'Alex.Capone · -Lovegood- · Tope@francisco@', 'Persuasión'),
    (2020, 'Cosa Nostra', 'Alex.Capone · LuisStrazzio · F.Cassetti · JosephCapone', 'Persuasión'),
    (2018, 'Calderone', 'AlbertoCapone', 'Persuasión'),
    (2018, 'Savianno', 'Alex.Capone', 'Persuasión'),
    (2018, 'Varone', 'AlbertoCapone', 'Persuasión'),
    (2018, 'Valacchi', 'AlbertoCapone', 'Persuasión'),
    (2018, 'Valacchi', 'FedericoCapone', 'Infiltración'),
    (2018, 'Giordano', 'Zenit', 'Infiltración'),
    (2018, 'Marsellesa', 'AlbertoCapone · Alex.Capone', 'Persuasión'),
    (2018, 'Milifiore', 'Zennin', 'Infiltración'),
    (2018, 'Rossellini', 'AlbertoCapone', 'Persuasión'),
    (2018, 'Rizzo', 'AlbertoCapone · Alex.Capone', 'Persuasión'),
    (2018, 'Strada', 'AlbertoCapone', 'Persuasión'),
    (2018, 'Carminati', 'AlbertoCapone', 'Persuasión'),
    (2015, 'Bonetto', 'F.Cassetti', 'Infiltración'),
    (2014, 'Saglieri', 'F.Cassetti', 'Persuasión'),
    (2014, 'Corleone Old House', 'F.Cassetti', 'Engaño'),
    (2014, 'Rosatto', 'F.Cassetti', 'Persuasión'),
    (2013, 'Musso', 'F.Cassetti', 'Infiltración'),
    (2013, 'Ravinlli', 'JosephCapone', 'Persuasión'),
    (2013, 'Foresta', 'F.Cassetti · JosephCapone', 'Oferta monetaria'),
    (2012, 'Bonetto', 'F.Cassetti · JosephCapone', 'Persuasión'),
    (2012, 'Ravinlli', 'JosephCapone', 'Persuasión'),
    (2012, 'Capriotti', '@X.christian.X@', 'Infiltración'),
    (2012, 'Salvatore', 'george982 (F.Cassetti) · JosephCapone.', 'Persuasión'),
    (2012, 'Mancini', 'F.Cassetti', 'Infiltración'),
    (2012, 'Colombo', 'JosephCapone', 'Persuasión'),
    (2012, 'Leone', 'JosephCapone', 'Persuasión'),
    (2012, 'Casteglia', 'Juanqui96', 'Infiltración'),
    (2012, 'Pentangeli', 'Ivanoxo', 'Trampa'),
    (2012, 'Bonachesse', 'SoyAlberto13', 'Infiltración'),
    (2012, 'Bonachesse', 'JosephCapone', 'Persuasión'),
    (2012, 'Gambetta', 'JosephCapone', 'Persuasión'),
    (2012, 'Gianetti', 'JosephCapone', 'Persuasión'),
    (2010, 'Gabanelli', '.lRoman.', 'Persuasión'),
    (2009, 'Salvatore', '.lRoman.', 'Persuasión'),
    (2009, 'Berdasco', '.lRoman.', 'Persuasión'),
    (2009, 'Leggio', '.lRoman.', 'Persuasión'),
    (2009, 'Moretti', '.lRoman.', 'Persuasión'),
    (2009, 'Cassano', '.lRoman.', 'Persuasión'),
    (2008, 'Blazzeti', '.lRoman.', 'Persuasión'),
]

for anio, org, guerreros, metodo in conquistas:
    Conquista.objects.create(anio=anio, organizacion=org, guerreros=guerreros, metodo=metodo)

print(f'✅ {len(conquistas)} conquistas cargadas correctamente')