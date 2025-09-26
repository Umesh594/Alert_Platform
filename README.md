# Alerting & Notification Platform (MVP)
 # Features (Implemented)
  # Admin
  -Create Alerts with:
  -Title & Message 
  -Severity: Info / Warning / Critical 
  -Delivery Type: In App (MVP) 
  -Start & Expiry times 
  -Reminder frequency (default 2 hours, simulated every 30s for demo) 
  -Visibility: Entire Organization, Specific Teams or Specific Users  – visibility filtering not fully implemented
  -Enable/Disable reminders 
  # Update Alerts
   -Edit title, message, severity, expiry, reminders 
  # List Alerts
   -Fetch all alerts with current properties 
 # End User
  -Receive Alerts
  -Alerts delivered according to visibility (org/team/user)  – visibility filtering not fully implemented
  -Alerts automatically re-trigger every 2 hours until:
  -The user snoozes it for the day 
  -Alert expires 
 # Snooze Alerts
  -Snooze an alert for the current day 
  -Next day, if alert is still active, reminders resume 
 # View Alerts
  -See list of active alerts 
  -Mark alerts as read/unread 
  -Track snoozed alerts 
 # Reminders
  -Auto re trigger every 2 hours (simulated every 30s in demo) 
  -Implemented using threaded scheduler 
 # Analytics
  -System wide metrics:
  -Total alerts created 
  -Alerts delivered vs. read/unread/snoozed 
  -Breakdown by severity (Info/Warning/Critical) 
 # Future Scope / Not in MVP
  -Enforce visibility filtering for End Users 
  -Additional Delivery Channels: Email & SMS
  -Customizable reminder frequencies (beyond default 2h)
  -Scheduled alerts / Cron jobs
  -Escalation logic if alerts not acknowledged in 24h
  -Role based access control for Admin features
  -Push Notification integration
 # Run Project
  -Install dependencies
  -pip install -r requirements.txt
  -Start FastAPI server
  -uvicorn app.main:app --reload
 # Available APIs
  -Admin
  -POST /admin/alerts – Create alert 
  -PUT /admin/alerts/{alert_id} – Update alert 
  -GET /admin/alerts – List alerts 
  -End User
  -GET /user/{user_id} – Fetch user details 
  -GET /user/{user_id}/alerts – Fetch alerts for user 
  -POST /user/{user_id}/alerts/{alert_id}/read – Mark alert as read 
  -POST /user/{user_id}/alerts/{alert_id}/unread – Mark alert as unread 
  -POST /user/{user_id}/alerts/{alert_id}/snooze – Snooze alert 
  -Analytics
  -GET /analytics/ – Aggregated alert metrics 
 # Tech Stack
  -Backend: Python, FastAPI 
  -Data storage: In memory Python dicts/lists 
  -Scheduler: Threaded reminder simulation 
 # Design Patterns:
  -Strategy (Notification Channels) 
  -Observer (User subscriptions) 
 # Deployed Link : https://alert-platform-mot9.onrender.com/docs
