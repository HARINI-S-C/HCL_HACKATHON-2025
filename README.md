# HCL_HACKATHON-2025 --> Smart Bank – Modular Banking Backend System  
### Focus Use Case: User Registration & KYC Verification  

-------

## 1. Project Description
---------------------------------
**Smart Bank** is a modular, secure, and scalable backend system designed to streamline core banking operations.  
This prototype focuses on the **User Registration and KYC Verification module**, which enables customers to securely register, verify their identity, and get onboarded into the banking system with a verified digital profile.

### Purpose & Scope
- Simplify **user onboarding** by automating registration and KYC processes.
- Ensure **data integrity, authentication, and compliance** with banking standards.
- Build a **scalable API backend** that can later extend to full banking operations (accounts, loans, transactions, fraud detection).

---

## 2. Understanding the Problem
---------------------------------
### 🔹Project Goal
To design and develop a **secure registration and KYC module** for a digital banking backend that allows users to create accounts, upload verification documents, and establish a verified identity in the system.

### 🔹Target Users
| Role | Capabilities |
|------|---------------|
| **Customer** | Register account, submit personal details, upload KYC docs, view KYC status |
| **Bank Admin** | Review, approve/reject KYC submissions, manage user data |
| **Auditor** | Access KYC logs and review system activities for compliance |

### 🔹Pain Points in Existing Systems
- Lengthy manual KYC verification process.  
- Paper-based identity proof submissions.  
- Lack of transparency and real-time updates for users.  
- Data breaches due to insecure handling of sensitive information.

### 🔹User Expectations
- Quick and seamless registration.  
- Simple KYC upload with real-time verification status.  
- Secure storage of personal and document data.  
- Clear feedback if verification fails or requires resubmission.

---

## 3. Root Cause Analysis
---------------------------------
| **Issue** | **Root Cause** | **Smart Bank Solution** |
|-------|-------------|----------------------|
| Manual onboarding | Physical paperwork | Online digital registration |
| Fraudulent accounts | Lack of strong identity verification | Enforced KYC process |
| Poor user experience | No instant feedback | Automated status updates |
| Data leaks | Weak security | JWT + bcrypt + input sanitization |

---

## 4. System Architecture
---------------------------------
### 🔹Overview
Smart Bank follows a **modular layered architecture**:
- **Client (Frontend)**: Web/mobile interface for registration and KYC upload.
- **Backend (FastAPI)**: Manages user registration, authentication, and KYC workflow.
- **Database (PostgreSQL)**: Stores user data, KYC details, and verification status.
- **File Storage (Cloud / Local)**: Stores uploaded KYC documents securely.

### 🔹Flow Diagram
1. User registers → Data validated via FastAPI + Pydantic.  
2. Password is hashed using bcrypt and stored in PostgreSQL.  
3. User uploads KYC documents (e.g., ID proof).  
4. Admin reviews and updates KYC status.  
5. User receives real-time verification updates.

---

## 5. Tech Stack
---------------------------------
| Component | Technology |
|------------|-------------|
| **Backend** | FastAPI (Python) |
| **Database** | PostgreSQL |
| **ORM** | SQLAlchemy |
| **Auth** | JWT (PyJWT) + bcrypt |
| **Rate Limiting** | SlowAPI |
| **File Handling** | FastAPI UploadFile + local/cloud storage |
| **Frontend (demo)** | HTML, CSS, JavaScript (fetch API) |

---

## 6. Key Features (User Registration & KYC)
---------------------------------
| Feature | Description |
|----------|-------------|
| **User Registration** | Create a new user account with basic personal information. |
| **Password Security** | Passwords are hashed using `bcrypt` before storage. |
| **Login Authentication** | Secure login via JWT tokens. |
| **KYC Upload** | Users upload ID proof (e.g., PAN, Aadhar, Passport). |
| **Document Validation** | System validates file type, size, and format. |
| **KYC Review** | Admin can approve, reject, or flag submissions. |
| **Status Tracking** | Users can check KYC verification status in real time. |
| **Rate Limiting** | Protects API from brute force attacks. |
| **Input Validation** | Enforced via Pydantic models to sanitize inputs. |

---

