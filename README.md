<h1 align="center">Hi, I'm Vinay Kumar Reddy Molakathala 👋</h1>

<h3 align="center">Gen AI Engineer · RAG Systems · AI Agents · MCP · Full-Stack (Java + Python)</h3>

<p align="center">
  I build retrieval-grounded LLM applications, multi-agent systems and MCP tooling, and the production-grade backends they run on.
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/molakathala-vinay-kumar-reddy/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:vinaykumarreddy467@gmail.com"><img src="https://img.shields.io/badge/Email-D44638?style=for-the-badge&logo=gmail&logoColor=white" alt="Email"></a>
  <a href="https://portfolio-pink-gamma-k8pt11kzv1.vercel.app"><img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio"></a>
  <img src="https://img.shields.io/badge/Bengaluru,_India-4B5563?style=for-the-badge&logo=googlemaps&logoColor=white" alt="Bengaluru">
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=Vinaykumarreddy467&color=8e44ad&style=flat-square&label=Profile+views" alt="Profile views">
</p>

---

## 🧑‍💻 About Me

- 🏢 **Software Engineer Intern @ Lifetrenz** (Bengaluru, Sep 2026 – present)
- 🤖 Previously a **Gen AI Intern @ Dr. Reddy's Foundation**: LangChain, LangGraph, RAG, vector search, multi-agent systems and MCP
- 🌐 Before that, a **Frontend Developer @ NeoSOFT** on the **Infosys.com** client engagement: 2,200+ pages, WCAG 2.1 AA accessibility and an AI-powered Text-to-Speech feature
- 🧠 Currently building **Context Layer**, a persistent, model-agnostic memory layer for AI coding agents, served over MCP
- 🌱 Selected **Open Source Connect India 2026 Contributor**
- 🎙️ Active in Bengaluru's AI community: volunteer at Neo4j and Amadeus × Contentstack events, and a regular at AI Dev Circle, KSUG.AI, null | OWASP and Bengaluru Tech Week
- 🎓 B.Tech, Data Science Engineering, Sri Venkateswara College of Engineering & Technology (2025)

---

## 🚀 Featured Projects

<table>
<tr>
<td width="50%" valign="top">

### 🧠 [Context Layer](https://github.com/Vinaykumarreddy467/Context_Layer)
Persistent, model-agnostic project memory for AI coding agents. Stores structured handoffs in **SurrealDB** and exposes **17 MCP tools** with full-text, vector and hybrid search, token-budgeted context assembly, handoff lineage and a retrieval-evaluation harness.

`Python` `MCP` `SurrealDB` `Hybrid Search`

</td>
<td width="50%" valign="top">

### 📚 [Knowledge Base Management System](https://github.com/Vinaykumarreddy467/knowledge-base-management-system)
A knowledge base with a **grounded AI assistant** that answers only from retrieved content and cites the exact chunks it used. Keyword plus **pgvector** semantic search, Tika ingestion, role-based access (Admin/Editor/Viewer) and an audit log, all running on local LLMs.

