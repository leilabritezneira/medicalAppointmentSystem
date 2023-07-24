<div align="end">
  :uk: :es: :fr: 
</div>

<hr>
<h1> :uk: Final Medical Appointment Project with Python </h1>
:octocat: In this repository you will find the Final Medical Appointment System made during the third semester of the Technical University in Programming of the National Technological University.
<br> 
<br> During the third semester, we have intensified our learning of Python language and its framework Django. At the same time, we have deepened our knowledge of databases, in particular with PostgresSQL. This is the  reason why the semester project was carried out with these two technologies. 
<br>
<br>The project is a medical appontment system in which the user can: 
<dl>
  <dd><br> 🩺 Register patients and services.</dd>
  <dd> 💉 Assign shifts according to service and priority level.</dd>
  <dd> 🚑 Live visualisation of current appointments per queue.</dd>
  <dd> 🌡 Create different queue according to the services available.</dd>
  <dd> 🩻 Have the administration panel to manage the different data..</dd>
  <dd> 💊 Manage users and their permissions.</dd>
</dl>

<br> 🖥️ Used technology: Python - Django - PostgreSQL

🗒️ _Summary: The medial appontment system serves to organize medial appontment in a health institution, it allows to view all the information of the patients, availability services and delayof them._

**▶️ Running the project :**

1. After cloning the repository : `https://github.com/leilabritezneira/medicalAppointmentSystem.git `.<br>

2. Let's go to the project folder : `cd medicalAppointmentSystem `.<br> 

3. Let's start our virtual environment, which is already created and is called turnero-env : `turnero-env\scripts\activate `.<br>

4. We install our project requirements : `pip install -r requirements.txt `.<br>

5. Create a local database in PostgreSQL. <br>

6. We modify the settings.py file to connect the project to the recently created PostgreSQL database : <br>

```
'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '< your database name >',
        'USER': '< your user name >',
        'PASSWORD': '< your password >',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
```

7. We make the corresponding migrations of our tables to our database : `python manage.py makemigrations` + `python manage.py migrate `.<br>

8. We collect our static files : `python manage.py collectstatic `.<br>

9. We start our server : `python manage.py runserver `.<br>

10. Let's go to http://127.0.0.1:8000/ to see the interfaces of our application.<br>

<hr>
<h1> :es: Proyecto Final de Citas Médicas con Python </h1>
:octocat: En este repositorio encontrarás el Proyecto Final de Sistema Citas Médicas realizado durante el tercer semestre de la Tecnicatura Universitaria en Programación de la Universidad Tecnológica Nacional.
<br> 
<br> Durante el tercer semestre, hemos intensificado nuestro aprendizaje del lenguaje Python y su framework Django. Al mismo tiempo, hemos profundizado en el conocimiento de las bases de datos, en especialmente con PostgresSQL. Esta es la razón por la que el proyecto semestral se llevó a cabo con estas dos tecnologías.
<br>
<br>El proyecto es un sistema de citas médicas en el cual el usuario puede: 
<dl>
  <dd><br> 🩺 Registrar pacientes y servicios.
  <dd> 💉 Asignar turnos según servicio y su nivel de prioridad.
  <dd> 🚑 Visualizar en vivo los turnos actuales por fila.
  <dd> 🌡 Crear diferentes filas según los servicios disponibles.
  <dd> 🩻  Disponer del panel de administración para gestionar los diferentes datos.
  <dd> 💊 Gestionar usuarios y permisos de los mismos
</dl>

<br> 🖥️ Tecnología usada: Python - Django - PostgreSQL

🗒️ _Resumen: El sistema de citas médicas sirve para organizar la citación médica en una institución sanitaria, permite visualizar toda la información de los pacientes, servicios disponibles y demora de los mismos._

**▶️ Puesta en marcha del proyecto :**

1. Luego de clonar el repositorio : `https://github.com/leilabritezneira/medicalAppointmentSystem.git `.<br>

