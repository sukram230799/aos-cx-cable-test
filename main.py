# %% [markdown]
# # Central API Notebook
# 
# [![](data:image/png;base64,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)](https://developer.arubanetworks.com/aoscx/)
# 
# Find the documentation here: https://developer.arubanetworks.com/aoscx/
# 
# Find the API reference here: https://developer.arubanetworks.com/aoscx/reference/
# 
# Find the introduction here: https://developer.arubanetworks.com/aoscx/docs/introduction

# %% [markdown]
# ## Import packages

# %%
import httpx
from urllib.parse import quote_plus
import json
import time
from typing import Optional

# %% [markdown]
# ## Login to Switch
# 
# Using httpx Client. Session metadata, such as cookies, is stored in the client object.
# Sessions are limited to 6 per Switch

# %%
base_url = "https://192.168.0.78"
version = "v10.15"


client = httpx.Client(verify=False)

login_result = client.post(f"{base_url}/rest/{version}/login", params={
    "username": "admin",
    "password": ""
})

login_result.text

# %% [markdown]
# ## CLI Test

# %%
def cli(client: httpx.Client, cmd: str) -> str:
    result = client.post(f"{base_url}/rest/{version}/cli",
                         json={"cmd": cmd})
    return result.text

cli(client=client, cmd="show uptime")

# %% [markdown]
# ## Cable Diagnostics
# 
# **Important**: During the cable diagnostics the switch will interrupt client connectivity.
# 
# 1. Initiate Interface Diagnostics Tests
# 2. Wait for completion (`result.json()["state"] == "complete"`)
# 3. Delete request (to allow retest, we could also check beforehand)

# %%
test_interface = "1/1/1"

# %%
def interface_diag_test(client: httpx.Client, interface: str, test: str) -> httpx.Response:
    result = client.post(f"{base_url}/rest/{version}/system/interfaces/{quote_plus(interface)}/interface_diag_tests", json={
        "interface": f"/rest/{version}/system/interfaces/{quote_plus(interface)}",
        "test": test
    })

    print(result.status_code, result.text)

    time.sleep(7)
    while True:
        result = client.get(
            f"{base_url}/rest/{version}/system/interfaces/{quote_plus(interface)}/interface_diag_tests/{test}")
        print(result.status_code, result.text)
        if (result.json()["state"] != "complete"):
            time.sleep(1)
        else:
            break

    client.delete(
        f"{base_url}/rest/{version}/system/interfaces/{quote_plus(interface)}/interface_diag_tests/{test}")
    return result


interface_diag_test(client, test_interface, "cable_diagnostic").json()

# %% [markdown]
# ### Result
# 
# 10/100mbit:
# ```json
# {
#     "cable_diagnostic_result": {
#         "1-2": { "status": "good" },
#         "3-6": { "status": "good" },
#         "4-5": { "status": "good" },
#         "7-8": { "status": "good" }
#     }
# }
# ```
# 
# 1gbit:
# ````json
# {
#     "cable_diagnostic_result": {
#         "1-2": { "status": "good" },
#         "3-6": { "status": "good" },
#         "4-5": { "status": "open" },
#         "7-8": { "status": "open" }
#     }
# }
# ```

# %% [markdown]
# ## Set interface speed

# %%
def set_speed(client: httpx.Client, interface: str, speeds: str) -> httpx.Response:
    result = client.patch(f"{base_url}/rest/{version}/system/interfaces/{quote_plus(interface)}", json={
        "user_config": {
            "speeds": speeds
        }
    })
    return result

set_speed(client, test_interface, "10-full 10-half 100-half 100-full")

# %% [markdown]
# ## Remove interface speed

# %%
def remove_speed(client: httpx.Client, interface: str) -> httpx.Response:
    result = client.patch(f"{base_url}/rest/{version}/system/interfaces/{quote_plus(interface)}", json={
        "user_config": {
            "speeds": ""
        }
    })
    return result

remove_speed(client, test_interface)

# %% [markdown]
# ## Logout of switch
# 
# Sessions are limited to 6 per Switch

# %%
logout_result = client.post(f"{base_url}/rest/{version}/logout")

logout_result


