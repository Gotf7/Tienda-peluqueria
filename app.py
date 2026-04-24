from flask import Flask, render_template, abort

app = Flask(__name__)

# Definición de Colecciones (Las portadas principales)
colecciones = [
    {
        "id": "Skala-Experto", 
        "nombre": "LÍNEA SKALA EXPERTO", 
        "img": "ColecciónSkala.png", 
        "desc": "Tratamientos intensivos brasileños para cada tipo de hebra."
    },
    {
        "id": "Linea-Oro-Revitalizante", 
        "nombre": "LÍNEA DE ORO PROFESSIONAL", 
        "img": "Colección Nazca Origem.png", 
        "desc": "Nutrición extrema y reparación profunda para cabellos procesados."
        "img": "Colección Nevada _Nazca Origem-1kg.jpg", 
        "desc": "Mantenimiento esencial para un cabello radiante todos los días."
    },
    {
      "id":"Crema-Desrizadora-o-Alisadora",
    "nombre": "Nevada Super Crema No-Lye Relaxer",
    "img":"Derriz Nevada.jpg",
    "desc":"""Nevada Super Crema No-Lye Relaxer, un kit de desrizado o alisado, para el cabello en dos pasos enriquecido con vitamina E. Está diseñado para transformar cabellos rizados o crespos en melenas lisas y manejables directamente en casa. 

Detalles del producto
Contenido del kit: Incluye dos sobres numerados: el Paso 1 (Activator Cream) y el Paso 2 (Relaxer Cream).

Fórmula: Es una fórmula sin lejía (no-lye), lo que suele ser más suave para el cuero cabelludo que los desrizadores tradicionales. Contiene vitamina E para nutrir y acondicionar el cabello durante el proceso.

Beneficios: Promete un alisado de larga duración, aportando brillo y suavidad."""
    },
]

