import os

changed_files = os.popen(
    f"git diff --name-only ${{{{ github.event.pull_request.base.sha }}}} ${{{{ github.sha }}}}").read()

if "package.json" in changed_files:
    print("::set-output name=PACKAGE_JSON_CHANGED::true")
else:
    print("::set-output name=PACKAGE_JSON_CHANGED::true")
