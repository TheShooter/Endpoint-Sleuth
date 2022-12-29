import subprocess

def decompile_jar(jar_file, output_dir):
    
    cmd = ['java', '-jar', 'fernflower.jar', '-dgs=1', jar_file, output_dir]
    subprocess.run(cmd)