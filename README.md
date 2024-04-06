## Configuración inicial
### Paso a paso para poder clonar el repo
#### 0. Prerequisitos
-  [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
-  [Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
-  [git-remote-codecommit](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-git-remote-codecommit.html#setting-up-git-remote-codecommit-install)
-  [Docker](https://docs.docker.com/engine/install/) & [docker-compose](https://docs.docker.com/compose/install/)

#### 1. Configurar credenciales
Ejecuta el siguiente comando en tu terminal de preferencia:
```sh
aws configure
```
E introduce las credenciales previamente proporcionadas.

#### 2. Clonar el repositorio
Clonar el repositorio en la ruta deseada:
```sh
git clone codecommit::us-east-1://Odoo-Track0-Repo
```
Y accede a la carpeta del proyecto:
```sh
cd Odoo-Track0-Repo/
```

#### 3. Ejecutar Docker-Compose
Para levantar los servicios definidos en el archivo **docker-compose.yml**, ejecuta el siguiente comando en la raíz del repositorio:
```sh
docker-compose up
```
Para detener y eliminar los contenedores creados por Docker-Compose, utiliza el siguiente comando:
```sh
docker-compose down
```

#### 4. Acceso a Odoo a través del navegador
Una vez que Odoo esté en ejecución, abre tu navegador web y visita la siguiente URL:
```sh
http://localhost:8069
```