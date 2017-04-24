import json
from twisted.enterprise import adbapi
from twisted.internet import defer
from event_handler.use_cases import request_objects as req
from event_handler.repository import adbapirepo as mr
from event_handler.use_cases import event_use_cases as uc
from event_handler.serializers import application_serializer as app_ser


DBPOOL = adbapi.ConnectionPool(
    "MySQLdb",
    host='localhost',
    user='root',
    database='dummy_sportsbook',
    password='dummy_password'
)


from klein import Klein
app = Klein()


@app.route('/events/<int:event_id>')
@defer.inlineCallbacks
def list_one_event(request, event_id):

    request_object = req.EventListRequestObject.from_dict(
        {"filters":
             {"event_id": event_id}
         })

    repo = mr.MysqlAsyncRepo(DBPOOL)
    use_case = uc.EventListUseCase(repo)
    response = yield use_case.execute(request_object)

    request.setHeader('Content-Type', 'application/json')
    defer.returnValue(json.dumps(response.value, cls=app_ser.EventEncoder))


@app.route('/events/<int:event_id>/shift/<int:secs>', methods=['POST'])
@defer.inlineCallbacks
def postpone_event(request, event_id, secs):

    request_object = req.EventShiftRequestObject.from_dict(
        {"event_id": event_id,
         "secs": secs
         }
    )

    repo = mr.MysqlAsyncRepo(DBPOOL)
    use_case = uc.EventShiftUseCase(repo)
    response = yield use_case.execute(request_object)

    request.setHeader('Content-Type', 'application/json')
    defer.returnValue(json.dumps(response.value, cls=app_ser.EventEncoder))


app.run("localhost", 8080)
