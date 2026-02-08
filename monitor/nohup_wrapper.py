"""
Sources:
    https://github.com/yuliu625/Yu-CLI-Wrapper/monitor/nohup_wrapper.py

References:
    - https://www.gnu.org/software/coreutils/manual/html_node/nohup-invocation.html
    - https://man7.org/linux/man-pages/man1/nohup.1.html

Synopsis:
    nohup命令的参数转义和运行封装。

Notes:
    nohup使用频率较高，但是其参数和符号可读性很差。我转义和封装了所有nohup的所有可选配置参数。

    更优选择:
        - subprocess.Popen: nohup的本质本身就已经是一个wrapper:
            nohup进行:
                - 信号处理: 拦截SIGHUP(Signal Hang Up)
                - 重定向: 输出脱离终端，指向目标文件。
            这使得:
                - 这2个系统调用不如python原生系统调用更加干净可控。
                - wrapper上的wrapper很奇怪。
        - screen / tmux: 仅shell条件下，linux其他命令。更易进行检查和控制。

    停止维护说明:
        在可以运行python的机器上，该方法完全被纯python系统控制取代。当前方法仅进行存档，不再维护。
"""

from __future__ import annotations

import subprocess

from typing import TYPE_CHECKING, Sequence
# if TYPE_CHECKING:


class NoHupWrapper:
    """
    nohup参数转义，运行封装工具。

    对照拆解:
        - > | >> : shell重定向指令。这是shell的功能。
        - 2>&1 : 文件描述符绑定。
        - & : 任务控制符。
    """
    @staticmethod
    def run(
        command_args: Sequence[str],
        log_file_path: str,
        is_log_append: bool,
        is_dry_run: bool,
    ) -> str | subprocess.Popen[bytes]:
        # 由于nohup的特殊符号，命令启动需要以str进行。
        command_str = "nohup " + " ".join(command_args)
        # 选择追加模式或覆盖模式。
        redirect_operator = '>>' if is_log_append else '>'
        # 命令拼接。
        command_str = f"{redirect_operator} {command_str}{log_file_path} 2>&1 &"
        if is_dry_run:
            print(command_str)
            return command_str
        else:
            # 非阻塞运行。
            return subprocess.Popen(
                command_str,
                shell=True,
            )


if __name__ == '__main__':
    # 运行示例。
    ## dry run test
    NoHupWrapper.run(
        command_args=['python', "program_path",],
        log_file_path="/path/to/log_file.log",
        is_log_append=True,
        is_dry_run=True,
    )
    ## run with nohup
    NoHupWrapper.run(
        command_args=['python', "program_path",],
        log_file_path="/path/to/log_file.log",
        is_log_append=True,
        is_dry_run=False,
    )

