# Git Branch Detailed Report

## Branch: `fix-windows-exec`
### Last 3 Commits:
```
42b480b (fix-windows-exec) fix(tools): use temp files instead of pipes for shell output on Windows
5a08bee fix(slack): handle empty text responses without regressing thread and media support
2e50a98 merge main into pr-673 and keep slack empty-text fallback without regressing thread/media support
```
### Unique Changes (vs main):
```
README.md                    | 111 +++++++--------------------------
 bridge/src/whatsapp.ts       |   3 +-
 nanobot/agent/tools/shell.py | 144 ++++++++++++++++++++++++++++++++-----------
 nanobot/channels/discord.py  |   3 +-
 nanobot/channels/feishu.py   |   4 +-
 nanobot/channels/matrix.py   |   6 +-
 nanobot/channels/mochat.py   |   4 +-
 nanobot/channels/telegram.py |   6 +-
 nanobot/cli/commands.py      |  40 ++++--------
 nanobot/config/__init__.py   |  26 +-------
 nanobot/config/loader.py     |  20 +++---
 nanobot/config/paths.py      |  55 -----------------
 nanobot/session/manager.py   |   3 +-
 nanobot/utils/__init__.py    |   4 +-
 nanobot/utils/helpers.py     |  11 ++++
 tests/test_commands.py       |  97 +----------------------------
 tests/test_config_paths.py   |  42 -------------
 17 files changed, 180 insertions(+), 399 deletions(-)
```

---
## Branch: `nnb`
### Last 3 Commits:
```
acf33b8 (origin/nnb, nnb) feat: integrate Telegram Pro (PR-1474) and Agent Swarm skill
e1cf248 Merge branch 'pr-1489' into pr-1474Merge branch 'pr-1489' into pr-1474
49d3e6d fix(subagent): dedupe duplicate spawn calls within session
```
### Unique Changes (vs main):
```
.gitignore                                 |   3 +-
 README.md                                  | 126 +--------
 bridge/src/whatsapp.ts                     |  88 ++-----
 nanobot/agent/context.py                   |  11 +-
 nanobot/agent/loop.py                      |  36 +--
 nanobot/agent/memory.py                    |   7 -
 nanobot/agent/subagent.py                  |  33 +++
 nanobot/agent/tools/base.py                |  77 +-----
 nanobot/agent/tools/mcp.py                 |  39 +--
 nanobot/agent/tools/message.py             |   2 +-
 nanobot/agent/tools/registry.py            |   4 -
 nanobot/channels/base.py                   |   5 +-
 nanobot/channels/dingtalk.py               |  57 +----
 nanobot/channels/discord.py                | 132 ++--------
 nanobot/channels/feishu.py                 | 307 ++++------------------
 nanobot/channels/manager.py                |   3 +-
 nanobot/channels/matrix.py                 |   6 +-
 nanobot/channels/mochat.py                 |   4 +-
 nanobot/channels/qq.py                     |  57 ++---
 nanobot/channels/slack.py                  |   7 +-
 nanobot/channels/telegram.py               | 331 +++++++-----------------
 nanobot/channels/whatsapp.py               |  13 -
 nanobot/cli/commands.py                    | 166 ++++++------
 nanobot/config/__init__.py                 |  26 +-
 nanobot/config/loader.py                   |  20 +-
 nanobot/config/paths.py                    |  55 ----
 nanobot/config/schema.py                   |  96 ++++---
 nanobot/heartbeat/service.py               |  25 +-
 nanobot/providers/__init__.py              |   3 +-
 nanobot/providers/azure_openai_provider.py | 210 ---------------
 nanobot/providers/base.py                  |  14 -
 nanobot/providers/custom_provider.py       |   8 +-
 nanobot/providers/litellm_provider.py      |  89 ++-----
 nanobot/providers/registry.py              | 118 +++++----
 nanobot/session/manager.py                 |   3 +-
 nanobot/utils/__init__.py                  |   4 +-
 nanobot/utils/helpers.py                   |  56 +---
 pyproject.toml                             |   6 +-
 skills/agent-swarm/SKILL.md                | 178 +++++++++++++
 skills/agent-swarm/checkpoint.py           | 160 ++++++++++++
 skills/agent-swarm/demo.py                 | 194 ++++++++++++++
 skills/agent-swarm/memory_upgrade.py       | 172 +++++++++++++
 skills/agent-swarm/swarm.py                | 230 +++++++++++++++++
 tests/test_azure_openai_provider.py        | 399 -----------------------------
 tests/test_base_channel.py                 |  25 --
 tests/test_commands.py                     |  97 +------
 tests/test_config_paths.py                 |  42 ---
 tests/test_cron_service.py                 |   2 -
 tests/test_dingtalk_channel.py             |  66 -----
 tests/test_feishu_post_content.py          |  27 +-
 tests/test_feishu_table_split.py           | 104 --------
 tests/test_heartbeat_service.py            |  21 +-
 tests/test_matrix_channel.py               |  20 +-
 tests/test_memory_consolidation_types.py   |  75 ------
 tests/test_message_tool_suppress.py        |  29 ---
 tests/test_qq_channel.py                   |  66 -----
 tests/test_task_cancel.py                  |  79 ++++++
 tests/test_telegram_channel.py             | 184 -------------
 tests/test_tool_validation.py              | 231 -----------------
 59 files changed, 1587 insertions(+), 3061 deletions(-)
```

