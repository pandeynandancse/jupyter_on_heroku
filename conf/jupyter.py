import os
#this file changes configuration of jupyter notebook server
c = get_config()




c.IPKernelApp.pylab = 'inline'  # if you want plotting support always in your notebook
# Notebook config that means -->> in nbs directory our notebook project will be placed
c.NotebookApp.notebook_dir = 'nbs'
c.NotebookApp.allow_origin = u'https://jup-doc.herokuapp.com/' # put your public IP Address here
c.NotebookApp.ip = '*'
c.NotebookApp.allow_remote_access = True
c.NotebookApp.open_browser = False
#type -->>> ipython -c "from notebook.auth import passwd; passwd()" and set password 
c.NotebookApp.password = u'argon2:$argon2id$v=19$m=10240,t=10,p=8$PALZgMSug7d3NG9wBWjqQA$4oESCjFahOXZT98zneaptQ'
# http://localhost:8888/?token=28b42e38aec85ae55c5c9ded8a896358a366dde9f64cc403
#Now no token authentication
#http://localhost:8888/

c.NotebookApp.port = int(os.environ.get("PORT", 8888))
c.NotebookApp.allow_root = True
c.NotebookApp.allow_password_change = True
c.ConfigurableHTTPProxy.command = ['configurable-http-proxy', '--redirect-port', '80']




#if we now  open jupyter notebook then there will be no any files/folders because after lecture-2 of codingforenterpreneurs there was not anything inside 'nbs' folder.

   
