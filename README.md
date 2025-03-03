# Learning Day - Airflow Setup Guide

### 1. Clone the Repo

Clone the project repository (or start a new one) and navigate into the directory:

```bash
git clone https://github.com/javieradh/airflow.git
cd airflow
```

### 2. Install Airflow

Install Apache Airflow using pip:

```bash
pip3 install apache-airflow
```

### 3. Initialize Airflow

Initialize the Airflow database:

```bash
airflow db init
```

### 4. Create Admin User

Create an admin user with the following command: (needed to access the Airflow UI, choose anything you want but ensure role = Admin)

```bash
airflow users create \
    --username admin \
    --password admin \
    --firstname Admin \
    --lastname Admin \
    --email admin@example.com \
    --role Admin
```

### 5. Ensure Your DAGs Are Stored in the Correct Folder

Make sure your DAGs are located in the correct folder, which should be specified in the `airflow.cfg` file (look for `dags_folder`). You may have to edit this file to point to the correct path.
e.g 

```bash
dags_folder = /Users/javiera.leemhuis/airflow_learning_day/dags
```

### 6. Start Webserver and Scheduler

Start both the webserver and the scheduler in separate terminals:

```bash
airflow webserver --port 8080
```

```bash
airflow scheduler
```

Once the webserver is running, you can navigate to the UI by going to:

http://localhost:8080
