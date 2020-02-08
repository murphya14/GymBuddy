<h1 align="center">Gym Buddy</h1>

<div align="center">
https://github.com/murphya14/GymBuddy
</div>

<h1 align="center">
<img src="assets/css/images/simon-game.jpg">
</h1>

<div align="center">
This is an Interactive Frontend and Backend website to facilate a training plan for the user, a record of the weights the
user is lifting and a companion in the gym; __Gym Buddy__.<br>
The purpose of this website is to provide a challenging training plan that allows for an easy and intuitive layout while providing clear examples of how to execute the excercises.
The aim is to make the gym more accessible and have a plan to follow from your phone __Your health is your wealth!__


This is a program that appeals to __all ages__ and __all genders__. There is the
option of a recording the weights of your __main weights__ by using the __Weights button__ which allows the user to improve on previous weight and see progress.<br>
This provides a challenge for all levels. 
The aim of this website is to provide a detailed training plan that visually instructive and easy to engage with. 

[**View Gym Buddy website here!**](HEROKU LINK )
</div>



## UX Design

__Purpose:__<br>
The purpose of this website is to provide a challenging and clear training program for all users.
Clear instructions are provided to make the users aware of the how program is structered.

__The target customer has the following qualities:__
* Looking for a challenge
* Wants a program that is instructive and well planned 
* Suitable for ages 12+

__The goal for visitors to the site, created the following brainstorm for the
User story:__

- #### As a user, I would like to see:
   - a striking design that is visually stimulating and provides a clear path to follow.
   - I want to be able to access information so I can understand more about the training structure.
   - I want to be able to control the parts of the workout that I have completed so I can experience the interactive nature of Gym Buddy.
    - I want to be able to record the progress of the main weight lifts in order to improve.
    - I want to be able to record my own weight in order to track progress.
     - I want to be able to get instant examples on each excercise.

Wireframe Mock-ups using [Balsamiq](https://balsamiq.com/)
* [Main Desktop Display](assets/css/images/main-wireframe-desktop.pdf)
* [Information modal Desktop Display](/assets/css/images/modal-wireframe-desktop.pdf)
* [Main Tablet Display](/assets/css/images/main-wireframe-tablet.pdf)
* [Information modal Tablet Display](/assets/css/images/modal-wireframe-desktop.pdf)
* [Main Mobile Display](/assets/css/images/main-wireframe-mobile.pdf)
* [Information modal Mobile Display](/assets/css/images/modal-wireframe-mobile.pdf)


## Design
The design is simple core colours and a very basic layout. This was created to compliment the ease of use of the application and with consideration that the website would likely be used on a mobile and in a gym. 
Gym Buddy allows for quick and effective access to the training plan with minimum effort. 

### Fonts
The font Ubuntu was used as the primary font so as to give a friendly/simplistic feel that co-ordinates with the design.

### Colour
* The main header is black with contrasting white text. Once the text is hovered over it is highlighted in neon pink.
* The footer is also neon pink which is the base colour for Gym Buddy. 
* The main button colour is blue.
* Weights button - This is yellow to indicate that it is only to record the weight of the main lifts.
* Completed button - A green button indcating the completion of a section of the workout. 

### Styling
The styling is very basic and simple in order to convey the simplicity of the workout. More information/examples are accessible through modals and accordians whcih allows the user to choose how "clean" they wish the screen to be.


## Features
### Existing Features
#### Feature 1
_Dashboard:_
* This is a __interactive__ dashboard which welcomes the user with striking imagery that allows for an intuitive feel for the game.



#### Feature 2
_Game Information modal:_
* Clear access to the information about "How to play" is shown with a modal button.
* This is a fixed modal in bright pink to catch the users attention.


#### Feature 3
_Coloured Pads:_
* The four pads are faded and only light up once the power button has been clicked.
* The pads are primarily where the user interacts with the game.
* You can only click the pads when it is the players turn.


#### Feature 4
_Power and Start button:_
* The power button must be clicked before the start button and this has been carefully programmed to follow this sequence.
* Once the power button has been clicked the pads light up and the score board reflects that the power is on.
* Once the start button is pressed the game reacts by fading the pad lights and the score board reflects the beginning of the game
by showing zero.

#### Feature 5
_Strict Slider:_
* This is slider button is off by default and when slide on, it reflects this through a colour change.

#### Feature 7
_Scoreboard:_
* Once the page is loaded the score board will be empty.
* With the power button clicked it will show "--"
* Once start is clicked the scoreboard begins at "0"

#### Feature 8
_Header & Footer:_
* Footer copyrighting the design.
* Navigation bar boldy showing the name of the game and an intriging comment that hints at the games nature.

### Features to implement in the Future
* A range of levels including rotation of the pads to tailor for more abilities.
* Prompting modals that appear subtly as you hover over buttons to inform the player as they go.
* An optional trial game to allow new players to test it out before commiting to a game.
* A follow up message that challenges the player to another game.
* A functional calender keeping track of the players score over the course of time. This prompts the player to competively beat their previous scores.


## Technologies Used
* __HTML, CSS, JavaScript & Python:__
This project was created using HTML, CSS, Python and javaScript.

* __Gitpod:__
This project was written on Cloud9 and gitpod.
<br>https://www.gitpod.io/

* __JQuery:__
Used to work more efficiently with the DOM.
<br>(https://jquery.com)

* __W3C online validators:__
Online validators were used to check code was valid for both HTML and CSS.
<br>HTML validator: https://validator.w3.org
<br>CSS Validator: http://jigsaw.w3.org/css-validator/

* __BootstrapCDN:__
Bootstrap 4 was utilised to create a resposive web page and give a framework to the website.
<br>https://getbootstrap.com/


* __Google Fonts:__ The main font was sourced from <br>https://fonts.google.com/

* __Auto prefix tool:__ This tool allowed me to insure cross-browser compatability.
<br>https://autoprefixer.github.io/

* __Git:__ Pushed Local git repository to remote repository on GitHub.
<br> https://git-scm.com/
<br>https://github.com/

* __CSS Colour Codes:__ Used to obtain the colours for the project.
<br>https://www.quackit.com/css/css_color_codes.cfm


## Testing

Testing information can be found in separate [TESTING.md file](https://github.com/murphya14/Simon-game/blob/master/Testing.md)

## Deployment

This project was created using the [Cloud9 IDE](https://c9.io), committed to git and then pushed to GitHub.

To deploy this page to GitHub Pages from its [GitHub repository](https://github.com/murphya14/Simon-game.git), the following steps were taken:
1. Log into GitHub.
2. In the repositories, select **murphya14/Fitness-webpaget**.
3. Select **Settings** which is below the navigation bar.
4. Go to the **GitHub Pages** section.
5. Click the **Source** menu and select **Master Branch**
6. The website is now deployed.
7. Scroll back to **GitHub Pages** section to find the link.


### How to run this project locally

Cloning this project from GitHub:
1. Follow this link to the [Simon Game Github repository](https://github.com/murphya14/Simon-game.git).
2. Click the green button on the right hand side of the screen named "Clone or download".
3. Copy the URL shown for the repository.
4. Open a terminal in your local dev environment.
5. Change working directory to the location where you want the cloned directory to be made.
6. Type ```git clone```, and then paste the URL you copied.
```console
git clone https://github.com/murphya14/Simon-game.git
```
7. Press Enter to create your local clone.


## Credits

* I received inspiration from researching other projects such as [Free Code Academy](https://github.com/beaucarnes/simon-game)

### Disclaimer
The content of this Website is for educational purposes only.