# Base de datos detallada de Productos
productos = [
    # --- COLECCIÓN SKALA EXPERTO ---
    {"id": 1, "col_id": "skala-experto", "nombre": "Skala Moranco", "precio": "$3500 CUP", "img": "Skala Moranco.jpg", "detalle": """Skala Frutástica Morango (1kg)

Crema vegana 3 en 1 (acondicionador, mascarilla o finalizador) a base de fresa y aceite de oliva.

​Objetivo: Nutrir profundamente, eliminar el frizz y dar brillo intenso.

​Ideal para: Cabello seco, opaco y rebelde.

​Fórmula: Limpia (sin sulfatos, parabenos ni siliconas), apta para Low Poo.

​En resumen: Nutrición frutal masiva para devolverle la vida a tu pelo con un solo producto."""},

    {"id": 2, "col_id": "skala-experto", "nombre": "Skala Melancia", "precio": "$3500 CUP", "img": "Skala Melancia.jpg", "detalle": """Skala Frutástica Melancia (1kg)

Crema vegana de Nutrición que ofrece ultra definición por 72 horas para cabellos rizados, crespos o secos.

​Ingredientes: Aceites de sandía y argán + Vitaminas A y C.

​Efecto: Repone lípidos, elimina el frizz y fortalece la fibra.

​Usos: Mascarilla (con enjuague), crema de peinar (sin enjuague) o co-wash.

​Fórmula: 100% limpia (sin siliconas ni parabenos).

​En resumen: Nutrición profunda y rizos definidos por días en un solo pote."""},

    {"id": 3, "col_id": "skala-experto", "nombre": "Skala Maracujá", "precio": "$3500 CUP", "img": "Skala Maracujá.jpg", "detalle": """Skala Maracuyá y Patauá (1kg)

Crema vegana enfocada en nutrición, fuerza y crecimiento.

​Objetivo: Fortalecer la hebra y acelerar el crecimiento del cabello débil o estancado.

​Ingrediente clave: Aceite de Patauá (aporta lípidos y vitalidad).

​Versatilidad: Funciona como mascarilla, crema de peinar, co-wash o pre-shampoo.

​Fórmula: 100% limpia (sin sulfatos, siliconas ni parabenos).

​En resumen: Nutrición amazónica para rescatar cabellos débiles y estimular su largo."""},

    {"id": 4, "col_id": "skala-experto", "nombre": "Skala Coquetel de Frutas", "precio": "$3500 CUP", "img": "Skala Coquetel de Frutas.jpg", "detalle": """Skala Coquetel de Frutas (1kg)

Crema multifuncional 2 en 1 diseñada para la hidratación y suavidad diaria de todo tipo de cabello, incluyendo el de los niños.

​Ingredientes clave: Agua de coco, piña (vitaminas A, B y C) y mora.

​Beneficios: Ultra desenredante (sin tirones), elimina el frizz y devuelve el brillo al cabello opaco.

​Versatilidad: Úsala como acondicionador, mascarilla, crema de peinar, co-wash o pre-poo.

​Fórmula: 100% vegana y liberada (sin sulfatos, siliconas ni parabenos).

​En resumen: La solución familiar ideal para un cabello hidratado, brillante y fácil de peinar."""},

    {"id": 5, "col_id": "skala-experto", "nombre": "Skala Coconut", "precio": "$3500 CUP", "img": "Skala Coconut.jpg", "detalle": """Skala Frutástica Coconut (1kg)

Crema vegana 2 en 1 diseñada para la nutrición y revitalización de cabellos secos y frágiles.

​Ingredientes clave: Aceite de coco, manteca de murumuru y karité.

​Beneficios: Hidratación profunda, brillo natural y control de frizz sin pesadez.

​Multifunción: Mascarilla (3-15 min), crema de peinar (sin enjuague), co-wash o pre-shampoo.

​Fórmula: 100% limpia (sin sulfatos, siliconas ni petrolatos).

​En resumen: Un rescate nutritivo a base de coco para devolverle la elasticidad y el brillo al cabello deshidratado."""},

    # --- COLECCIÓN LÍNEA DE ORO ---
    {"id": 7, "col_id": "linea-oro-revitalizante", "nombre": "Nazca Origem Babosa 400g", "precio": "$1500 CUP", "img": "Nazca OrigemBabosa.jpg", "detalle": """Nazca Origem Babosa (1kg)

Crema 2 en 1 de ultra hidratación y fortalecimiento, ideal para rescatar cabellos secos y quebradizos.

​Ingredientes clave: Aloe Vera (Babosa), Manteca de Karité, Aceite de Aguacate y Pantenol.

​Beneficios: Regeneración profunda, mayor resistencia de la fibra y brillo inmediato.

​Rapidez: Resultados visibles en solo 3 minutos de actuación.

​Usos: Mascarilla de tratamiento (con enjuague) o Crema para peinar (sin enjuague).

​Fórmula: 100% vegana, libre de crueldad animal y sin parabenos.

​En resumen: Potencia la suavidad y resistencia del cabello con la fuerza regeneradora de la babosa en tiempo récord."""},

    {"id": 8, "col_id": "linea-oro-revitalizante", "nombre": "Nazca Origem Cachos", "precio": "$1500 CUP", "img": "Nazca Origem 400g verde.jpg", "detalle": """Nazca Origem Cachos (1kg)

Crema multifuncional 2 en 1 diseñada para nutrir, definir y control el frizz en cabellos rizados y ondulados.

​Ingredientes clave: Aceite de coco, Aceite de Argán y D-Pantenol.

​Beneficios: Hidratación profunda, regeneración de la fibra y brillo intenso sin dejar residuos pesados.

​Versatilidad: Funciona como acondicionador, mascarilla de acción rápida (3 a 5 min) o crema para peinar sin enjuague.

​Fórmula: 100% vegana y liberada (sin siliconas, parabenos, petrolatos ni parafinas).

​En resumen: Definición prolongada y nutrición esencial para mantener los rizos saludables y disciplinados."""},

    {"id": 9, "col_id": "linea-oro-revitalizante", "nombre": "Nazca Origem Crespos", "precio": "$1500 CUP", "img": "Nazca Origem Crespos.jpg", "detalle": """Nazca Origem Crespos (1kg)

Crema multifuncional 2 en 1 diseñada para las necesidades específicas de cabellos con curvaturas 4ABC (rizos muy cerrados y afro).

​Ingredientes Clave: Manteca de Karité, Aceite de Coco y Aceite de Ricino.

​Beneficios: Aporta nutrición extrema, fuerza y el volumen necesario para este tipo de hebra, controlando el frizz y definiendo la estructura.

​Fórmula Liberada: 100% vegana; sin siliconas, sulfatos, parabenos ni petrolatos.

​Doble Uso: 
​Mascarilla: Tratamiento rápido de 3 minutos con enjuague.
​Crema de Peinar: Aplicación sin enjuague para definición y estilizado diario.

​En resumen: Nutrición intensiva y fortalecimiento para lograr rizos tipo afro definidos, brillantes y con máximo volumen."""},
    
    # --- COLECCIÓN CUIDADO DIARIO ---
    {"id": 10, "col_id": "cuidado-diario", "nombre": "Nazca Origem Onduladas", "precio": "$3500 CUP", "img": "Nazca Origem-1kg.jpg", "detalle": """Origem Eu Escolho Cachos - Onduladas (1kg)

Crema de peinado ligera diseñada específicamente para ondas (tipos 2ABC) que buscan definición y movimiento natural sin pesadez.

​Trío Poderoso: Enriquecida con aceites de Coco, Karité y Argán para brillo, hidratación y reparación de puntas.

​Escudo Protector: Incluye protección solar contra rayos UV y agentes contaminantes.

​Fórmula Liberada: 100% vegana, sin siliconas, sulfatos ni petrolatos (apta para Low/No Poo).

​Modo de uso: Aplicar sobre cabello húmedo o seco y estilizar (ideal para técnica scrunch). Sin enjuague.

​Guía rápida de la línea Nazca Origem:
​Amarillo (Onduladas): Nutrición ligera y movimiento (el producto actual).
​Verde (Cacheadas): Definición y volumen para rizos medios.
​Rojo (Crespos): Nutrición intensa para rizos cerrados o afro.

​En resumen: El aliado perfecto para ondas definidas, protegidas del sol y con cero encrespamiento."""},

    {"id": 11, "col_id": "cuidado-diario", "nombre": "Nevada S.O.S", "precio": "$3500 CUP", "img": "Nevada S.O.S.jpg", "detalle": """Nevada S.O.S. Crecimiento (3 en 1)

Tratamiento intensivo de fórmula brasileña diseñado para frenar la caída y fortalecer cabellos delgados o frágiles.

​Ingredientes clave: Biotina y Aceite de semilla de café (estimulan el folículo y regeneran la fibra).

​Beneficios: Aumenta la densidad capilar, reduce la rotura y promueve un crecimiento saludable.

​3 Modos de uso: 
​Pre-lavado: Protección previa al champú (3-15 min).
​Mascarilla: Hidratación profunda con enjuague (15 min).
​Crema de peinar: Finalizador sin enjuague para uso diario.

​Fórmula: 100% vegana, sin sal, sulfatos, parabenos ni petrolatos.

​Compatibilidad: Apta para todo tipo de cabello, incluso procesados o teñidos.

​En resumen: Un potente complejo vitamínico de 1kg para recuperar la fuerza y estimular el largo de tu melena."""},

    {"id": 12, "col_id": "cuidado-diario", "nombre": "Nevada Cachos Perfectos", "precio": "$3500 CUP", "img": "Nevada Cachos Perfectos.jpg", "detalle": """Nevada Cachos Perfeitos (3 en 1)

Tratamiento multifuncional diseñado para nutrir, regenerar y definir rizos u ondas (tipos 2ABC a 3A).

​Ingredientes clave: Aloe Vera (hidratación y elasticidad) y Aceite de Semilla de Algodón (brillo y nutrición).

​Efecto: Sella cutículas, desenreda con facilidad y aporta un movimiento natural sin frizz.

​3 Modos de uso:
​Pre-Lavado: Protege las puntas (3 min antes del champú).
​Mascarilla: Tratamiento intensivo (15 min con enjuague).
​Crema de peinar: Definición y control diario (sin enjuague).

​Fórmula: Vegana, sin sulfatos, petrolatos ni parabenos.

​En resumen: Una solución completa para mantener los rizos elásticos, hidratados y perfectamente definidos."""},
{"id": 13, "col_id": "Crema-Desrizadora-o-Alisadora", "precio":"$1400cup"
    "nombre": "Nevada Super Crema No-Lye Relaxer",
    "img":"Derriz Nevada.jpg",
    "detalle": """Nevada Super Crema No-Lye Relaxer, un kit de desrizado o alisado, para el cabello en dos pasos enriquecido con vitamina E. Está diseñado para transformar cabellos rizados o crespos en melenas lisas y manejables directamente en casa. 

Detalles del producto
Contenido del kit: Incluye dos sobres numerados: el Paso 1 (Activator Cream) y el Paso 2 (Relaxer Cream).

Fórmula: Es una fórmula sin lejía (no-lye), lo que suele ser más suave para el cuero cabelludo que los desrizadores tradicionales. Contiene vitamina E para nutrir y acondicionar el cabello durante el proceso.

Beneficios: Promete un alisado de larga duración, aportando brillo y suavidad."""}
]

@app.route('/')
def index():
    return render_template('index.html', colecciones=colecciones)

@app.route('/coleccion/<id_linea>')
def ver_coleccion(id_linea):
    linea = next((c for c in colecciones if c['id'] == id_linea), None)
    if not linea: abort(404)
    items = [p for p in productos if p['col_id'] == id_linea]
    return render_template('coleccion.html', linea=linea, items=items)

@app.route('/producto/<int:id_prod>')
def detalle(id_prod):
    prod = next((p for p in productos if p['id'] == id_prod), None)
    if not prod: abort(404)
    return render_template('producto.html', p=prod)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
