
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

![image](https://github.com/user-attachments/assets/356dff71-e873-4596-94cf-3144077ee989)

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









## Resources Used

| Source                                                                                                               | Location       | Notes                        |
| -------------------------------------------------------------------------------------------------------------------- | -------------- | ---------------------------- |
| [Git](https://git-scm.com/)                                                                                          | Acros website  | for version control          |
| [GitHub](https://github.com/)                                                                                        | Acros website  | to store the project files.  |
| [GitPod](https://www.gitpod.io/)                                                                                     | Acros website  | as the IDE for development.  |
| [Heroku](https://dashboard.heroku.com/apps)                                                                          | Acros website  | as the IDE for development.  |
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

