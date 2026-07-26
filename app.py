import streamlit as st
import plotly.express as px
import pandas as pd


from motor_logico import (
    calcular_todos_los_progresos, 
    obtener_aprobadas_licenciatura, 
    obtener_aprobadas_ia
)

# Configuración de la página
st.set_page_config(page_title="Simulador Multi-Carrera UNaHur", layout="wide", page_icon="📊")

# Estilo personalizado
st.markdown("""
    <style>
    .main {
        background-color: #f5f7f9;
    }
    
    </style>
    """, unsafe_allow_html=True)

st.title("📊 Simulador de Transición UNaHur 2026")
st.markdown("Visualizá el impacto de tus materias aprobadas en los nuevos planes de estudio.")

# --- SECCIÓN DE SELECCIÓN EN BARRA LATERAL ---
st.sidebar.header("📋 Mi Progreso Académico")

seleccionadas = []

# 1. Menú Desplegable: Materias Comunes
with st.sidebar.expander("⭐ Materias Comunes", expanded=False):
    materias_comunes = [
        "Inglés I", 
        "Inglés II", 
        "Materia UNAHUR I", 
        "Materia UNAHUR II", 
        "Nuevos Entornos y Lenguajes"
    ]
    for m in materias_comunes:
        if st.checkbox(m, key=f"com_{m}"):
            seleccionadas.append(m)

# 2. Menú Desplegable: Compartidas de Informática (LISTA DIRECTA)
with st.sidebar.expander("💻 Compartidas de Informática", expanded=False):
    # Definimos la lista acá mismo para evitar errores de lectura de CSV
    materias_compartidas_lista = [
        "Matemática para informática I",
        "Matemática para informática II",
        "Introducción a Logica y Problemas Computacionales",
        "Programación Estructurada",
        "Organización de Computadoras I",
        "Organización de Computadoras II",
        "Programación con Objetos I",
        "Bases de Datos",
        "Redes de Computadoras",
        "Construccion de Interfaces de Usuario",
        "Elementos de Ingeniería de Software",
        "Sistemas Operativos",
        "Tecnología y Sociedad"
    ]
    for m in materias_compartidas_lista:
        if st.checkbox(m, key=f"tronk_{m}"):
            seleccionadas.append(m)

    # 3. Materias de Redes (NUEVO)
    with st.sidebar.expander("🌐 Materias Redes", expanded=False):
        redes_mats = [
            "Sistemas de comunicación", 
            "Taller de intérpretes de comandos",
            "Operaciones I", 
            "Operaciones II", 
            "Redes avanzadas"
        ]
        for m in redes_mats:
            if st.checkbox(m, key=f"red_{m}"): seleccionadas.append(m)

    # 4. Materias de Videojuegos
    with st.sidebar.expander("🎮 Materias Videojuegos", expanded=False):
        videojuegos_mats = [
            "Introducción a los Videojuegos", 
            "Arte digital para videojuegos",
            "Taller de diseño conceptual de juegos", 
            "Introducción a motores de videojuegos",
            "Programación de videojuegos I", 
            "Programación de videojuegos II",
            "Diseño Lúdico", 
            "Planificación de negocios"
        ]
        for m in videojuegos_mats:
            if st.checkbox(m, key=f"vj_{m}"):
                seleccionadas.append(m)

    
    #IA----------------------------------------
    # 5. Materias de Inteligencia Artificial
    with st.sidebar.expander("🤖 🤖  Materias IA", expanded=False):
        ia_mats = [
            "Taller de programación I", 
            "Taller de programación II", 
            "Taller de programación III",
            "Introducción a la inteligencia artificial", 
            "Álgebra lineal", 
            "Cálculo",
            "Fundamentos de ciencias de datos", 
            "Fundamentos Redes Neuronales",
            "Aprendizaje Automático", 
            "Aprendizaje Automático Avanzado",
            "Procesamiento de Imágenes y Visión por Computadora", 
            "Proyecto integrador"
        ]
        for m in ia_mats:
            if st.checkbox(m, key=f"ia_{m}"):
                seleccionadas.append(m)

    #las demas 
    # 6. Materias de Programación Avanzada
    with st.sidebar.expander("💻 Materias Programación", expanded=False):
        programacion_mats = [
            "Taller de marcado", 
            "Estructuras de Datos", 
            "Programación con Objetos II",
            "Programación Concurrente", 
            "Programación Funcional", 
            "Estrategias de Persistencia", 
            "Sist Inf Geografica (Electiva)"
        ]
        for m in programacion_mats:
            if st.checkbox(m, key=f"prog_{m}"):
                seleccionadas.append(m)

    # 7. Materias Licenciatura en Informática
