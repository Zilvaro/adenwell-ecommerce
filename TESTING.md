# AdenWell-Ecommerce Testing

[Back to the README.md file](https://github.com/Zilvaro/adenwell-ecommerce/blob/main/README.md)  

[Back to the Testing section in the README.md file](https://github.com/Zilvaro/adenwell-ecommerce/blob/main/README.md#testing)

[View the live website here](https://adenwell-ecommerce.herokuapp.com/)  

## Table of Contents

1. [Testing User Stories](#testing-user-stories)
2. [Code Validation](#code-validation)
3. [Accessibility](#accessibility)
4. [Tools Testing](#tools-testing)
5. [Manual Testing](#manual-testing)
6. [Unit Testing](#unit-testing)

***


## Testing User Stories


### Epic 1 - Shopping Experience


#### As a shopper, I want to easily find the products and their details.

* Products page is available, displaying the products and their main details.


#### As a shopper, I want to view products on a specific category.

* Links to each product category are provided in the home page.

* A product navigation bar is present in the products page, allowing the shopper to filter products per category.


#### As a shopper, I want to be able to sort the products depending on their price, rating or category.
* A sorting functionality is provided in the products page, allowing the shopper to sort products by price, name, rating and category.


#### As a shopper, I want to be able to search for products using specific keywords.

* A search bar is available on the website header, allowing the shopper to find a product by keyword across the whole website.


#### As a shopper, I want to easily select the quantity of products to be purchased.

* Quantity field is available in the product details page, allowing the shopper to select the desired product quantity before adding the product to the shopping bag.


#### As a shopper, I want to easily view the current purchase amount.

* The current purchase amount is available under the shopping cart icon in the header, making the information available across the whole website.


### Epic 2 - Shopping Bag and Checkout

#### As a shopper, I want to view all items currently on my shopping bag and be able to update them.
* Products added to the shopping bag are displayed in the shopping bag page.

* A quantity form is available in the shopping bag page for the shopper to update the product quantity.


#### As a shopper, I want to easily provide my shipping and payment information during the checkout.

* A form is available at the checkout for the shopper to provide the necessary information to complete the purchase.


#### As a shopper, I want to feel my personal and payment data is being handled securely.

* Stripe payments has been implemented as a payment method for the website in order to provide secure and easy transactions for the shoppers.


#### As a shopper, I want to receive an order confirmation once I have finished my purchase.

* A checkout success page is displayed to the shopper after completing the purchase.


#### As a shopper, I want to receive an order confirmation email for my records.

* An email is being sent to the email address provided by the shopper during the checkout.


### Epic 3 - Shopper Accounts


#### As a frequent shopper, I want to be able to register an account using my email address to be able to keep my records and interact with the website.

* All-auth has been implemented to handle user authentication, allowing the user to register an account.


#### As a frequent shopper, I want to receive a confirmation once my account has been registered to make sure the information entered was correctly.

* A confirmation is sent to the registered email address in order to validate it.


#### As a registered shopper, I want to easily log in and out from my account.

* All-auth has been implemented to handle user authentication, allowing the user to easily login and logout from their account.


#### As a registered shopper, I want to be able to recover access to my account in case I forget my password.

* All-auth can send a recovery link to the shopper's email address in the case they forget their credentials.


#### As a registered shopper, I want to have a personalized profile page where I can keep my contact information updated and see my past orders.

* A profile page is available for the shopper to keep their contact information updated as well as access their past orders.


### Epic 4 - Product Reviews

#### As a shopper, I want to be able to read product reviews left by other shoppers.

* Product reviews are available in the product details page for each product.

#### As a shopper, I want to be able to sort the reviews by date or rating.

* A sorting functionality has been provided for the reviews for the shopper to sort the reviews either by date or rating.

#### As a registered shopper, I want to be able to leave product reviews and rate the products.

* Forms are available for registered shoppers if to review and rate products.

* Registered shoppers are also able to update or delete their existing reviews.


**Epic 5 - Product Admin**

#### As a site admin, I want to be able to add and update products.

* CRUD functionality is implemented that allows to add or edit product from the front-end while being notified on the stage of activity and success or failure of it.

* Products and categories can also be conveniently added from the admin module.

#### As a site admin, I want to be able to remove product no longer available.

* Products can be easily removed from the fron-end (CRUD) or admin backend.

#### As a site admin, I want to display company/brand news and promotions.

* The convienient form in admin allows to upload image, alt-text, heading, excerpt, article (photo, text, links, video).
* Admin can choose in which carousel window to place the content and which position the content shall be within the window (eg. 1st or 3rd) 
* Admin can upload any image file with title and use it in one of the category field to promote a specific category or offer (by allocating the image#), or use the image anywhere in the application.


### Epic 6 - Newsletter Subscription & Contact

#### As a site admin, I want shoppers to be able to provide their contact information to be able to reach out to them with information and offers.

* A newsletter subscription form had been added to the website footer, making it available for the shoppers across the whole website.

![Epic 6 Subscription form](/media/testing_files/pre-filled-subscription-form.JPG)
![Epic 6 Subscription confirmation](/media/testing_files/thank-you-subscription-form.JPG)
![Epic 6 Subscriber information](/media/testing_files/subscriber-subscription-form.JPG)

#### As a site User I want to be able to send a message to admin, so that I can ask question or make inquiry about a product

* A contact form had been added to the website footer, making it available for the users across the whole website to write a message.

![Epic 6 Contact form](/media/testing_files/pre-filled-contact-form.JPG)
![Epic 6 Contact Message confirmation](/media/testing_files/thank-you-contact-form.JPG)
![Epic 6 Contact Content](/media/testing_files/contact-contact-form.JPG)



## Code Validation

### HTML

* No significant errors were returned when passing through the [W3C Markup Validator](https://validator.w3.org/) validator. However, there were warnings where Summernote text field was rendered within H-element - that elements mismatch  

### CSS
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) found no errors on my CSS files.

### Python

Pylint was used continuously during the development process to analyze the Python code for programming errors.

The code was then checked for errors via the terminal command "python3 -m flake8". This returned a number of whitespace and indentation errors which were rectified where possible. (The unfixed errors were situated in root files such as .vscode/artictern)

Other errors regarding unused imports were corrected by removing the unnecessary files.

### Javascript

* [JSHint](https://jshint.com/) found several warnings concerning missing or unnecessary semicolons. These warnings were corrected.


## Accessibility

Lighthouse in Chrome DevTools has been used to confirm that the colors and fonts being used throughout the website are easy to read and accessible. See reports in the table below:


### Lighthouse Reports

Page | Lighthouse Report |
| --- | --- |
| Home | ![Home Lighthouse Report](/media/testing_files/lighthouse-home.JPG) |
| Products | ![Products Lighthouse Report](/media/testing_files/lighthouse-products.JPG) |
| Product Details | ![Product Details Lighthouse Report](/media/testing_files/lighthouse-product-details.JPG) |
| Add Product | ![Add Product Lighthouse Report](/media/testing_files/lighthouse-add-product.JPG) |
| Edit Product | ![Edit Product Lighthouse Report](/media/testing_files/lighthouse-edit-product.JPG) |
| Shopping Bag !| ![Shopping Bag Lighthouse Report](/media/testing_files/lighthouse-shopping-bag.JPG) |
| Checkout | ![Checkout Lighthouse Report](/media/testing_files/lighthouse-checkout.JPG) |
| Checkout Success | ![Checkout Success Lighthouse Report](/media/testing_files/lighthouse-checkout-success.JPG) |
| Profile | ![Profile Lighthouse Report](/media/testing_files/lighthouse-myprofile.JPG) |
| Contact | ![Contact Lighthouse Report](/media/testing_files/lighthouse-contact-form.JPG) |

The low score on the product admin pages, depends mostly on the aria-labels being suggested for the "Select image" button and the image example.

## Tools Testing


### [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

* Chrome DevTools was used during the development process to test, explore and modify HTML elements and CSS styles used in the project.


### Responsiveness

* Chrome DevTools was used to test responsiveness in different screen sizes during the development process.


## Manual Testing


### Browser Compatibility

Browser | Outcome | Pass/Fail | 
--- | --- | --- |
Google Chrome | No appearance, responsiveness nor functionality issues.| <span style="color:green">Pass</span> |
Safari | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
Mozilla Firefox | No responsiveness nor functionality issues.| <span style="color:green">Pass</span> |
Microsoft Edge | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |


### Device Compatibility

Device | Operative System |Outcome | Pass/Fail
--- | --- | --- | --- |
HP Lattitude | Windows 10 | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
Del XPS13 | Windows10 | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
iPhone 6 | iOS 14 | No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
Samsung S20 | Android 10 |No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |
Nokia 8 | Android 9 |No appearance, responsiveness nor functionality issues. | <span style="color:green">Pass</span> |



### Test Results

#### General

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Main Logo Link | Clicking the link redirects to the home page. |<span style="color:green">Pass</span> |
Shop Now Link | Clicking the link redirects to the products page. | <span style="color:green">Pass</span> |
My Account Icon - Register Link | Clicking the link redirects to the account sign up page. | <span style="color:green">Pass</span> |
My Account Icon - Login Link | Clicking the link redirects to the account sign in page. | <span style="color:green">Pass</span> |
My Account Icon - Logout link | Clicking the link redirects to the account sign out page. | <span style="color:green">Pass</span> |
My Account Icon - Product Management Link | Clicking the link redirects to the add product page. | <span style="color:green">Pass</span> |
My Account Icon - My Profile Link | Clicking the link redirects to the profile page. | <span style="color:green">Pass</span> |
Shopping Cart Icon | Clicking the link redirects to the shopping cart. | <span style="color:green">Pass</span> |
Search Bar | Clicking the link redirects to the products page and display the matching products. | <span style="color:green">Pass</span> |
Privacy Policy Link | Clicking the link opens the privacy policy. | <span style="color:green">Pass</span> |
Facebook Icon | Clicking the link open the business Facebook page on a separate tab. | <span style="color:green">Pass</span> |
Contact Link | Clicking the link opens the message form. | <span style="color:green">Pass</span> |
Newsletter Form | Email address gets registered to the database when submitting the form. | <span style="color:green">Pass</span> |


#### Home Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Content Links | Clicking any of carousel cards the links will redirect to the article or more related information. | <span style="color:green">Pass</span> |
Categories Links | Clicking any of the links will redirect to the products page and filter the products on that category. | <span style="color:green">Pass</span> |
Down Arrow Link | Clicking the link redirects to about section in the home page. | <span style="color:green">Pass</span> |


#### Products Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Product Navigation Bar Links | Clicking any of the links will filter the products on that category. | <span style="color:green">Pass</span> |
Sort By Selector | Sort by functionality sort the products depending on the selection. | <span style="color:green">Pass</span> |
Product Image | Clicking the image redirect to the product details page for that specific product. | <span style="color:green">Pass</span> |
Product Edit Link | Clicking the link redirects to the edit product page. | <span style="color:green">Pass</span> |
Product Delete Link | Clicking the link delete the product from the database. | <span style="color:green">Pass</span> |


#### Product Details Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Product Navigation Bar Links | Clicking any of the links will redirect to the products page and filter the products on that category. | <span style="color:green">Pass</span> |
Product Image | Clicking the image opens it on a separate tab. | <span style="color:green">Pass</span> |
Product Edit Link | Clicking the link redirects to the edit product page. | <span style="color:green">Pass</span> |
Product Delete Link | Clicking the link deletes the product from the database. | <span style="color:green">Pass</span> |
Decrease Quantity Button | Decreases the quantity on the input form. | <span style="color:green">Pass</span> |
Increase Quantity Button | Increases the quantity on the input form. | <span style="color:green">Pass</span> |
Keep Shopping Button | Clicking the button redirects to the products page. | <span style="color:green">Pass</span> |
Add To Bag Button | Clicking the button adds the specified quantity of the product to the shopping bag. | <span style="color:green">Pass</span> |
Sort By Selector | Sort by functionality sort the reviews depending on the selection. | <span style="color:green">Pass</span> |


#### Add Product Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Select Image Button | Clicking the button allows to add an image to the form | <span style="color:green">Pass</span> |
Add Product Form | Product gets registered to the database when submitting the form. | <span style="color:green">Pass</span> |
Cancel Button | Clicking the button redirects to the products page. | <span style="color:green">Pass</span> |


#### Edit Product Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Select Image Button | Clicking the button allows to add or replace the image | <span style="color:green">Pass</span> |
Edit Product Form | Product gets updated when submitting the form. | <span style="color:green">Pass</span> |
Cancel Button | Clicking the button redirects to the products page. | <span style="color:green">Pass</span> |


#### Shopping Bag Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Decrease Quantity Button | Decreases the quantity on the input form. | <span style="color:green">Pass</span> |
Increase Quantity Button | Increases the quantity on the input form. | <span style="color:green">Pass</span> |
Update Link | Clicking the link update the product quantity on the shopping bag. | <span style="color:green">Pass</span> |
Delete Link | Clicking the link removed the product from the shopping bag. | <span style="color:green">Pass</span> |
Keep Shopping Button | Clicking the button redirects to the products page. | <span style="color:green">Pass</span> |
Secure Checkout Button | Clicking the button redirects to the checkout page. | <span style="color:green">Pass</span> |


#### Checkout Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Checkout Form | An order gets created when submitted the form. | <span style="color:green">Pass</span> |
Login Link | Clicking the link redirects to the account sign in page. | <span style="color:green">Pass</span> |
Register Link | Clicking the link redirects to the account sign up page. | <span style="color:green">Pass</span> |
Save Information Check | Checking the box update the user's profile information during the checkout process. | <span style="color:green">Pass</span> |
Adjust Bag Link | Clicking the link redirects to shopping bag page. | <span style="color:green">Pass</span> |


#### Profile Page

Element | Expected Outcome | Pass/Fail |
--- | --- | --- |
Update Information Form | User's information gets updated when submitting the form. | <span style="color:green">Pass</span> |
Order Link | Clicking the link redirects to order view. | <span style="color:green">Pass</span> |


## Unit Testing

Unit tests were written for views on the adenapp app, practicing test-driven development on those methods.

![Test AdenApp Views](/media/testing_files/test-views.jpg)