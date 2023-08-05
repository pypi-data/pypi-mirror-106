# -*- coding: utf-8 -*-
#    Copyright (C) 2021  The Project TONA Authors
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from flask import render_template, request, jsonify, flash
import datetime
from tona.web.main import app
from tona.models.project import create_project, Project
from tona.models.project_task import create_project_task, edit_project_task, ProjectTask
from tona.utils import api_response, convert_datetime


@app.route("/project")
@app.route("/project/<project_id>")
@app.route("/project/<project_id>/task")
@app.route("/project/<project_id>/task/<int:task_id>")
def project(project_id="", task_id=0):

    is_today = False
    is_tomorrow = False
    is_week  = False
    is_project = False
    is_task = False

    projects = None
    project = None
    tasks = None
    task = None

    if project_id == "today":
        is_today = True
        now = datetime.datetime.utcnow()
        due = datetime.datetime.utcnow() + datetime.timedelta(days=-1)
        due = due.replace(hour=23, minute=59, second=59)
        tasks = {
            "overdue": ProjectTask.select().where(ProjectTask.due < due,
                                                    ProjectTask.active == True,
                                                    ProjectTask.due != None,
                                                    ProjectTask.status != 'done'),
            "today": ProjectTask.select().where( (ProjectTask.due.year == now.year) & (ProjectTask.due.month == now.month) & (ProjectTask.due.day == now.day),
                                                    ProjectTask.active == True,
                                                    ProjectTask.due != None,
                                                    ProjectTask.status != 'done'),
        }
    elif project_id == "tomorrow":
        is_tomorrow = True
        now = datetime.datetime.utcnow() + datetime.timedelta(days=1)
        tasks = {            
            "tomorrow": ProjectTask.select().where( (ProjectTask.due.year == now.year) & (ProjectTask.due.month == now.month) & (ProjectTask.due.day == now.day),
                                                    ProjectTask.active == True,
                                                    ProjectTask.due != None,
                                                    ProjectTask.status != 'done'),
        }
    elif project_id == "week":
        is_week = True
        tasks = {}
        groups = {"overdue": -1, "today": 0, "+1": 1, "+2": 2,"+3": 3, "+4": 4, "+5": 5}
        for group in groups:
            now = datetime.datetime.utcnow() + datetime.timedelta(days=groups.get(group))
            if group == 'overdue':
                now = now.replace(hour=23, minute=59, second=59)
                tasks[group] = ProjectTask.select().where(ProjectTask.due < now,
                                                    ProjectTask.active == True,
                                                    ProjectTask.due != None,
                                                    ProjectTask.status != 'done')
            else:
                label = convert_datetime(now, tz_out=app.config['TZ'], fmt_out="%A, %b %d") if group != 'today' else 'today'
                tasks[label] = ProjectTask.select().where(
                                                    (ProjectTask.due.year == now.year) &
                                                    (ProjectTask.due.month == now.month) &
                                                    (ProjectTask.due.day == now.day),
                                                    ProjectTask.active == True,
                                                    ProjectTask.due != None,
                                                    ProjectTask.status != 'done')

    else:
        try:
            project_id = int("".join([n for n in project_id if n.isdigit()]))
            if project_id:
                project = Project.check(project_id)[0]
                is_project = True
                tasks = {
                    'todo': ProjectTask.select().where(ProjectTask.project_id == project.id, ProjectTask.active == True, 
                                                        ProjectTask.status == 'todo'),
                    'doing': ProjectTask.select().where(ProjectTask.project_id == project.id, ProjectTask.active == True, 
                                                        ProjectTask.status == 'doing'),
                    'review': ProjectTask.select().where(ProjectTask.project_id == project.id, ProjectTask.active == True, 
                                                        ProjectTask.status == 'review'),
                }
        except Exception as e:
            flash(str(e))

    if task_id:
        try:
            task = ProjectTask.check(task_id)[0]
            is_task = True
        except Exception as e:
            flash(str(e))

    projects = Project.select().where(Project.active == True).order_by(Project.name.asc())

    rt = render_template(
        "project.html",
        is_today=is_today,
        is_tomorrow=is_tomorrow,
        is_week=is_week,
        is_project=is_project,
        projects=projects,
        project=project,
        is_task=is_task,
        tasks=tasks,
        task=task)
    return rt

@app.route("/api/project", methods=['POST'])
def api_project():
    payload = api_response()
    code = 400
    try:
        data = request.json
        payload['payload'] = create_project(data.get('name'))
        payload['ok'] = True
        code = 200
    except Exception as e:
        app.logger.error(e)
        payload['message'] = str(e)
    return jsonify(payload), code

@app.route("/api/project/task", methods=['POST'])
@app.route("/api/project/task/<int:id>", methods=['PUT'])
def api_project_task(id=0):
    payload = api_response()
    code = 400
    try:
        data = request.json
        if request.method == 'POST':
            payload['payload'] = create_project_task(data.get('project_id', 0), data.get('name'))
        else:
            if id:
                payload['payload'] = edit_project_task(id, name=data.get('name', None),
                                                        description=data.get('description', None),
                                                        status=data.get('status', None),
                                                        due=data.get('due', None))
            else:
                raise Exception("For Edit is required ID")
        payload['ok'] = True
        code = 200
    except Exception as e:
        app.logger.error(e)
        payload['message'] = str(e)
    return jsonify(payload), code