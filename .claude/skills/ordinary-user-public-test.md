# /ordinary-user-public-test — Ordinary User Public Test Link

为普通用户提供可访问的临时公开测试链接，并验证它真的能打开、能提问、能返回证据。

## 触发条件

当用户要求：
- 提供普通用户可访问的测试链接
- 检查测试页面为什么报错
- 继续处理 public test / ordinary-user test
- 修复 Streamlit public tunnel 卡在 loading / CONNECTING

## 核心判断

优先使用普通 HTTP 测试页：

```bash
OPENROUTER_DAILY_BUDGET_USD=1.00 OPENROUTER_MODEL=openai/gpt-4.1-mini .venv/bin/python scripts/public_test_app.py --host 127.0.0.1 --port 8510
```

不要把 Streamlit quick tunnel 当成默认公开交付路径。已经验证过多次：Streamlit 本地页面可用，Cloudflare quick tunnel 也可能返回 HTTP 200 和 `/_stcore/health=ok`，但浏览器端仍可能停在 `data-test-connection-state="CONNECTING"`，普通用户看到的就是空转页面。

HTTP 测试页应尽量保持和 Streamlit 版一致的呈现结构：左侧 Answer engine / Condition / Advanced settings / Find by keyword，主区 Research Chat / Ask the vault / 统计行 / 示例问题，底部 chat input，回答后显示 read path、trust block、provenance badges、source titles。

## 启动公开链接

### Step 1: 启动 HTTP 测试页

```bash
cd /Users/jiawei/Desktop/insclaude/feline-research-os
OPENROUTER_DAILY_BUDGET_USD=1.00 OPENROUTER_MODEL=openai/gpt-4.1-mini .venv/bin/python scripts/public_test_app.py --host 127.0.0.1 --port 8510
```

### Step 2: 启动 Cloudflare quick tunnel

```bash
/tmp/cloudflared-bin/cloudflared tunnel --protocol http2 --url http://127.0.0.1:8510
```

记录 tunnel 输出里的 `https://*.trycloudflare.com` 链接。说明这是临时链接，依赖本地 HTTP 进程和 cloudflared 进程继续运行。

## 验证标准

至少跑 3 个样本后再交付链接：

1. 本地健康检查
2. 公开健康检查
3. 公开首页内容检查
4. 至少 1 个真实问答 POST

推荐命令：

```bash
bash scripts/check_public_test_page.sh https://YOUR-TUNNEL.trycloudflare.com
```

Manual equivalent:

```bash
curl -sS --max-time 10 http://127.0.0.1:8510/health
curl -sS --max-time 15 https://YOUR-TUNNEL.trycloudflare.com/health
curl -sS --max-time 20 https://YOUR-TUNNEL.trycloudflare.com/ | rg -n "Feline Research OS|Ask the Vault|解释CKD|FIP怎么识别"
curl -sS --max-time 180 -X POST --data-urlencode 'question=FIP怎么识别' https://YOUR-TUNNEL.trycloudflare.com/ask
```

可选但推荐：用 browse/gstack 做浏览器级检查。若 browse 自身异常，不要把 browse 故障误判成页面故障；用 HTTP 健康、HTML 内容和真实 POST 结果交叉判断。

## 失败处理

### 预算错误

如果页面提示 `OPENROUTER_DAILY_BUDGET_USD not set`，用同一个 shell 重新启动服务：

```bash
OPENROUTER_API_KEY=<key> OPENROUTER_DAILY_BUDGET_USD=1.00 .venv/bin/python scripts/check_openrouter_budget_guard.py
OPENROUTER_DAILY_BUDGET_USD=1.00 OPENROUTER_MODEL=openai/gpt-4.1-mini .venv/bin/python scripts/public_test_app.py --host 127.0.0.1 --port 8510
```

For hosted Streamlit, set the same values in Streamlit secrets and redeploy/restart. Do not debug disease routing until this preflight passes or the sidebar says the OpenRouter key and project daily budget guard are loaded.

### Streamlit 一直 loading

不要继续调 Streamlit quick tunnel 作为普通用户入口。改用 `scripts/public_test_app.py`，因为它是普通 HTML form + HTTP POST，不依赖 websocket hydration。

### 本地 curl 假阴性

如果沙箱内 `curl http://127.0.0.1:8510/health` 失败，但 public tunnel 访问命中本地日志，可以在沙箱外重跑 curl。不要因此立刻杀掉服务。

## 文档更新

交付前更新：

- `HANDOFF.md`：最新接力文档放在最前面
- `HANDOFF-YYYY-MM-DD-ORDINARY-USER-HTTP-PUBLIC-TEST.md`：记录当前链接、进程、验证结果
- `system/health-checks/ordinary-user-public-http-test-session-YYYYMMDD.md`：记录样本表
- `system/indexes/ordinary-user-public-test-runbook-YYYYMMDD.md`：如果流程变化，更新运行手册

## 输出格式

最终回复必须包含：

- 当前公开链接
- 本地备用链接
- 明确说明这是临时 Cloudflare quick tunnel，不是永久部署
- 已验证项：health、首页、真实问答
- 如有失败项，说明失败属于 Streamlit tunnel / browse 工具 / 预算配置中的哪一种
