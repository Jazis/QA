import os
import json
import allure
import jsonschema


def validate_json_schema(data, json_schema_filename):
    with allure.step(f'Validation of JSON schema "{json_schema_filename}"'):
        try:
            data = json.loads(data) if isinstance(data, str) else data
            jsonschema.validate(data, get_json_schema(json_schema_filename))
        except jsonschema.exceptions.ValidationError as e:
            raise AssertionError("well-formed but invalid JSON:", e)
        except json.decoder.JSONDecodeError as e:
            raise AssertionError("poorly-formed text, not JSON:", e)


def get_json_schema(json_name):
    if isinstance(json_name, set):
        json_name = next(iter(json_name))
    current_dir = os.path.dirname(__file__)
    root_dir = os.path.abspath(os.path.join(current_dir, '..'))
    path_to_json = os.path.join(root_dir, 'data', 'json_schemas', f'{json_name}.json')
    json_schema = json.loads(open(path_to_json, encoding='utf-8').read())
    allure.attach.file(path_to_json,
                       name=f'json_schema: {json_name}.json',
                       attachment_type=allure.attachment_type.JSON)
    return json_schema
