# Testing Instructions

## Table of Contents

- [Manual Testing](#manual-testing-guide)
    - [Global](#global)
    - [Forum](#forum)


## Manual Testing Guide

### Global

#### User Feedback

Alert messages are displaying for the following user actions:

**Sign Up**:

| Feature | Action                   | Result                 |
| :-----: | :-----------------------:| :---------------------:|
| **Sign Up** | Click Sign Up button on Logout page | Alert messages informs user of successful sign out |
| **Sign In** | Click Sign out button on Logout page | Alert messages informs user of successful sign out |
| **Logout** | Click Sign out button on Logout page | Alert messages informs user of successful sign out |
| **Posting forum response** | Submit a response on a forum post | Alert message informs user that reponse is awaiting approval |


#### Real emails (needs editing)

- register for account with temporary email (example: [TempMail.org](https://temp-mail.org/en/))
- receive confirmation on fake email address and click on confirmation link
- site will reload and redirect to sign in page

### Forum

#### Unauthenticated Users

| Feature | Expect             | Action                   | Result                 |
| :-----: | :-----------------:| :-----------------------:| :---------------------:|
| **Forum page** | Tiled list view of forum entries | Navigate to Forum via navlink | User sees all entries listed as linked tiles |
| **Entry Detail** | Full content of forum entry | Click on entry on forum page | User sees new page with entry content, and approved comments below |
| **Filter option** | Displays all entries of same type | Either on forum or on entry detail page, click on "type" button near entry title | User sees list of entries of same type |
| **Clear filter** | Displays all forum entries | After selecting an entry type, click "Clear Filter" button | User is brought back to forum page with all entries |

#### Authenticated Users

| Feature | Expect             | Action                   | Result                 |
| :-----: | :-----------------:| :-----------------------:| :---------------------:|
| **Responding** | Response form under forum entry with submit option | Fill out response form and submit | Alert message informs user that response is awaiting approval |
| **View Responses** | Approved responses to specifice entries listed below entry | Scroll below forum entry in entry detail page | User can read approved responses |

#### Admin Users (CRUD)

| Feature | Expect             | Action                   | Result                 |
| :-----: | :-----------------:| :-----------------------:| :---------------------:|
| **Adding entry** | Forum entry form allows submission of new entry which displays on forum page | Complete forum entry form in Profile > Post in Forum and submit form | Form validation is effective.User is redirected to detail page of newly submitted entry. Success alert displays. |
| **Editing entry** | Edit option on each entry detail page allows admin user to edit existing entry. | Click Edit at the bottom of forum entry. Update pre-populated form and submit. | After clicking Edit, info alert tells user that post is being edited. Form validation is effective. Form submit redirects user to entry detail page with updated content. Success alert displays. |
| **Deleting entry** | Delete option on each entry detail page allows admin user to delete existing entry. | Click Delete at the bottom of forum entry. | User is requested to confirm deletion of entry. "Yes, I'm sure" button deletes entry and success alert confirms action. "No, I'm not" button cancels delete action. |

