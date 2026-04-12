🚀 Built a WhatsApp-based AI Study Planner with Scheduling & Automation!
Excited to share a project I recently worked on where I combined FastAPI, scheduling, and WhatsApp integration to build a fully automated learning assistant 📚
🔧 What it does:
Users generate a personalized study plan using AI
Subscribe with their phone number
Receive daily study tasks directly on WhatsApp 📲
Smart scheduler ensures messages are sent only once per day (no duplicates!)
⚙️ Tech Stack:
FastAPI for backend APIs
APScheduler for background job scheduling
SQLite for lightweight data persistence
Twilio (WhatsApp Sandbox) for messaging
Deployed on Render for 24/7 availability
💡 Key Learning:
Instead of calling APIs internally, I decoupled business logic into reusable functions — making the system more efficient and scalable.
🚧 Challenges solved:
Handling scheduler lifecycle in production
Preventing duplicate message delivery
Managing user-specific data dynamically
🌱 Next Steps:
Move to WhatsApp Cloud API (Meta) for production scale
Add multi-user scheduling & unsubscribe feature
Convert into a SaaS product
This project gave me hands-on experience in building real-world backend systems with automation and integrations.

https://jobagent-ca8e.onrender.com/docs
