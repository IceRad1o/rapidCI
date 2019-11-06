# -*- coding:utf-8 -*-
import tornado.web
import subprocess
from multiprocessing import process

class RegisterGit(tornado.web.RequestHandler):
    def post(self):
        repo_url = self.get_argument("repo_url")
        repolist = repo_url.split('/')
        repo_name = repolist[-2]+"_"+repolist[-1].split(".")[-2]
        # Q1 if repo_already in folder ?
        try:
            subprocess.check_output(["./create_obs_runner.sh", repo_url, repo_name])
        except subprocess.CalledProcessError as e:
            raise Exception("Could not build obs and runner repo. Reason: %s" % e.output)
        # no db yet, write into file
        f = open("repo.txt", "w+")
        localrepo = "../Git_repo/"
        f.write(localrepo+repo_name) # no obs here
        self.write("%s" % repo_name)


# end
