import os
import time
from pathlib import Path

from flask import make_response, request, jsonify, Blueprint
from marker import Marker, TokenNotFoundError

from .console import WebConsole
from .jobs import JobTracker
from .utils import getArgsDefaults

############################# Init Flask ######################################

markerBP = Blueprint('marker', __name__)

############################# Global Variables ################################

MARKER = None
ARGS = {}

###############################################################################

@markerBP.route('/state')
def route_get_state():
    isValid = (MARKER is not None)
    if 'assgn_dir' in ARGS:
        path = ARGS.get('assgn_dir')
    else:
        path = os.path.abspath(Path.home())
    config = MARKER.cfg if isValid else None
    return { 'valid': isValid, 'path': path, 'config': config  }

@markerBP.route('/state', methods=["POST"])
def route_set_path():
    path = request.args.get('path', None)
    if path is None:
        return make_response("Path not included", 400)
    args = getArgsDefaults(assgn_dir=path)
    if setupMarker(args):
        return make_response("Success", 200)
    else:
        return make_response("Path isn't valid", 400)


###############################################################################


@markerBP.route('/')
def route_home():
    message = { 'message': 'Everything is OK here :)' }
    return make_response(message, 200)

###############################################################################

@markerBP.route('/config', methods=['GET', 'POST'])
def route_config():
    if request.method == 'GET':
        return MARKER.cfg
    else:
        return make_response("This isn't implemented yet :(", 400)

###############################################################################

@markerBP.route('/progress')
def route_progress():
    return JobTracker.getInfo()

@markerBP.route('/stopjob', methods=['POST'])
def route_stop_job():
    JobTracker.setStop()
    for i in range(30):
        if JobTracker.done:
            return make_response("Job stopped.", 200)
        time.sleep(0.1)
    return make_response("There was an error stopping the thread.", 400)
    
###############################################################################

@markerBP.route('/tokens', methods=['POST'])
def route_save_token():
    token = request.args.get('token', None)
    MARKER.lms.save_token(token)
    return make_response("Saved.", 200)


###############################################################################
############################# Results #########################################
###############################################################################


@markerBP.route('/results/')
def route_results():
    data = MARKER.getMarksheet().data
    if data is None:
        return make_response({"error": "Marksheet was not found"}, 401)
    response = [ {'username': u, 'marks': m} for u, m in data.items() ]
    return jsonify(response)


@markerBP.route('/results/<string:student_id>', methods=['GET', 'POST'])
def route_single_result(student_id): 
    student_dir = MARKER.getStudentDir(student_id)
    if student_dir is None:
        student_result = { 
            "marked": False, 
            "message": "Student directory doesn't exist. You may need to delete the marksheet and re-download submissions." ,
        }
        return student_result

    json_path = f'{student_dir}/{MARKER.cfg["results"]}'
    if not os.path.isfile(json_path):
        student_result = { 
            "marked": False, 
            "message": "Submission is not marked yet.",
            "path": os.path.abspath(student_dir),
        }
        return student_result
        
    student_result = {}
    # Add the directory onto the result so we can open up vscode :^)
    student_result["path"] = os.path.abspath(student_dir)
    student_result["marked"] = True
    student_result["data"] = open(json_path).read()
    return student_result

@markerBP.route('/stats')
def route_stats():
    return MARKER.stats([])


###############################################################################
############################# Downloading #####################################
###############################################################################

@markerBP.route('/download', methods=['POST'])
def route_download_all():
    allow_late = request.args.get('allow_late', 'false') == 'true'
    students = [] if request.json is None else request.json
    return JobTracker.runAsync(lambda:
        MARKER.download(students, False),
        "Downloading Submissions", "download"
    )

@markerBP.route('/download/<string:student_id>', methods=['POST'])
def route_download_single(student_id):
    allow_late = request.args.get('allow_late', 'false') == 'true'
    JobTracker.runSync(lambda:
        MARKER.download([student_id], allow_late)
    )
    return make_response("Download was successful", 200)


###############################################################################
############################# Preparing #######################################
###############################################################################

@markerBP.route('/prepare', methods=['POST'])
def route_prepare_all():
    students = [] if request.json is None else request.json
    return JobTracker.runAsync(lambda:
        MARKER.prepare(students),
        "Preparing Submissions", "prepare"
    )

@markerBP.route('/prepare/<string:student_id>', methods=['POST'])
def route_prepare_single(student_id):
    JobTracker.runSync(lambda:
        MARKER.prepare([student_id])
    )
    return route_single_result(student_id)

