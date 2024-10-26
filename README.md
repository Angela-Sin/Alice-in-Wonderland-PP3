
# Text-Based Adventure Game Alice in Wonderland


## Project Overview

The Alice in Wonderland text-based adventure game is an interactive fiction game where players navigate the world of Lewis Carroll's Alice's Adventures in Wonderland through text commands. The game presents descriptive scenarios, and players type commands like "go north," "take the key," or "talk to the rabbit" to explore the story. The gameplay relies on imagination and problem-solving, staying true to Wonderland's whimsical and surreal nature. Each decision influences the narrative, making it an immersive storytelling experience. [Wikipedia](https://en.wikipedia.org/wiki/Choose_Your_Own_Adventure)

The Alice in Wonderland text-based adventure game you're referring to is a Python-based project that runs in a mock terminal environment provided by Code Institute and is deployed using the Heroku platform. In this setup, Python creates the game's logic, manages user input, and handles the narrative's flow. Players interact with the game via a command-line interface, where they input text commands to control the protagonist, typically Alice, as she explores Wonderland.

The game likely uses Python libraries for handling input/output and basic control flow (like if-else statements for decisions). It might include data structures (like dictionaries or lists) to manage the game's state, inventory, or rooms. It runs on Heroku, a cloud platform that allows developers to deploy, manage, and scale applications easily, ensuring the game is accessible online without needing a local Python setup.

## Rules

- The game begins by asking the player to input their name.
- Later players have a long, descriptive welcome message.
- The player is asked whether they want to start the game: Y/N
  - If the player enters "N" or "n", they get a friendly message saying they can come back later >>
  -  If they choose "Y" or "y", the function is called to start the game >>
- If the player inputs anything other than 'Y' or 'N', the invalid_choice() function is triggered, which notifies them of the error and prompts them to choose again:
- The player has initial choices in the adventure presented. The player can choose between the options provided in the game.
- If the player inputs anything other than '1' or '2', the invalid_choice() function is triggered, which notifies them of the error and prompts them to choose again:
- After the narrative ends, the player is given the option to restart the game: Y/N
  - If they say "N" or "n", they receive a friendly message encouraging them to come back later >>
  - If they say "Y" or "y", the game loops back by calling play_game() to restart the adventure >>
- If the player inputs anything other than 'Y' or 'N', the invalid_choice() function is triggered, which notifies them of the error and prompts them to choose again:

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


![image](https://github.com/user-attachments/assets/3950f0a4-d493-49af-802a-9f5dfeb579ae)


### The flowchart represents a decision-based adventure game inspired by "Alice in Wonderland." Here's a brief explanation:

## Start


-The game begins with the player starting and entering their name.

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
- The game allows replayability by giving the player the choice to Play Again or end the game.
- Overall, it's a branching narrative structure where choices guide the outcome of the adventure.

# Features


## First Screen


![Image](https://github.com/user-attachments/assets/5e6c366d-5ba6-450f-a795-fb73b0e624f4)

- After a valid name entry you are greeted and introduced to the outline of the game.

![image](https://github.com/user-attachments/assets/5ca9ffc2-0651-42b2-aafc-37f403334320)

- Then you find yourself deciding to play the game or not.

![image](https://github.com/user-attachments/assets/7b15155c-625b-4c34-a6b0-66e56fd3c8be)

- If you input anything other than 'Y' or 'N', the invalid_choice() function is triggered, which notifies them of the error and prompts them to choose again

![image](https://github.com/user-attachments/assets/da2b85cb-4e77-4109-9de1-305647dfb3b0)

- If your decision is negative you will find nice greetings.
  
![image](https://github.com/user-attachments/assets/a3fb65bb-c7d2-4cb2-9b67-d7a293da588d)

- If your decision is positive You'll move into the beginning of the game.
- Here you find some story and multiple-choice input.

![image](https://github.com/user-attachments/assets/506e1b36-f420-43b4-8194-efcc00a35b2c)

- If you input anything other than '1' or '2', the invalid_choice() function is triggered, which notifies them of the error and prompts them to choose again

![image](https://github.com/user-attachments/assets/46349073-eba0-47ac-bd22-1b841038d026)

- When the story will end, you will get a choice to play the game again or not.
- If you choose to play again, you will start the game from the beginning of the game with an intro story and multiple choice.

![image](https://github.com/user-attachments/assets/75d0fe1a-d8d3-4130-b643-8583ccfe5ca1)

- If you chose 'No' You will be greeted with warm greetings for goodbye.

![image](https://github.com/user-attachments/assets/a30029fa-6caa-4121-acc6-fed1ad1104a1)


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
8. Scroll down to the 'config vars' section and key: PORT and value: 8000.
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
| [Chat GBT](https://chatgpt.com/)                                                                                     | Across website | For Text Generation          |
| [Asciiart](https://asciiart.website/)                                                                                | Across website | As ASCII library             |
| [ASCII](https://www.asciiart.eu/)                                                                                    | Across website | To create pictures for a game|






# Credits

- Special mention is also deserved by my mentor Medale Oluwafemi for helping me understand the requirements and guiding me through the realization of this project!
- As a tutoring team for help and support during the project.
- Code Institute's 'Love Sandwiches' project.
- Code Institute mock terminal template to run the app.
- Stack Overflow.