---
## Branch: `nnb-restart`
### Last 3 Commits:
```
ec3f9d8 (origin/nnb-restart, nnb-restart) feat(telegram): add /restart command and windows-compatible restart script
acf33b8 (origin/nnb, nnb) feat: integrate Telegram Pro (PR-1474) and Agent Swarm skill
e1cf248 Merge branch 'pr-1489' into pr-1474Merge branch 'pr-1489' into pr-1474
```
### Unique Changes (vs main):
```
.gitignore                                 |   3 +-
 README.md                                  | 126 +--------
 bridge/src/whatsapp.ts                     |  88 ++-----
 nanobot/agent/context.py                   |  11 +-
 nanobot/agent/loop.py                      |  36 +--
 nanobot/agent/memory.py                    |   7 -
 nanobot/agent/subagent.py                  |  33 +++
 nanobot/agent/tools/base.py                |  77 +-----
 nanobot/agent/tools/mcp.py                 |  39 +--
 nanobot/agent/tools/message.py             |   2 +-
 nanobot/agent/tools/registry.py            |   4 -
 nanobot/channels/base.py                   |   5 +-
 nanobot/channels/dingtalk.py               |  57 +----
 nanobot/channels/discord.py                | 132 ++--------
 nanobot/channels/feishu.py                 | 307 ++++------------------
 nanobot/channels/manager.py                |   3 +-
 nanobot/channels/matrix.py                 |   6 +-
 nanobot/channels/mochat.py                 |   4 +-
 nanobot/channels/qq.py                     |  57 ++---
 nanobot/channels/slack.py                  |   7 +-
 nanobot/channels/telegram.py               | 365 +++++++++-----------------
 nanobot/channels/whatsapp.py               |  13 -
 nanobot/cli/commands.py                    | 166 ++++++------
 nanobot/config/__init__.py                 |  26 +-
 nanobot/config/loader.py                   |  20 +-
 nanobot/config/paths.py                    |  55 ----
 nanobot/config/schema.py                   |  96 ++++---
 nanobot/heartbeat/service.py               |  25 +-
 nanobot/providers/__init__.py              |   3 +-
 nanobot/providers/azure_openai_provider.py | 210 ---------------
 nanobot/providers/base.py                  |  14 -
 nanobot/providers/custom_provider.py       |   8 +-
 nanobot/providers/litellm_provider.py      |  89 ++-----
 nanobot/providers/registry.py              | 118 +++++----
 nanobot/session/manager.py                 |   3 +-
 nanobot/utils/__init__.py                  |   4 +-
 nanobot/utils/helpers.py                   |  56 +---
 nanobot/utils/restart_gateway.py           |  71 +++++
 pyproject.toml                             |   6 +-
 skills/agent-swarm/SKILL.md                | 178 +++++++++++++
 skills/agent-swarm/checkpoint.py           | 160 ++++++++++++
 skills/agent-swarm/demo.py                 | 194 ++++++++++++++
 skills/agent-swarm/memory_upgrade.py       | 172 +++++++++++++
 skills/agent-swarm/swarm.py                | 230 +++++++++++++++++
 tests/test_azure_openai_provider.py        | 399 -----------------------------
 tests/test_base_channel.py                 |  25 --
 tests/test_commands.py                     |  97 +------
 tests/test_config_paths.py                 |  42 ---
 tests/test_cron_service.py                 |   2 -
 tests/test_dingtalk_channel.py             |  66 -----
 tests/test_feishu_post_content.py          |  27 +-
 tests/test_feishu_table_split.py           | 104 --------
 tests/test_heartbeat_service.py            |  21 +-
 tests/test_matrix_channel.py               |  20 +-
 tests/test_memory_consolidation_types.py   |  75 ------
 tests/test_message_tool_suppress.py        |  29 ---
 tests/test_qq_channel.py                   |  66 -----
 tests/test_task_cancel.py                  |  79 ++++++
 tests/test_telegram_channel.py             | 184 -------------
 tests/test_tool_validation.py              | 231 -----------------
 60 files changed, 1693 insertions(+), 3060 deletions(-)
```

