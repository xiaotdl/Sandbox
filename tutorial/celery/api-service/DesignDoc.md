# Code Coverage as a Service

## Docs
- GitLab wiki - user/dev guide
- GitLab page - source code sphinx doc


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
See WebSequenceDiagram.txt

## Database Schema
```
user
--+--
PK| id: int
    name: varchar
    email: varchar
    created_at: datetime
    last_login: datetime

task
--+--
PK| id: int
FK| user_id: int
    name: varchar
    priority: int
    status: enum
    created_at: datetime
    type (polymorphic discriminator): varchar
    result: ???

code_coverage_task
--+--
PF| id: int
    bigip_mgmt_ip: varchar
    module: varchar
    daemons: varchar
    mode: varchar

core_extraction_task
--+--
PF| id: int
    ...
```

## REST API Design
Strech:
- API Versioning

```
1. register user
POST /api/task/user
{
	"name": "xili",
	"email": "xili@f5.com"
}

2. request service - code-coverage start
POST /api/task/code-coverage
{
	"name": "xili-code-coverage-task",
	"user": "xili",
	"priority": 10,
	"data": {
		"bigip-mgmt-ip": bigip_mgmt_ip,
		"module": "afm",
		"daemons": "autodosd",
		"mode": "start"
	}
}

>>>
HTTP/1.1 202 OK
Location: http://localhost/api/task/<task-status-id>/status

3. monitor service - code-coverage start
GET /api/task/<task-status-id>/status
{
  "result": {
    "status": "running task...",
    "step-current": 2,
    "step-total": 3,
    "task-id": <task-id> 
  },
  "state": "IN_PROGRESS"
}


4. request service - code-coverage end
POST /api/task/code-coverage
{
	"name": "xili-code-coverage-task",
	"user": "xili",
	"priority": 10,
	"data": {
		"bigip-mgmt-ip": bigip_mgmt_ip,
		"module": "afm",
		"daemons": "autodosd",
		"mode": "end"
	}
}

>>>
HTTP/1.1 202 OK
Location: http://localhost/api/task/<task-status-id>/status

5. monitor service - code-coverage end
GET /api/task/<task-status-id>/status
{
  "result": {
    "commands": [ ... ],
    "links": {
      "log": "http://10.192.10.235/service/code-coverage/task-76/code-coverage.start.log",
      "report": "http://10.192.10.235/service/code-coverage/task-76"
    }
  },
  "state": "SUCCESS"
}


6. monitor all tasks
GET /api/task
{
    "total": <total-tasks>,
    "tasks": [ ... ]
}
```


## System Design
Strech:
- standalone Static File(html) Host Server
- CICD without downtime
- Scale

Host: Nginx+gunicorn+supervisord

```
REST API Server(Flask) -->  Task Queue(RabbitMQ)  --> Async Worker(Celery)
                       --> Datastore(Redis+MySQL) <--
```
