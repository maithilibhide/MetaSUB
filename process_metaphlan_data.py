import os

directory = "metasub_input/"
f = open("PROCESSED_files.txt", "a")
for ip_fname in os.listdir(directory):
    print(ip_fname)
    op_fname = "metasub_output/" + ip_fname.split(".fastq.gz")[0] + ".txt"
    command = "metaphlan2.py metasub_input/" + ip_fname + " --input_type fastq --nproc 5 > " + op_fname
    os.system(command)
    f.write(ip_fname+"\n")
f.close()

