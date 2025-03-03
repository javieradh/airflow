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

### 3. Check Configuration Files

Ensure that your Airflow configuration files are correctly set up. You can check the `airflow.cfg` file located in the `AIRFLOW_HOME` directory for correct configurations.

### 4. Initialize Airflow

Initialize the Airflow database:

```bash
airflow db init
```

### 5. Create Admin User

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

### 6. Ensure Your DAGs Are Stored in the Correct Folder

Make sure your DAGs are located in the correct folder, which should be specified in the `airflow.cfg` file (look for `dags_folder` under the `[core]` section).

### 7. Start Webserver and Scheduler

Start both the webserver and the scheduler in separate terminals:

```bash
airflow webserver --port 8080
```

```bash
airflow scheduler
```

