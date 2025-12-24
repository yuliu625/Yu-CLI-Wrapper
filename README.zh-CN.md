# CLI Wrapper
**让复杂的 CLI 命令回归简单。** 这是一个基于 Python 封装的声明式命令行工具集，旨在替代晦涩难写的 Shell 脚本，提供更友好、更安全的交互体验。


## 核心理念
在日常开发中，我们经常面临以下困扰:
- **Shell 语法之痛**: 逻辑控制、字符串处理在 Shell 中极其繁琐，直接编写和维护脚本体验不佳。
- **交互不便**: 终端输入缺乏补全，长命令修改困难。
- **黑盒操作**: 直接运行脚本往往不确定会发生什么。

**CLI Wrapper 的解决方案：**
1. **声明式设计**: 通过简单的配置而非复杂的逻辑来定义工具行为。
2. **安全预检 (Dry Run)**: **默认开启预览模式。** 先检查生成的命令，确认无误后再执行。
3. **零依赖优先**: 核心功能尽可能仅依赖 Python 标准库(`subprocess`, `asyncio`)，保持轻量快速。


## 项目内容

| 模块 | 描述 | 包含内容 |
| --- | --- | --- |
| **`core`** | 统一的设计标准与工具类（非强制）。 | - |
| **`llm_launcher`** | 部署 LLM 推理后端。 | `vllm`, `litellm` |
| **`computing`** | 计算密集型任务处理。 | `multimedia` |
| **`devops`** | 环境部署、容器编排与自动化流程。 | `docker` |
| **`monitor`** | 资源状态监控和分析。 | `nohup`, `nvidia-smi` |
| **`network`** | 网络调试、代理控制与通信工具。 | `cloud`, `download` |
| **`storage`** | 数据与文件管理。 | `compression`, `database` |
| **`system`** | 操作系统管理和控制。 | `security`, `text_processing` |

*工具列表正根据日常使用需求持续更新中。*


## 如何使用
本项目设计的初衷是**开箱即用**。每个脚本通常可以独立运行:
1. **配置**：打开对应模块下的 Python 脚本，修改脚本顶部的配置项（如路径、端口、模型名称等）。
2. **预览 (Dry Run)**：直接运行脚本。程序会打印出即将执行的完整 Shell 命令，但**不会**真正触碰系统。
3. **执行**：确认命令无误后，将脚本中的 `dry_run=True` 改为 `dry_run=False`，再次运行即可真实执行。

```python
# 示例逻辑
dry_run = True  # 修改为 False 即可正式运行
```


## 相关项目
我维护的其他工具库，可能对你有用: 
- **[Python-Environment-Configs](https://github.com/yuliu625/Yu-Python-Environment-Configs)**: 针对 Python 工具链（Pip, Conda, UV 等）的环境配置仓库。
- **[Deployment-Toolkit](https://github.com/yuliu625/Yu-Deployment-Toolkit)**: 原始 OS 脚本（Shell/PowerShell）的工具包合集。
- **[CLI-Wrapper](https://github.com/yuliu625/Yu-CLI-Wrapper)**: 用 Python 封装的复杂 CLI 工具集，让操作更安全友好。

