from flask import Flask, render_template, abort

app = Flask(__name__)

# --- DEFINICIÓN DE COLECCIONES ---
# Nota: He sincronizado los IDs para que coincidan exactamente con los productos
colecciones = [
    {
        "id": "skala-experto", 
        "nombre": "LÍNEA SKALA EXPERTO", 
        "img": "ColecciónSkala.png", 
        "desc": "Tratamientos intensivos brasileños para cada tipo de hebra."
    },
    {
        "id": "linea-oro-revitalizante", 
        "nombre": "LÍNEA DE ORO PROFESSIONAL", 
        "img": "Colección Nazca Origem.png", 
        "desc": "Nutrición extrema y reparación profunda para cabellos procesados."
    },
    {
        "id": "cuidado-diario", 
        "nombre": "CUIDADO DIARIO", 
        "img": "Colección Nevada _Nazca Origem-1kg.jpg", 
        "desc": "Mantenimiento esencial para un cabello radiante todos los días."
    },
    {
        "id": "crema-desrizadora-o-alisadora",
        "nombre": "CREMA DESRIZADORA",
        "img": "1777016240219.png",
        "desc": "Kit de desrizado o alisado para un cabello liso, brillante y suave."
    }
]

# --- BASE DE DATOS DE PRODUCTOS ---
productos = [
    # --- COLECCIÓN SKALA EXPERTO ---
    {"id": 1, "col_id": "skala-experto", "nombre": "Skala Moranco", "precio": "$3500 CUP", "img": "Skala Moranco.jpg", "detalle": "Skala Frutástica Morango (1kg)..."},
    {"id": 2, "col_id": "skala-experto", "nombre": "Skala Melancia", "precio": "$3500 CUP", "img": "Skala Melancia.jpg", "detalle": "Skala Frutástica Melancia (1kg)..."},
    {"id": 3, "col_id": "skala-experto", "nombre": "Skala Maracujá", "precio": "$3500 CUP", "img": "Skala Maracujá.jpg", "detalle": "Skala Maracuyá y Patauá (1kg)..."},
    {"id": 4, "col_id": "skala-experto", "nombre": "Skala Coquetel de Frutas", "precio": "$3500 CUP", "img": "Skala Coquetel de Frutas.jpg", "detalle": "Skala Coquetel de Frutas (1kg)..."},
    {"id": 5, "col_id": "skala-experto", "nombre": "Skala Coconut", "precio": "$3500 CUP", "img": "Skala Coconut.jpg", "detalle": "Skala Frutástica Coconut (1kg)..."},

    # --- COLECCIÓN LÍNEA DE ORO ---
    {"id": 7, "col_id": "linea-oro-revitalizante", "nombre": "Nazca Origem Babosa 400g", "precio": "$1500 CUP", "img": "Nazca OrigemBabosa.jpg", "detalle": "Nazca Origem Babosa (1kg)..."},
    {"id": 8, "col_id": "linea-oro-revitalizante", "nombre": "Nazca Origem Cachos", "precio": "$1500 CUP", "img": "Nazca Origem 400g verde.jpg", "detalle": "Nazca Origem Cachos (1kg)..."},
    {"id": 9, "col_id": "linea-oro-revitalizante", "nombre": "Nazca Origem Crespos", "precio": "$1500 CUP", "img": "Nazca Origem Crespos.jpg", "detalle": "Nazca Origem Crespos (1kg)..."},
    
    # --- COLECCIÓN CUIDADO DIARIO ---
    {"id": 10, "col_id": "cuidado-diario", "nombre": "Nazca Origem Onduladas", "precio": "$3500 CUP", "img": "Nazca Origem-1kg.jpg", "detalle": "Origem Eu Escolho Cachos - Onduladas (1kg)..."},
    {"id": 11, "col_id": "cuidado-diario", "nombre": "Nevada S.O.S", "precio": "$3500 CUP", "img": "Nevada S.O.S.jpg", "detalle": "Nevada S.O.S. Crecimiento (3 en 1)..."},
    {"id": 12, "col_id": "cuidado-diario", "nombre": "Nevada Cachos Perfectos", "precio": "$3500 CUP", "img": "Nevada Cachos Perfectos.jpg", "detalle": "Nevada Cachos Perfeitos (3 en 1)..."},

    # --- COLECCIÓN DESRIZADORA ---
    {"id": 13, "col_id": "crema-desrizadora-o-alisadora", "nombre": "Nevada Super Crema No-Lye Relaxer", "precio": "$1400 CUP", "img": "Derriz Nevada1.png", "detalle": "Kit de desrizado enriquecido con vitamina E..."}
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
