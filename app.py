import streamlit as st

st.set_page_config(
    page_title="Aniversario 8",
    page_icon="❣"
)

st.title("Feliz mesiversario 8 mi amor")
st.markdown("### **Te amoooooooo**")

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Nuestras aventuras", "Nuestros regalos", 
"Nuestros besos", "Nuestras Clases", "Nosotros"])

with tab1:
    col1, col2 = st.columns(2)

    with col1:
        st.image("LASOL.jpg", caption="Lagosol")
        st.image("Salitre.jpg", caption="Salitre Mágico")

    with col2:
        st.image("Squi1.jpg", caption="Squid Games")
        st.write("Eres la mejor novia del mundo y mi compañera de aventuras favorita. Cada momento contigo se convierte en una experiencia increíble. Aquí están nuestros recuerdos más preciados, y sueño con todas las aventuras que aún nos faltan por vivir.")
        st.image("Squi2.jpg", caption="Squid Games")
    
    st.image("Xcape.jpg", caption="Xcape")
    
with tab2:
    col1, col2 = st.columns(2)

    with col1:
        st.image("Anillo.jpg", caption="Tu anillo")
    
    with col2:
        st.image("FlorA.jpg", caption="Flores Amarillas")

    st.write("Estos son algunos de los regalos que te he dado con todo mi amor. Aunque sé que ningún regalo podrá expresar completamente lo mucho que te amo, cada uno lleva un pedacito de mi corazón y no puedo esperar a sorprenderte con los siguientes.")

with tab3:
    col1, col2 = st.columns(2)

    with col1:
        st.image("PrimeB.jpg", caption="Nuestro Beso")
        st.write("Tus besos son mi debilidad… y también mi felicidad. No puedo ni quiero dejar de besarte.")
        st.write("Te amo mi preciosa")
    
    with col2:
        st.image("BSibat.jpg", caption="Beso en Sibaté")      

with tab4:
    col1, col2 = st.columns(2)

    with col1:
        st.image("ProgA.jpg", caption="Nuestra foto en Programación")
    
    with col2:
        st.image("ProgE.jpg", caption="Programadores ❣")

    st.write("Ver clases contigo ha sido, sin duda, ha sido una de las experiencias más hermosas en nuestro paso por la universidad. No solo compartimos apuntes y proyectos, sino también miradas, risas y momentos que se quedan grabados para siempre. Estar a tu lado incluso en lo cotidiano, como una simple clase, convierte cada día en algo especial. No imagino una mejor manera de vivir esta etapa que contigo a mi lado.")

with tab5:
    col1, col2 = st.columns(2)

    with col1:
        st.image("EspejoAt.jpg", caption="Nuestro espejo")
        st.image("Navidad.jpg", caption="¡Feliz Navidad!")
        st.write("Nada se compara a lo que siento cuando estoy contigo. Eres lo mejor que me ha pasado, y me emociona pensar en todo lo que aún nos queda por vivir juntos.")
    
    with col2:
        st.image("Anima.jpg", caption="Nos Vemos Perfectos Juntos")
        st.image("Eleg.jpg", caption="Nuestra Foto Elegante")







