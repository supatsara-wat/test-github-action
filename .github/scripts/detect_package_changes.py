import os

changed_files = os.popen(
    f"git diff --name-only ${{{{ github.event.pull_request.base.sha }}}} ${{{{ github.sha }}}}").read()

if "package.json" in changed_files:
    print("PACKAGE_JSON_CHANGED=true")
else:
    print("PACKAGE_JSON_CHANGED=false")

print(str(changed_files))
