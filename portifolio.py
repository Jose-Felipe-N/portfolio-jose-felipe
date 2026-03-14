import streamlit as st

st.set_page_config(
    page_title="Portfólio | José Felipe", 
    page_icon=":briefcase:", 
    layout="wide")

st.sidebar.title("Menu")
pagina_selecionada = st.sidebar.radio("Selecione uma página:", ["Sobre Mim", "Projetos", "Contato"])

if pagina_selecionada == "Sobre Mim":
    st.title("Olá, eu sou José Felipe!")
    st.subheader("Estudante de Ciência da Computação e Ciência e Tecnologia na UFABC")
    st.divider()
    col1, col2 = st.columns([1, 3.5])
    
    with col1:
        st.image("IMG_4658.jpg", use_column_width=120)
        
        st.info("""
        **🛠️ Principais Habilidades:**
        * Python
        * Streamlit
        * Lógica de Programação
        * Raciocínio Matemático
        """)
        
    with col2:
        st.write("""
        Tenho uma base forte em ciências exatas, com grande interesse nas intersecções entre matemática, 
        física e tecnologia. Atualmente, meu foco principal de desenvolvimento é em Python, linguagem que 
        utilizo para transformar lógicas complexas em soluções reais e eficientes. 
        
        Gosto de desafios que exigem pensamento analítico e estou sempre em busca de aprender novas 
        formas de otimizar sistemas e processos.
        """)
        
elif pagina_selecionada == "Projetos":
    st.title("Meus Projetos")
    st.subheader("Projeto 1: 📊 Sistema de Triagem Financeira")
    st.write("**O que é:** Uma aplicação web interativa que avalia a saúde financeira do usuário e recomenda estratégias de investimento personalizadas. O sistema cruza dados de fluxo de caixa, capital disponível e tolerância ao risco para gerar diagnósticos precisos sobre o momento financeiro do usuário.")

    st.write("**Principais Funcionalidades:**")
    st.markdown("""
**Principais Funcionalidades:**

* **Autenticação de Usuários:** Sistema de login e cadastro com armazenamento local em JSON.
* **Cálculo de Reserva de Emergência:** Algoritmo que calcula a meta de segurança financeira e o progresso do usuário.
* **Motor de Recomendação:** Classificação inteligente do perfil de investimento baseada em 6 variáveis financeiras (idade, renda, capital, etc.).
* **Geração de Relatórios:** Download de recibos dinâmicos em `.txt` com o diagnóstico.
""")

    st.write("**Tecnologias:** Python, Streamlit, JSON.")

elif pagina_selecionada == "Contato":
    st.title("Entre em Contato")
    st.write("Informações de contato e links para redes sociais.")
    
    st.divider()
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.subheader("Profissional")
        st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/josé-felipe-da-silva-neto/)")
        
    with col2:
        st.subheader("Projetos")
        st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Jose-Felipe-N)")
        
    with col3:
        st.subheader("E-mail")
        st.markdown("[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](https://mail.google.com/mail/?view=cm&fs=1&to=contato.josefelipe.dev@gmail.com)")
        st.caption("Email: contato.josefelipe.dev@gmail.com")
    with col4:
        st.subheader("Telefone")
        st.markdown("[![WhatsApp](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)](https://wa.me/5511997902696)")
        st.caption("📱 (11) 99790-2696")

    st.divider()
    st.write("Você também pode me encontrar pelos corredores da UFABC! 🎓")
    
    
