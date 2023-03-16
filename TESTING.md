# Testing Instructions

## Table of Contents

- [Manual Testing](#manual-testing-guide)
    - [Global](#global)
    - [Forum](#forum)


## Manual Testing Guide

### Global

**Navigation**

| Feature | Action             | Expected Result                 |
| :-----: | :-----------------:| :------------------------------:|
| **Home Link Logo** | While not on homepage, click logo. | User is redirected back to homepage. |
| **"Home" Link** | While not on homepage, click "Home". | User is redirected back to homepage. |
| **"Live Poultry" dropdown** | Click dropdown in navbar | User is presented with a list of links (all categories, specific sub-categories) |
| **Poultry sub-categories** | From "Live Poultry" dropdown, select sub-link | User is directed to page listing all products of same category |
| **"Forum" link** | Click Forum link in navbar | User is directed to main forum page listing all entries |
| **"About Us" link** | Click About Us link in navbar | User is directed to about page with general business info |
| **"Profile" dropdown** | Click Profile dropdown | Authenticated user sees option to "Manage Profile". Admin user sees option to "Manage Profile", "Manage Products" and "Post in Forum". Dropdown is not visible to unregistered users. |
| **"Login" Link** | While not authenticated, click "Login". | User is directed to Login form. |
| **"Sign Up" Link** | While not authenticated, click "Sign Up". | User is directed to Sign Up form. |
| **"Logout" Link** | While authenticated, click "Logout". | User is directed to page with Sign Out button. |
| **"Basket" Link** | Click Basket link in navbar | User is directed to shopping basket page. |


**Social media links (located in footer)**

| Feature | Action                  | Expected Result                 |
| :-----: | :----------------------:| :------------------------------:|
| **Social media links** | Click on any of the social media icons | New tab opens with respective social media site |

**Newsletter**

No actual newsletter is set up to be sent out to subscribers. However, the infrastructure for subscription is in place as a form in the footer.

| Feature | Action                  | Expected Result                 |
| :-----: | :----------------------:| :------------------------------:|
| **Newsletter form** | Enter email address and click Subscribe | Users sees message "Thanks for subscribing!" |

**Privacy Policy**

| Feature | Action                  | Expected Result                 |
| :-----: | :----------------------:| :------------------------------:|
| **Privacy Policy page** | Click "Privacy Policy" link in footer | Users is directed to policy page where they can read the complete GDPR compliant document |

**404 error page**

| Feature | Action                  | Expected Result                 |
| :-----: | :----------------------:| :------------------------------:|
| **Custom 404 page** | Append faulty extension to home URL (or simply /404) | Users is directed to customised 404 error page, informing them of invalid URL with a Back to Homepage button |


#### Home 

**Shop Now button**

| Feature | Action                  | Expected Result                 |
| :-----: | :----------------------:| :------------------------------:|
| **Buy Live Poultry button** | Click button located on homepage | Users is directed to all products page, listing all available categories |


#### About

| Feature | Action                  | Expected Result                 |
| :-----: | :----------------------:| :------------------------------:|
| **Opening Hours link** | Click link in pick-up info section | Page scrolls down to opening hours section |
| **Forum link** | Click link in contact section | User is directed to main forum page |


#### Forum

**Unauthenticated Users**

| Feature | Expect             | Action                   | Result                 |
| :-----: | :-----------------:| :-----------------------:| :---------------------:|
| **Forum page** | Tiled list view of forum entries | Navigate to Forum via navlink | User sees all entries listed as linked tiles |
| **Entry Detail** | Full content of forum entry | Click on entry on forum page | User sees new page with entry content, and approved comments below |
| **Filter option** | Displays all entries of same type | Either on forum or on entry detail page, click on "type" button near entry title | User sees list of entries of same type |
| **Clear filter** | Displays all forum entries | After selecting an entry type, click "Clear Filter" button | User is brought back to forum page with all entries |

**Authenticated Users**

| Feature | Expect             | Action                   | Result                 |
| :-----: | :-----------------:| :-----------------------:| :---------------------:|
| **Responding** | Response form under forum entry with submit option | Fill out response form and submit | Alert message informs user that response is awaiting approval |
| **View Responses** | Approved responses to specifice entries listed below entry | Scroll below forum entry in entry detail page | User can read approved responses |

**Admin Users (CRUD)**

| Feature | Expect             | Action                   | Result                 |
| :-----: | :-----------------:| :-----------------------:| :---------------------:|
| **Adding entry** | Forum entry form allows submission of new entry which displays on forum page | Complete forum entry form in Profile > Post in Forum and submit form | Form validation is effective.User is redirected to detail page of newly submitted entry. Success alert displays. |
| **Editing entry** | Edit option on each entry detail page allows admin user to edit existing entry. | Click Edit at the bottom of forum entry. Update pre-populated form and submit. | After clicking Edit, info alert tells user that post is being edited. Form validation is effective. Form submit redirects user to entry detail page with updated content. Success alert displays. |
| **Deleting entry** | Delete option on each entry detail page allows admin user to delete existing entry. | Click Delete at the bottom of forum entry. | User is requested to confirm deletion of entry. "Yes, I'm sure" button deletes entry and success alert confirms action. "No, I'm not" button cancels delete action. |

#### User Feedback EDIT STiLL!!!!

Alert messages are displaying for the following user actions:

**Sign Up**:

| Feature | Action                   | Result                 |
| :-----: | :-----------------------:| :---------------------:|
| **Sign Up** | Click Sign Up button on Logout page | Alert messages informs user of successful sign out |
| **Sign In** | Click Sign out button on Logout page | Alert messages informs user of successful sign out |
| **Logout** | Click Sign out button on Logout page | Alert messages informs user of successful sign out |
| **Posting forum response** | Submit a response on a forum post | Alert message informs user that reponse is awaiting approval |


#### Real emails (needs editing) EDIT STiLL!!!!

- register for account with temporary email (example: [TempMail.org](https://temp-mail.org/en/))
- receive confirmation on fake email address and click on confirmation link
- site will reload and redirect to sign in page