---
## Branch: `pr-1678`
### Last 3 Commits:
```
ed28f36 (pr-1678) Merge PR #1678 into pr-1678 (keeping local fixes for conflicts)
42b480b (fix-windows-exec) fix(tools): use temp files instead of pipes for shell output on Windows
5a08bee fix(slack): handle empty text responses without regressing thread and media support
```
### Unique Changes (vs main):
```
README.md                            | 111 +++---------
 bridge/src/whatsapp.ts               |   3 +-
 nanobot/agent/loop.py                |  30 ++--
 nanobot/agent/subagent.py            |  33 ++++
 nanobot/agent/tools/shell.py         | 144 +++++++++++----
 nanobot/channels/discord.py          |   3 +-
 nanobot/channels/feishu.py           |   4 +-
 nanobot/channels/matrix.py           |   6 +-
 nanobot/channels/mochat.py           |   4 +-
 nanobot/channels/telegram.py         | 331 ++++++++++-------------------------
 nanobot/cli/commands.py              | 166 ++++++++----------
 nanobot/config/__init__.py           |  26 +--
 nanobot/config/loader.py             |  20 +--
 nanobot/config/paths.py              |  55 ------
 nanobot/config/schema.py             |  96 +++++-----
 nanobot/heartbeat/service.py         |  25 ++-
 nanobot/session/manager.py           |   3 +-
 nanobot/utils/__init__.py            |   4 +-
 nanobot/utils/helpers.py             |  11 ++
 skills/agent-swarm/SKILL.md          | 178 +++++++++++++++++++
 skills/agent-swarm/checkpoint.py     | 160 +++++++++++++++++
 skills/agent-swarm/demo.py           | 194 ++++++++++++++++++++
 skills/agent-swarm/memory_upgrade.py | 172 ++++++++++++++++++
 skills/agent-swarm/swarm.py          | 230 ++++++++++++++++++++++++
 tests/test_commands.py               |  97 +---------
 tests/test_config_paths.py           |  42 -----
 tests/test_heartbeat_service.py      |  21 ++-
 tests/test_task_cancel.py            |  79 +++++++++
 28 files changed, 1479 insertions(+), 769 deletions(-)
```

---
## Branch: `pr-1696`
### Last 3 Commits:
```
071b649 (HEAD -> pr-1696) Merge PR #1678 into pr-1696 (manual conflict resolution with Windows fixes)\n\nPR #1678: Fix Windows shell execution hang by using temp files instead of pipes for stdout/stderr. This prevents deadlocks when child processes (like browsers) are spawned from the agent loop on Windows.
3f5d87e Merge PR #1678 into pr-1696 (manual conflict resolution with Windows fixes)
bc1adea feat: add task queue system for background task execution
```
### Unique Changes (vs main):
```
README.md                             |  20 ++
 nanobot/agent/loop.py                 |  51 ++-
 nanobot/agent/subagent.py             |  33 ++
 nanobot/agent/tools/shell.py          | 144 ++++++--
 nanobot/channels/telegram.py          | 321 +++++------------
 nanobot/cli/commands.py               | 540 +++++++++++++++++++----------
 nanobot/config/schema.py              |  87 ++---
 nanobot/gateway.py                    | 142 ++++++++
 nanobot/heartbeat/service.py          |  25 +-
 nanobot/providers/custom_provider.py  |   3 +-
 nanobot/providers/litellm_provider.py |   2 +
 nanobot/task_queue.py                 | 636 ++++++++++++++++++++++++++++++++++
 nanobot/task_queue_gateway.py         | 197 +++++++++++
 skills/agent-swarm/SKILL.md           | 178 ++++++++++
 skills/agent-swarm/checkpoint.py      | 160 +++++++++
 skills/agent-swarm/demo.py            | 194 +++++++++++
 skills/agent-swarm/memory_upgrade.py  | 172 +++++++++
 skills/agent-swarm/swarm.py           | 230 ++++++++++++
 task_queue_cli.py                     | 277 +++++++++++++++
 test_task_queue.py                    |  20 ++
 tests/test_commands.py                | 141 +++++++-
 tests/test_heartbeat_service.py       |  21 +-
 tests/test_task_cancel.py             |  79 +++++
 23 files changed, 3149 insertions(+), 524 deletions(-)
```

