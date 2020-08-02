# jupyter_on_heroku_using_docker
Link of Hosted Notebook : https://jup-doc.herokuapp.com/

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Directory Tree](#directory-tree)
  * [Bug / Feature Request](#bug---feature-request)
  * [Contribution](#contribution)
  * [Technologies Used](#technologies-used)
  * [Contributor](#contributor)
  * [Credit](#credit)


## Demo

![https://jup-doc.herokuapp.com/](https://i.imgur.com/E3a3wnH.png)


## Directory Tree 
```

├── conf
├── nbs
├── scripts
├── Docker_for_ai
├── Dockerfile
├── Pipfile
├── Pipfile.lock
├── README.md
├── summary.txt



```
conf is for configuraation of notebook. Here, it is password protected.<br>
nbs contains all notebooks that will be zipped and one another notebook that will load/unload all zipped notebooks. These zipped notebooks are your project notebooks.<br>
scripts contains all essential shell scripts such as build and run docker file. Entrypoint of dockerfile and push and release script for and after deploying on heroku.<br>
If you are working on AI project then use Docker_for_ai as Dockerfile so rename this file.<br>
If you are working on normal project then use Dockerfile. In both dockerfiles you are free to add custom requirement and dependencies.<br>
Pipfile and Pipfile.lock are created automatically when pipenv environment is created .<br>
summary.txt is summary of this whole project.

## Bug / Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/pandeynandancse/jupyter_on_heroku_using_docker/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/pandeynandancse/jupyter_on_heroku_using_docker/issues/new). Please include sample queries and their corresponding results.


## Contribution
If you'd like to do some contribution, feel free to do so by opening a pull request [here](https://github.com/pandeynandancse/jupyter_on_heroku_using_docker/pulls). Please include sample queries and their corresponding results.




## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)


[<img target="_blank" src="https://i.imgur.com/6Ux6U5K.jpg" width=170>](https://docker.com/) 
[<img target="_blank" src="https://i.imgur.com/b4hdrpz.png" width=170>](https://jupyter.org/) 
[<img target="_blank" src="https://i.imgur.com/aMqQ4nd.png" width=170>](https://heroku.com/) 



## Contributor
[![Nandan Pandey](https://qph.fs.quoracdn.net/main-thumb-189737418-200-jmwzsixdznlgemnejuecomukeluqkgzd.jpeg)](https://pandeynandancse.github.io) |
-|
[Nandan Pandey](https://pandeynandancse.github.io) |)


## Credit
This project is part of my learning process from https://www.codingforentrepreneurs.com/blog/jupyter-production-server-on-docker-heroku

 

