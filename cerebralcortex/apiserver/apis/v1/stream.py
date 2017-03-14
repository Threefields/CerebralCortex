from pprint import pprint

from flask import request
from flask_restplus import Namespace, Resource, fields

api = Namespace('stream', description='Data and annotation stream related information')

# TODO: Look in to this: Define model using JSON Schema
# http://flask-restplus.readthedocs.io/en/stable/marshalling.html
stream = api.model('Stream', {
    'identifier': fields.String(required=True),
    'name': fields.String(required=True)
})

STREAMS = [
    {
        "identifier": "31a84a5d-549b-480b-8b6d-9faa898894f0",
        "owner": "a970e186-e960-11e6-bf0e-fe55135034f3",
        "name": "ecg",
        "description": "RAW ecg from AutoSense",
        "data_descriptor": [
            {
                "type": "number",
                "unit": "none"
            }
        ],
        "execution_context": {
            "processing_module": "61b7e1ca-3112-40bd-a754-442361b9b62d"
        },
        "annotations": [
            {
                "name": "study",
                "identifier": "5b7fb6f3-7bf6-4031-881c-a25faf112dd9"
            },
            {
                "name": "privacy",
                "identifier": "01dd3847-4bae-418b-8fcd-03efc4607df0"
            },
            {
                "name": "access control",
                "identifier": "d1108a2c-fe86-4adc-8d95-f8bcf379955b"
            },
            {
                "name": "platform",
                "identifier": "aec29183-3a45-4ab4-9beb-72475b3cf38a"
            },
            {
                "name": "informed consent",
                "identifier": "aec29183-3a45-4ab4-9beb-72475b3cf38b"
            }
        ]
    },
    {
        "identifier": "8405dc31-fca9-4390-840e-5c888c3dbba0",
        "user": "a970e186-e960-11e6-bf0e-fe55135034f3",
        "name": "80th_percentile_rr_variance",
        "description": "80th percentile",
        "data_descriptor": [
            {
                "type": "number",
                "unit": "milliseconds",
                "descriptive_statistic": "80th_percentile"
            }
        ],
        "execution_context": {
            "processing_module": "ac72b0bc-8e0f-45f2-87a9-08642b757f61",
            "input_parameters": [
                {
                    "name": "window_size",
                    "value": 60.0
                },
                {
                    "name": "window_offset",
                    "value": 60.0
                }
            ],
            "input_streams": [
                {
                    "name": "ecg_rr_interval",
                    "stream_identifier": "5b7fb6f3-7bf6-4031-881c-a25faf112dd1"
                }
            ]
        },
        "annotations": [
            {
                "name": "study",
                "identifier": "5b7fb6f3-7bf6-4031-881c-a25faf112dd9"
            },
            {
                "name": "privacy",
                "identifier": "01dd3847-4bae-418b-8fcd-03efc4607df0"
            },
            {
                "name": "access control",
                "identifier": "d1108a2c-fe86-4adc-8d95-f8bcf379955b"
            },
            {
                "name": "data_source",
                "identifier": "d7cfab9d-c5c1-436f-a145-b03a7e3e1704"
            },
            {
                "name": "platform",
                "identifier": "aec29183-3a45-4ab4-9beb-72475b3cf38a"
            }
        ]
    }

]


@api.route('/')
class StreamList(Resource):
    @api.doc('list_streams')
    # @api.marshal_list_with(stream)
    def get(self):
        return STREAMS


@api.route('/<uuid:identifier>')
@api.param('identifier', 'Stream Details')
@api.response(404, 'Stream not found')
class Stream(Resource):
    @api.doc('get_stream_by_identifier')
    # @api.marshal_with(stream)
    def get(self, identifier):
        for u in STREAMS:
            if u['identifier'] == str(identifier):
                return u
        api.abort(404)

    @api.doc('create_stream_by_identifier')
    def post(self, identifier):
        pprint(request.json)

        # TODO: What should the response object look like?
        return request.json, 201


@api.route('/<uuid:identifier>/data')
@api.param('identifier', 'stream identifier')
class StreamData(Resource):
    @api.doc('put data into stream')
    def put(self, identifier):
        pprint(request.json)

        # TODO: What should the response object look like?
        return request.json
        # api.abort(404)


        # Error format: https://github.com/googleapis/googleapis/blob/master/google/rpc/code.proto
        # {
        #     "error": {
        #         "code": 401,
        #         "message": "Request had invalid credentials.",
        #         "status": "UNAUTHENTICATED",
        #         "details": [{
        #             "@type": "type.googleapis.com/google.rpc.RetryInfo",
        #             ...
        #         }]
        #     }
        # }
