# TODO
- [Admin] support delete user through API

- [Code Coverage] integrate cl2tests service
    - merge web service from Perforce //depot/project/automation/fit/cl2tests/main into GitLab https://gitswarm.f5net.com/secauto/api-service 
        - implementation choices:
            - extend cc worker synchronously within a task
            - or decouple into seperate indexing subtask and chained it with cc task (celery chaining)
    - move src2test db to a standalone server (or just api server for now)
    - APIs

    ```
        - POST /api/task/code-coverage
          { ...
            "data": {
              "dump-src2test-stats": "yes",
              "test": {
                "framework": <framework, e.g. fit, pytest>,
                "test-id": <test-id>
              }
            }
          }
        - GET /api/src2tests?file=:srcfile-p4-fullpath
        - GET /api/cl2tests?cl=:cl-id
        - GET /api/bz2tests?bz=:bz-id
    ```

    - Workflow
        - User post code coverage start&end task and can optionally indicate to record src2test stats
        - Code coverage worker need to work on recording src2test stats if asked to
            - requires code coverage script to dump src2test stats
            - requires code coverage task to collect the stats and save it to src2test database
        - User can query most relevant tests based on srcfile fullpath, changelist id, and bugzilla id
            - requires service to provide srcfile fullpaths given changelist
            - requires service to provide srcfile fullpaths given bugzilla
