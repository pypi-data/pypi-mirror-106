import subprocess
from typing import Dict, List, Union

from cleo.commands.command import Command
from cleo.io.inputs.argument import Argument
from poetry.console.application import Application
from poetry.plugins.application_plugin import ApplicationPlugin


class CustomCommand(Command):
    name = "do"
    description = "Run customized commands."
    help = """\
Config <info>pyproject.toml</info> with <info>tool.poetry_scripts.scripts</info>

<info>
[tool.poetry_scripts.scripts]
test = 'pytest'
</info>
"""

    arguments = [
        Argument("cmd", required=True, description="pre-defined command to run"),
    ]

    def __init__(self, config: Dict[str, Dict[str, Union[str, List[str]]]]):
        super().__init__()
        self._scripts = config.get("scripts", {})
        self._options = config.get("options", {})

    def handle(self) -> int:
        command = self.argument("cmd")
        script = self._scripts.get(command)
        if not script:
            print(f"missing script {command}")
            return 2
        subprocess.run(script)
        return 0


class MyApplicationPlugin(ApplicationPlugin):
    def activate(self, application: Application) -> None:
        config = application.poetry.pyproject.data["tool"].get("poetry_scripts")
        application.command_loader.register_factory("do", lambda: CustomCommand(config))
