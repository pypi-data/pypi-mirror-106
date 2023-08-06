from typing import List
import os
import shutil
import subprocess
from uuid import uuid4
from aws_cdk import core
import aws_cdk.aws_lambda as lambda_


class AppLambdaLayer(lambda_.LayerVersion):

    def __init__(self, scope: core.Construct, construct_id: str, include_paths: List[str] = None):
        if include_paths is None:
            include_paths = []

        shutil.rmtree("_build/app_lambda_layer", ignore_errors=True)
        os.makedirs("_build/app_lambda_layer/python")
        requirements_file_name = uuid4().hex
        subprocess.run(["poetry", "export", "-f", "requirements.txt", ">", f"_build/{requirements_file_name}"])
        subprocess.run(
            ["pip", "install", "-r", f"_build/{requirements_file_name}", "-t", "_build/app_lambda_layer/python"])
        for path in include_paths:
            shutil.copytree(path, f"_build/app_lambda_layer/python")

        super().__init__(
            scope,
            construct_id,
            code=lambda_.Code.from_asset("_build/app_lambda_layer"),
            compatible_runtimes=[lambda_.Runtime.PYTHON_3_8],
        )

        os.remove(f"_build/{requirements_file_name}")