2. Accedemos a la carpeta del proyecto : `cd medicalAppointmentSystem `.<br> 

3. Iniciamos nuestro entorno virtual que ya está creado y se llama turnero-env : `turnero-env\scripts\activate `.<br>

4. Instalamos los requerimientos de nuestro proyecto : `pip install -r requirements.txt `.<br>

5. Creamos una base de datos local en PostgreSQL. <br>

6. Modificamos el archivo settings.py para conectar el proyecto con la base de datos PostgreSQL recién creada : <br>

```
'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '< nombre de su base de datos >',
        'USER': '< su usuario >',
        'PASSWORD': '< su contraseña >',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
```

7. Realizamos las migraciones correspondientes de nuestras tablas a nuestra base de datos : `python manage.py makemigrations` + `python manage.py migrate `.<br>

8. Recolectamos nuestros archivos estáticos : `python manage.py collectstatic `.<br>

9. Iniciamos nuestro servidor : `python manage.py runserver `.<br>

10. Entramos al http://127.0.0.1:8000/ para poder ver las interfaces de nuestra aplicación.<br>

<hr>
<h1> :fr: Projet Final de Rendez-vous Médicaux avec Python </h1>
:octocat: Dans ce dépôt, vous trouverez le projet final du système de rendez-vous médicaux réalisé au cours du troisième semestre du diplôme universitaire en programmation de l'Université Technologique Nationale.
<br>
<br>Au cours du troisième semestre, nous avons intensifié notre apprentissage du langage Python et de son framework Django. Parallèlement, nous avons approfondi notre connaissance des bases de données, en particulier PostgresSQL. C'est la raison pour laquelle le projet du semestre a été réalisé avec ces deux technologies. 
<br>
<br>Le projet est un système de rendez-vous médicaux dans lequel l'utilisateur peut : 
<dl>
  <dd><br> 🩺 Enregistrer les patients et les services.
  <dd> 💉 Attribuer des rendez-vous en fonction du service et du niveau de priorité.
  <dd> 🚑 Visualiser en direct les rendez-vous en cours, par rangées.
  <dd> 🌡 Créer différentes lignes en fonction des services disponibles.
  <dd> 🩻 Utiliser un panneau d'administration pour gérer les différentes données.
  <dd> 💊 Gérer les utilisateurs et leurs autorisations.
</dl>

<br> 🖥️ Technologie utilisée : Python - Django - PostgreSQL

🗒️ _Résumé: Le système de rendez-vous médicaux est utilisé pour organiser les rendez-vous médicaux dans un établissement de santé. Il permet de visualiser toutes les informations relatives au patient, les services disponibles et leurs délais._

**▶️ Démarrage du projet :**

1. Après avoir cloné le dépôt : `https://github.com/leilabritezneira/medicalAppointmentSystem.git `.<br>

2. Accédons au dossier du projet : `cd medicalAppointmentSystem `.<br> 

3. On démarre notre environnement virtuel qui est déjà créé et qui s'appelle turnero-env : `turnero-env\scripts\activate `.<br>

4. On installe les requis de notre projet : `pip install -r requirements.txt `.<br>

5. On crée une base de données locale dans PostgreSQL. <br>

6. On modifie le fichier settings.py pour connecter le projet à la base de données PostgreSQL récemment créée : <br>

```
'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '< nom de votre base de données >',
        'USER': '< votre utilisateur >',
        'PASSWORD': '< votre mot de pass >',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
```

7. On effectue les migrations correspondantes de nos tables vers notre base de données. : `python manage.py makemigrations` + `python manage.py migrate `.<br>

8. On recueille nos fichiers statiques : `python manage.py collectstatic `.<br>

9. On démarre notre serveur : `python manage.py runserver `.<br>

10. On se rend sur http://127.0.0.1:8000/ pour voir les interfaces de notre application.<br>
