from flask_restplus import Namespace, Resource, fields

api = Namespace('user', description='User related information')

user = api.model('User', {
    'identifier': fields.String(required=True),
    'name': fields.String(required=True)
})

USERS = [
    {'identifier': '123', 'name': 'Foo'},
    {'identifier': '456', 'name': 'Bar'}
]


@api.route('/')
class UserList(Resource):
    @api.doc('list_users')
    @api.marshal_list_with(user)
    def get(self):
        return USERS


@api.route('/<id>')
@api.param('id', 'User Identifier')
@api.response(404, 'User not found')
class User(Resource):
    @api.doc('get_user')
    @api.marshal_with(user)
    def get(self, id):
        for u in USERS:
            if u['identifier'] == id:
                return u
        api.abort(404)
