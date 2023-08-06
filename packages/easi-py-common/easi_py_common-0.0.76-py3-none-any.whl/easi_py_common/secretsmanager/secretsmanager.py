import json
from typing import Optional

import boto3
import yaml


class ContentType:
    json = "json"
    yaml = "yaml"


class SecretsManager:
    def __init__(
        self,
        aws_access_key_id: str,
        aws_secret_access_key: str,
        region_name: str,
        aws_session_token: Optional[str] = None,
        **kwargs,
    ):
        session = boto3.session.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            region_name=region_name,
            aws_session_token=aws_session_token,
        )
        self.client = session.client(service_name="secretsmanager", **kwargs)

    def create_secrets(self, name: str, secret: str, **kwargs):
        response = self.client.create_secret(Name=name, SecretString=secret, **kwargs)
        return response

    def get_secret(
        self,
        secret_id: str,
        content_type: ContentType = ContentType.json,
        version_stage: Optional[str] = None,
        version_id: Optional[str] = None,
    ):
        kwargs = {"SecretId": secret_id}
        if version_stage is not None:
            kwargs["VersionStage"] = version_stage
        if version_id is not None:
            kwargs["VersionId"] = version_id
        response = self.client.get_secret_value(**kwargs)
        secret = response["SecretString"]
        if content_type == ContentType.json:
            return json.loads(secret)
        elif content_type == ContentType.yaml:
            return yaml.load(secret)
        else:
            raise ValueError("Unknown content type")
