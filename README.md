# movies

This is another simple python application that is using the semantic similarity module to compare the descriptions of a few movies to a movie called Planet Hulk.
It will read from the movies.txt file and compare each movies descriptions with the one passed in the functions parameter. If the similarity rate is higher or equal to 0.5, it will return a recommendation list of movies from the movies.txt file.

# How to run the code

Download the files from the repo, and make sure they are both in the same directory.
Next you need to open the command line in the same directory as the files, once you have done this.
Type in the command `docker build -t movies-app`. It should take a few seconds to install everything.
Once that is done, type in the command `docker run -i movies-app`. If all goes well, the code should be running,
You can also open the folder in an editor like VSC and run it in there as well.
