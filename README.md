# 📜 A Proclamation Regarding the Noble Data Engineering Books ETL Pipeline Project! 📜

## 🗂️ Table of Contents

1. 📜 [Of Overview and Noble Purpose](#-of-overview-and-noble-purpose)  
2. 📜 [Of Purpose, Intention, and Worthy Usage](#-of-purpose-intention-and-worthy-usage)  
3. 🖼️ [BEHOLD! The Diagrammatic Depiction of the ETL Pipeline](#-behold-the-diagrammatic-depiction-of-the-etl-pipeline)  
4. ✨ [Features of Noble Craft](#-features-of-noble-craft)  
5. 🏗️ [The Grand Architecture](#-the-grand-architecture)  
   - 🧩 [Components of Ye ETL Pipeline](#-components-of-ye-etl-pipeline)  
6. 🚀 [For the Journeyman Getting Started](#-for-the-journeyman-getting-started)  
   - ⚙️ [Preparations for Thy Quest](#-preparations-for-thy-quest)  
   - 📥 [Commencement of Deployment](#-commencement-of-deployment)  
7. 🛠️ [Usage of This Mechanism](#-usage-of-this-mechanism)  
8. 🔧 [Customize to Thy Liking](#-customize-to-thy-liking)  
9. 📂 [Project Structure](#-project-structure)  
10. ⚠️ [Known Issues and Their Vanquishment](#-known-issues-and-their-vanquishment)  
11. 🎯 [A Roadmap of Future Glories](#-a-roadmap-of-future-glories)  
12. 🤝 [The Spirit of Fellowship](#-the-spirit-of-fellowship)  
13. 📜 [License](#-license)
14. 📖 [For the Unversed in Antiquity’s Tongue](#-for-the-unversed-in-antiquitys-tongue)

## 🌟Of Overview and Noble Purpose
Greetings, kind scholars and brave data wranglers! Lend thy ears and open thine eyes, for I shall regale thee with the tale of a most wondrous endeavor: the Books ETL Pipeline Project. In this hallowed pursuit, we dost weave together the intricate threads of data extraction, transformation, and loading to uncover knowledge most profound.

This grand mechanism, devised by tireless toil and wisdom, doth unite the realms of Python, Docker, PostgreSQL, and Airflow. By its might, one may harvest bookly treasures from the vast libraries of OpenLibrary and Google Books, cleanse and refine them, and store them in databanks for enlightenment and analysis.

Lo, this project is not merely a tool but a masterwork that doth exemplify the art and science of data engineering. Scholars, practitioners, and seekers of wisdom alike may find value herein, as it is both a tome of learning and a marvel of modern craft.

Thus, embark, good reader, upon this journey of discovery, and let the annals of data yield their secrets unto thee!

## 📜 Of Purpose, Intention, and Worthy Usage 📜
Hark! This noble endeavor is fashioned to fetch and hold knowledge, tracking the comings and goings of books upon the digital shelves. But lo! Its utility extendeth far beyond the boundaries of this humble purpose. Prithee know, fair user, that **thou mayest adapt its workings to suit thine own curiosities.** By a simple **tweak of query**, *thou mayest turn this engine toward thine own pursuits*—be it tracking wares, scrolls, or other matters of great import. Wield this tool as thy will decrees, and may it serve thee well in thy noble quests!

## 🖼️ BEHOLD! The Diagrammatic Depiction of the ETL Pipeline 🖼️
Hear ye, hear ye! Gather thy gaze upon this most wondrous depiction of the grand ETL pipeline!

Within its bounds, thou shalt witness the harmonious interplay of myriad parts, each a vital cog in this celestial mechanism. From Security Sanctuaries to ensure the sacred safety of thine operations, to the Testing Grounds whereupon thy code is proven and hardened, this diagram illustrates the majestic flow of data, transformed from its humble JSON origins into a regal table of fields—fit for analysis and insight.
![Ye Old Diagrams of Pipeline Wizardry](Books%20ETL%20Architecture%20Diagram1.jpg)
![Ye Old Diagrams of Pipeline Wizardry](Books%20ETL%20Architecture%20Diagram2.jpg)
![Ye Old Diagrams of Pipeline Wizardry](Books%20ETL%20Architecture%20Diagram3.jpg)

🔒 **Security:** Lo, the bastions of access control and protection, ensuring no ill-begotten hand may meddle with the data's purity.

🧪 **Testing:** Prithee, regard this as the proving grounds where robustness is forged, where bugs are vanquished, and the pipeline stands resilient.

🐳 **Docker Enclosure:** Witness the orchestration of containers, wherein each component dwelleth in isolation yet communicateth with precision, making the entire pipeline agile and portable.

📤 **Data Extraction:** Here lieth the cradle of our endeavor, whence data is lifted from its JSON confines and set forth upon its transformative journey.

🛠️ **Data Transformation:** The alchemy of the pipeline! Fields are cleansed, shaped, and readied for their destined purpose. Here, titles, authors, years, and sources are refined into their final glorious forms.

📊 **Final Table:** The culmination of all labors! Behold the tabular majesty, wherein the fruits of thy efforts—titles, authors, publication years, and more—stand ready to enlighten thy endeavors.

🎩 **Airflow Sorcery:** Marvel at the enchanted scheduler, tirelessly orchestrating the pipeline's every step with grace and precision.
![Airflow_1](airflow_books1.PNG)
*Here, in this tableau of wisdom, the ETL process cometh alive. Gaze upon its intricacies, for herein liest not just a method but a marvel, where chaos is tamed and knowledge is borne.*

## ✨ Features of Noble Craft
- 🛠️ **Extraction of Many Founts:** Gathers knowledge from the OpenLibrary and Google Books APIs, like a wise scholar pulling treasures from ancient tomes.
- 🧹 **Purification of Data:** Cleanseth and enriches the raw information, ensuring it is fair and fit for study.
- 📊 **Integration with the Repository of Postgres:** Deposits the bounty into a steadfast database for safekeeping and recall.
- 🛡️ **Defenses and Logging of Errors:** Implements vigilant sentinels to guard against mishaps and record the chronicles of the pipeline.
![Logs2](airflow_books_log2.PNG)

- ⏰ **Automation of Timely Tasks:** Employeth the magic of Airflow to schedule thy tasks, ensuring they commence with precision.
![airflowgant](airflow_books_log3.PNG)

- 📩 **Slack Heraldry:** Dispatches messengers to announce the state of thine efforts in real-time.
![Slackexample](slack_books_etl.PNG)

- 📦 **Encasement in Docker’s Vessel:** Encircles the pipeline in the aegis of Docker for deployment and scaling to lands far and wide.
![Dockerimagepng](docker_books_etl.PNG)
---
## 🏗️ The Grand Architecture
### 🧩 Components of Ye ETL Pipeline
1. **🔍 Extraction:**

- Summoneth data from OpenLibrary and Google Books 📡.
- Handles peculiarities of pagination and rate limits, like a skilled juggler with flaming torches.
2. **🔄 Transformation:**

- Cleanseth and standardizes the records 🧼.
- Resolves missing fields and maketh the data ready for usage.
3. **📥 Loading:**

- Deposits the enriched bounty into Postgres’ eternal vaults 💾.
- Employeth conflict resolution to smite duplicate entries.
4. **🌀 Orchestration:**

- Commands the dance of tasks through an Airflow DAG ♻️.
- Schedules and retries with the wisdom of experience 🕒.
5. **🐳 Containerization:**

- Packages all components within Docker's might vessel 🌍.
- Uses Docker Compose to steer the ships 🎛️.
6. **🔔 Monitoring:**

- Announceth pipeline statuses via Slack 📲.
- Airflow's interface reveals all activity 📋.

## 🚀 For the Journeyman Getting Started
### ⚙️ Preparations for Thy Quest
- 🐳 Docker & Docker Compose
- 🐍 Python 3.8 or above
- 📜 requirements.txt should provide thee with required Python incantations
- 🔐 Slack Token, should thou seek notifications
- 🛠️ Basic wit in SQL and Python

## 📥 Commencement of Deployment
1. **Cloneth the repository:**

    ``` bash
    git clone https://github.com/VBlackie/books_etl.git
    cd Books_ETL_Pipeline
2. **Declare Thy Secrets:** Create a .env file with:

    ```
    POSTGRES_USER=airflow
    POSTGRES_PASSWORD=airflow
    POSTGRES_DB=books_db
    AIRFLOW__WEBSERVER__SECRET_KEY=<your_secret_key>
    AIRFLOW_ADMIN_USERNAME=admin
    AIRFLOW_ADMIN_PASSWORD=admin
    SLACK_CHANNEL=<your-slack-channel>
    SLACK_API_TOKEN=<your-slack-api-token>
    GOOGLE_BOOKS_API_KEY=<your-google-books-api-key>
3. **Raise Thy Docker Containers:**

    ```
    docker-compose up --build
4. **Enter the Interface of Airflow:**

    - Navigate to http://localhost:8080.
    - Credentials:
    Username: admin
    Password: admin

## 🛠️ Usage of This Mechanism
- Command Thy Pipeline through the hallowed Airflow UI 🌀.
![Airflow_2](airflow_books2.PNG)

- Monitor Thy Logs with diligence for assurance 📜.
![Logs1](airflow_books_log1.PNG)

- Query Thy Database and unearth its treasures:
Should thou prefer the sanctity of pgAdmin4:
![PGadmin](Pgadmin_books_etl.PNG)

- Connect unto the database with the following credentials:
    - Host: localhost
    - Port: 5433
    - Username: airflow
    - Password: airflow
    - Database Name: books_db
  
Alternatively, should thou be inclined to use the command line:

    psql -h localhost -p 5433 -U airflow -d books_db

## 🔧 Customize to Thy Liking

✍️ **Modify the Query to Suit Thy Quest**  
Dost thou seek knowledge beyond data engineering? Fear not, for the script is designed to be molded to thy whims! Within the sacred function `extract_books_data` in `extract.py`, thou shalt find the query:
    
    def extract_books_data(): 
    url = 'https://openlibrary.org/search.json?q=data+engineering'  # Focused query on data engineering
Replace 'data+engineering' with the essence of thy pursuit. Forsooth, be it "philosophy", "alchemy", or any subject dear to thee, and lo, the knowledge shall be fetched accordingly.

### 🛠️ Add Thine Own Sources

Should thee wish to extend the reach of this mechanism, thou mayst craft a new script for extracting data. To ensure thy creation aligns with the grand pipeline, thou must honor the sacred format of the `transform.py script`. The records must be transformed thusly:
    
    transformed_data.append({
        'title': book['title'],
        'author': book['author'],
        'published_date': book['published_date'],
        'isbn': book['isbn'],
        'source': book['source']
    })

This ensures the data from thy new source melds seamlessly with the rest of the enriched tome of knowledge.

### ⚔️ Test for Compatibility and Righteousness

Ere thou dost deploy thy customizations, ensure thy worketh withstands the trials of unit tests. Use the tests provided within the tests/ realm to confirm compatibility. The command to summon the trials is:
    
    pytest tests/

Run this incantation within thy project’s sanctuary to verify thy changes passeth all scrutiny.
### 🛡️ Heed These Words
By following these steps, thou canst tailor this repository to serve thy most peculiar pursuits. Modify, expand, and test—this pipeline shall bend to thy will whilst retaining its elegance and might.

## 📂 Project Structure

📁 Books_ETL_Pipeline/ 

├── 📂 dags/    
│   ├── book_etl_dag.py         # DAG of Airflow  
│   ├── extract.py              # Gatherer of Data from OpenLibrary  
│   ├── extract_from_google.py  # Gatherer of Data from GoogleBooks  
│   ├── transform.py            # Purifier of Records  
│   ├── load.py                 # Depositor of Information  
│   ├── slack_notifications.py  # Herald of Notifications  
├── 📂 logs/                    # Chronicles of Airflow  
├── 📂 plugins/                 # Custom Enhancements  
├── 📂 tests/                   # Realm of Testing and Validation  
│   ├── test_extract.py         # Examiner of Gatherer Logic  
│   ├── test_transform.py       # Scrutinizer of Data Purification  
│   ├── test_load.py            # Overseer of Data Deposition  
│   ├── test_etl_pipeline.py    # Examiner of Integrity  
├── 🐳 docker-compose.yml       # Configuration of the Fleet  
├── 📜 requirements.txt         # The Scroll of Dependencies  
└── 🌐 .env                     # Hidden Secrets 

## ⚠️ Known Issues and Their Vanquishment
1. **Scheduler Heartbeat Falters 🛠️:**
- Ensure Airflow volumes are intact.
- Use docker system prune -f to cleanse thy setup.
2. **SQL Insert Woes 🔄:**
- Ensure table schema matches the load.py script.
3. **Log Vanish into the Ether 🧐:**
- Verify mappings in docker-compose.yml
4. **The Goblins of Slumber Delay Thy Database 💤:**  
- At first run, the database machinery doth refuse to awaken promptly, for the goblins within linger in slumber.  
- Prithee, restart thy services twice, and lo, the machinery shall spring to life!  
## 🎯 A Roadmap of Future Glories
- 🌐 Extend support to Goodreads or others.
- 📈 Bind the pipeline with Metabase for noble visualization.
- 📊 Enhance metadata reporting.
- 🚀 Embrace CI/CD for automated testing.

## 🤝 The Spirit of Fellowship
Contributions are welcome! Sharpen thy code and submit thy Pull Requests. Together, let us make this project legendary 🌟.
## 📜 License
This project is bestowed under the MIT License. It is free to use, modify, and cherish.

## 📖 For the Unversed in Antiquity’s Tongue
A Glossary of Ye Olde Terms

Fear not, gentle reader, should the flowery language of this proclamation confound thee! Below is a humble guide to the more curious words thou mayst encounter within this hallowed text:
- Alas! – A cry of sorrow or regret, used to express lamentation.
Example: "Alas! The goblins of slumber delay thy database!"

- Anon – Soon, shortly, in a little while.
Example: "Deploy thy pipeline anon and uncover treasures untold!"

- Behold! – Look upon this with awe and wonder!
Example: "Behold! The Diagrammatic Depiction of the ETL Pipeline!"

- Doth – An archaic form of 'does,' used for emphasis.
Example: "Lo, this project doth exemplify the art of data engineering."

- Hark! – Pay heed! Listen well, for what follows is of utmost importance.
Example: "Hark! This noble endeavor is fashioned to fetch and hold knowledge!"

- Hear ye! Hear ye! – An announcement or proclamation, commanding attention.
Example: "Hear ye, hear ye! Gather thy gaze upon this most wondrous depiction!"

- Lo! – Behold! A word to draw attention to something noteworthy.
Example: "Lo, this pipeline is not merely a tool but a masterwork!"

- Methinks – I believe, I consider, or it seems to me.
Example: "Methinks this endeavor shall serve thee well in thy noble quest!"

- Prithee – I entreat thee, or I ask of thee.
Example: "Prithee know, fair user, that thou mayest adapt its workings."

- Thou/Thy/Thee/Thine – You/Your/To You/Yours (respectively).
Example: "Command thy pipeline and monitor thy logs with diligence."

- Verily – Truly, indeed, without a doubt.
Example: "Verily, this mechanism is a marvel of data engineering!"

