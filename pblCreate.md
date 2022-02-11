# Create Task Trial Run - Tri 2 PBL related 
## The Task Description 
The Create Task is a College board assessment of capability. We are simulating the creation of a college board-compliant create task that relates to the overall theme of our website. As such, these assignments may not be what we finally produce as a create task product, but rather a attempt to practice for the eventual creation of the create task itself. 

## PBL Create Task Ideas and outline

### Krish's Create Task
**Name**: Linux capability test
**Description of Program**: This program is a series of questions that will attempt to discern how well a user is versed in Linux. Through several questions from a randomized bank, each of these questions will have an intrinsic value that will eventually be compared to a set of pre-determined point thresholds that, based on the users score in the quiz, indicate what level of Linux understanding they have. 
**Technical Goals/Ideas**: 
* Questions and answers will be stored key-value format, respectively, in a dictionary 
* Randomizers will select several questions from the bank which will be displayed to the user 
* User will have an input area to put in answers that will be auto formatted to prevent syntax errors
* Answers will be stored in a list to be used later to compare 
* users answers will be compared to the specific key's values in question bank dictionary. 
* At end of game, users scores will be totaled and then compared to another dictionary which will determine their comprehension level of Linux based on pre-determined requisites 
* This will then be displayed out to the user

**Future Implementation**
* Connect quiz to database, eventually when user information can be stored, so that understanding level can also be noted 
* Use this understanding rating to recommend people certain lessons or unlock others when those lessons are created 
* Use in existing forum to mark certify people's responses so that other users may know how credible people's advice is

Note: Using key and dictionary systems instead of simply setting if statements would allow for further editing of this system later on if further levels of understanding need to be added or if further questions need to be added to the bank. 

### Sophie + Val's Create Task
Name: War
Description of Program: Uses standard 52-card deck and randomly shuffles it for both the computer and the player.  The player can see their top 3 cards and can choose which card to put down.  The computer will put down whatever card is at the top of its stack.  The player with the higher card value (Ace is high, 2 is low) will gain both cards and put it at the bottom of their stack.  If one card is joker, the joker player automatically wins that round.  If the values are equal, then the next 3 cards are put down as well.  The player with the cards with the higher combined value takes all of the cards and puts them at the bottom of the stack.  If the 4 cards are equal, then the game ends and whoever has the most cards at that time wins the game.  If the combined cards are of equal value then the game ends as a tie.  Otherwise the game continues until one player has taken all of the cards.

Technical Goals/Ideas:
* Cards are stored in dictionary with string name of card and numerical value. ie. `"Ace of Spades": 14`
* If statements to check which card is greater
* Loop to repeat game until endgame
* User input for card selection
* Cards are sorted in order, fundamental part of the game
