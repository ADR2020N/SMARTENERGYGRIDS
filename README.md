**Project Overview**

SmartEnergyGrids is a smart energy grid simulation and analytics project that demonstrates how real-time smart meter data can be streamed, stored, and analyzed using modern IoT and big data technologies.
The system simulates multiple smart meters that continuously publish electrical measurements such as power, voltage, current, frequency, and energy consumption. Data is transmitted using the MQTT protocol, stored in a time-series database (TimescaleDB), and visualized through an interactive Streamlit dashboard.
This project is designed for academic, learning, and demonstration purposes, particularly in the areas of smart grids, IoT data streaming, and big data analytics.

**Project Objectives**

- Simulate smart meter data generation
- Stream data in real time using MQTT
- Store high-frequency time-series data efficiently
- Perform raw and aggregated data analysis
- Visualize real-time and historical energy trends
- Demonstrate a scalable smart grid data architecture
  
**System Architecture**

**1. Smart Meter Simulator (Publisher)**
   Generates and publishes meter readings at fixed intervals.
**2. MQTT Broker (EMQX)**
  Manages message distribution between publishers and subscribers.
**3. Subscriber Service**
   Consumes MQTT messages and stores them in the database.
**4. TimescaleDB (PostgreSQL)**
  Stores time-series data using hypertables and continuous aggregates.
**5. Streamlit Dashboard**
   Displays real-time metrics and historical energy trends.

**Technologies Used**

- Programming Language: **Python**
- Messaging Protocol: **MQTT**
- Broker: **EMQX**
- Database: **PostgreSQL with TimescaleDB**
- Visualization: **Streamlit**
- Query Language: **SQL**

**Data Metrics Collected**

- Power (kW)
- Voltage (V)
- Current (A)
- Frequency (Hz)
- Energy Consumption (kWh)
- Timestamp
- Meter ID
  
**Key Features**

- Real-time smart meter data simulation
- Publisher–Subscriber architecture
- Time-series data storage using hypertables
- Continuous aggregates for performance optimization
- SQL-based analytics
- Interactive dashboards
- Scalable and modular design

 **Project Structure**

  SmartEnergyGrids/
│
├── publisher.py        # Smart meter data simulator
├── subscriber.py       # MQTT subscriber and database ingestion
├── dashboard.py        # Streamlit dashboard
├── database/
│   ├── schema.sql      # Database schema and hypertables
│   └── aggregates.sql # Continuous aggregate queries
├── requirements.txt   # Python dependencies
└── README.md

**How to Run the Project**
- Start MQTT Broker to Ensure EMQX is running locally or remotely.
- **Install Dependencies**
-  - pip install -r requirements.txt
**Run the Subscriber**
python subscriber.py
**Run the Publisher**
python publisher.py
**Launch the Dashboard**
streamlit run dashboard.py

**Dashboard Features**

- Real-time power monitoring
- Energy trends (last 24 hours)
- Voltage and frequency stability analysis
- Comparison between raw data and aggregated data
- Meter-specific analytics
  
**Use Cases**
- Academic projects (Big Data Analytics, IoT, Smart Grids)
- Learning MQTT and streaming architectures
- Time-series database performance analysis
- Energy consumption monitoring simulations

**Learning Outcomes**

- Understanding MQTT-based streaming systems
- Working with time-series databases
- Implementing continuous aggregates
- Building data-driven dashboards
- Designing scalable IoT architectures

**Author**
Adrien Nkurikiyumukiza
MSc in Big Data Analytics
Smart Energy & IoT Data Analytics Project
