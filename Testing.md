# GymBuddy - Testing

[README.md](https://github.com/murphya14/GymBuddy/blob/master/README.md)

[Website available to view in GitHub Pages](https://gymbuddya.herokuapp.com/)


## Testing

The following validators were used to test the code:

* [W3C Markup Validation]( https://validator.w3.org/)
* [W3C CSS validation](https://jigsaw.w3.org/css-validator/)
* [JS Hint](https://jshint.com/)

### Client stories testing:

Most common path through the website:
- The user will be brought to the Home page(the only page) be default.
  Depending on the user, they may want to get more information on how to play the game before starting.

### Testing client stories from UX section of README.md

1. I want be introduced to the website and have access to a sign up or find my profile - Welcome Page
     * The text is Ubuntu which allows for the impression of a simplistic theme that reflects the attitude of the application (making excercise easy and .)
     * The white background and sparse colours further enhance the simplistic feel of GymBuddy. 
     * The striking pink colour as you hover over the links in the navbar incentive the potential user to click it and sign up or go to the members area.

2. I want to be able to make an account with my personal information in it
    * The sign up page allows you to input your name, weight and the workout you would like to begin.

3. I want to be able to access my account that has already been created 
    * The Members Area allows the user to choose their name. 
    * Once selected, the user will be brought to their current workout.

4. I want to be able to get more information about the workout 
     * The button labelled "Workout Structure" provides information about the layout of the program and how to complete the workout.
    
5. I want to be able to get access to examples of the excercises
     * The option is available, through an accordian, to access links which gives examples of each excercise.
     * The user does not have to look at all examples as they may already be aware of how to execute the excercise. This is why an accordian was utilised as it gives the user control of how much instruction is required. 

6. I want to be able to record the weight of the main lifts 
     * The yellow "Weight" button that accompany the main excercises allows the user to access a page the records the weight of the main lifts (e.g. squat, bench press etc.)
     * This page is also accessable through the navbar "Record your Main Lifts"

    
7. I want to be able to see only the excercises that I have not already completed
     * There is a green "Completed" button under each set of excercise (e.g. warmups.) Once clicked, the corressponding set of excercises will disappear.
     * The workout page will only display the sets of excercises left to be completed. 

8. I want to be able to move onto the next workout 
     * The green "Select Next Workout" button will bring the user to the edit_user page where they can intuitivially select their next workout.
     * If they were on workout 1A, the next workout would be 1B and so on. 

9. I want to be able to access links through the navbar and see copyright info in the footer 
     * Both have been created with further information.

10. I want to be able to edit my profile
     * The user can edit their name, delete their profile and edit their weight in this page.


### Manual (logical) testing of all elements and functionality on every page.


1. Welcome Page:
Confirmed
    * the page was displaying properly on all screens.
    * If name in Session, redirects to get_user
    * Links for Sign up and Members Area are working and directing appropriately
    * The header and footer were sitting correctly.
    * Spelling was correct and clear.
    
2. Sign up page
Confirmed 
 * can create new user
 * dropdown detailing all the workouts is enabled
 * redirects to the welcome page

3. Members Area page
Confirmed 
 * dropdown detailing all the users is enabled
 * redirects to the wworkout page


4. "Workout Structure" modal:
Confirmed
     * Positioned correctly when the page was opened.
     * Visually appealing and obvious to the user.
     * All spelling is correct.
     * Closing the modal is accessable by re-clicking the button or clicking "Close."

5. Workout Page:
Confirmed
    * The correct greeting message appears with the current workout and user.
    * The accordian works and has links to the excercise 
    * Selecting the complete button means the associating excercise set is removed from view.
    * Clicking the weight button brings the user to the edit weights page
    * User can select the button at the end of the page to choose the next workout
    * All links in the nav bar work 

6. Edit weight page:
Confirmed
    * The user can change or create new weight values for the lifts specified and be redirected back to their workout.
   
7. Edit user/Selct next workout:
Confirmed
    * The user can select another workout which will display that workout once they have returned to get_user.
    * The user ca edit their weight or name.
    * The user can delete their profile.


8. Footer:
Confirmed
    * Check the responsive design at each width.




## Further testing:

1. Received feedback from students, friends and family who viewed the game on different devices. _ There was a problem with redirecting to the get_user page once the user was created. This was rectified by redirecting to welcome and accessing the new user in the members area._
2. Used Chrome Developer tools to get appropriate placing and design.




















