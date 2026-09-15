<div align="center">

  <h1>Rodrigo Calderón</h1>
  <h3>Multiplatform Application Developer · Backend, ERP & Data Pipelines</h3>
  <p align="center">
    <b>English</b> | <a href="./README.es.md">Español</a>
  </p>
  <p>
    <a href="mailto:roro.calderon@hotmail.com">
      <img src="https://img.shields.io/badge/Outlook-Contact_Me-0078D4?style=for-the-badge&logo=microsoftoutlook&logoColor=white" alt="Email"/>
    </a>
    <a href="https://www.linkedin.com/in/rodrigo-calderon-dev/">
      <img src="https://img.shields.io/badge/LinkedIn-Conectar-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
    </a>
  </p>
  <p align="center">
  <a href="#about-me">About Me</a> •
  <a href="#tech-stack--tooling">Tech Stack</a> •
  <a href="#featured-projects">Featured Projects</a> •
  <a href="#lets-connect">Contact</a>
</p>

</div>

---
### About Me

Junior Software Developer and Higher Technician in **Multiplatform Application Development (DAM)** focused on backend architectures, workflow automation, and data handling.

* **Professional Experience:** Developed internal accounting and automated invoicing modules in **C#** and optimized relational databases at **BittaSoftware**.
* **International Mobility:** Co-designed data ingestion and predictive analytics software within a cross-border agile team (Romania Project), operating entirely in English across sprint planning, technical syncs, and codebase collaboration.
* **Core Philosophy:** Engineering maintainable backend architectures, ERP workflows (Odoo), and replacing manual operational bottlenecks with robust automated services.
* **Current Objective:** Seeking Junior Software Engineer / Backend Developer opportunities to contribute to production environments, collaborate with experienced engineering teams, and expand scalable software systems.
* **Location:** Barcelona, Spain (Open to hybrid and remote opportunities).

---

### Tech Stack & Tooling

<div align="center">

