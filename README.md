# 📚 Data Engineering Books ETL Pipeline Project 🚀
## 🌟Overview
This project is a 🌐 Extract, Transform, Load (ETL) pipeline designed to bring book data from various APIs to life 📖! It automates the process of fetching, cleaning, and storing book data into a PostgreSQL database 🐘. With Apache Airflow 🌀 orchestrating the tasks and Docker 🐳 ensuring portability, this pipeline is ready to tackle real-world data engineering challenges.

## ✨ Features
- 🛠️ Multi-Source Data Extraction: Integrates with OpenLibrary and Google Books APIs.
- 🧹 Data Transformation: Ensures clean and consistent data for easy analysis.
- 📊 PostgreSQL Integration: Stores enriched data for long-term use.
- 🛡️ Error Handling and Logging: Robust mechanisms to track and resolve issues.
- ⏰ Scheduled Automation: Automates the workflow using Apache Airflow.
- 📩 Slack Notifications: Keeps you in the loop with real-time updates.
- 📦 Containerized Deployment: Fully Dockerized for easy setup and scaling.
---
## 🏗️ Architecture
🧩 Components
1. 🔍 Extract:

Fetches data from OpenLibrary and Google Books APIs 📡.
Handles API quirks like pagination and rate limits.
2. 🔄 Transform:

Cleanses and enriches data 🧼.
Standardizes formats and resolves missing fields.
3. 📥 Load:

Inserts clean data into a PostgreSQL database 💾.
Uses conflict resolution to prevent duplicate entries.
4. 🌀 Orchestration:

Airflow DAG to manage task dependencies and retries ♻️.
Automatic scheduling for hands-free operation 🕒.
5. 🐳 Containerization:

Dockerized setup ensures easy deployment everywhere 🌍.
Docker Compose orchestrates all services 🎛️.
6. 🔔 Monitoring:

Slack integration for pipeline notifications 📲.
Airflow UI for manual runs and monitoring 📋.
## 🚀 Getting Started
### ⚙️ Prerequisites
- 🐳 Docker & Docker Compose
- 🐍 Python 3.8
- 🔐 Slack API Token (optional for notifications)
- 🛠️ Basic SQL & Python Knowledge
## 📥 Installation
1. Clone the repository:

    ``` bash
    git clone https://github.com/yourusername/Books_ETL_Pipeline.git
    cd Books_ETL_Pipeline
2. Set up environment variables: Create a .env file with:

    ```
    SLACK_API_TOKEN=<your-slack-api-token>
    POSTGRES_USER=airflow
    POSTGRES_PASSWORD=airflow
    POSTGRES_DB=books_db
3. Start the containers:

    ```
    docker-compose up --build
4. Access Airflow UI:

Navigate to http://localhost:8793.
Login:
Username: admin
Password: admin
## 🛠️ Usage
Trigger the pipeline in the Airflow UI 🌀.
Monitor logs for task statuses 📜.
Query your PostgreSQL database for enriched data 📊:
    ```psql -h localhost -p 5433 -U airflow -d books_db```
    
## 📂 Project Structure
    ```
        📁 Books_ETL_Pipeline/
        ├── 📂 dags/
        │   ├── book_etl_dag.py         # Airflow DAG definition
        │   ├── extract.py              # Data extraction scripts
        │   ├── transform.py            # Data transformation scripts
        │   ├── load.py                 # Data loading scripts
        ├── 📂 logs/                    # Airflow logs
        ├── 📂 plugins/                 # Custom Airflow plugins
        ├── 🐳 docker-compose.yml        # Docker Compose configuration
        ├── 🌐 .env                     # Environment variables
        └── 📖 README.md
    
## Project documentation
📊 DAG Overview
Here's the DAG in action! 🎢

<!-- Add the actual DAG image here -->

## ⚠️ Known Issues
1. Scheduler Heartbeat Errors 🛠️:

- Ensure Airflow volumes are properly set up.
- Try docker system prune -f to clean up and restart the containers.
2. SQL Insert Errors 🔄:

- Ensure table schema matches the load.py script.
3. Log File Issues 🧐:

- Check the Airflow logs/ directory mapping in docker-compose.yml.
## 🎯 Roadmap
- 🌐 Add support for more data sources (e.g., Goodreads API).
- 📈 Integrate with visualization tools like Metabase or Looker Studio.
- 📊 Enhance metadata tracking and reporting.
- 🚀 Add CI/CD for automated testing and deployment.
## 🤝 Contributing
Contributions are welcome! Submit your PRs to make this project even better 🌟.

## 📜 License
This project is licensed under the MIT License.