import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from core.models import Era, Lider, Victoria, Tag, Estadistica

# Limpiar datos previos
Era.objects.all().delete()

# ── ERA I ──
e1 = Era.objects.create(
    numero=1,
    periodo="2008 — 2011",
    titulo="Era Antigua",
    titulo_dorado="Antigua",
    tagline="El origen de una promesa que se volvería leyenda",
    texto="""Fundada en el año 2008 por XxRubio-tqxX (AlfonsoCaponne), la famiglia nació como una promesa dentro de la comunidad, creciendo bajo múltiples nombres que con el tiempo se volverían símbolo de respeto: AlCapone Gangsters House, Chicago Mafia, AlCapone Old House y AlCapone Hawks, junto a franquicias como Chicago Outfit, Capone Syndicate y Capone Family.

Desde sus primeros pasos, la organización destacó por su disciplina, constancia y capacidad de formar generaciones leales. No era una familia común; era una escuela de mafiosos honorables.

Durante el año 2009, bajo el liderazgo del fundador y con Roman. como hombre de guerra, la famiglia protagonizó una etapa gloriosa, derrotando rápidamente a múltiples organizaciones enemigas.

En 2010 llegó un periodo de silencio estratégico. Y en 2011, Alfonso cedió el mando a Miguel, quien mantuvo la llama viva en medio de una crisis que pondría a prueba el verdadero espíritu de la casa."""
)
Lider.objects.create(era=e1, avatar="AC", nombre="XxRubio-tqxX · AlfonsoCaponne", rol="Fundador & Don Supremo", orden=1)
Lider.objects.create(era=e1, avatar="R.", nombre="Roman.", rol="Hombre de Guerra · 2009", orden=2)
Lider.objects.create(era=e1, avatar="MG", nombre="Miguel", rol="Don · 2011", orden=3)
Victoria.objects.create(era=e1, nombre="Salvatore", orden=1)
Victoria.objects.create(era=e1, nombre="Berdasco", orden=2)
Victoria.objects.create(era=e1, nombre="Cassano", orden=3)
Victoria.objects.create(era=e1, nombre="Moretti", orden=4)
Victoria.objects.create(era=e1, nombre="Leggio", orden=5)
Tag.objects.create(era=e1, nombre="AlCapone Gangsters House")
Tag.objects.create(era=e1, nombre="Chicago Mafia")
Tag.objects.create(era=e1, nombre="AlCapone Old House")
Tag.objects.create(era=e1, nombre="AlCapone Hawks")
Tag.objects.create(era=e1, nombre="Chicago Outfit")
Tag.objects.create(era=e1, nombre="Capone Syndicate")

# ── ERA II ──
e2 = Era.objects.create(
    numero=2,
    periodo="2012",
    titulo="Era de Oro",
    titulo_dorado="de Oro",
    tagline="La revolución que desafió al mundillo entero — y lo conquistó",
    texto="""Cuando parecía que el apellido AlCapone debía reinventarse, el destino colocó el legado en manos de dos nombres que marcarían la historia para siempre.

Bajo su mando nació el A.R.M — AlCapone Revolutionary Movement — una revolución que desafió al mundillo entero. Contra toda expectativa, la famiglia declaró guerra global prometiendo derrotar a todas las organizaciones existentes.

Y lo logró.

En apenas semanas, AlCapone arrasó con doce organizaciones en una hazaña histórica que consolidó a la famiglia como una de las fuerzas más dominantes jamás vistas."""
)
Lider.objects.create(era=e2, avatar="JP", nombre=".peligr0 · JosephCapone.", rol="Joseph.Pascale — Guerrero & Co-Fundador", orden=1)
Lider.objects.create(era=e2, avatar="FC", nombre="george982 · F.Cassetti", rol="Don.Rimelio — Estratega & Co-Fundador", orden=2)
for i, v in enumerate(["Salvatore","Ravinlli","Capriotti","Colombo","Casteglia","Leone","Mancini","Bonachesse","Pentangeli","Gambetta","Gianetti","Bonetto"], 1):
    Victoria.objects.create(era=e2, nombre=v, orden=i)
Estadistica.objects.create(era=e2, numero="12", label="Organizaciones caídas", orden=1)
Estadistica.objects.create(era=e2, numero="1", label="Año, un solo año", orden=2)
Estadistica.objects.create(era=e2, numero="A.R.M", label="El movimiento", orden=3)
Estadistica.objects.create(era=e2, numero="∞", label="Legado", orden=4)

