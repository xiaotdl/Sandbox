# Code Coverage as a Service

## Docs
GitLab wiki - user/dev guide
GitLab page - source code sphinx doc


## Feature Requirements
- User provides BIGIP access information and modules/daemons to be profiled.
- User interacts with the Code Coverage API server.
- User gets Code Coverage Report.

Strech:
- Command log monitoring
- User Auth
- Prioritized Tasks
- Upon TaskCompletion/Crash, send Slack/Email Notification
- [admin] Web GUI that monitors the tasks
- [admin] Service Usage History (Task Requested/Finished)
- [admin] Web GUI that monitor/alert on service metrics (Datadog)
- Integration with Yifan's cl2test service
- Full text DB search

## User Flow Diagram


## REST API Design
Strech:
- API Versioning

1. CC start
POST /tasks
{
  "name": "(optional) Code Coverage start",
  "user": "<user>",
  "priority": "<priority>",
  "type": "code-coverage-start",
  "data": {
    "command": "...",
    "args": "..." # bigip_mgmt_ip, etc.
  }
}

GET /tasks/<task_id>
{
  "status": "pending",
  "selflink": "http://localhost/tasks/12345",
  "timestamp": ...
}

2. CC end
POST /tasks
{
  "name": "(optional) Code Coverage end",
  "user": "<user>",
  "priority": "<priority>",
  "type": "code-coverage-end",
  "data": {
    "command": "...",
    "args": "..." # bigip_mgmt_ip, etc.
  }
}

GET /tasks/<task_id>
{
  "status": "pending",
  "selflink": "http://localhost/tasks/54321",
  "result": [
    "link": "http://10.192.10.141/~vagrant/10.192.10.136/code_coverage/"
  ],
  "timestamp": ...
}

3. monitor all tasks, filter tasks by status, user?
GET /tasks
{
    "count": X,
    "collection": [
        "<task_id>": [
            "selflink": "<task_selflink>",
            "status": "<task_status>"
        }
    ]
}


## System Design
Everything on One Server

Strech:
- CICD without downtime
- Scale

Host: Nginx+uwsgi+supervisord
REST API Server(Flask) --> Task Queue(RabbitMQ) --> Async Worker(Celery) --> Datastore(Redis)
                       --> Datastore(Redis+MySQL)

Static File(html) Host Server
