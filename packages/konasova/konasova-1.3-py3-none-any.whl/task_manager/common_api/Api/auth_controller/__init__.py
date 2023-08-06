from task_manager.common_api.Api import api, APIv1
from .auth_resources import UserAuth, RefreshAccessToken, UserRegistration, UserLogout,\
     UserInfo, CheckToken, ChangePassword, UpdateUser

api.add_resource(UserAuth(), APIv1 + '/auth')
api.add_resource(RefreshAccessToken(), APIv1 + '/refresh')
api.add_resource(UserRegistration(), APIv1 + '/register')
api.add_resource(UserLogout(), APIv1 + '/logout')
api.add_resource(CheckToken(), APIv1 + '/check-token')
api.add_resource(UserInfo(), APIv1 + '/user/{id}')
api.add_resource(ChangePassword(), APIv1 + '/user/change-password')
api.add_resource(UpdateUser(), APIv1 + '/user/update')