with st.sidebar.expander("🎓 Licenciatura en Informática", expanded=False):
    lic_info_mats = [
        "Algoritmos",
        "Laboratorio de Sistemas Op. y Redes",
        "Lógica y Programación",
        "Programación con Objetos III",
        "Seguridad de la Información",
        "Análisis Matemático",
        "Matemática II",
        "Matemática III",
        "Probabilidad y Estadística",
        "Ingeniería de Requerimientos",
        "Desarrollo de Aplicaciones",
        "Gestión de Proyectos de Des. de Software",
        "Práctica Profesional Supervisada (PPS)",
        "Teorías de la Computación",
        "Arquitectura de SW I",
        "Sistemas Distribuidos y Tiempos Real",
        "Lenguajes Formales y Autómatas",
        "Características de Lenguajes de Comp.",
        "Arquitectura de SW II",
        "Arquitectura de Computadoras",
        "Parseo y Generación de Código",
        "Ejercicio Profesional",
        "Tesina de Licenciatura",
        "Materia Optativa 1 (no Ap. Automático ni Redes Neur.)",
        "Materia Optativa 2 (no Ap. Automático ni Redes Neur.)",
        "Sistemas y Organizaciones"
    ]
    for m in lic_info_mats:
        if st.checkbox(m, key=f"lic_info_{m}"):
            seleccionadas.append(m)

    # Actividades de Créditos: Espacio de Integración Curricular
    with st.sidebar.expander("🎖️ Espacio de Integración Curricular", expanded=False):
        eic_mats = [
            "Desarrollo de Aplicaciones, en UNAHUR (Prog)",
            "Práctica Profesional Supervisada PPS (Prog)",
            "Proyecto Integrador (Prog)",
            "Desarrollo de Aplicaciones, en UNAHUR (Redes)",
            "Práctica Profesional Supervisada PPS (Redes)",
            "Proyecto Integrador (Redes)",
            "Proyecto integrador Final (VJ)"
        ]
        for m in eic_mats:
            if st.checkbox(m, key=f"eic_{m}"):
                seleccionadas.append(m)


    # Actividades de Créditos: Formativas Académicas y Profesionales
with st.sidebar.expander("📚 Formativas Académicas y Profesionales", expanded=False):
    formativas_mats = [
        "Participación como asistente en Jornadas / Workshops / Congresos",
        "Participación como asistente en Jornadas / Workshops / Congresos - (Evento de 1 día presencial)",
        "Talleres especiales - Taller de GitHub",
        "Talleres especiales - Taller de Gestión de la seguridad informática",
        "Talleres Especiales - Gestión de Firewall",
        "Talleres Especiales (más de 32hs)",
        "Participación en Competencias Estudiantiles - Rally Innovación",
        "Participación en competencias estudiantiles",
        "Rally Latinoamericano de Innovación - 1ra participación",
        "Rally Latinoamericano de Innovación - 2da participación",
        "Participación en Proyectos Abiertos",
        "Intercambios estudiantiles presenciales y/o virtuales",
        "Cursadas Voluntarias en otras Universidades",
        "Formación Profesional",
        "Formación Profesional (Segunda Participación)",
        "Taller de Procesamiento digital de imágenes",
        "Taller de Introducción al procesamiento digital de Imágenes",
        "Curso Project Management",
        "Curso Oracle SQL & PL SQL",
        "Curso Redes Móviles Celulares",
        "Curso Enlaces Inalámbricos Fijos",
        "Curso Redes de Fibra Óptica",
        "Curso Introducción al Cómputo Paralelo",
        "Presentación de nuevos planes de las carreras de informática",
        "Cómo hacer videojuegos sin volverse loco: Gestión, Diseño y Validación de Usuario",
        "Creación y Animación de Personajes 2D-Del boceto al Sprite Sheet.",
        "Diseño Narrativo de Personajes: Cómo comenzar un relato",
        "Del Prototipo al Portfolio Profesional",
        "Taller de robótica",
        "Charlas con Graduados",
        "PIA Taller 1",
        "Taller Introductorio de Integrales",
        "Lenguajes educativos para aprender a programar",
        "Git",
        "GraphQL en Springboot",
        "De wollok a Java",
        "Taller de programación",
        "Principios básicos de la Seguridad de la Información y la Ciberseguridad",
        "Vibe Coding",
        "Taller de uso de herramientas para el procesamiento de datos",
        "Curso Introducción a UML"
    ]
    for m in formativas_mats:
        if st.checkbox(m, key=f"fap_{m}"):
            seleccionadas.append(m)

    
    # Actividades de Créditos: Sociales, Culturales y Deportivas