## 7. Application Overview (Project Structure)
---------------------------------
```
smartbank/
│
├─ app/
│  ├─ __init__.py
│  ├─ main.py                         # Entry point of FastAPI
│  │
│  ├─ api/
│  │  ├─ __init__.py
│  │  └─ routes/
│  │     ├─ __init__.py
│  │     ├─ auth.py                   # /auth/signup, /auth/login, /auth/logout
│  │     ├─ users.py                  # /users/me, /users/all
│  │     ├─ kyc.py                    # /kyc/upload, /kyc/status, /kyc/verify/{user_id}
│  │     ├─ admin.py                  # /admin/kyc/pending
│  │     ├─ audit.py                  # /audit/logs
│  │     └─ account.py                # /account/create, /account/balance, etc.
│  │
│  ├─ db/
│  │  ├─ __init__.py
│  │  ├─ session.py                   # SQLAlchemy engine, session
│  │  └─ models.py                    # SQLAlchemy models: User, Account, KYC, AuditLog
│  │
│  ├─ schemas/
│  │  ├─ __init__.py
│  │  ├─ auth_schema.py               
│  │  ├─ user_schema.py               
│  │  ├─ kyc_schema.py                
│  │  └─ account_schema.py            
│  │
│  ├─ utils/
│  │  ├─ __init__.py
│  │  ├─ auth.py                      
│  │  ├─ jwt.py                       
│  │  └─ rate_limiter.py              
│  │
│  ├─ core/
│  │  ├─ __init__.py
│  │  ├─ config.py                    
│  │  └─ security.py                 
│  │
│  └─ test_files/                     
│
├─ venv/                             
│
├─ requirements.txt                   
├─ .env                               
└─ README.md                         

```

---

## 8. Setup Instructions
---------------------------------
### 1. Clone the Repo
```
git clone https://github.com/yourusername/smartbank.git
cd smartbank
```
### 2. Create Virtual Environment
```
python -m venv venv      
venv\Scripts\activate
```  
### 3.Install Dependencies
```pip install -r requirements.txt```

### 4. Configure Environment Variables
Create .env:

```DATABASE_URL=postgresql://user:password@host:port/dbname
JWT_SECRET=your_secret_key
```
### 5. Run Migrations (optional)
```
alembic upgrade head
```
### 6. Start the Server
```
uvicorn main:app --reload
```
Visit: http://127.0.0.1:8000/docs

---

## 9. Featured API Endpoints (Registration & KYC)
---------------------------------

| **Endpoint** | **Method** | **Description** |
|---------------|------------|-----------------|
| `/account/create` | **POST** | Account create |
| `/auth/signup` | **POST** | Register a new user |
| `/auth/login` | **POST** | Authenticate and get JWT token |
| `/users/me` | **GET** | Get current logged-in user details |
| `/kyc/upload` | **POST** | Upload KYC document |
| `/admin/kyc/pending` | **GET** | Pending KYC |
| `/kyc/status` | **GET** | View current KYC verification status |
| `/kyc/verify/{user_id}` | **PATCH** | Admin approves or rejects KYC |
| `/users/all` | **GET** | List all users (Admin only) |
| `/auth/logout` | **POST** | Invalidate current session |
| `/admin/kyc/pending` | **GET** | View all pending KYC verifications |
| `/audit/logs` | **GET** | Auditor views KYC review logs |

---

## 10. Authentication & Security
-----------------------

### 🔹JWT Authentication:
- On successful login, user receives a JWT token.
- Token used for protected API routes.

### 🔹Password Hashing:
- Implemented using bcrypt.

### 🔹Role-Based Access Control (RBAC):
1. **Customer**: Register, upload KYC, check status.
2. **Admin**: Review and approve KYC.
3. **Auditor**: Read-only access to logs.

### 🔹Rate Limiting:
- Managed by slowapi to prevent spam and brute-force login.

### 🔹Input Validation:
All inputs (email, password, documents) validated via Pydantic models.

### 🔹Document Sanitization:
File type (e.g., PDF, JPEG) and size are verified before saving.

---

## 11. Database Models
---------------------------------

### 🔹User Model
```
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    kyc_status = Column(String, default="pending")

    accounts = relationship("Account", back_populates="user")
```

## 🔹Account Model
```
class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    account_number = Column(String, unique=True, index=True)
    account_type = Column(String)

    user = relationship("User", back_populates="accounts")
```

### 🔹KYC Model
```
class KYC(Base):
    __tablename__ = "kyc"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    document_path = Column(String)
    status = Column(String, default="pending")  # pending, approved, rejected

    user = relationship("User", back_populates="kyc_documents")
```

---

## 12. Contributors
---------------------------------
**Project Maintainer:** Harini Chandrusekaran

---

## 13. Conclusion
---------------------------------
This **Smart Bank: User Registration & KYC Verification ** module lays the foundation for a robust digital banking backend.  
It ensures that every user joining the system is **securely registered**, **authenticated**, and **identity-verified** through a modern, automated KYC pipeline.  

The architecture can easily scale to support **accounts, transactions, loans, and fraud detection**, making it a critical microservice in the broader **Smart Bank ecosystem**.

---
