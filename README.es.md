<div align="center">

  <h1>Rodrigo Calderón</h1>
  <h3>Desarrollador de Aplicaciones Multiplataforma · Backend, ERP & Data Pipelines</h3>

  <p>
    <a href="./README.md">English</a> | <b>Español</b>
  </p>

  <p>
    <a href="mailto:roro.calderon@hotmail.com">
      <img src="https://img.shields.io/badge/Outlook-Contactar-0078D4?style=for-the-badge&logo=microsoftoutlook&logoColor=white" alt="Email"/>
    </a>
    <a href="https://www.linkedin.com/in/rodrigo-calderon-dev/">
      <img src="https://img.shields.io/badge/LinkedIn-Conectar-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"/>
    </a>
  </p>

  <p align="center">
    <a href="#sobre-mí">Sobre mí</a> •
    <a href="#stack-tecnológico--herramientas">Stack Tecnológico</a> •
    <a href="#proyectos-destacados">Proyectos Destacados</a> •
    <a href="#contacto">Contacto</a>
  </p>

</div>

---

### Sobre mí

Desarrollador de Software Junior y Técnico Superior en **Desarrollo de Aplicaciones Multiplataforma (DAM)** enfocado en arquitecturas backend, automatización de flujos operativos y tratamiento de datos.

* **Experiencia Profesional:** Desarrollo de módulos de contabilidad interna y facturación recurrente en **C#**, optimizando esquemas de bases de datos relacionales en **BittaSoftware**.
* **Movilidad Internacional:** Co-diseño de un pipeline de ingesta de datos y análisis predictivo en un equipo ágil internacional (Proyecto Rumanía), operando íntegramente en inglés durante la planificación de sprints, sincronizaciones técnicas y revisiones de código.
* **Filosofía Técnica:** Ingeniería de arquitecturas backend limpias, flujos ERP (Odoo) y sustitución de cuellos de botella manuales por servicios automatizados robustos.
* **Objetivo Actual:** En búsqueda de roles de Junior Software Engineer / Backend Developer para integrarme en entornos productivos, colaborar con equipos experimentados y escalar sistemas de software.
* **Ubicación:** Barcelona, España (Abierto a modalidades presenciales e híbridas).

---

### Stack Tecnológico & Herramientas

<div align="center">

| Área | Tecnologías |
| :--- | :--- |
| **Lenguajes** | ![C#](https://img.shields.io/badge/C%23-239120?style=for-the-badge&logo=csharp&logoColor=white) ![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white) ![Kotlin](https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white) ![Dart](https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)|
| **Empresa & Datos** | ![Odoo](https://img.shields.io/badge/Odoo-714B67?style=for-the-badge&logo=odoo&logoColor=white) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) ![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)|
| **Bases de Datos** | ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white) ![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white) ![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white) |
| **Frameworks & Core** | ![.NET](https://img.shields.io/badge/.NET-512BD4?style=for-the-badge&logo=dotnet&logoColor=white) ![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=for-the-badge&logo=springboot&logoColor=white) ![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white) ![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white) |

</div>

---

### Proyectos Destacados

---

#### 1. Predictive Real Estate Pipeline & Enterprise Analytics
> Arquitectura Medallion multicapa para el procesamiento de flujos de datos en crudo hacia modelos predictivos y reporting empresarial.

```mermaid
flowchart LR
    A["<b>Ingesta en Crudo (Bronze)</b><br/>• Fuentes heterogéneas<br/>• Almacenamiento en Python"]
    -->|Limpieza y Filtrado de Outliers| B["<b>Almacén Curado (Silver)</b><br/>• Modelado en Esquema de Estrella<br/>• Base de Datos PostgreSQL"]
    -->|Agregaciones y KPIs| C["<b>Capa de Negocio (Gold)</b><br/>• Modelos Predictivos de ML<br/>• Métricas Estandarizadas"]
    -->|Analítica y Simulación| D["<b>Endpoints de Negocio</b><br/>• Cuadros de Mando en Power BI<br/>• Validación Operativa en SAP"]

    classDef default fill:#161b22,stroke:#0078d4,stroke-width:1.5px,color:#e6edf3;
```
* **Contexto y Colaboración Internacional:** Co-diseñado en un equipo ágil internacional (España, Suiza, Rumanía y Portugal), coordinando dailies, flujos de ramas en Git y entregas técnicas íntegramente en inglés.
* **Arquitectura de Pipeline Medallion:**
  * **Capa Bronze:** Extracción y almacenamiento automatizado de datos inmobiliarios y registros de mercado sin procesar.
  * **Capa Silver:** Depuración de nulos, detección de anomalías y modelado dimensional en estrella dentro de **PostgreSQL**.
  * **Capa Gold:** Ejecución de pipelines de agregación analítica y entrenamiento de modelos predictivos de tendencias con **Pandas** y computación científica.
* **Reporting y Validación Operativa:** Diseño de paneles interactivos en **Power BI** e integración de salidas operativas sobre entornos **SAP** para validar casos de negocio.
* **Impacto:** Reducción del tiempo de preparación de datos de horas de procesamiento manual por sprint a scripts automatizados ejecutables en menos de 2 minutos.
* **Tech Stack:**
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=flat-square&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Power_BI-F2C811?style=flat-square&logo=powerbi&logoColor=black"/>
  <img src="https://img.shields.io/badge/SAP-008FD3?style=flat-square&logo=sap&logoColor=white"/>

---

#### 2. Enterprise Financial & Invoice Automation
> Módulo de facturación recurrente y automatización contable de alta integridad para operativa empresarial.

```mermaid
flowchart LR
    A["<b>Capa de Cliente (UI)</b><br/>WinForms Desktop (.NET)<br/>• Interfaces Transaccionales<br/>• Validación de Entrada de Datos<br/>• Flujos de Trabajo Modulares"]
    -->|Payloads Seguros HTTPS / JSON| B["<b>Capa de Lógica y API</b><br/>ASP.NET Core REST API<br/>• Controladores y Enrutamiento<br/>• Validación y Reglas de Negocio<br/>• Desacoplamiento de Cliente"]
    -->|ADO.NET y Stored Procedures| C["<b>Capa de Persistencia</b><br/>SQL Server Database<br/>• Procedimientos Almacenados<br/>• Control de Registros Duplicados<br/>• Bloqueos Transaccionales ACID"]
    -->|Pipeline Batch Automatizado| D["<b>Salida de Contabilidad</b><br/>Libro Mayor Empresarial<br/>• Registro Automatizado de Facturas<br/>• Procesamiento Recurrente en Lote<br/>• Informes de Cierre Financiero"]

    classDef default fill:#161b22,stroke:#239120,stroke-width:1.5px,color:#e6edf3;