with st.sidebar.expander("🎨 Sociales, Culturales y Deportivas", expanded=False):
    scd_mats = [
        "Voluntariados",
        "Talleres deportivos",
        "Taller de eSport",
        "UNAHUR@TIC #1 - Encuentro de Informática",
        "UNAHUR@TIC #1 - Encuentro de Informática (medio día)",
        "UNAHUR@TIC - Encuentro de Informática (segunda participación)",
        "UNAHUR@TIC - Encuentro de Informática (Tercera participación)",
        "Actividades de Perspectiva de Género (12hs)",
        "Actividades de Biblioteca",
        "Talleres Culturales"
    ]
    for m in scd_mats:
        if st.checkbox(m, key=f"scd_{m}"):
            seleccionadas.append(m)

    # Actividades de Créditos: Formativas en Docencia e Investigación
with st.sidebar.expander("🔬 Formativas en Docencia e Investigación", expanded=False):
    doc_inv_mats = [
        "Participación en el programa “Un estudiantes/Un compañero/a”",
        "Participación como Estudiante Asistente",
        "Colaboración en materias",
        "Participación en actividades de difusión académica",
        "Participación en actividades de difusión académica (2da participación)",
        "Computación Cuántica",
        "Asistencia Técnica a grupos de Investigación de la Universidad",
        "Python Day",
        "Python Day (Segunda Participación)",
        "Jornadas de la Industria 1ra Participación - Día 1",
        "Jornadas de la Industria 2da Participación - Día 2",
        "Exposición en Jornadas - 1ra Participación"
    ]
    for m in doc_inv_mats:
        if st.checkbox(m, key=f"di_{m}"):
            seleccionadas.append(m)

st.sidebar.divider()
st.sidebar.info("El cálculo aplica las equivalencias automáticas entre planes.")

# --- CÁLCULO DE RESULTADOS ---
df_resultados = calcular_todos_los_progresos(seleccionadas)

# --- GRÁFICO PRINCIPAL ---
st.subheader("📈 Instituto de Tecnología e Ingeniería: Avance.")
df_grafico = df_resultados.sort_values(by='Avance (%)', ascending=True)

fig = px.bar(
    df_grafico, 
    x='Avance (%)', 
    y='Carrera', 
    orientation='h',
    text='Avance (%)',
    color='Avance (%)',
    color_continuous_scale='Greens',
    range_x=[0, 100]
)

fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
fig.update_layout(height=600, showlegend=False, xaxis=dict(ticksuffix="%"))

st.plotly_chart(fig, use_container_width=True)

# --- TABLA DE DETALLE ---
st.subheader("📋 Detalle de lo que te falta")
df_tabla = df_resultados.sort_values(by='Avance (%)', ascending=False)

