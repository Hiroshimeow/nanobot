from nanobot.agent.tools.registry import ToolRegistry
from nanobot.bus.queue import MessageBus
from nanobot.agent.subagent import SubagentManager
from nanobot.config.schema import ExecToolConfig
from nanobot.agent.tools.shell import ExecTool
from nanobot.agent.tools.web import WebSearchTool, WebFetchTool
from nanobot.agent.tools.filesystem import EditFileTool, ListDirTool, ReadFileTool, WriteFileTool
from pathlib import Path


def register_core_tools(
    tools: ToolRegistry,
    workspace: Path,
    bus: MessageBus,
    provider: str,
    subagents: SubagentManager,
    brave_api_key: str | None = None,
    web_proxy: str | None = None,
    exec_config: ExecToolConfig | None = None,
    restrict_to_workspace: bool = False,
):
    """Register core tools for the agent."""
    allowed_dir = workspace if restrict_to_workspace else None
    for cls in (ReadFileTool, WriteFileTool, EditFileTool, ListDirTool):
        tools.register(cls(workspace=workspace, allowed_dir=allowed_dir))

    web_search_tool = WebSearchTool(api_key=brave_api_key, proxy=web_proxy)
    tools.register(web_search_tool)

    web_fetch_tool = WebFetchTool(proxy=web_proxy)
    tools.register(web_fetch_tool)

    exec_tool = ExecTool(
        timeout=exec_config.timeout if exec_config else 60,  # Default timeout
        working_dir=str(workspace),
        restrict_to_workspace=restrict_to_workspace,
        path_append=exec_config.path_append if exec_config else "",
    )
    tools.register(exec_tool)
