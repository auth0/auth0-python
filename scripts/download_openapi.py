import json
import requests

from pathlib import Path

openapi_management_url = 'https://auth0.com/docs/api/management/openapi.json'
openapi_management_path = Path.cwd() / 'openapi.management.json'

def read_json_file(path: Path) -> dict:
    with path.open('r', encoding='utf-8') as f:
        return json.load(f)

def download_file(url: str, path: Path, timeout=10) -> None:
    with requests.get(url, stream=True, timeout=timeout) as response:
        response.raise_for_status()
        with path.open('wb') as out_file:
            for chunk in response.iter_content(chunk_size=None):
                out_file.write(chunk)

def main():
    if openapi_management_path.exists():
        print(f'Reading current file {openapi_management_path.name}')
        current_openapi_management = read_json_file(openapi_management_path)
        current_title = current_openapi_management['info']['title']
        current_version = current_openapi_management['info']['version']
        print(f'Current title: {current_title}, version: {current_version}')

    print(f'Downloading {openapi_management_url} to {openapi_management_path.name}')
    download_file(openapi_management_url, openapi_management_path)

    print(f'Reading new file {openapi_management_path.name}')
    new_openapi_management = read_json_file(openapi_management_path)
    new_title = new_openapi_management['info']['title']
    new_version = new_openapi_management['info']['version']
    print(f'New title: {new_title}, version: {new_version}')

if __name__ == "__main__":
    main()
