import streamlit as st

st.title("Test de Intereses Profesionales de Holland")

# Parte A: Autoconocimiento
st.header("Parte A: Autoconocimiento")
st.write("**Instrucciones:** Marque con una X todos los adjetivos que describan su personalidad. Señale tantos como desee. Trate de definirse tal como es, no como le gustaría ser.")
adjetivos = [
    "Huraño", "Discutidor", "Arrogante", "Capaz", "Común Y Corriente", 
    "Conformista", "Concienzudo", "Curioso", "Dependiente", "Eficiente", 
    "Paciente", "Dinámico", "Femenino", "Amistoso", "Generoso", "Dispuesto a ayudar", 
    "Inflexible", "Insensible", "Introvertido", "Intuitivo", "Irritable", "Amable", 
    "De buenos modales", "Varonil", "Inconforme", "Poco realista", "Poco culto", 
    "Poco idealista", "Impopular", "Original", "Pesimista", "Hedonista", "Práctico", 
    "Rebelde", "Reservado", "Culto", "Lento de movimientos", "Sociable", "Estable", 
    "Esforzado", "Fuerte", "Suspicas", "Cumplido", "Modesto", "Poco convencional"
]

col1, col2, col3 = st.columns(3)
selected_adjetivos = []

for i, adjetivo in enumerate(adjetivos):
    if i % 3 == 0:
        with col1:
            if st.checkbox(adjetivo, key=f'adjetivo_{i}'):
                selected_adjetivos.append(adjetivo)
    elif i % 3 == 1:
        with col2:
            if st.checkbox(adjetivo, key=f'adjetivo_{i}'):
                selected_adjetivos.append(adjetivo)
    else:
        with col3:
            if st.checkbox(adjetivo, key=f'adjetivo_{i}'):
                selected_adjetivos.append(adjetivo)

# Parte B: Comparación con otras personas
st.header("Parte B: Comparación con otras personas")
st.write("**Instrucciones:** Califíquese de acuerdo con las siguientes características tal como considera ser en comparación con otras personas de su edad. Encierre en un círculo la respuesta que más se ajuste a sí mismo.")
part_b_questions = [
    "Distraído", "Capacidad artística", "Capacidad Burocrática", 
    "Conservador", "Cooperación", "Expresividad", "Liderazgo", 
    "Gusto en ayudar a los demás", "Capacidad matemática", 
    "Capacidad mecánica", "Originalidad"
]
part_b_responses = []
for question in part_b_questions:
    response = st.radio(f"{question}:", ["Más que los demás", "Igual que los demás", "Menos que los demás"], key=question)
    part_b_responses.append(response)

# Parte C: Importancia de logros y aspiraciones
st.header("Parte C: Importancia de logros y aspiraciones")
st.write("**Instrucciones:** Indique qué importancia da a las siguientes clases de logros, aspiraciones y metas.")
part_c_questions = [
    "Estar feliz y satisfecho", "Descubrir o elaborar un producto útil", 
    "Ayudar a quiénes están en apuros", "Llegar a ser una autoridad en algún tema", 
    "Llegar a ser un deportista destacado", "Llegar a ser un líder en la comunidad", 
    "Ser influyente en asuntos públicos", "Observar una conducta religiosa formal", 
    "Contribuir a la ciencia en forma teórica", "Contribuir a la ciencia en forma técnica", 
    "Escribir bien (novelas, poemas)", "Haber leído mucho", "Trabajar mucho", 
    "Contribuir al bienestar humano", "Crear buenas obras artísticas (teatro, pintura)", 
    "Llegar a ser un buen músico", "Llegar a ser un experto en finanzas y negocios", 
    "Hallar un propósito real en la vida"
]
part_c_responses = []
for question in part_c_questions:
    response = st.radio(f"{question}:", ["Muy Importante", "Más o Menos Importante", "Poco Importante"], key=question)
    part_c_responses.append(response)

# Parte D: Preferencias y habilidades
st.header("Parte D: Preferencias y habilidades")
st.write("**Instrucciones:** Para las siguientes preguntas, escoja una sola alternativa, según lo que más se ajuste a Usted.")
part_d_questions = [
    "Me gusta leer y meditar sobre los problemas",
    "Mi mayor habilidad se manifiesta en negocios",
    "Soy muy incompetente en mecánica",
    "Las materias que más me gustan son arte",
    "Si tuviera que realizar alguna de estas actividades, la que menos me agradaría es participar en actividades sociales muy formales"
]
part_d_responses = []
for question in part_d_questions:
    response = st.radio(f"{question}:", ["a) Sí", "b) No", "c) Tal vez"], key=question)
    part_d_responses.append(response)

# Botón de envío
if st.button("Enviar"):
    st.write("Resultados enviados con éxito!")
    # Aquí puedes agregar lógica para procesar y guardar las respuestas
