# launcher/minecraft.py
import subprocess
import os

def launch_minecraft(container):
    # Path to Minecraft jar (inside container/version/)
    version_jar = os.path.join(container["path"], "version", "minecraft.jar")
    if not os.path.exists(version_jar):
        print("Minecraft jar not found!")
        return

    # JVM args from profile
    jvm_args = container["profile"].get("jvm_args", "-Xmx2G")

    # Command
    cmd = [
        "java",
        *jvm_args.split(),
        "-jar",
        version_jar,
        "--gameDir",
        container["path"]
    ]

    print("Running command:", " ".join(cmd))
    subprocess.Popen(cmd)