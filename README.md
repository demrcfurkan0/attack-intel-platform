#  Attack Intel Platform - AI-Powered Cyber Attack Simulation & Response

The **Attack Intel Platform** is a full-stack, AI-driven web application that simulates modern Security Operations (SecOps). This platform allows analysts to launch common cyber-attacks in a controlled environment, detect these attacks using an AI model, and practice incident response workflows.

This project aims to provide a hands-on experience in attack detection, analysis, and response by mimicking the daily workflow of a SOC (Security Operations Center) analyst.

---

## Key Features

### Attack Simulation

Users can launch four different types of cyber-attack simulations:

- **DDoS (HTTP Flood):** Sends a high volume of HTTP requests to a target URL.
- **Brute Force:** Attempts various username and password combinations.
- **SQL Injection:** Injects malicious SQL queries into application inputs.
- **SYN Flood (Network Layer):** Sends numerous SYN packets to a target IP to exhaust network resources.

### AI-Based Detection

- Real-time analysis using a pre-trained **XGBoost** machine learning model.
- The model classifies traffic as either `BENIGN` or a specific **attack type**.

### Real-Time Interface

- **WebSocket** integration for live updates.
- Detected attacks appear instantly in the **Alerts** tab.

### Incident Response Center

- **Triage & Analysis**: Each alert can be investigated in the **Response Center**.
- **Analyst Notes**: Add notes, mark false positives, and apply tags like `critical` or `under investigation`.
- **Dynamic Playbooks**: Each attack type has a guided checklist for mitigation steps.

### AI Co-Pilot

- Ask natural language questions using **Google Gemini API**.
- Get summaries, response suggestions, or incident analysis.

### Dashboard & Reporting

- Charts visualizing:
  - Attack trends
  - Detection rates
  - Model accuracy (Confusion Matrix)
- Historical log of simulations and detections.

### User Management

- **JWT-based** authentication system.
- Role-based access control for analysts and admins.

---

## Tech Stack

| Layer        | Tools / Libraries                                |
|--------------|--------------------------------------------------|
| **Frontend** | React (TypeScript), Vite, Tailwind CSS, shadcn/ui |
| **Backend**  | Python 3.10+, FastAPI, Pydantic, WebSockets       |
| **Database** | MongoDB                                           |
| **ML Model** | Scikit-learn, XGBoost, Pandas                     |
| **Chatbot**  | Google Gemini API                                 |
| **Containerization**| Docker, Docker Compose                     |
| **Async & Communication:** | asyncio, httpx, WebSockets          |

---

## Getting Started

> Requires: Docker & Docker Compose installed on your system

### 1. Clone the Repository

```bash
git clone https://github.com/demrcfurkan0/attack-intel-platform.git
cd attack-intel-platform
#.env Configration

#Mongo Conf.
MONGO_URI=mongodb://mongo:27017/cyber_attack_sim_db
DATABASE_NAME="cyber_attack_sim_db"

#Path to Model
MODEL_PATH="models/final_xgboost_model.pkl"
SCALER_PATH="models/final_scaler.pkl"
FEATURE_COLUMNS_PATH="models/feature_columns.json"

#SecretKey
SECRET_KEY = 7b33b4563809b3b4f942e64e9aae463bcc9ffc30808ffcd63604cbfa9bdce292

#Gemini Apı Key
GOOGLE_API_KEY = AIzaSyA0xYMBU55whDXjScFTckzpXSr1SIK-qnI

#Email Notification Conf.
SMTP_SERVER="smtp.gmail.com"
SMTP_PORT=587
EMAIL_SENDER="ydemirci376@gmail.com"
EMAIL_PASSWORD="drsxuwooipcarsbk"
EMAIL_RECIPIENT="yfurkandemirci@stu.aydin.edu.tr"

#Api Conf.
INTERNAL_API_BASE_URL="http://fastapi:8000"
VITE_API_BASE_URL="http://localhost:8000"

#Base User Credentials.
ADMIN_USERNAME=admin
ADMIN_EMAIL=admin@cybershield.com
ADMIN_PASSWORD=admin


#Run the App
docker-compose up --build
npm run dev

#See at:

* Frontend: http://localhost:8080
* Backend: http://localhost:8000/docs
* Mongo Express: http://localhost:8081

## Use Platform:

* Go to http://localhost:8080
* Username: admin
* Password: admin123
* Go to the "Simulation" tab, choose an attack type, and click "Launch Simulation."
* Navigate to the "Alerts" tab to see the detections made by the AI.
* Click the "Triage & Respond" button on an alert to open the "Response Center."
* Analyze the incident, add notes, apply tags, follow the Playbook steps, and chat with the Co-Pilot to resolve the incident!

