import os
from worker.config import Config
from worker.app import celery, db
from worker.app.util import run, cmd_info, CommandErrorException


@celery.task(bind=True)
def code_coverage_task(self, task_id, bigip_mgmt_ip, module, daemons, mode):
    print "Invoking code_coverage_task(%s, %s, %s, %s, %s, %s)" \
            % (self, task_id, bigip_mgmt_ip, module, daemons, mode)
    self.update_state(state='IN_PROGRESS')

    db.update_task_status(task_id, 'STARTED')
    db.add_task_msg(task_id, '[CodeCoverageWorker] Started task %s...' % task_id) # noqa

    # executing task...
    cmds = []

    # tmpdir = '%s/task-%s' % (Config.CODE_COVERAGE_TMPDIR, task_id)
    # shared among start task and end task
    tmpdir = '%s/bigip-%s' % (Config.CODE_COVERAGE_TMPDIR, bigip_mgmt_ip)
    sources_copy_path = '%s/sources-cp' % tmpdir
    outdir = '%s/task-%s' % (Config.CODE_COVERAGE_OUTDIR, task_id)
    # rel_outdir = outdir[len(Config.WORKER_WEB_SERVER_ROOT_FOLDER):]
    logfile = os.path.join(outdir, 'code-coverage.%s.log' % mode)
    rel_logfile = logfile[len(Config.WORKER_WEB_SERVER_ROOT_FOLDER):]
    reportfile = os.path.join(outdir, 'code-coverage')
    rel_reportfile = reportfile[len(Config.WORKER_WEB_SERVER_ROOT_FOLDER):]
    log_link = 'http://%s%s' % (Config.WORKER_MGMT_IP, rel_logfile)
    report_link = 'http://%s%s' % (Config.WORKER_MGMT_IP, rel_reportfile)

    cmd = 'sudo mkdir -p %s' % outdir
    r = run(cmd)
    cmds.append(cmd_info(cmd, r))
    if r.rc != 0:
        raise CommandErrorException(cmd_info(cmd, r))

    def construct_cmd():
        return (
            'sudo python cli.py'
            + ' --sources-copy-path %s' % sources_copy_path
            + ' --bigip-mgmtip %s' % bigip_mgmt_ip
            + ' --module %s' % module
            + (' --daemons %s' % daemons if daemons else '')
            + ' --outdir %s' % outdir
            + ' --tmpdir %s' % tmpdir
            + ' --mode %s' % mode
            + ' > %s' % logfile
        )
    cmd = 'cd %s && %s' % (Config.CODE_COVERAGE_BINDIR, construct_cmd())

    # update cache
    meta = {
        'cmd': cmd,
        'links': {
            'log': log_link
        }
    }
    self.update_state(state='IN_PROGRESS', meta=meta)
    db.add_task_msg(task_id, '[CodeCoverageWorker] Running Command: %s' % cmd)
    db.add_task_msg(task_id, '[CodeCoverageWorker] Log Link: %s' % log_link)
    db.add_task_msg(task_id, '[CodeCoverageWorker] Report Link: %s' % report_link) # noqa

    r = run(cmd)
    cmds.append(cmd_info(cmd, r))
    if r.rc != 0:
        raise CommandErrorException(cmd_info(cmd, r))

    db.update_task_status(task_id, 'COMPLETED')
    db.add_task_msg(task_id, '[CodeCoverageWorker] Completed task %s...' % task_id) # noqa

    return {
        'commands': cmds,
        'links': {
            'log': log_link,
            'report': report_link
        }
    }
