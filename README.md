# FastAPI + React Coding Challenge Generator

A full-stack web application that generates **coding challenges** using an AI/LLM.  
Users can **sign in**, choose a **difficulty level** (easy / medium / hard), generate challenges, view **explanations**, and track their **history** with a **daily usage quota** to prevent abuse.

---

## ✨ Features

- 🔐 **Authentication** with Clerk (Sign in / Sign up, social login support)
- 🧠 **AI-generated coding challenges** by difficulty level
- ✅ **Multiple-choice style questions** with explanations
- 🧾 **History page** to view previously generated challenges per user
- ⏳ **Daily quota system** (limited number of generations per day + reset time)
- 🔄 Secure **Frontend ↔ Backend** API communication

---

## 🧰 Tech Stack

### Backend
- **Python**
- **FastAPI**
- **SQLAlchemy (ORM)**
- **Database**: SQLite (local development) or PostgreSQL (production-ready)
- **Clerk** (backend authentication verification via JWT/session tokens)
- **OpenAI / LLM** integration for question generation

### Frontend
- **React (Vite)**
- **React Router**
- **Clerk React SDK** (authentication UI & session handling)

---

## 🔐 Clerk Setup (Required)

### Create a Clerk Project
- Create a project on Clerk
- Enable sign-in methods (Google / Email / etc.)
- Copy the required keys from the Clerk dashboard

---

## 🔁 How It Works

- User signs in on the frontend (Clerk handles authentication and sessions)
- Clerk provides an authentication token for the logged-in user
- Frontend sends API requests to the backend along with the token
- Backend verifies the token using Clerk and identifies the user
- Backend checks the user’s **daily quota**:
  - ✅ If quota is available → generates a new challenge using AI/LLM and stores it in the database
  - ❌ If quota is exhausted → returns the next quota reset time
- User can view the **history** of all previously generated challenges

---
