import streamlit as st
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import urllib.parse
import base64

# Configuración de la página
st.set_page_config(page_title="Botarmy_hub - Sé un Aliado de la Revolución IA]", page_icon="🤖", layout="wide")

# Título
st.title("🚀 Únete a :red[Botarmy_hub] y sé parte de la :blue[revolución IA]")

# Descripción introductoria
st.markdown("""
### Llega más lejos con las herramientas de inteligencia artificial.
Con **Botarmy_hub**, te ofrecemos la oportunidad de **convertirte en aliado estratégico** en la venta y promoción de herramientas basadas en IA para tu network, independientemente de tu profesión o sector.

Ya seas emprendedor, profesional o alguien con ganas de explorar nuevas oportunidades, nuestras herramientas se adaptan a **cualquier industria**.
""")

# Imagen de cabecera o logo
col1, col2 = st.columns ([1,4])
with col1:
    st.image("Botarmy_logo.png", width=150)
with col2:
# Beneficios
    st.subheader("🎯 ¿Qué obtienes siendo un aliado de Botarmy_hub?")
    st.markdown("""
- **Comisiones atractivas**: Gana un porcentaje significativo por cada venta que realices, entre el 35% al 50% del precio final.
- **Capacitación personalizada**: No necesitas experiencia en IA, te enseñamos todo lo necesario.
- **Acceso a herramientas IA innovadoras**: Lleva soluciones tecnológicas avanzadas a tu network.
- **Flexibilidad total**: Trabaja a tu propio ritmo y con libertad total.
""")

# Casos de uso y herramientas de IA
st.subheader("🔍 Casos de uso y herramientas de IA")

# Ejemplos de herramientas y casos de uso
st.markdown("Aquí te mostramos algunas de nuestras herramientas IA y cómo están transformando diversas industrias:")

# Columna 1 - Caso de Uso 1
col1, col2, col3 = st.columns(3)

with col1:
    st.image("image1.jpeg", caption="Industria: Atención al cliente", use_column_width=True)
    st.write("""
    :red[**Asistentes Virtuales para Servicio al Cliente**]  
    Herramienta que utiliza IA para atender consultas de clientes de forma automatizada, ofreciendo respuestas inmediatas y personalizadas, reduciendo tiempos de espera y mejorando la satisfacción del cliente.
    **Aplicación**: Empresas que buscan mejorar su servicio al cliente, como retail, banca y telecomunicaciones.
    """)

# Columna 2 - Caso de Uso 2
with col2:
    st.image("image2.jpeg", caption="Industria: Marketing Digital", use_column_width=True)
    st.write("""
    :blue[**IA para Análisis de Tendencias y Predicciones de Mercado**]  
    Utilizando algoritmos de aprendizaje automático, esta herramienta identifica patrones de consumo, predice tendencias de mercado y optimiza campañas de marketing para aumentar la conversión de ventas.
    **Aplicación**: Departamentos de marketing que desean optimizar sus estrategias y maximizar su ROI.
    """)

# Columna 3 - Caso de Uso 3
with col3:
    st.image("image3.jpeg", caption="Industria: Recursos Humanos", use_column_width=True)
    st.write("""
    :red[**IA para Selección de Personal y Análisis de Talento**] 
    Herramienta que analiza grandes volúmenes de datos de candidatos, optimiza la selección y evalúa habilidades clave, reduciendo el tiempo de contratación y mejorando la calidad de los empleados seleccionados.
    **Aplicación**: Empresas que buscan mejorar la eficiencia en el reclutamiento.
    """)

# Más casos de uso (si lo deseas)
st.markdown("---")
st.subheader("🔧 Otras herramientas de IA aplicables")
st.markdown("""
- **Automatización de Tareas Repetitivas**: Utiliza IA para automatizar procesos manuales y repetitivos, permitiendo que los empleados se concentren en tareas más estratégicas.
- **Asistentes Virtuales para Colaboradores Internos**: Optimiza la comunicación interna en grandes organizaciones, ayudando a empleados a encontrar información, programar reuniones o resolver problemas rápidamente.
- **IA para Diagnóstico Médico**: Apoya a médicos y personal de salud con sistemas de IA que analizan imágenes y datos clínicos para diagnósticos más rápidos y precisos.
""")

# Llamada a la acción (CTA)
st.subheader("🔗 ¡No pierdas la oportunidad!")
st.markdown("""
¿Listo para llevar el futuro de la IA a tu red de contactos? Regístrate ahora para unirte a **Botarmy_hub**.
""")

# Crear el formulario de registro
with st.form(key='Formulario de registro'):
       nombre = st.text_input("Nombre completo")
       email = st.text_input("Correo electrónico")
       profesion = st.text_input("Profesión / Industria")
       idea = st.text_area("¿Cómo piensas integrar IA en tu red de contactos?", placeholder="Cuéntanos brevemente tu idea")
        
       submit_button = st.form_submit_button(label='Quiero registrarme')
        
       if submit_button:
            # Enviar el correo electrónico
            email_recipient = "jjusturi@gmail.com"
            email_subject = f"Botarmy- hub challenge Contact Form Submission: {nombre}"
            email_body = f"Reason: {idea}\nContact Info: {email}\nName: {nombre}"
            
            msg = MIMEMultipart()
            msg['From'] = nombre
            msg['To'] = email_recipient
            msg['Subject'] = email_subject
            msg.attach(MIMEText(email_body, 'plain'))
            
            try:
                # Configurar el servidor SMTP
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(st.secrets["smtp"]["username"], st.secrets["smtp"]["password"])
                text = msg.as_string()
                server.sendmail(nombre, email_recipient, text)
                server.quit()
                st.success("En breve nos pondremos en contacto por mail para darte la bienvenida oficial!!")
            except Exception as e:
                st.error(f"Error sending message: {e}")
            
# Footer con contacto
st.markdown("---")
st.write("Para más información, síguenos en nuestras redes sociales o envíanos un correo a: **jjusturi@gmail.com**")
st.write("🌐 [Visita nuestra web](https://codecodix.com)")
st.write("📲 [Síguenos en LinkedIn](https://www.linkedin.com/in/imanolasolo/)")
