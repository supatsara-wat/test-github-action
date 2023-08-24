import os


def set_github_action_output(output_name, output_value):
    f = open(os.path.abspath(os.environ["GITHUB_OUTPUT"]), "a")
    f.write(f'{output_name}={output_value}')
    f.close()


changed_files = os.popen(
    f"git diff --name-only ${{{{ github.event.pull_request.base.sha }}}} ${{{{ github.sha }}}}").read()

if "package.json" in changed_files:
    set_github_action_output('PACKAGE_JSON_CHANGED', 'true')
else:
    set_github_action_output('PACKAGE_JSON_CHANGED', 'true')
