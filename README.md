
# Text-Based Adventure Game Alice in Wonderland


## Project Overview

The Alice in Wonderland text-based adventure game is an interactive fiction game where players navigate the world of Lewis Carroll's Alice's Adventures in Wonderland through text commands. The game presents descriptive scenarios, and players type commands like "go north," "take the key," or "talk to the rabbit" to explore the story. The gameplay relies on imagination and problem-solving, staying true to Wonderland's whimsical and surreal nature. Each decision influences the narrative, making it an immersive storytelling experience.

The Alice in Wonderland text-based adventure game you're referring to is a Python-based project that runs in a mock terminal environment provided by Code Institute and is deployed using the Heroku platform. In this setup, Python is used to create the game's logic, manage user input, and handle the narrative's flow. Players interact with the game via a command-line interface, where they input text commands to control the protagonist, typically Alice, as she explores Wonderland.

The game likely uses Python libraries for handling input/output and basic control flow (like if-else statements for decisions) and might include data structures (like dictionaries or lists) to manage the game's state, inventory, or rooms. It runs on Heroku, a cloud platform that allows developers to deploy, manage, and scale applications easily, ensuring that the game is accessible online without needing a local Python setup.

## Rules

- The game begins by asking the player to input their name.
- Later players have a long, descriptive welcome message.
- The player is asked whether they want to start the game: Y/N
  - If the player enters "N" or "n", they get a friendly message saying they can come back later >>
  -  If they choose "Y" or "y", the function is called to start the game >>
- The player has initial choices in the adventure presented. The player can choose between the options provided in the game.
- If the player inputs anything other than 1 or 2, the invalid_choice() function is triggered, which notifies them of the error and prompts them to choose again:
- After the narrative ends, the player is given the option to restart the game: Y/N
  - If they say "N" or "n", they receive a friendly message encouraging them to come back later >>
  - If they say "Y" or "y", the game loops back by calling play_game() to restart the adventure >>




# Flow Chart


![image](https://github.com/user-attachments/assets/93782981-defd-45bd-a015-617edc8acdbb)

## Resources Used

| Source                                                                                                               | Location       | Notes                        |
| -------------------------------------------------------------------------------------------------------------------- | -------------- | ---------------------------- |
| [Git](https://git-scm.com/)                                                                                          | Acros website  | for version control |
| [GitHub](https://github.com/)                                                                                        | Acros website  | to store the project files.  |
| [GitPod](https://www.gitpod.io/)                                                                                     | Acros website  | as the IDE for development.  |
| [Readme](https://github.com/Angela-Sin/Retro-Game)                                                                   | Acros website  | As an example, created originally by me for hackathon |
| [YouTube](https://www.youtube.com/)                                                                                  | Acros website  | Tutorial for troubleshooting |
| [W3Schools](https://www.w3schools.com/)                                                                              | Across website | Various help pages           |
| [CSS Validator](https://jigsaw.w3.org/css-validator/)                                                                | Across website | CSS Validator           |
| [JavaScript Validator](https://jshint.com/)                                                                          | Across website | JavaScript Validator           |
| [Python Validator](https://pep8ci.herokuapp.com/)                                                                    | Across website | Python Validator          |
| [Chat GBT](https://chatgpt.com/)                                                                                     | Across website | For Text Generation             |
| [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview)                                                  | Across website | Speed testing for Mobile and Desctope           |
| [amiresponsive](https://ui.dev/amiresponsive)                                                                        | Across website | was used to take the screenshot with different devices presented at the top of this document.        |






# Credits

- Special mention is also deserved by my mentor Medale Oluwafemi for helping me understand the requirements and guiding me through the realization of this project!
- As a tutoring team for help and support during the project.
- Code Institute's 'Love Sandwiches' project.
- Code Institute mock terminal template to run the app.
- Stack Overflow.

