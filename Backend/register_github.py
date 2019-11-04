# -*- coding:utf-8 -*-
import tornado.web
import subprocess


class RegisterGit(tornado.web.RequestHandler):
    def post(self):
        repo_url = self.get_argument("repo_url")
        # subprocess.check_output(["./create_obs_runner.sh", repo_url])
        self.write("%s" % repo_url)

# end
