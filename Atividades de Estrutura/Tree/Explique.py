def animal() :
5.    # start with a singleton
6.    root = Tree("bird")
7.  
8.    # loop until the user quits
9.    while 1 :
10.      print("Are you thinking of an animal? ")
11.      if not:
            break
12. 
13.      # walk the tree
14.      tree = root
15.      while tree.getLeft() != None :
16.        prompt = tree.getCargo() + "? "
17.        if yes(prompt):
18.          tree = tree.getRight()
19.        else:
20.          tree = tree.getLeft()
21. 
22.      # make a guess
23.      guess = tree.getCargo()
24.      prompt = "Is it a " + guess + "? "
25.      if yes(prompt) :
26.        print ("I rule!")
27.        continue
28. 
29.      # get new information
30.      prompt  = "What is the animal\'s name? "
31.      animal  = input(prompt)
32.      prompt  = "What question would distinguish a %s from a %s? "
33.      question = input(prompt % (animal,guess))
34. 
35.      # add new information to the tree
36.      tree.setCargo(question)
37.      prompt = "If the animal were %s the answer would be? "
38.      if yes(prompt % animal) :
39.        tree.setLeft(Tree(guess))
40.        tree.setRight(Tree(animal))
41.      else :
42.        tree.setLeft(Tree(animal))
43.        tree.setRight(Tree(guess))
 
