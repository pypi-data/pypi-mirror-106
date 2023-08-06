import re
from sys import path
from fastapi.openapi.utils import get_openapi

def custom_openapi(api):
    if api.openapi_schema:
        return api.openapi_schema

    openapi_schema = get_openapi(
        title="Konasova API",
        version="1.0.0",
        description="OpenAPI for backend API",
        routes=api.routes,
        tags=[
            {
                "name": "auth",
                "description": "Эндпоинты для работы с **авторизацией**"
            },
            {
                "name": "system",
                "description": "Системные эндпоинты"
            }
        ]
    )


    # Custom documentation fastapi-jwt-auth
    headers = lambda type_token: {
        "name": "Authorization",
        "in": "header",
            "description": f"Bearer <{type_token}>",
        "required": True,
        "schema": {
            "title": "Authorization",
            "type": "string"
        },
    }

    mapp_type_token = {
        "authorize_access": "access_token",
        "authorize_refresh": "refresh_token"
    }

    def get_type_router(operation_id):
        if operation_id:
            if re.search(r"authorize_access", operation_id):
                return mapp_type_token["authorize_access"]
            elif re.search(r"authorize_refresh", operation_id):
                return mapp_type_token["authorize_refresh"]
            else:
                return ''
        else:
            return ''

    router_authorize = [route for route in api.routes[4:] if get_type_router(route.operation_id) != '']


    for route in router_authorize:
        method = list(route.methods)[0].lower()
        try:
            # If the router has another parameter
            openapi_schema["paths"][route.path][method]['parameters'].append(headers(get_type_router(route.operation_id)))
        except Exception:
            # If the router doesn't have a parameter
            openapi_schema["paths"][route.path][method].update({"parameters":[headers(get_type_router(route.operation_id))]})

    api.openapi_schema = openapi_schema
