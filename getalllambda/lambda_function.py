import json

import boto3

from Advertiser import Advertisers
from JsonReader import JsonReader
from YamlReader import YamlReader


def _get_client():
    s3_client = boto3.client('s3')
    return s3_client


def get_response(response_code, content):
    response = {
        "isBase64Encoded": False,
        "statusCode": response_code,
        "body": content,
        "headers": {
            "content-type": "application/json"
        }
    }
    return response


def lambda_handler(event, context):
    client = _get_client()
    result = client.list_objects(Bucket=event.get("s3_bucket", "orderlogs-to-json"),
                                 Prefix=event.get("s3_prefix", "prices"))
    advertisers = Advertisers()
    for o in result.get('Contents'):
        prefix_key = o.get('Key')
        data = client.get_object(Bucket=event.get("s3_bucket", "orderlogs-to-json"), Key=prefix_key)
        contents = data['Body'].read()
        if "yaml" in prefix_key:
            reader = YamlReader(contents)
        else:
            reader = JsonReader(contents)
        advertisers.append_advertiser(reader.parse())
    advertiser_json = json.dumps(advertisers.get_advertiser())
    return get_response(200, advertiser_json)
