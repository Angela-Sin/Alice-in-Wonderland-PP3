
# Text-Based Adventure Game Alice in Wonderland

- Here You can find a link for an app. [Adventure Game](https://alice-in-wonderland-3e603879e053.herokuapp.com/)


![image](https://github.com/user-attachments/assets/a4aefeaf-a81a-4d2c-a58a-a1527950db21)



## Project Overview

The Alice in Wonderland text-based adventure game is an interactive fiction game where players navigate the world of Lewis Carroll's Alice's Adventures in Wonderland through text commands. The game presents descriptive scenarios, and players type commands like "go north," "take the key," or "talk to the rabbit" to explore the story. The gameplay relies on imagination and problem-solving, staying true to Wonderland's whimsical and surreal nature. Each decision influences the narrative, making it an immersive storytelling experience. [Wikipedia](https://en.wikipedia.org/wiki/Choose_Your_Own_Adventure)

The Alice in Wonderland text-based adventure game you're referring to is a Python-based project that runs in a mock terminal environment provided by Code Institute and is deployed using the Heroku platform. Python creates the game's logic, manages user input, and handles the narrative's flow in this setup. Players interact with the game via a command-line interface, where they input text commands to control the protagonist, typically Alice, as she explores Wonderland.

The game likely uses Python libraries for handling input/output and basic control flow (like if-else statements for decisions). It might include data structures (like dictionaries or lists) to manage the game's state, inventory, or rooms. It runs on Heroku, a cloud platform that allows developers to deploy, manage, and scale applications easily, ensuring the game is accessible online without needing a local Python setup.

# Rules

## Start


- The game begins with the player starting and entering their name.

## Welcome Section


- The player is welcomed and asked to make a decision (Yes/No). Based on the choice, different paths open up.

## Listening to the Rabbit or Calling for Help


- Early choices involve either listening to a rabbit or calling for help, leading to multiple pathways:
- Exploring the Tunnel or proceeding to the introduction section.
- Finding keys, drinking from bottles, or following a rabbit.

## Exploring Paths


- The player may encounter various locations such as a garden, a forest, or a tea party.
- The player can interact with characters (like the Cat or the Queen) or objects (like taking or leaving keys).

## Making Choices

- Decisions lead to different scenarios, such as challenging the Queen or exploring new doors (Green or Blue).
- Outcomes depend on the choice probabilities (e.g., 1/2 or 1/3), indicating multiple possible scenarios.

## Ending or Looping


- Players can find the way home, reach the end of the game, or loop back to make choices again.
- The game allows replayability by allowing the player to Play Again or end the game.
- It's a branching narrative structure where choices guide the adventure's outcome.

## User Goal


- I want the site to be easy and intuitive to use.
- I want to be able to decide to start the game, and not worry about captalisation or typing 'y' or 'n'.
- I want to be told if I have entered text incorrectly into the input areas.
- I want the game to be challenging.
- I want to be able to have the option of playing again after the story ends.
- I want it to be fun and interesting to play with a route that is not obvious on my first try.


# Flow Chart


The first example of a Flowchart I made during game creation.

![image](https://github.com/user-attachments/assets/fd277389-d1d3-4c1b-afb2-4abd5e4a8fa9)

## Here is an updated example of a flowchart.


![image](https://github.com/user-attachments/assets/7cca21e6-233a-4f7d-963b-25f7f6955c3b)


# Features


## First Screen


- On the first page, you can find an ASCII art title screen, likely for a text-based or console game version of Alice's Adventures in Wonderland.
- In the top right corner, the title "Alice's Adventure in Wonderland!", gives a brief explanation of what players should expect from a game, and also is highlighted with stars.
- The prompt "Please enter your name >>>" at the bottom indicates this is the starting point of the game, where the player can input their name to begin.
- The ASCII art and interactive prompt suggest a retro, nostalgic design, fitting for classic text-based or adventure games.
- 
![image](https://github.com/user-attachments/assets/c34a4f70-36d4-4066-9029-0458a63e12b6)


- After a valid name the second step greets the player by 'Name' and invites him into the "Magical World of Wonderland."
- The description encourages players to join Alice on a whimsical adventure filled with talking animals, mischievous characters like the Cheshire Cat, and the notorious Queen who shouts, "Off with their heads!" It emphasizes that players' choices will shape the journey, uncovering secrets and facing challenges along the way. It asks if they're ready to follow the White Rabbit and dive into the mysterious, unpredictable world of Wonderland, where "nothing is quite what it seems."
-The invitation to "find out what's behind the mirror" sets a mysterious, exploratory tone, aligning with the theme of curiosity and discovery central to Alice in Wonderland. This text likely serves as a setup for the player's adventure, building excitement for the imaginative experience ahead.

![image](https://github.com/user-attachments/assets/061412a7-8814-41fa-be22-95c8be1f794d)


- Here is a starting screen for a text-based adventure game, inviting the player to begin the story by entering either 'Y' (Yes) to play or 'N' (No) to decline.
- The use of ASCII art adds a visual element, making the start of the game engaging.

![image](https://github.com/user-attachments/assets/089d2485-6db9-44bc-ba0a-aff9bc491ed7)


- If you input anything other than 'Y' or 'N', the invalid_choice() function is triggered, which notifies them of the error and prompts them to choose again

![image](https://github.com/user-attachments/assets/36826102-601a-4745-8aa2-31dc691497ca)


- If your decision is negative you will find nice greetings.
  
![image](https://github.com/user-attachments/assets/79ef7cfb-f7e8-48f2-9f9d-f584a6e862dd)


- If your decision is positive You'll move into the beginning of the game.
- Here you find some story and multiple-choice input.

![image](https://github.com/user-attachments/assets/88e24c44-5471-4c4d-a2b0-f9803ae071c6)


- If you input anything other than '1' or '2', the invalid_choice() function is triggered, which notifies them of the error and prompts them to choose again

![image](https://github.com/user-attachments/assets/4072d39c-ff20-4642-996c-f59164b59162)


- When the story will end, you will get a choice to play the game again or not.
- If you choose to play again, you will start the game from the beginning of the game with an intro play_again() story and multiple choice.

![image](https://github.com/user-attachments/assets/a485dd93-3fb0-4e34-9216-4e01f4c4e9df)


- If you chose 'No' You will be greeted with warm greetings for goodbye.

![image](https://github.com/user-attachments/assets/8446f64b-a983-4c8a-bd0e-e32427b8c405)



# Future Features


- Use an API link to Google Sheets to rework and extend the storyline.
- Make the game so multiple people are capable of playing and track their scores, compared to other players.
- Make a game with multiple choices of the stories written by Lewis Carroll.
- Implement a scoreboard.
- Add separate challenges to make the game more challenging and live.


# Deployment


### Making a Local Clone


1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste [https://github.com/YOUR-USERNAME/YOUR-REPOSITORY] in.
7. Press Enter. Your local clone will be created.
8. $ git clone [https://github.com/YOUR-USERNAME/YOUR-REPOSITORY]
9. Cloning into `CI-Clone`...
10. remote: Counting objects: 10, done.
11. remote: Compressing objects: 100% (8/8), done.
12. remove: Total 10 (delta 1), reused 10 (delta 1)
13. Unpacking objects: 100% (10/10), done.

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.


### Forking the GitHub Repository


By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not the top of the page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

-- Forking allows you to make any changes without affecting the original project. You can send the suggestions by submitting a pull request. Then the Project Owner can review the pull request before accepting the suggestions and merging them.

-- When you have a fork to a repository, you don't have access to files locally on your device, to get access you will need to clone the forked repository.

For more details on how to fork the repo, to for example suggest any changes to the project you can:[Link](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo)


### Heroku App Deployment


The app is deployed from Heroku using the following steps:
1. Use pip freeze > requirements.txt to add external libraries to the deployed app.
2. Create a Heroku account.
3. In the top right, click 'New'.
4. Click 'Create new app'.
5. Give your app a name and select your region from drop-down.
6. Click 'Create new app'.
7. Go to the 'settings' tab, you must do it before deployment.
8. Scroll down to the 'config vars' section, and the key is PORT, and the value is 8000.
9. Scroll down to the 'Buildpacks' section.
10. Click 'Add buildpack'.
11. Add Python as the first dependency and select 'Save changes'.
12. Add node.js as a second dependency and save again (This is the settings section done).
13. Select the 'Deploy' tab at the top.
14. Select 'Github' from 'Deployment method'.
15. Type the name given to your project in GitHub and click 'search'.
16. Scroll down and select the Manual deployment method.
17. You can also use The auto-deployment method to allow the project to update every time you push the code.
18. You can now click to view the app is ready and running.

-- The web application is displayed and deployed using the template provided by Code Institute to test the code.

-- For this project I used the Manual deployment method to deploy the current state of the branch, every time I pushed the code from Gitpod.

## Validation

Run the code several times through the Code Institute Validator. No Error.

![image](https://github.com/user-attachments/assets/42df0fe7-ebc1-43c4-80e7-36e7e3bc7668)



## Bug
- ASCII art causes a bug in one of the loops. def rest_in_garden, got '/app/run.py:335: SyntaxWarning: invalid escape sequence '\)'' as in ASCII was to many '\'.


## Resources Used


| Source                                                                                                               | Location       | Notes                        |
| -------------------------------------------------------------------------------------------------------------------- | -------------- | ---------------------------- |
| [Git](https://git-scm.com/)                                                                                          | Acros website  | for version control          |
| [GitHub](https://github.com/)                                                                                        | Acros website  | to store the project files.  |
| [GitPod](https://www.gitpod.io/)                                                                                     | Acros website  | as the IDE for development.  |
| [Heroku](https://dashboard.heroku.com/apps)                                                                          | Acros website  | as the IDE for development.  |
| [draw.io](https://app.diagrams.net/)                                                                                 | Flow-Chart     | Flow-Chart                   |
| [Readme](https://github.com/Angela-Sin/Retro-Game)                                                                   | Acros website  | As an example, created originally by me for hackathon |
| [YouTube](https://www.youtube.com/)                                                                                  | Acros website  | Tutorial for troubleshooting |
| [W3Schools](https://www.w3schools.com/)                                                                              | Across website | Various help pages           |
| [CSS Validator](https://jigsaw.w3.org/css-validator/)                                                                | Across website | CSS Validator                |
| [JavaScript Validator](https://jshint.com/)                                                                          | Across website | JavaScript Validator         |
| [Python Validator](https://pep8ci.herokuapp.com/)                                                                    | Across website | Python Validator             |
| [makeusof.com](https://www.makeuseof.com/python-text-adventure-game-create/)                                         | Across website | How to buid game             |
| [Chat GBT](https://chatgpt.com/)                                                                                     | Across website | For Text Generation          |
| [Asciiart](https://asciiart.website/)                                                                                | Across website | As ASCII library             |
| [ASCII](https://www.asciiart.eu/)                                                                                    | Across website | To create pictures for a game|






# Credits

- Special mention is also deserved by my mentor Medale Oluwafemi for helping me understand the requirements and guiding me through the realization of this project!
- As a tutoring team for help and support during the project.
- Code Institute's 'Love Sandwiches' project.
- Code Institute mock terminal template to run the app.
- Stack Overflow.

