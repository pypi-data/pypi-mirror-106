from fastapi_restful import Resource, set_responses

class Heartbeat(Resource):
    @set_responses(
        str,
        200,
        tags=["system"]
    )
    async def get(self):
        """ Проверка на активность сервиса """
        return 'OK'