| Area | Technologies |
| :--- | :--- |
| **Languages** | ![C#](https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=csharp&logoColor=white) ![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white) ![Kotlin](https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white) ![Dart](https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)|
| **Enterprise & Data** | ![Odoo](https://img.shields.io/badge/Odoo-714B67?style=for-the-badge&logo=odoo&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)|
| **Databases** | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white) ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white) |
| **Frameworks & Core** | ![.NET](https://img.shields.io/badge/.NET-512BD4?style=for-the-badge&logo=dotnet&logoColor=white) ![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white) ![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white) ![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white) |

</div>

---

### Featured Projects

---

#### 1. Predictive Real Estate Pipeline & Enterprise Analytics
> Multi-layer Medallion Architecture processing raw ingestion streams into predictive models and enterprise reporting.

```mermaid
flowchart LR
    A["<b>Raw Ingestion (Bronze)</b><br/>• Multi-source listings<br/>• Python / Staging Storage"]
    -->|Cleansing & Outlier Filtering| B["<b>Curated Storage (Silver)</b><br/>• Star Schema Modeling<br/>• PostgreSQL Relational Store"]
    -->|Aggregations & KPIs| C["<b>Business Layer (Gold)</b><br/>• Predictive ML Models<br/>• Standardized Metric Sets"]
    -->|Analytics & Simulation| D["<b>Enterprise Endpoints</b><br/>• Power BI Dashboards<br/>• SAP Operational Sync"]

    classDef default fill:#161b22,stroke:#0078d4,stroke-width:1.5px,color:#e6edf3;
```

* **Context & International Collaboration:** Co-engineered in an English-speaking cross-border agile team (Spain, Switzerland, Romania, Portugal), driving daily standups, Git branch workflows, and technical handoffs entirely in English.
* **Medallion Pipeline Architecture:**
  * **Bronze Layer:** Automated extraction and ingestion of unstructured real estate and market feeds.
  * **Silver Layer:** Cleaned datasets, resolved missing dimensions, and structured normalized dimensional models inside **PostgreSQL**.
  * **Gold Layer:** Executed metric aggregation pipelines and trained predictive algorithms using **Pandas** and scientific computing modules.
* **Enterprise Reporting & Business Validation:** Designed stakeholder dashboards in **Power BI** and mapped outputs into **SAP** environments to validate business operations.
* **Impact:** Reduced manual dataset wrangling from hours per sprint to scripted end-to-end pipelines running in under 2 minutes.
* **Tech Stack:**
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Power_BI-F2C811?style=flat-square&logo=powerbi&logoColor=black"/>
  <img src="https://img.shields.io/badge/SAP-008FD3?style=flat-square&logo=sap&logoColor=white"/>

---

#### 2. Enterprise Financial & Invoice Automation
> High-integrity accounting and recurring invoice automation module built for core enterprise operations.

```mermaid
flowchart LR
    A["<b>Client Layer (UI)</b><br/>WinForms Desktop Client (.NET)<br/>• Transactional Desktop Interfaces<br/>• Invoice Data Input & Validation<br/>• Modular UI Workflows"]
    -->|Secure HTTPS / JSON Payloads| B["<b>API & Business Logic Layer</b><br/>ASP.NET Core REST API<br/>• RESTful Controllers & Routing<br/>• Model Validation & Rules<br/>• Core Transactional Logic"]
    -->|ADO.NET & Stored Procedures| C["<b>Persistence Layer</b><br/>SQL Server Database<br/>• Robust Stored Procedures<br/>• Duplicate Elimination Logic<br/>• ACID Concurrency Locks"]
    -->|Automated Batch Pipeline| D["<b>Accounting Module Output</b><br/>Enterprise Accounting Ledger<br/>• Automated Invoicing Records<br/>• Recurring Invoice Processing<br/>• Batch Financial Reports"]

    classDef default fill:#161b22,stroke:#239120,stroke-width:1.5px,color:#e6edf3;
```

* **Context & Team Structure:** Developed in production during software developer internship at **BittaSoftware**, collaborating directly in a 2-person engineering unit alongside the Senior Lead Developer through pair programming and code reviews.
* **Architecture & UI:** Developed transactional desktop interfaces using **WinForms (.NET)**, integrating modular UI workflows with backend business logic.
* **API & Routing:** Implemented RESTful controllers and endpoint routing in **ASP.NET Core** to decouple desktop clients from database operations and secure data payloads.
* **Transaction Safety:** Structured robust SQL Server stored procedures and validation logic to eliminate duplicate invoice records and handle concurrency.
* **Impact:** Replaced manual cross-spreadsheet data entry, saving 5–7 administrative hours weekly.
* **Tech Stack:**
  <img src="https://img.shields.io/badge/C%23-239120?style=flat-square&logo=csharp&logoColor=white"/>
  <img src="https://img.shields.io/badge/.NET-512BD4?style=flat-square&logo=dotnet&logoColor=white"/>
  <img src="https://img.shields.io/badge/WinForms-239120?style=flat-square&logo=windows&logoColor=white"/>
  <img src="https://img.shields.io/badge/ASP.NET_Core-512BD4?style=flat-square&logo=dotnet&logoColor=white"/>
  <img src="https://img.shields.io/badge/SQL_Server-CC292B?style=flat-square&logo=microsoftsqlserver&logoColor=white"/>


---

#### 3. EasyTeeth · Clinical Scheduling & Dental Management System
> Distributed multiplatform system coordinating real-time clinical box allocation, odontologist schedules, and patient records.

```mermaid
flowchart LR
    A["<b>Android Client (Kotlin)</b><br/>• MVVM Architecture<br/>• Retrofit 2 + Coroutines<br/>• Non-blocking UI Threads"]
    -->|Asynchronous REST Calls| B["<b>Domain Routing API</b><br/>• Scheduling & Slot Allocation<br/>• Clinical Assets & Odontograms<br/>• Patient & Medical Records"]
    -->|Spring Boot & Hibernate| C["<b>MySQL Persistence</b><br/>• Relational Constraints<br/>• ACID Slot Reservations<br/>• Medical Histories"]

    classDef default fill:#161b22,stroke:#7f52ff,stroke-width:1.5px,color:#e6edf3;
```
* **Context & Team Collaboration:** Co-engineered across a 9-month lifecycle (September to May) in a 4-developer engineering team at STUCOM (Barcelona), driving sprint iterations, Git branching strategies, and full ownership of mobile network architecture.
* **Mobile Client:** Built a native mobile interface in **Android Studio using Kotlin**, consuming asynchronous REST endpoints and managing real-time inventory states.
* **Backend Architecture:** Developed a decoupled REST API with **Java & Spring Boot**, handling business logic, resource routing, and secure payload serialization.
* **API Testing & Documentation:** Validated HTTP methods, request headers, and response payloads using **Postman** (contract testing and endpoint simulation).
* **Concurrency Control:** Engineered transactional database locks in **MySQL** to eliminate race conditions and prevent double-booking of surgical boxes.
* **Tech Stack:** 
  <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white"/>
  <img src="https://img.shields.io/badge/Android-3DDC84?style=flat-square&logo=android&logoColor=white"/>
  <img src="https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white"/>
  <img src="https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white"/>
  <img src="https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white"/>
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white"/>

---

#### 4. Custom ERP & Business Workflow Automation
> Custom module development, business logic extension, and data integration within Odoo ecosystem.

```mermaid
flowchart LR
    A["<b>UI & Presentation Layer</b><br/>Odoo Web Interface<br/>• Custom XML Views & Forms<br/>• Kanban & Tree Layouts<br/>• Operational Action Triggers"]
    -->|User Requests & RPC| B["<b>Business Logic Layer</b><br/>Python & Odoo ORM<br/>• Modular Business Rules<br/>• Automated Record Computed Fields<br/>• Pipeline Event Hooks"]
    -->|ORM Relational Queries| C["<b>Persistence Layer</b><br/>PostgreSQL Database<br/>• Relational Integrity Checks<br/>• Transactional Table Locking<br/>• Automated Record Auditing"]
    -->|Workflow Automation| D["<b>Operational Output</b><br/>Enterprise Workflows<br/>• Real-Time Inventory Updates<br/>• Automated Sales Orders<br/>• Synchronization Exports"]

    classDef default fill:#161b22,stroke:#714B67,stroke-width:1.5px,color:#e6edf3;
```

* **Context & Team Collaboration:** Co-developed within a 3-developer team at STUCOM (Barcelona), collaborating on module specifications, version control workflows, and business requirement mapping.
* **Architecture:** Developed modular extensions using **Python** and **Odoo ORM** to automate sales and inventory operational flows.
* **Data Integration:** Designed relational database constraints and automated record synchronization backed by **PostgreSQL**.
* **Tech Stack:**
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Odoo-714B67?style=flat-square&logo=odoo&logoColor=white"/>
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white"/>

  ---

#### 5. NexTech · Tech Event Discovery & Ticketing Portal
> Geolocation-aware discovery platform aggregating regional tech events with direct ticketing routing.

```mermaid
flowchart LR
    A["<b>Client Browser & UI</b><br/>Semantic HTML5 & CSS3<br/>• Mobile-First Responsive Grid<br/>• Dynamic Event Catalog View<br/>• Category & Proximity Inputs"]
    -->|DOM Events & Filtering| B["<b>Client-Side Logic (PoC)</b><br/>Vanilla JavaScript Engine<br/>• Event State & Filtering Engine<br/>• Mock Dataset Ingestion (JSON)<br/>• Dynamic DOM Node Injection"]
    -->|Simulated Checkout Flow| C["<b>Referral Simulation Layer</b><br/>Ticketing Prototype<br/>• Mock Deep-Link Redirections<br/>• Simulated Seat Reservation<br/>• Outbound Navigation Models"]

    classDef default fill:#161b22,stroke:#f7df1e,stroke-width:1.5px,color:#e6edf3;
```

* **Context & Team Collaboration:** Built in a 3-developer team at STUCOM (Barcelona) as a frontend Proof of Concept (PoC) to benchmark vanilla JavaScript DOM rendering speeds and simulate user journeys.
* **Client-Side Architecture:** Implemented dynamic filtering algorithms in **vanilla JavaScript** using structured mock JSON datasets to simulate real-time search queries by category and proximity.
* **Referral Flow Simulation:** Designed deep-linking outbound patterns to emulate user handoffs to third-party vendor platforms for ticket checkout and seat allocations.
* **Zero-Dependency Styling:** Structured a lightweight, mobile-first interface using semantic **HTML5** and modern **CSS3** (Flexbox/Grid), eliminating heavy UI framework overhead.
* **Tech Stack:**
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white"/>
---

### Let's Connect

I am currently open to **Junior Backend Developer**, **Data Engineering**, and **ERP Consulting** roles in Barcelona (hybrid or on-site).

<a href="mailto:roro.calderon@hotmail.com"><img src="https://img.shields.io/badge/OUTLOOK-CONTACT_ME-0078D4?style=flat-square&logo=microsoftoutlook&logoColor=white"/></a>
<a href="https://www.linkedin.com/in/rodrigo-calderon-dev/"><img src="https://img.shields.io/badge/LINKEDIN-CONNECT-0A66C2?style=flat-square&logo=linkedin&logoColor=white"/></a>

Feel free to reach out for technical inquiries, project collaborations, or engineering opportunities.
