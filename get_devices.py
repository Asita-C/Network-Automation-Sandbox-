import requests
from auth_token import auth_token

def main():
    token = auth_token()

    api_path = "https://sandboxdnac.cisco.com/dna"
    headers = {"Content-Type": "application/json", "X-Auth-Token": token}

    get_resp = requests.get( f"{api_path}/intent/api/v1/network-device", headers=headers )

    import json; print(json.dumps(get_resp.json(), indent=2))


if __name__ == "__main__":
    main()




