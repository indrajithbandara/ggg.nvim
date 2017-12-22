import neovim
import time
import os
'''examples'''
@neovim.plugin
class ggg(object):
  def __init__(self, nvim):
    self.nvim = nvim
    self.nvim.command("echo '非同期でgggプラグインが有効になりました'")

  @neovim.command("Gecho")
  def gecho(self):
    self.nvim.command("echo '[Echo Test]'")
  
  @neovim.command("Pwd")
  def pwd(self):
    pwd = os.popen('pwd').read()
    self.nvim.command("echo '[PWD@GGG]={}'".format(pwd))
  
  @neovim.command("Git")
  def git(self):
    add = os.popen('git add *').read()
    commit = os.popen('git commit -m "add"').read()
    self.nvim.command("echo '[Load Git Repo function@GGG]\n{add}\n{commit}'".format(add=add, commit=commit))
    #self.nvim.command("echo '{}'".format(commit))
    #push = os.popen('git push').read()
    #self.nvim.command("echo '{}'".format(push))

  '''存在しないoptを適用する'''
  @neovim.command("Dot")
  def dot(self):
    git_opts = 'G=`git config --global credential.helper "cache --timeout=10000"`'
    go_opts = 'PATH=$HOME/go/bin:$PATH'
    gcloud_opts = 'PATH=$HOME/google-cloud-sdk/bin:$PATH'

    HOME = os.environ['HOME']
    lines = [ line.strip() for line in open(HOME + '/.bashrc').read().split('\n') ]

    opts = [ git_opts, go_opts, gcloud_opts ]
    opts = filter(opt not in lines, opts)

    f = open(HOME + '/.bashrc')
    for opt in opts:
      f.write( opt + '\n' )
      
