# 1. Installez le module Streamlit Authenticator avec pip

# 2. Importez le module et créez une instance d'authentification
import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# import streamlit_authenticator as stauth

# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,         # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,         # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}


authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",         # Le nom du cookie, un str quelconque
    "cookie key",          # La clé du cookie, un str quelconque
    30,                    # Le nombre de jours avant que le cookie expire
)

# 3. Utiliser la méthode login pour afficher le formulaire de connexion et
# vérifier les informations d'identification de l'utilisateur
authenticator.login()


# page d'acceuil apres connection
def accueil():
    # On affiche un menu déroulant (selectbox) DANS la barre latérale (sidebar)
    st.title("Bienvenu sur ma page")
    st.image("https://gifdb.com/images/high/standing-ovation-crowd-applause"
             "photo -oscar-awards-ai72icmh1ac7apdz.gif")


# Page des photos
def chat():
    st.title("Bienvenu dans l'album des animaux  😻")

    # Création du menu qui va afficher les choix qui se trouvent dans la
    # variable options
    # Création de 3 colonnes
    col1, col2, col3 = st.columns(3)

    # Contenu de la première colonne :
    with col1:
        st.image("https://static.streamlit.io/examples/cat.jpg")

    # Contenu de la deuxième colonne :
    with col2:
        st.image("https://www.melty.fr/wp-content/uploads/meltyfr/2023/07/1-6-"
                 "729x410.jpg")

    # Contenu de la troisième colonne :
    with col3:
        st.header("Un hiboux")
        st.image("https://static.streamlit.io/examples/owl.jpg")


# Bloc
if st.session_state["authentication_status"]:
    # notre bloc qui est à gauche
    with st.sidebar:
        # Le bouton de déconnexion
        authenticator.logout("Déconnexion")

        st.write(f"Bienvenue {st.session_state['name']}")

        # Création du menu qui va afficher les choix qui se trouvent dans la
        #  variable options
        selection = option_menu(
            menu_title=None,
            options=["🤩 Accueil", "😻 Photos"]
        )

    # On indique au programme quoi faire en fonction du choix
    if selection == "🤩 Accueil":
        accueil()
    elif selection == "😻 Photos":
        chat()
    # ... et ainsi de suite pour les autres pages
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')

# Bas de page
st.write('___')
st.write("<h7 style='text-align: center; color: green;'>© 2025 Samuel M. All"
         "rights reserved.🦁</h7>", unsafe_allow_html=True)
st.link_button("LinkedIn", "https://www.linkedin.com/in/samuel-m-co")
