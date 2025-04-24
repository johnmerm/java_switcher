import os
import sys




# try:
#     import pydevd_pycharm
#     pydevd_pycharm.settrace('localhost', port=5678, stdoutToServer=True, stderrToServer=True)
# except ImportError:
#     pass

# Function to detect shell type
def detect_shell():
    parent_names = []
    try:
        import psutil
        pid = os.getpid()
        p = psutil.Process(pid)
        while True:
            parent_names.append(p.name())
            ppid = p.parent()
            if ppid is None:
                break
            else:
                p = ppid
    except ImportError:
        pass

    # Check for common environment variables
    if 'SHELL' in os.environ:
        shell_path = os.environ['SHELL'].lower()
        if 'bash' in shell_path or 'git' in shell_path:
            return 'bash'
    # Check for Windows CMD
    if sys.platform.lower().startswith('win'):
        if 'powershell.exe' in parent_names or 'pwsh.exe' in parent_names:
            return 'powershell'
        else:
            return 'cmd'
    return None



shell_type = detect_shell()

tgt=sys.argv[1]
JAVA_HOME=os.environ.get('JAVA_HOME')
PATH=os.environ.get('PATH')
if shell_type == 'bash':
    JAVA_HOME = JAVA_HOME.replace("\\","/").replace("C:", "/C")
    PATH= PATH.replace("\\","/").replace("C:", "/C").replace(";",":")



old_path = PATH
old_java_home = JAVA_HOME
prefix = '/C/Suite/jdks' if shell_type == 'bash' else 'C:\\Suite\\jdks'

sep = "/" if shell_type == 'bash' else "\\"

JAVA_HOME=f'{prefix}{sep}{tgt}'
if old_java_home in PATH:
    PATH=old_path.replace(old_java_home, JAVA_HOME)
else:
    exit(1)

if shell_type == 'cmd':
    print(f"set JAVA_HOME={JAVA_HOME}")
    print(f"set PATH={PATH}")
elif shell_type == 'powershell':
    print(f"$env:JAVA_HOME = '{JAVA_HOME}'")
    print(f"$env:PATH='{PATH}'")
elif shell_type == 'bash':
    # Convert Windows path to Unix format for Git Bash
    print(f"export JAVA_HOME='{JAVA_HOME}'")
    print(f"export PATH='{PATH}'")
