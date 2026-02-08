# 🚀 CLI Wrapper
**Bringing simplicity back to complex CLI commands.** This is a declarative command-line toolkit built on Python wrappers. It is designed to replace obscure Shell scripts with a more user-friendly, secure, and interactive experience.


## 💡 Core Philosophy
Developers often face these common frustrations:
- **The Pain of Shell Syntax**: Logic control and string manipulation in Shell are cumbersome, making scripts difficult to write and maintain.
- **Poor Interactivity**: Terminal inputs often lack proper autocompletion, and modifying long, complex commands is tedious.
- **"Black Box" Operations**: Running a script directly can be risky when you aren't 100% sure what it will execute.

**CLI Wrapper's Solutions:**
1. **Declarative Design**: Define tool behavior through simple configurations rather than complex logic.
2. **Safety First (Dry Run)**: **Preview mode is enabled by default.** Inspect the generated command first; execute only after verification.
3. **Zero-Dependency Priority**: Core functions rely primarily on the Python Standard Library (`subprocess`, `asyncio`) to remain lightweight and fast.


## 📦 Project Structure (Contents)

| Module | Description | Included Tools |
| --- | --- | --- |
| **`core`** | Unified design standards and utility classes (optional). | - |
| **`llm_launcher`** | Deploy LLM inference backends. | `vllm`, `litellm` |
| **`computing`** | Processing for compute-intensive tasks. | `multimedia` |
| **`devops`** | Environment deployment, container orchestration, and automation. | `docker` |
| **`monitor`** | Resource status monitoring and analysis. | `nohup`, `nvidia-smi` |
| **`network`** | Network debugging, proxy control, and communication tools. | `cloud`, `download` |
| **`storage`** | Data and file management. | `compression`, `database` |
| **`system`** | OS management and control. | `security`, `text_processing` |

*The tool list is continuously updated based on daily requirements.*


## 🛠️ How to Use
This project is designed to be **out-of-the-box**. Each script is typically standalone:
1. **Configure**: Open the Python script in the relevant module and modify the configuration variables at the top (e.g., paths, ports, model names).
2. **Dry Run**: Run the script directly. The program will print the full Shell command it *intends* to run but **will not** actually execute it on your system.
3. **Execute**: Once you verify the command is correct, change `is_dry_run=True` to `is_dry_run=False` in the script and run it again to perform the real action.

```python
# Example Logic
is_dry_run = True  # Change to False for actual execution
```


## 🔗 Related Projects
Other toolkits I maintain that you might find useful:
- **[Python-Environment-Configurations](https://github.com/yuliu625/Yu-Python-Environment-Configurations)**: Environment configurations for Python toolchains (Pip, Conda, UV, etc.).
- **[Deployment-Toolkit](https://github.com/yuliu625/Yu-Deployment-Toolkit)**: A collection of raw OS scripts (Shell/PowerShell).
- **[CLI-Wrapper](https://github.com/yuliu625/Yu-CLI-Wrapper)**: A safer, more user-friendly Python wrapper for complex CLI tools.

