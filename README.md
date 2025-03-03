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

# Learning Day - Ideas on what to try out!


1. **Multiple Tasks & Dependencies**  
   Create a DAG with a few tasks and set some simple dependencies between them.

2. **XCom**  
   Pass data between tasks using XCom to see how tasks can communicate with each other.

3. **Task Retry Logic**  
   Add retry logic to a task that might fail, and set up some retry delay just in case.

4. **Schedule a DAG**  
   Make a DAG run automatically on a schedule (like daily) using cron expressions or preset schedules like `@daily`.

5. **Branching**  
   Use the `BranchPythonOperator` to split tasks into different paths depending on conditions.
