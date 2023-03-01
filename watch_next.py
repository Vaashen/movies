import spacy

# creating a function that will read from a movies.txt file and returna recommendation of movies
# it takes in a movie description as the parameter
def watch_next(movie):
    
    #loading the module that will check t=for the similarities in the descriptions
    nlp = spacy.load('en_core_web_md')
    
    # passing the parameter into the module
    model_sentence = nlp(movie)
    
    # openning the txt file
    # creating a variable that will store the descriptions of each movie
    with open('movies.txt', 'r') as f:
        for line in f.readlines():
            description = line[9:]
            
            # checking the similarity of the parameter to the descriptions of the movies from the txt file
            similarity = nlp(description).similarity(model_sentence)
            
            # printing a statement 
            print("We recommend the following movies:\n")
            
            # if the similarity between the descriptions are above 0.5 
            # print out the title of the movie
            if similarity >= 0.5:
                print(line[:8])
            

# calling the function and passing the Planet Hulk description as an arguement 
watch_next('''Will he save thier world or destroy it? When the hulk becomes too dangerous
           for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet
           where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into 
           slavery and trained as a gladiator.''')