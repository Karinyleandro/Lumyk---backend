from flask_restx import Namespace, Resource

api = Namespace('health', description='Health de checagem')

@api.route('/')
class HealthCheck(Resource):
    def get(self):
        return {"mensagem": "Backend online!"}, 200