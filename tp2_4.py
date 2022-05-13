import os
import re
import sys
import subprocess

clone_doc = sys.argv[1]
source_filename = sys.argv[2]

with open(source_filename, "r") as file:
    repo_list = [repo.strip() for repo in file.readlines()]

regex = r"/([^/]+)\.git$"

for repo in repo_list:
    doc_name = re.findall(regex, repo)[0]
    os.system(f'git clone {repo} "{clone_doc}/{doc_name}"')

dir_result = subprocess.run(
    ["dir", clone_doc, "/A:D", "/B"],
    shell=True,     #pour l'utilisation sur Windows en programme de ligne de commande
    capture_output=True,
    text=True
)
if len(dir_result.stdout.strip().split("\n")) == len(repo_list):
  print(f"[+] Succès : le(s) {len(repo_list)} reposite(s) ont bien été clonés dans le dossier {clone_doc}.")
else:
  print(f"[-] Erreur : une erreur est survenue...Dommage. Hein?") 