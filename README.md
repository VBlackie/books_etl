# 📜 A Proclamation Regarding the Noble Data Engineering Books ETL Pipeline Project! 📜
## 🌟Overview
Hear Ye, Hear Ye!
Greetings, kind scholars and brave data wranglers! Lend thy ears and open thine eyes, for I shall regale thee with the tale of a most wondrous endeavor: the Books ETL Pipeline Project. In this hallowed pursuit, we dost weave together the intricate threads of data extraction, transformation, and loading to uncover knowledge most profound.

This grand mechanism, devised by tireless toil and wisdom, doth unite the realms of Python, Docker, PostgreSQL, and Airflow. By its might, one may harvest bookly treasures from the vast libraries of OpenLibrary and Google Books, cleanse and refine them, and store them in databanks for enlightenment and analysis.

Lo, this project is not merely a tool but a masterwork that doth exemplify the art and science of data engineering. Scholars, practitioners, and seekers of wisdom alike may find value herein, as it is both a tome of learning and a marvel of modern craft.

Thus, embark, good reader, upon this journey of discovery, and let the annals of data yield their secrets unto thee!

## 📜 Of Purpose, Intention, and Worthy Usage 📜
Hark! This noble endeavor is fashioned to fetch and hold knowledge, tracking the comings and goings of books upon the digital shelves. But lo! Its utility extendeth far beyond the boundaries of this humble purpose. Prithee know, fair user, that thou mayest adapt its workings to suit thine own curiosities. By a simple tweak of query, thou mayest turn this engine toward thine own pursuits—be it tracking wares, scrolls, or other matters of great import. Wield this tool as thy will decrees, and may it serve thee well in thy noble quests!

## 🖼️ BEHOLD! The Diagrammatic Depiction of the ETL Pipeline 🖼️
Hear ye, hear ye! Gather thy gaze upon this most wondrous depiction of the grand ETL pipeline!

Within its bounds, thou shalt witness the harmonious interplay of myriad parts, each a vital cog in this celestial mechanism. From Security Sanctuaries to ensure the sacred safety of thine operations, to the Testing Grounds whereupon thy code is proven and hardened, this diagram illustrates the majestic flow of data, transformed from its humble JSON origins into a regal table of fields—fit for analysis and insight.
![Ye Old Diagrams of Pipeline Wizardry](Books%20ETL%20Architecture%20Diagram.jpg)
🔒 Security: Lo, the bastions of access control and protection, ensuring no ill-begotten hand may meddle with the data's purity.

🧪 Testing: Prithee, regard this as the proving grounds where robustness is forged, where bugs are vanquished, and the pipeline stands resilient.

🐳 Docker Enclosure: Witness the orchestration of containers, wherein each component dwelleth in isolation yet communicateth with precision, making the entire pipeline agile and portable.

📤 Data Extraction: Here lieth the cradle of our endeavor, whence data is lifted from its JSON confines and set forth upon its transformative journey.

🛠️ Data Transformation: The alchemy of the pipeline! Fields are cleansed, shaped, and readied for their destined purpose. Here, titles, authors, years, and sources are refined into their final glorious forms.

📊 Final Table: The culmination of all labors! Behold the tabular majesty, wherein the fruits of thy efforts—titles, authors, publication years, and more—stand ready to enlighten thy endeavors.

🎩 Airflow Sorcery: Marvel at the enchanted scheduler, tirelessly orchestrating the pipeline's every step with grace and precision.

Here, in this tableau of wisdom, the ETL process cometh alive. Gaze upon its intricacies, for herein liest not just a method but a marvel, where chaos is tamed and knowledge is borne.

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