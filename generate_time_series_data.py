import os
import subprocess




#Launch the shell command:


"""
algorithm

tags = get all tags
for tag in tags:
     branch checkout branch
     for each tool in tools:
          metrics =  run tool on branch
          formatted_metrics = format metrics
          write metric to data_file
"""          

import logging
import sys

logging.basicConfig(level=logging.INFO,filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')



def get_version_tags(git_dir):
     try:
        command=f'git --git-dir={git_dir}  for-each-ref --format="%(refname:short) | %(creatordate)" "refs/tags/*"'
        process  = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
        tags = process.communicate()
        return list(tags)
     except Exception as e:
          print
          logging.error(f"Exception occurred:{e}")

     return []

def check_out_tag_version(tag_name,command):
     try:
        process  = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
        result = process.communicate()
        return result
     except Exception as e:
          print(f"Exception occurred:{e}")


     


def delete_branch(branch_name):
     print(f"deleting branch {branch_name}")
     return 


def do_static_analysis(git_dir, command):
     logging.info(f"analysing {git_dir}")
     logging.info(f"running command: {command}")
     process  = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)
     result = process.communicate()
     process.wait()
     return result



if __name__ == "__main__":
    analytic_flags = ["raw" , "hal", "mi", "cc"] 
    git_dir = "../metrics_final_project_data/input/pytorch/.git"
    source_dir = "../metrics_final_project_data/input/pytorch/"
    tags = get_version_tags(git_dir)
    tags = str(tags[0]).split("|")
    cnt = 0
    for t in tags[1:]:
         t = t.replace("\\n", ",")
         tag_name = (t.split(","))[1].strip()
         tag_date = (t.split(","))[0].strip()
         tag_date = tag_date.replace(" ", "_")
         output_file_name =  f"{tag_name}_{tag_date}.txt"
         logging.info(f"processing {output_file_name}.....")
         checkout_tag_command = f'git  --git-dir={git_dir} checkout -f  tags/{tag_name} -B {tag_name}-branch'
         result = check_out_tag_version(tag_name,checkout_tag_command)
         logging.info(f"result of checking out branch: {result}")
         for flag in analytic_flags:
              print(f"performing  {flag} analysis and storing results to output/{flag}_{output_file_name}")
              logging.info(f"performing  {flag} analysis and storing results to output/{flag}_{output_file_name}")
              cyclomatic_complexity_radon_command = f"radon {flag}  {source_dir} -O output/{flag}_{output_file_name}"
              result = do_static_analysis(git_dir,cyclomatic_complexity_radon_command)

          
          
