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


**Authentication**

| Feature | Action             | Expected Result                 |
| :-----: | :-----------------:| :------------------------------:|
| **Login** | As already registered user, got to login page, complete login form and click login button. | Form validation is in effect. Remember me checkbox will store user information for next login. User is directed to homepage and success message informs of successful login as "username" |
| **Forgot Password function** | On Login page, click Forgot Password link. | User is directed to Reset Password page. Form validation is in effect. Reset link is sent to user email through which password can be reset. |
| **Sign Up** | As unregistered user, go to Sign Up page, complete form and submit | Form validation is in effect. User is directed to Login page. Success message informs of successful account registration. |
| **Logout** | As authenticated user, got to Logout page and click Sign out button | User is directed to homepage and success message informs user of successful sign out. |


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


#### Products 

**All Products page**

| Feature | Action                  | Expected Result                 |
| :-----: | :----------------------:| :------------------------------:|
| **Forum link** | Click link in info paragraph | User is directed to main forum page |
| **Contact Us link** | Click contact us link in info paragraph | User is directed to Contact section on About Us page |
| **Category link** | Click on any category tile below info paragraph | User is directed to products page of respective category |


**Products page (of same category)**

| Feature | Action                  | Expected Result                 |
| :-----: | :----------------------:| :------------------------------:|
| **Forum link** | Click link in info paragraph | User is directed to main forum page |
| **Quick link (back to all products)** | Click link at the top of the page, just below navbar | User is directed back to the All Products page |
| **Product tile link** | Click on any product tile below info paragraph | User is directed to product details page of respective product |


**Product Details page**

| Feature | Action                  | Expected Result                 |
| :-----: | :----------------------:| :------------------------------:|
| **Quick link (back to category)** | Click link at the top of the page, just below navbar | User is directed back to the category page of this product's category |
| **Page content** | On products detail page | User can see product image (or placeholder in case of no image), read product specs and see price |
| **Quantity form** | Enter different value into quantity input. | Values outside the range of 1-99 will show form validation error when adding product to basket |
| **Quantity adjustment buttons** | Adjust quantity input value with - or + button | Value will not go below 1 or above 99. Buttons become pale when reaching top or bottom range |
| **Browse more button** | Click button | User is directed back to all products page |
| **Add to basket button** | Click button | Product is added to basket with specified quantity. Basket nav link updates to show current number of product types |


**Products admin user (CRUD)**

| Feature | Expect             | Action                   | Result                 |
| :-----: | :-----------------:| :-----------------------:| :---------------------:|
| **Adding products** | Add products form allows submission of new entry which displays on forum page | Complete add products form in Profile > Manage Products and submit form | Form validation is effective. User is redirected to detail page of newly submitted product. Success alert displays. |
| **Editing products** | Edit option on each product detail page allows admin user to edit existing product. | Click Edit below product image. Update pre-populated form and submit. | After clicking Edit, info alert tells user that post is being edited. Form validation is effective. Form submit redirects user to product detail page with updated content. Success alert displays. |
| **Deleting products** | Delete option on each product detail page allows admin user to delete existing product. | Click Delete at the bottom of forum entry. | User is requested to confirm deletion of product. "Yes, I'm sure" button deletes product and success alert confirms action. "No, I'm not" button cancels delete action. |


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


#### Profile


#### Basket


#### Checkout

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



