# UASZ-GPT 🤖

UASZ-GPT est une application de **Retrieval-Augmented Generation (RAG)** conçue pour permettre aux utilisateurs d'interagir intelligemment avec leurs documents PDF. 

L'application utilise l'IA de Google (Gemini) pour analyser le contenu des fichiers téléchargés et répondre aux questions de manière précise en citant ses sources.

## 🚀 Fonctionnalités

- **Upload de PDF** : Chargez vos documents directement dans l'interface.
- **Analyse Intelligente** : Découpage automatique des documents en segments (chunking).
- **Chat avec vos documents** : Posez des questions en langage naturel sur le contenu de vos PDF.
- **Citations des sources** : Affichez les extraits exacts et les numéros de page utilisés pour générer la réponse.
- **Interface Moderne** : Développé avec Streamlit pour une expérience utilisateur fluide.

## 🛠️ Stack Technique

- **Frontend** : [Streamlit](https://streamlit.io/)
- **Orchestration IA** : [LangChain](https://www.langchain.com/)
- **Modèles d'IA** : Google Gemini (Pro & Flash)
- **Embeddings** : Google Text Embedding 004
- **Base de données Vectorielle** : [ChromaDB](https://www.trychroma.com/) (en mémoire)

## 💻 Installation Locale

1. **Cloner le projet** :
   ```bash
   git clone https://github.com/VOTRE_NOM_UTILISATEUR/UASZ-GPT.git
   cd UASZ-GPT
   ```

2. **Créer un environnement virtuel** :
   ```bash
   python -m venv venv
   # Sur Windows
   .\venv\Scripts\activate
   # Sur macOS/Linux
   source venv/bin/activate
   ```

3. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer l'API Key** :
   Créez un fichier `.env` à la racine du projet et ajoutez votre clé API Google Gemini :
   ```text
   GOOGLE_API_KEY=votre_cle_api_ici
   ```

5. **Lancer l'application** :
   ```bash
   streamlit run app.py
   ```

## 🌐 Déploiement

Cette application est prête à être déployée sur **Streamlit Community Cloud** :
1. Poussez votre code sur GitHub.
2. Connectez votre dépôt sur [share.streamlit.io](https://share.streamlit.io/).
3. Ajoutez votre `GOOGLE_API_KEY` dans les **Advanced Settings > Secrets**.

---
*Développé pour l'UASZ.*