---
## Branch: `true-swarm-test`
### Last 3 Commits:
```
ab31024 (true-swarm-test) feat: implement load balancing between gemini-3-flash and flash-preview
846a5f6 feat: upgrade True Swarm to support Multi-Model allocation
6502fb5 feat: implement True Swarm orchestration using spawn tool
```
### Unique Changes (vs main):
```
.gitignore                                 |     3 +-
 README.md                                  |   126 +-
 bridge/src/whatsapp.ts                     |    88 +-
 logs/error.log                             | 15774 +++++++++++++++++++++++++++
 logs/out.log                               |     0
 nanobot/agent/context.py                   |    11 +-
 nanobot/agent/loop.py                      |    36 +-
 nanobot/agent/memory.py                    |     7 -
 nanobot/agent/subagent.py                  |    33 +
 nanobot/agent/tools/base.py                |    77 +-
 nanobot/agent/tools/cron.py                |    24 +-
 nanobot/agent/tools/mcp.py                 |    39 +-
 nanobot/agent/tools/message.py             |     2 +-
 nanobot/agent/tools/registry.py            |     4 -
 nanobot/channels/base.py                   |     5 +-
 nanobot/channels/dingtalk.py               |    57 +-
 nanobot/channels/discord.py                |   132 +-
 nanobot/channels/feishu.py                 |   307 +-
 nanobot/channels/manager.py                |     3 +-
 nanobot/channels/matrix.py                 |     6 +-
 nanobot/channels/mochat.py                 |     4 +-
 nanobot/channels/qq.py                     |    57 +-
 nanobot/channels/slack.py                  |     7 +-
 nanobot/channels/telegram.py               |   331 +-
 nanobot/channels/whatsapp.py               |    13 -
 nanobot/cli/commands.py                    |   166 +-
 nanobot/config/__init__.py                 |    26 +-
 nanobot/config/loader.py                   |    20 +-
 nanobot/config/paths.py                    |    55 -
 nanobot/config/schema.py                   |    96 +-
 nanobot/heartbeat/service.py               |    25 +-
 nanobot/providers/__init__.py              |     3 +-
 nanobot/providers/azure_openai_provider.py |   210 -
 nanobot/providers/base.py                  |    14 -
 nanobot/providers/custom_provider.py       |     8 +-
 nanobot/providers/litellm_provider.py      |    89 +-
 nanobot/providers/registry.py              |   118 +-
 nanobot/session/manager.py                 |     3 +-
 nanobot/utils/__init__.py                  |     4 +-
 nanobot/utils/helpers.py                   |    56 +-
 pyproject.toml                             |     6 +-
 skills/agent-swarm/SKILL.md                |    37 +
 skills/agent-swarm/checkpoint.py           |   160 +
 skills/agent-swarm/demo.py                 |   194 +
 skills/agent-swarm/memory_upgrade.py       |   172 +
 skills/agent-swarm/swarm.py                |   160 +
 tests/test_azure_openai_provider.py        |   399 -
 tests/test_base_channel.py                 |    25 -
 tests/test_commands.py                     |    97 +-
 tests/test_config_paths.py                 |    42 -
 tests/test_cron_service.py                 |     2 -
 tests/test_dingtalk_channel.py             |    66 -
 tests/test_feishu_post_content.py          |    27 +-
 tests/test_feishu_table_split.py           |   104 -
 tests/test_heartbeat_service.py            |    21 +-
 tests/test_matrix_channel.py               |    20 +-
 tests/test_memory_consolidation_types.py   |    75 -
 tests/test_message_tool_suppress.py        |    29 -
 tests/test_qq_channel.py                   |    66 -
 tests/test_task_cancel.py                  |    79 +
 tests/test_telegram_channel.py             |   184 -
 tests/test_tool_validation.py              |   231 -
 workspace/memory/MEMORY.md                 |     9 +
 63 files changed, 17181 insertions(+), 3063 deletions(-)
```

---
## Branch: `main`
### Last 3 Commits:
```
0a5daf3 (upstream/main, origin/main, origin/HEAD, main) docs: update readme for multiple instances and cli
7fa0cd4 merge: integrate pr-1581 multi-instance path cleanup
20dfaa5 refactor: unify instance path resolution and preserve workspace override
```

---