###############################################################################
############################# Running #########################################
###############################################################################

@markerBP.route('/run', methods=['POST'])
def route_run_all():
    recompile = request.args.get('recompile', 'false') == 'true'
    run_all = request.args.get('all', 'false') == 'true'
    students = [] if request.json is None else request.json
    return JobTracker.runAsync(lambda:
        MARKER.run(students, recompile, run_all, False),
        "Marking Submissions", "run"
    )

@markerBP.route('/run/<string:student_id>', methods=['POST'])
def route_run_single(student_id):
    recompile = request.args.get('recompile', 'false') == 'true'
    JobTracker.runSync(lambda:
        MARKER.run([student_id], recompile, False, False)
    )
    return route_single_result(student_id)

###############################################################################
######################### Uploading Marks #####################################
###############################################################################

@markerBP.route('/upload-marks', methods=['POST'])
def route_upload_marks_all():
    students = [] if request.json is None else request.json
    return JobTracker.runAsync(lambda:
        MARKER.upload_marks(students),
        "Uploading Marks", "upload-marks"
    )

@markerBP.route('/upload-marks/<string:student_id>', methods=['POST'])
def route_upload_marks_single(student_id):
    JobTracker.runSync(lambda:
        MARKER.upload_marks([student_id])
    )
    return make_response("Uploading marks successful", 200)

###############################################################################
####################### Uploading Reports #####################################
###############################################################################

@markerBP.route('/upload-reports', methods=['POST'])
def route_upload_reports_all():
    students = [] if request.json is None else request.json
    return JobTracker.runAsync(lambda:
        MARKER.upload_reports(students),
        "Uploading reports", "upload-reports"
    )

@markerBP.route('/upload-reports/<string:student_id>', methods=['POST'])
def route_upload_reports_single(student_id):
    JobTracker.runSync(lambda:
        MARKER.upload_reports([student_id])
    )
    return make_response("Uploading reports successful", 200)

###############################################################################
####################### Deleting Reports ##########*###########################
###############################################################################

@markerBP.route('/delete-reports', methods=['POST'])
def route_delete_reports_all():
    students = [] if request.json is None else request.json
    return JobTracker.runAsync(lambda:
        MARKER.delete_reports(students),
        "Deleting reports", "delete-reports"
    )

@markerBP.route('/delete-reports/<string:student_id>', methods=['POST'])
def route_delete_reports_single(student_id):
    JobTracker.runSync(lambda:
        MARKER.delete_reports([student_id])
    )
    return make_response("Deleting reports successful", 200)

###############################################################################
######################### Setting Status ######################################
###############################################################################

@markerBP.route('/set-status', methods=['POST'])
def route_set_status_all():
    students = [] if request.json is None else request.json
    status = request.args.get('status', 'incomplete')

    return JobTracker.runAsync(lambda:
        MARKER.set_status(status, students),
        "Setting status " + status, "set-status"
    )

@markerBP.route('/set-status/<string:student_id>', methods=['POST'])
def route_set_status_single(student_id):
    status = request.args.get('status', 'incomplete')
    JobTracker.runSync(lambda:
        MARKER.set_status(status, [student_id])
    )
    return make_response("Setting status successful", 200)

###############################################################################
###############################################################################
###############################################################################

import traceback

@markerBP.errorhandler(TokenNotFoundError)
def route_token_not_found(exc):
    return make_response({
        "status": 400,
        "message": "no_token",
    }, 400)

@markerBP.errorhandler(Exception)
def route_other_error(exc):
    return make_response({
        "message": traceback.format_exc(),
    }, 400)


@markerBP.route('/<path:u_path>')
def route_catch_all(u_path):
    message = { 'message': 'Request made to an invalid endpoint: ' + u_path }
    return make_response(message, 404)


###############################################################################
###############################################################################
###############################################################################

def setupMarker(args):
    """
    Attempts to set up the marker with the specified arguments. If the marker
    is set up successfully, `True` is returned, otherwise `False`.

    A `False` return value means that the configuration file specified was
    not found or able to be loaded properly.

    `args` must be as follows:
    ```
    args = {
        'assgn_dir': '...',
           'config': '...',
          'src_dir': '...'
    }
    ```
    """

    global ARGS
    global MARKER

    try:
        ARGS = args
        MARKER = Marker(args, WebConsole())
        return True
    except BaseException as exc:
        MARKER = None
        return False