st.dataframe(
    df_tabla, 
    use_container_width=True,
    column_config={
        "Avance (%)": st.column_config.ProgressColumn("Progreso", format="%.1f%%", min_value=0, max_value=100),
        "Horas Faltantes": st.column_config.NumberColumn("Horas Reloj"),
        "ACA Faltante": st.column_config.NumberColumn("Créditos ACA"),
        "Materias Restantes": st.column_config.NumberColumn("Materias")
    },
    hide_index=True
)

# --- VISTA DETALLADA DE LA LICENCIATURA EN INFORMÁTICA ---
st.divider()
st.subheader("🎓 Materias Aprobadas / Reconocidas en Licenciatura en Informática (Nuevo Plan)")

dict_lic = obtener_aprobadas_licenciatura(seleccionadas)
total_reconocidas = sum(len(mats) for mats in dict_lic.values())

if total_reconocidas == 0:
    st.info("Aún no tenés materias tildadas que acrediten directa o por combo en la Licenciatura.")
else:
    st.success(f"¡Tenés **{total_reconocidas}** materias reconociéndose en el nuevo plan de la Licenciatura!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.expander("📌 1er Año", expanded=True):
            if dict_lic["1er año"]:
                for m in dict_lic["1er año"]:
                    st.markdown(f"- ✅ **{m}**")
            else:
                st.caption("Sin materias aprobadas en este módulo.")

        with st.expander("📌 2do Año", expanded=True):
            if dict_lic["2do año"]:
                for m in dict_lic["2do año"]:
                    st.markdown(f"- ✅ **{m}**")
            else:
                st.caption("Sin materias aprobadas en este módulo.")

        with st.expander("📌 3er Año", expanded=False):
            if dict_lic["3er año"]:
                for m in dict_lic["3er año"]:
                    st.markdown(f"- ✅ **{m}**")
            else:
                st.caption("Sin materias aprobadas en este módulo.")

    with col2:
        with st.expander("📌 4to Año", expanded=False):
            if dict_lic["4to año"]:
                for m in dict_lic["4to año"]:
                    st.markdown(f"- ✅ **{m}**")
            else:
                st.caption("Sin materias aprobadas en este módulo.")

        with st.expander("📌 5to Año", expanded=False):
            if dict_lic["5to año"]:
                for m in dict_lic["5to año"]:
                    st.markdown(f"- ✅ **{m}**")
            else:
                st.caption("Sin materias aprobadas en este módulo.")



# --- VISTA DETALLADA DE LA TECNICATURA EN INTELIGENCIA ARTIFICIAL ---
st.divider()
st.subheader("🤖 Materias Aprobadas / Reconocidas en Tecnicatura Univ. en Inteligencia Artificial")

dict_ia = obtener_aprobadas_ia(seleccionadas)
total_reconocidas_ia = sum(len(mats) for mats in dict_ia.values())

if total_reconocidas_ia == 0:
    st.info("Aún no tenés materias tildadas que acrediten en la Tecnicatura en IA.")
else:
    st.success(f"¡Tenés **{total_reconocidas_ia}** materias reconociéndose en la Tecnicatura en IA!")
    
    col_ia1, col_ia2, col_ia3 = st.columns(3)
    
    with col_ia1:
        with st.expander("📌 1er Año", expanded=True):
            if dict_ia["1er año"]:
                for m in dict_ia["1er año"]:
                    st.markdown(f"- ✅ **{m}**")
            else:
                st.caption("Sin materias aprobadas.")

    with col_ia2:
        with st.expander("📌 2do Año", expanded=True):
            if dict_ia["2do año"]:
                for m in dict_ia["2do año"]:
                    st.markdown(f"- ✅ **{m}**")
            else:
                st.caption("Sin materias aprobadas.")

    with col_ia3:
        with st.expander("📌 3er Año", expanded=True):
            if dict_ia["3er año"]:
                for m in dict_ia["3er año"]:
                    st.markdown(f"- ✅ **{m}**")
            else:
                st.caption("Sin materias aprobadas.")



st.caption("Simulador desarrollado por Martín Maldonado - UNaHur")