# ── ERA III ──
e3 = Era.objects.create(
    numero=3,
    periodo="2013 — 2015",
    titulo="La Resistencia del A.R.M",
    titulo_dorado="A.R.M",
    tagline="La gloria trae enemigos… y AlCapone aprendió a resistir",
    texto="""Tras la guerra global, comenzaron las conspiraciones, las difamaciones y el abandono de algunos miembros. Pero lejos de caer, surgió una nueva generación forjada en la adversidad.

En 2013 se reorganizaron ofensivas estratégicas contra Foresta, Ravinlli y Musso, dirigidas por Sir.Nostra y Sr.BradC.

Para 2014, la famiglia se convirtió en una organización de inteligencia y guerra pura. Fue entonces cuando F.Cassetti junto a Sr-Aldair ejecutaron una histórica pettada contra Corleone — una famiglia considerada intocable desde los tiempos de PanchoCorleone.

El 2015 marcó una pausa necesaria. La organización exploró una nueva etapa orientada a estrategias económicas, culminando el año con una segunda caída de Bonetto."""
)
Lider.objects.create(era=e3, avatar="FC", nombre="F.Cassetti", rol="Don — Estratega Principal", orden=1)
Lider.objects.create(era=e3, avatar="SN", nombre="Sir.Nostra", rol="Comandante de Guerra · 2013", orden=2)
Lider.objects.create(era=e3, avatar="BC", nombre="Sr.BradC", rol="Comandante de Guerra · 2013", orden=3)
Lider.objects.create(era=e3, avatar="AL", nombre="Sr-Aldair", rol="Operativo Élite · 2014", orden=4)
Lider.objects.create(era=e3, avatar="IC", nombre="ICaponne", rol="Liderazgo estratégico · 2015", orden=5)
for i, v in enumerate(["Foresta — 2013","Ravinlli (2ª caída) — 2013","Musso — 2013","Corleone (pettada histórica) — 2014","Saglieri — 2015","Rosatto — 2015","Bonetto (2ª caída) — 2015"], 1):
    Victoria.objects.create(era=e3, nombre=v, orden=i)

# ── ERA IV ──
e4 = Era.objects.create(
    numero=4,
    periodo="2016 — 2020",
    titulo="La Nueva Era",
    titulo_dorado="Nueva Era",
    tagline="Formar sangre nueva — de guerreros a maestros",
    texto="""El 10 de octubre de 2016, AlCapone regresó con una visión distinta: formar sangre nueva. Bajo la dirección de sus líderes históricos, la famiglia dejó atrás la guerra constante para convertirse en una escuela de generaciones.

Durante 2017 y 2018, la organización alcanzó su mayor nivel de estructura y formación interna. Los veteranos comenzaron a apadrinar a miembros desde cero, creando líderes que crecerían hasta convertirse en verdaderos Dones.

La famiglia fue reconocida en múltiples ocasiones como una de las más organizadas y respetadas del mundillo, consolidando su legado no solo en batalla, sino en formación.

Nacieron departamentos que darían forma a la estructura moderna de la famiglia, sentando las bases para la generación que vendría."""
)
Victoria.objects.create(era=e4, nombre="Lifeblood Hoodlums", orden=1)
Victoria.objects.create(era=e4, nombre="Charter Roughnecks", orden=2)

# ── ERA V ──
e5 = Era.objects.create(
    numero=5,
    periodo="2021 — 2023",
    titulo="Renacimiento",
    titulo_dorado="Renacimiento",
    tagline="Los tiempos difíciles forjan líderes inolvidables",
    texto="""En mayo de 2021 surgió una nueva generación encabezada por la primera Donna en la Comisión General: -Lovegood- (HelenaCapone), junto a JulianCapone y Tope@francisco@ (FranciscoCapone).

A ellos se unieron veteranos como lCordova., Alex.Capone y el mítico Pressidente (Rogen!!).

Aunque el mundillo dudaba y antiguos enemigos se burlaban, la famiglia respondió con hechos. Siempre con hechos.

El primer gran golpe cayó sobre Galeano, orquestado por Alex.Capone, -Lovegood- y Tope@francisco@. Poco después, junto a Vivacamilo10, ejecutaron una ofensiva histórica contra Corleone Old House. Finalmente, JulianCapone y Yamii! lideraron la caída definitiva de Vitelli, sellando una nueva era de poder."""
)
Lider.objects.create(era=e5, avatar="HC", nombre="-Lovegood- · HelenaCapone", rol="Primera Donna — Comisión General", orden=1)
Lider.objects.create(era=e5, avatar="JC", nombre="JulianCapone", rol="Liderazgo ofensivo", orden=2)
Lider.objects.create(era=e5, avatar="FC", nombre="Tope@francisco@ · FranciscoCapone", rol="Comisión General", orden=3)
Lider.objects.create(era=e5, avatar="AC", nombre="Alex.Capone", rol="Veterano — Operaciones", orden=4)
Lider.objects.create(era=e5, avatar="PR", nombre="Pressidente · Rogen!!", rol="Veterano Mítico", orden=5)
for i, v in enumerate(["Galeano — Alex.Capone, -Lovegood-, FranciscoCapone","Corleone Old House — con Vivacamilo10","Vitelli — JulianCapone & Yamii!"], 1):
    Victoria.objects.create(era=e5, nombre=v, orden=i)

print("✅ Datos cargados correctamente")