`Spring Boot 3.5` `Java 21` `pgvector` `Angular 22` `Ollama`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🛡️ [Redis API Rate Limiting & DDoS Protection](https://github.com/Vinaykumarreddy467/redis-api-rate-limiting-ddos-protection-poc)
Six Redis-backed rate-limiting algorithms (fixed window, sliding window, token bucket, leaky bucket, concurrency leases) enforced atomically and **proven shared across two JVMs**. Dynamic admin policies, fail-open/fail-closed behaviour and **237 automated tests**.

`Spring Boot` `Redis` `Angular` `Actuator`

</td>
<td width="50%" valign="top">

### ✈️ [AI Travel Assistant](https://github.com/Vinaykumarreddy467/travel-assistant)
Built at the **Amadeus × Contentstack "Beyond GenAI" hackathon**. A deterministic **LangGraph** multi-agent graph: an intent router fans out to flight, hotel, weather and activity agents, then a composer builds a budget-aware, day-by-day itinerary. Fully traced in **LangSmith**.

`LangGraph` `LangSmith` `Groq Llama 3.3` `Duffel API` `Streamlit`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🔎 [Hybrid Search RAG over Internal Docs](https://github.com/Vinaykumarreddy467/Hybrid_Search_RAG_over_Internal_Docs)
A RAG app with a custom **Reciprocal Rank Fusion** engine that fuses dense (ChromaDB) and sparse (BM25) retrieval. Layout-aware ingestion with **Docling**, a live weight-tuning sandbox and source-cited chat.

`FastAPI` `ChromaDB` `BM25` `Docling` `Hugging Face`

</td>
<td width="50%" valign="top">

### 🤖 [Auto Job Application Agent](https://github.com/Vinaykumarreddy467/auto-job-application-agent)
A **12-agent, 13-tool** pipeline that discovers jobs, analyses skill gaps against a JD, tailors the resume, has an LLM judge check its quality, exports an ATS-ready PDF and tracks everything on a dashboard. Runs fully locally.

`FastAPI` `Multi-Agent` `Angular` `Docling` `WebSockets`

</td>
</tr>
<tr>
<td width="50%" valign="top">

### ✅ [Task Manager with AI QA](https://github.com/Vinaykumarreddy467/task-manager)
Task tracking with **LLM-generated test cases** (positive, negative, boundary, business-rule) and a human-in-the-loop review flow: Draft → Approve → Execute. Pluggable Groq, Gemini and Ollama providers with automatic fallback.

`Spring Boot 4` `Angular 22 SSR` `PostgreSQL` `Groq` `Gemini`

</td>
<td width="50%" valign="top">

### 🧾 [Research Assistant with Memory](https://github.com/Vinaykumarreddy467/Research-Assistant-With-Memory)
Drop in URLs and query them as one document. An **n8n** webhook ingestion pipeline feeds chunking and local Ollama embeddings into a citation-backed RAG over FastAPI, with React and Streamlit front ends.

`FastAPI` `n8n` `Ollama` `React` `RAG`

</td>
</tr>
</table>

---

## 🧩 More Things I've Built

| Project | What it is | Stack |
|---|---|---|
| [yt-summarizer](https://github.com/Vinaykumarreddy467/yt-summarizer) | MCP server exposing YouTube transcripts as tools, resources and prompts | Python, FastMCP |
| [Multi-Agent Research System](https://github.com/Vinaykumarreddy467/Multi-agent-research-system) | Search → reader → writer → critic agents that draft and self-review reports | LangChain, Groq, Streamlit |
| [n8n Workflows](https://github.com/Vinaykumarreddy467/n8n-workflows) | AI automations: Maps lead scraper, Google-tools chat agent, Sheets + Groq pipelines | n8n, Groq, Google APIs |
| [Doc-Intelligent](https://github.com/Vinaykumarreddy467/Doc-Intelligent) | Document classification, extraction and summarisation with a human verification step | Spring Boot, FastAPI, Ollama |
| [Chat with Files](https://github.com/Vinaykumarreddy467/Chat_with_files) | Chat with PDF/DOCX/XLSX documents using local models | Spring Boot, Angular, Ollama |
| [LangChain4j Document Extractor](https://github.com/Vinaykumarreddy467/LangChain4j-Document-Extractor) | Multi-format extraction plus RAG-ready chunking in Java | Java, LangChain4j |
| [AI Resume Analyzer](https://github.com/Vinaykumarreddy467/Ai_Resume_Analyzer) | ATS-style resume vs. JD scoring with an animated dashboard | FastAPI, Groq |
| [TeamTask Manager](https://github.com/Vinaykumarreddy467/TeamTask-Manager) · [live](https://team-task-manager-seven-jade.vercel.app) | Team task management app | Spring Boot, React, MySQL |
| [AI Travel Planner](https://github.com/Vinaykumarreddy467/Travel_Planner) | LLM trip planner with live weather | FastAPI, Groq, OpenWeather |
| [E-Commerce Website](https://github.com/Vinaykumarreddy467/E-Commerce_Website) | 30+ REST endpoints, JWT + RBAC, Razorpay payments | Spring Boot, React, MySQL |
| [Insight Admin Panel](https://github.com/Vinaykumarreddy467/insight-admin-panel) | Full-stack admin dashboard | Spring Boot, Angular, MySQL |
| [ZymSync Gym Management](https://github.com/Vinaykumarreddy467/Zym-Management-System) | Gym membership and operations system | Spring Boot, Angular 17, MySQL |
| [SympAI](https://github.com/Vinaykumarreddy467/Sympai) · [live](https://sym-ai-v8.vercel.app) | Symptom-based disease prediction (85% accuracy) | Flask, scikit-learn |

---

## 🛠️ Tech Stack

**Gen AI & Agents**<br>
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat-square&logo=langgraph&logoColor=white)
![LangSmith](https://img.shields.io/badge/LangSmith-1C3C3C?style=flat-square&logo=langchain&logoColor=white)
![MCP](https://img.shields.io/badge/MCP_/_FastMCP-191919?style=flat-square&logo=anthropic&logoColor=white)
![LangChain4j](https://img.shields.io/badge/LangChain4j-3A3A3A?style=flat-square)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-F55036?style=flat-square)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=flat-square&logo=googlegemini&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging_Face-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![n8n](https://img.shields.io/badge/n8n-EA4B71?style=flat-square&logo=n8n&logoColor=white)

**Retrieval & Data**<br>
![pgvector](https://img.shields.io/badge/pgvector-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B6B?style=flat-square)
![Neo4j](https://img.shields.io/badge/Neo4j-4581C3?style=flat-square&logo=neo4j&logoColor=white)
![SurrealDB](https://img.shields.io/badge/SurrealDB-FF00A0?style=flat-square&logo=surrealdb&logoColor=white)
![Redis](https://img.shields.io/badge/Redis-DC382D?style=flat-square&logo=redis&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)

**Backend**<br>
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Java](https://img.shields.io/badge/Java_21-ED8B00?style=flat-square&logo=openjdk&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)

**Frontend**<br>
![Angular](https://img.shields.io/badge/Angular-DD0031?style=flat-square&logo=angular&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)

**Tools**<br>
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)

---

## 💼 Experience

| Role | Organisation | Period |
|---|---|---|
| **Software Engineer Intern** | Lifetrenz | Sep 2026 – Present |
| **Gen AI Intern** | Dr. Reddy's Foundation | Apr 2026 – Aug 2026 |
| **Frontend Developer** (Infosys.com client engagement) | NeoSOFT | Jul 2025 – Dec 2025 |
| **Java Full-Stack Trainee** | EduBridge Learning | Mar 2025 – Jun 2025 |
| **Data Analysis Intern** | APSSDC | Jul 2024 – Sep 2024 |
| **Python Full-Stack Intern** | Techno-hub Foundation | Aug 2023 – Sep 2023 |

---

## 🏅 Certifications

- **Neo4j Certified Professional**, Neo4j (2026)
- **Introduction to Model Context Protocol**, Anthropic (2026)
- **Introduction to Agent Skills**, Anthropic (2026)
- **Claude Code 101** and **Claude 101**, Anthropic Academy (2026)
- **Java Full Stack**, Capgemini Digital Academy (2025)
- **Computer Vision 101**, Infosys Springboard
- **Project Management Fundamentals**, IBM SkillsBuild

---

## 🌍 Community

- 🧑‍🤝‍🧑 **Volunteer**, Neo4j Agentic AI Workshop (Bengaluru Tech Week 2026): helped attendees with Cypher, graph modelling and GraphRAG
- 🏁 **Participant and volunteer**, Amadeus × Contentstack "Beyond GenAI" hackathon
- 🌱 **Contributor**, Open Source Connect India 2026
- 🎤 Regular at **AI Dev Circle**, **KSUG.AI**, **null | OWASP Bangalore**, **Snowflake World Tour**, **IBM Bob-a-thon**, **n8n Build Hours** and the **Self-Learning Agents Builders Mixer** (Microsoft), writing up what I learn on [LinkedIn](https://www.linkedin.com/in/molakathala-vinay-kumar-reddy/)

---

## 📊 GitHub Stats

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=Vinaykumarreddy467&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" alt="GitHub stats">
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Vinaykumarreddy467&layout=compact&theme=tokyonight&hide_border=true&langs_count=8" alt="Top languages">
</p>
<p align="center">
  <img src="https://streak-stats.demolab.com?user=Vinaykumarreddy467&theme=tokyonight&hide_border=true" alt="GitHub streak">
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Vinaykumarreddy467/Vinaykumarreddy467/output/github-contribution-grid-snake-dark.svg">
    <img alt="Contribution snake" src="https://raw.githubusercontent.com/Vinaykumarreddy467/Vinaykumarreddy467/output/github-contribution-grid-snake.svg">
  </picture>
</p>

---

<p align="center">
  <b>Open to Gen AI / AI Engineer opportunities and collaborations on RAG, agents and MCP.</b><br>
  Let's connect on <a href="https://www.linkedin.com/in/molakathala-vinay-kumar-reddy/">LinkedIn</a> or drop me an <a href="mailto:vinaykumarreddy467@gmail.com">email</a>.
</p>
