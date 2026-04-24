 HEAD
# SDN-Based Path Tracing Tool

## Overview
This project implements a **Path Tracing Tool using Software Defined Networking (SDN)** to identify and display the path taken by packets in a network by analyzing flow rules installed in OpenFlow switches.

The project uses **Mininet** for network emulation, **Ryu Controller** for SDN control, and **Flask** for a web-based GUI to visualize packet forwarding paths.

---

## Objective
- Track flow rules installed in switches  
- Identify forwarding path of packets  
- Display the route through a GUI  
- Validate paths using network tests  

---

## Technologies Used
- Python  
- Flask  
- Mininet  
- Ryu Controller  
- OpenFlow 1.3  
- REST APIs  

---

## System Architecture

```text
Mininet (Hosts + Switches)
        ↓
Ryu Controller (Flow Rules)
        ↓
REST API (Port 8080)
        ↓
Flask Application (Port 5000)
        ↓
Path Visualization GUI
```

---

## Project Structure

```text
Cn Mini project Orange/
│
├── app.py                # Flask application
├── templates/
│   └── index.html        # GUI
├── ryu/                  # Ryu source
├── sdn-env/              # Python virtual environment
└── README.md
```

---

## Features
- Flow rule tracking  
- Packet path reconstruction  
- GUI-based route display  
- Validation using ping tests  

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd project-folder
```

---

## 2. Create Virtual Environment
```bash
python3.10 -m venv sdn-env
source sdn-env/bin/activate
```

---

## 3. Install Dependencies
```bash
pip install flask requests
pip install eventlet==0.33.3 greenlet==2.0.2 dnspython==2.2.1
pip install netaddr oslo.config webob routes
```

---

## 4. Run Ryu Controller
```bash
cd ryu
PYTHONPATH=. python3 ryu/cmd/manager.py \
ryu/app/simple_switch_13.py \
ryu/app/ofctl_rest.py
```

---

## 5. Start Mininet
Open a new terminal:

```bash
sudo mn --topo linear,3 --controller remote
```

Generate traffic:

```bash
pingall
```

---

## 6. Run Flask App
Open another terminal:

```bash
python3 app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## Sample Output

```text
S1 → OUTPUT:2
S2 → OUTPUT:3
S3 → OUTPUT:1
```

---

## Flow Rule Validation

View switch flow entries:

```bash
sh ovs-ofctl dump-flows s1
```

Example:

```text
in_port=s1-eth2, dl_dst=<mac>
actions=output:s1-eth1
```

---

## How It Works
1. Mininet creates network topology  
2. Ping traffic generates ICMP packets  
3. Ryu installs flow rules dynamically  
4. Flask retrieves flow rules through REST APIs  
5. Output actions are analyzed to reconstruct packet path  

---

## Challenges Faced
- Ryu pip installation failed due to Python compatibility issues  
- Resolved by running Ryu directly from source  
- Dependencies were installed manually  

---

## Future Scope
- Real-time path visualization  
- Graph-based topology display  
- Fault detection and rerouting  
- Multi-path analysis  

---

## Authors
Developed as part of Computer Networks Mini Project.

# Path-Tracing-Tool
 47262cb75712cff571bd9ae7e4275af364d5629f
