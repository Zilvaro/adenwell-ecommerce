![Aden Wellness Logo](/media/aden-logo-no-background.png)


# Welcome!


The idea is to develop a digital e-commerce solution for a real SME "Aden Wellness" where they can communicate their business ideas to their potential clients, promote products and sell directly online. 

Therefore, the app has 2 distinctive parts:
1.	Top part is the content selection of more permanent materials that are managed by the company (admin, UserAdmins)
2.	The e-commerce part where Aden Wellness can display products, collect orders and process payments  

The working version of the AdenWell e-commerce app can be found [here](https://adenwell-ecommerce.herokuapp.com/)


![website preview](/media/readme_files/am-i-responsive-black.JPG)




## Table of Contents

- [Welcome!](#welcome)
  - [Table of Contents](#table-of-contents)
  - [User Experience (UX)](#user-experience-ux)
    - [Strategy](#strategy)
      - [Project Goals](#project-goals)
      - [User Goals](#user-goals)
      - [Strategy Table](#strategy-table)
    - [Scope](#scope)
      - [User Stories](#user-stories)
        - [User Stories - Viewing and Navigation](#user-stories---viewing-and-navigation)
        - [User Stories - Registration and User Account](#user-stories---registration-and-user-account)
        - [User Stories - Sorting and Searching](#user-stories---sorting-and-searching)
        - [User Stories - Purchasing and Checkout](#user-stories---purchasing-and-checkout)
        - [User Stories - Admin and Store Management](#user-stories---admin-and-store-management)
      - [Things, left "for next Iteration"](#things-left-for-next-iteration)
    - [Structure](#structure)
      - [Database Model](#database-model)
      - [Wireframes](#wireframes)
    - [Surface](#surface)
      - [Color Scheme](#color-scheme)
      - [Typography](#typography)
  - [Marketing](#marketing)
    - [Search Engine Optimisation](#search-engine-optimisation)
    - [Facebook business page (mock-up)](#facebook-business-page-mock-up)
  - [Features - Finished Product](#features---finished-product)
    - [General](#general)
      - [Header](#header)
      - [Footer](#footer)
    - [Home Page](#home-page)
      - [Content Section](#content-section)
      - [Categories Section](#categories-section)
    - [Products Page](#products-page)
    - [Product Details Page](#product-details-page)
    - [Products Admin](#products-admin)
      - [Add/Edit Product](#addedit-product)
    - [Shopping Bag Page](#shopping-bag-page)
    - [Checkout \& Success Payment Page](#checkout--success-payment-page)
    - [Reviews Page](#reviews-page)
      - [My reviews](#my-reviews)
    - [Reviews CRUD](#reviews-crud)
      - [Add Review](#add-review)
      - [Edit Review](#edit-review)
    - [Profile Page](#profile-page)
    - [Contact Page](#contact-page)
    - [Accounts Pages](#accounts-pages)
    - [404 Error Page](#404-error-page)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Libraries and Frameworks](#libraries-and-frameworks)
    - [Packages / Dependencies Installed](#packages--dependencies-installed)
    - [Database Management](#database-management)
    - [Payment Service](#payment-service)
    - [Cloud Storage](#cloud-storage)
    - [Tools and Programs](#tools-and-programs)
  - [Testing](#testing)
  - [Deployment](#deployment)
    - [How To Use This Project](#how-to-use-this-project)
      - [Fork GitHub Repository](#fork-github-repository)
      - [Clone Github Repository](#clone-github-repository)
      - [Project Set Up After Forking or Cloning](#project-set-up-after-forking-or-cloning)
    - [Deployment to Heroku](#deployment-to-heroku)
    - [AWS Bucket Creation](#aws-bucket-creation)
    - [Connect Django to AWS Bucket](#connect-django-to-aws-bucket)
  - [Credits](#credits)
    - [Content](#content)
    - [Code](#code)
  - [Known Bugs](#known-bugs)
  - [Acknowledgements](#acknowledgements)


***


## User Experience (UX)

### Strategy

In effect, Adenwell is a business presentation and ecommerce application with full content management functionality from the front-end, and full online-store feature (excluding the delivery follow-up).

#### Project Goals

* Responsive design to make the website accessible on different screen sizes.

* Structure is easy to understand and navigates effortlessly for an easy shopping experience.

* The website design and colors are appealing to the customers.

* Customers are offered the opportunity to register an account.

* Easy shopping process to create a pleaseant experince for the customer.

* Flexible and clear content fields allowing to present the company and products


#### User Goals

**Epic 1 - Shopping Experience**

* As a shopper, I want to easily find the products and their details.

* As a shopper, I want to view products on a specific category.

* As a shopper, I want to be able to sort the products depending on their price, rating or category.

* As a shopper, I want to be able to search for products using specific keywords.

* As a shopper, I want to easily select the quantity of products to be purchased.

* As a shopper, I want to easily view the current purchase amount.
  

**Epic 2 - Shopping Bag and Checkout**

* As a shopper, I want to view all items currently on my shopping bag and be able to update them.

* As a shopper, I want to easily provide my shipping and payment information during the checkout.

* As a shopper, I want to feel my personal and payment data is being handled securely.

* As a shopper, I want to receive an order confirmation once I have finished my purchase.

* As a shopper, I want to receive an order confirmation email for my records.
  

**Epic 3 - User Accounts**

* As a frequent shopper, I want to be able to register an account using my email address to be able to keep my records and interact with the website.

* As a frequent shopper, I want to receive a confirmation once my account has been registered to make sure the information entered was correctly.

* As a registered shopper, I want to easily log in and out from my account.

* As a registered shopper, I want to be able to recover access to my account in case I forget my password.

* As a registered shopper, I want to have a personalized profile page where I can keep my contact information updated and see my past orders.
  

**Epic 4 - Product Reviews**

* As a shopper, I want to be able to read product reviews left by other shoppers.

* As a shopper, I want to be able to sort the reviews by date or rating.

* As a registered shopper, I want to be able to leave product reviews and rate the products.
  

**Epic 5 - Product Admin**

* As a site admin, I want to be able to add and update products.

* As a site admin, I want to be able to remove product no longer available.

* As a site admin, I want to display company/brand news and promotions.
  

**Epic 6 - Newsletter Subscription & Contact**

* As a site admin, I want shoppers to be able to provide their contact information to be able to reach out to them with information and offers.

* As a site User I want to be able to send a message to admin, so that I can ask question or make inquiry about a product



#### Strategy Table

Opportunity / Problem | Importance | Viability / Feasibility
--- | --- | ---
Responsive design | 5 | 5
Create, edit and delete products | 5 | 5
Account registration | 5 | 5
User profile | 5 | 5
Wishlist | 4 | 4
Save shipment information | 5 | 5
Product quick view | 3 | 2
Sort products by different criteria | 5 | 5
Search products by name or description | 5 | 5
Product details view | 5 | 5
Display similar products at the product details view | 3 | 2
Rate products | 4 | 3
Write product reviews | 4 | 3
Display current purchase total | 5 | 5
View current shopping cart | 5 | 5
Edit quantities inside the shopping bag | 4 | 4
Shopping cart quick view | 3 | 3
Card payment | 5 | 5
Additional payment options | 3 | 2
Content display | 5 | 4
Newsletter subscription | 5 | 5
**Total** | **93** | **87**


### Scope

According to the strategy table, not all features can be implemented in the first release of the project. For this reason, the project will be divided in multiple phases. The first phase will include the features that have been identified in order to build the minimum viable product and then add payments & database management.


**First Phase**

* Responsive design

* Create, edit and delete products (CRUD)

* Account registration

* User profile

* Save shipment information

* Sort products by different criteria

* Search products by name or description

* Product details view

* Display current purchase total

* View current shopping cart

* Edit quantities inside the shopping bag


**Second Phase**
  
* Content display

* Rate products

* Write product reviews

* Newsletter subscription



**Third Phase**

* Card Payment

* Manage products and content in PosgreSQL (ElephantSQL)

* Additional payment options


#### User Stories

GitHub projects was used as project management tool to track user stories. Using a Kanban board helped to focus on specific tasks and track the project progress. Each UserStory was given a priority label and a milestone note.
The issue that was decided not to complete received a comment before closing.


![User Stories Progress - GitHub](/media/readme_files/userstories-prioritylabels-milestones.JPG)
![User Stories Comments - GitHub](/media/readme_files/issue-not-completed.JPG)
![User Stories Issues Closed](/media/readme_files/closed-issues.JPG)



##### User Stories - Viewing and Navigation

1.	As a **Shopper** I want to be able **view a list of products**, so that I can **select some to purchase**
2.	As a **Shopper** I want to be able **view individual product details**, so that I can **identify the price, description, product rating, product image and available sizes**
3.	As a **Shopper** I want to be able **quickly identify deals, clearance items and special offers**, so that I can **take advantage of special savings on products I'd like to purchase**
4.	As a **Shopper** I want to be able **easily view the total of my purchases at any time**, so that I can **avoid spending too much**

##### User Stories - Registration and User Account

5.	As a **Site User** I want to be able **easily register for an account**, so that I can **have a personal account and be able to view my profile**
6.	As a **Site User** I want to be able **easily login or logout**, so that I can **access my personal account information**
7.	As a **Site User** I want to be able **easily recover my password in case I forget it**, so that I can **recover access to my account**
8.	As a **Site User** I want to be able **receive an email confirmation after registering**, so that I can **verify that my account registration was successful**
9.	As a **Site User** I want to be able **have a personalized user profile**, so that I can **view my personal order history and order confirmations, and save my payment information**
10.	As a **Site User** I want to be able **I can sign up for a newsletter**, so that I can **know new product releases and offers**
11.	As a **Site User** I want to be able **send a message to admin**, so that I can **Ask question or make inquiry about a product**

##### User Stories - Sorting and Searching

12.	As a **Shopper** I want to be able **sort the list of available products**, so that I can **easily identify the best rated, best priced, and categorically sorted products**
13.	As a **Shopper** I want to be able **sort a specific category of product**, so that I can **find the best-priced or best rated products in a specific category, or sort the products in that category by name**
14.	As a **Shopper** I want to be able** sort multiple categories of products simultaneously**, so that I can **find the best-priced or best-rated products across broad categories, such as "supplements" or "wellness"**
15.	As a **Shopper** I want to be able** search for a product by name or description**, so that I can** find a specific product I'd like to purchase**
16.	As a **Shopper** I want to be able **easily see what I've searched for and the number of results**, so that I can **quickly decide whether the product I want is available**

##### User Stories - Purchasing and Checkout

17.	As a **Shopper** I want to be able **easily select the variant and quantity of a product when purchasing it**, so that I can **ensure I don't accidentally select the wrong product, quantity or size**
18.	As a **Shopper** I want to be able** view items in my bag to be purchased**, so that I can **identify the total cost of my purchase before checkout**
19.	As a **Shopper** I want to be able **adjust the quantity of individual items in my bag**, so that I can **easily make changes to my purchase before checkout**
20.	As a **Shopper** I want to be able **easily enter my payment information**, so that I can **check out quickly and with no hassles**
21.	As a **Shopper** I want to be able **feel my personal and payment information is safe and secure**, so that I can **confidently provide the needed information to make a purchase**
22.	As a **Shopper** I want to be able **view an order confirmation after checkout**, so that I can **verify that I haven't made any mistakes**
23.	As a **Shopper** I want to be able **receive an email confirmation after checking out**, so that I can **keep the confirmation of what I've purchased for my records**

##### User Stories - Admin and Store Management

24.	As a **Admin** I want to be able **add a product**, so that I can **add new items to my store**
25.	As a **Admin** I want to be able **edit/update a product**, so that I can **change product prices, descriptions, images, and other product criteria**
26.	As a **Admin** I want to be able **delete a product**, so that I can **remove items that are no longer for sale**
27.	As a **Admin** I want to be able **add, edit or delete a content item**, so that I can **create an impulse to buy**
28.	As a **Admin** I want to be able **organize external database**, so that I can **manage all site’s data securely**


#### Things, left "for next Iteration"

* As a **Site Admin** I can **set the publishing and validity date (&time) of the content** so that **I can manage content appearance**.

* As a **Site Admin** I can **set the end date for the post** after which it moves to 'draft' status so that **I can keep the site cleaner**.
  
* Social media sign-up


### Structure

The website has been organized in a Hierarchical Tree Structure to ensure the site user navigates through the site effortlessly and intuitively. Here you can you can find the website map design.

![AdenWell website map](/media/readme_files/aden_e-com_wire_flow%20.png)

* Header, footer and navigation bar are consistent through all pages.

* Links and forms provide clear feedback to the site user.

* New additional content features are provided for the shopper once they register an account.

* A 404-error page is available.


#### Database Model

The database model has been designed using [lucidapp](https://lucid.app/). The type of database being used for the is relational database being managed using SQLite3 during development and deployed using [ElephantSQL](https://www.elephantsql.com/).

![AdenWell E-commerce Database Model](/media/readme_files/database-model.png)


Some of the new models here - Carousel content management , Media and category database, Contact Message clients registration, Reviews:

![Adenapp models-1](/media/readme_files/new-models-1.JPG)
![Adenapp models-2](/media/readme_files/new-models-2.JPG)

#### Wireframes

[Balsamiq](https://balsamiq.com/) has been used to showcase the appearance of the site and display the placement of the different elements within the pages.

Page | Mobile & Desktop Version 
--- | --- | ---
Home | ![Home wireframe image](/media/readme_files/aden-store-blsmq-home.png) | 
Products | ![Products wireframe image](/media/readme_files/aden-store-blsmq-products.png) | 
Product Details | ![Product details wireframe image](/media/readme_files/aden-store-blsmq-product-detail.png) | 
Shopping Bag | ![Shopping bag wireframe image](/media/readme_files/aden-store-blsmq-shopping-bag.png) | 
Checkout | ![Checkout wireframe image](/media/readme_files/aden-store-blsmq-checkout.png) | 
Profile | ![Profile wireframe image](/media/readme_files/aden-store-blsmq-profile.png) | 
Contact | ![Contact wireframe image](/media/readme_files/aden-store-blsmq-contact.png) | 



### Surface
[Go to the top](#table-of-contents)

#### Color Scheme

![Color scheme image](/media/readme_files/color-pallet.jpg)

The colors used in the ecommerce website respect the green-golden color-scheme of Aden Wellness, represented in the logo. 

Main colors in the application are achieved through images, so complementary slate-grey (#445261), navy-blue (#055772) and baby powder (#FFFFFD) were chosen just to create some contrast, improve readability and maintain consistent look. 


#### Typography

The main font being used in the site is Roboto, with sans-serif as a fallback in case Roboto doesn't get imported correctly. 

Roboto was chosen after refresher-research on fonts that are better for reading and Roboto has proven to be font-of-choice for a few years in app development.



## Marketing


### Search Engine Optimisation

To improve the search index rating on Google, research was carried out using a number of tools, such as [MOZ](https://moz.com/)  and [QuestionDB](https://questiondb.io) to search for relevant keywords to use in meta tags, alt-texts and content elements of the project.

![MOZ keyword search](/media/readme_files/moz-kw-dashboard.JPG)
![QuestionDB keyword search](/media/readme_files/questionDB-questions.JPG)

A number of short and long tail keywords were then selected:

* e-store
* online store app
* ecommerce platform for start-ups
* free app for my business
* ecommerce and engagement app 
* build online business community 
* online shop for small business
* healthy supplements
* hygge
* aromatic oils for home
* wellness


SEO steps taken in the projects to improve searchability

1.	In header/nav use <strong>Span</strong> for Title and then use H1 for some important keywords and text later
2.	Use <strong>H2</strong> to add another critical promo keyword information on the page
3.	Use the <strong>Strong</strong> html element when including some exact & long-tail keywords to provide visual emphasis and search engines will understand their semantic value from this too.
4.	Always use keyword-rich, but still meaningfully describing picture <strong>ALT</strong> and image file name
5.	Social network links must include the <strong>rel="noopener nofollow"</strong> attribute, which tells search engines not to include these links when it looks at our search engine ranking.

![External links noopener ](/media/readme_files/facebook-nofollow-rel.JPG)

6. Include a sitemap.xml to allow search engine bot crawling

![SEO sitemap.xml ](/media/readme_files/sitemap-xml.JPG)

7. Include a robots.txt file to control search engine bot crawling

![SEO robots.txt ](/media/readme_files/robots-txt.JPG)



These keywords later will be continually improved and refined and over time it should ultimately assist in the site ranking higher on Google.


### Facebook business page (mock-up)

As a real FB page has been in a build-process, the mock-up version was used for this project:

![Facebook mock-up page](/media/readme_files/facebook-balsamique.png)



## Features - Finished Product
[Go to the top](#table-of-contents)

### General

* The website has been designed from a mobile first perspective.

* Responsive design across all device sizes.
  

####  Header 
![Adenwell header product pages](/media/readme_files/header-2.JPG)

* The header contains the main logo, navigation links and search product functionality.

* The main logo works as a link to the home page.

* The search bar allows the user to search the website for products using specific keywords.

* The search can is hidden at first for better visuals and can be toggled using the search icon link in case the shopper needs.

* The navigation links allow the shopper access to all sections to facilitate navigation across the website. It also has a hover effect that changes color to provide feedback to the shopper for a better user experience.

* The delivery-fee information is only on product related pages



#### Footer
![Adenwell footer](/media/readme_files/footer.JPG)

* The footer contains business information as well as links to our Facebook page and privacy policy.

* It has an invitation and a link to leave a comment, suggestion or ask a question

* A newsletter registration form has been located at the footer allowing the user to subscribe to healthy news from every page of the app.


### Home Page


#### Content Section
![Adenwell home page](/media/readme_files/home-page.JPG)

* Provide relevant information, promo offer, brand messages to the shopper looking to learn more about our business.



#### Categories Section
![Adenwell home page-categories](/media/readme_files/product-links.JPG)

* Display to the shopper the product categories available, providing a link to each category.


### Products Page
![Adenwell product page](/media/readme_files/product-page.JPG)

* Display all the products currently available or filtered on a specific category.

* Display an image of the products as well as their main information such as name, price and rating.

* Provides a product navigation bar to allow the shopper to filter products per category

* Provides sorting functionality to sort products by price, rating, name or category.

* A back to the top button is available so the shopper can easily come back to the top of the page.

* Links to edit and remove are available for each product.


### Product Details Page
![Adenwell product-details](/media/readme_files/product-detail.JPG)

* The products navigation bar is present in case the shopper wants to go back to the products.

* Provide a larger image of the product and display its detailed information

* Allow the user to select the quantity of products to be added to the shopping bag.

* Provide a "Keep Shopping" button to go back to the products.

* An "Add to Bag" button is available to add the desired quantity of the product to the shopping bag.

* All reviews the product has received are being displayed on the reviews section at the bottom of the page. 

* Sort functionality allows the shopper to sort the products either by date created or rating.

* A link to leave a review is available at the bottom of the reviews.

* Provide edit and delete link for the logged in shopper's own reviews.


### Products Admin

#### Add/Edit Product
![Adenwell product management CRUD](/media/readme_files/product-management.JPG)

* Provide a form for the site admin to be able to add new products to the store or
* Provide a prefilled form for the site admin to be able to update products in the store.


### Shopping Bag Page
![Adenwell shopping bag](/media/readme_files/shoping-bag.JPG)


* A message alerts the user in case the free delivery threshold has not been reached, displaying the amount left.

* Display all products currently on the shopping bag and their information.

* Allow the user to update the product quantity or remove the product from the shopping bag.

* Display the current total cost including the bag total and delivery costs.

* Provide a "Keep Shopping" button to go back to the products.

* A button to checkout is provided for the shopper to finish the purchase.


### Checkout & Success Payment Page
![Adenwell checkout](/media/readme_files/checkout.JPG)
![Adenwell completed order](/media/readme_files/completed-order.JPG)
![Adenwell order visibility admin](/media/readme_files/order-visibility-admin.JPG)
![Adenwell order detail admin](/media/readme_files/order-detail-admin.JPG)
![Adenwell order confirmation email](/media/readme_files/order-confirmation-email.JPG)

* Provide a checkout form for the shopper to complete the purchase and provide the necessary contact, shipping and payment information.

* Display an order summary listing all the products to be purchased and their total cost including the bag total and delivery costs.

* Provide a link back to the shopping bag in the case the shopper would like to adjust the products in the shopping bag.

* A message is displayed, informing the shopper the amount to be charged on the provided card.

* Descriptive error messages are displayed in case there is any issue with the payment information provided.

* Display the payment is complete and the order confirmation email has been sent to the email address provided.


### Reviews Page

#### My reviews
![Adenwell product-MyReview-desktop](/media/readme_files/reviews-myreviews.JPG)
![Adenwell product-MyReview-mobile](/media/readme_files/reviews-myreviews-mobile.JPG)

* Display the reviews the registered shopper has provided and the review's information.

* Provide a link back to the product.

* Links to edit and delete the reviews are present for each review.


### Reviews CRUD

#### Add Review
![Adenwell review-Add](/media/readme_files/review-add.JPG)
![Adenwell review-Error](/media/readme_files/review-error-alreadysubmitted.JPG)
![Adenwell review-Success](/media/readme_files/review-submitted.JPG)

* Display the product being reviewed.

* Provide a form for the registered shopper to be able to add review to the product.

* Display error if user has already submitted the review for this product

* Inform user when he successfully submitted the review  

#### Edit Review
![Adenwell review-Edit](/media/readme_files/review-edit.JPG)
![Adenwell review-Updated](/media/readme_files/review-updated-notification.JPG)
![Adenwell review-Deleted](/media/readme_files/review-deleted.JPG)

* Provide a prefilled form for the registered shopper to be able to update their existing reviews.

* Notify user that he is in editing mode 
  
* Inform user when he successfully updated the review or deleted it  



### Profile Page
![Adenwell profile](/media/readme_files/profile.JPG)

* Provide a form for the registered shopper to update their default information.

* An order history section is present with all registered shopper's past orders information.


### Contact Page
![Adenwell contact](/media/readme_files/contact-page.JPG)

* Displays the form for the user to write a comment or ask a question.


### Accounts Pages

Page | Purpose | Image |
--- | --- | --- |
Sign Up | Allow the shopper to sign up an account for the website. | ![Adenwell contact](/media/readme_files/sign-up.JPG) |
Sign In | Allow the registered shopper to sign in with their account. | ![Adenwell contact](/media/readme_files/sign-in.JPG) |
Sign Out | Allow the registered shopper to sign out from their account. | ![Adenwell contact](/media/readme_files/sign-out.JPG) |


### 404 Error Page
![Adenwell 404 error page image](/media/readme_files/404-message.JPG)

* Provided information to the shopper in case the address entered cannot be found.

* A link to come back to the products is present.


[Back to top ⇧](#table-of-contents)


## Technologies Used
[Go to the top](#table-of-contents)

### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML)
* [CSS3](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


### Libraries and Frameworks

* [Django](https://www.djangoproject.com/)   
    * Django was used as web framework.

* [Django Template](https://jinja.palletsprojects.com)  
    * Django Template was used as a templating language for Django to display backend data to HTML.
   
* [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)  
    * Bootstrap 5 was used throughout the website to help with styling and responsiveness.

* [Google Fonts](https://fonts.google.com)  
    * Google fonts was used to import the fonts into the html file, and were used on all parts of the site.

* [Font Awesome](https://fontawesome.com)  
    * Font Awesome was used throughout the website to add icons for aesthetic and UX purposes. 

* [jQuery 3.6.0](https://jquery.com/)  
    * jQuery was used as a JavaScript library to help writing less JavaScript code.  


### Packages / Dependencies Installed

* [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)  
    * Django Allauth was used for user authentication, registration, and account management.

* [Django Crispy Form](https://django-crispy-forms.readthedocs.io/en/latest/)   
    * Django Crispy Form was used to control the rendering of the forms. 
 
* [Gunicorn](https://gunicorn.org/)  
    * Gunicorn was used as Python WSGI HTTP Server for UNIX to support the deployment of Django application.  

* [Django Countries](https://pypi.org/project/django-countries/) was used to provide country choices for use with forms and a country field for models.

* [Pillow](https://pypi.org/project/Pillow/) was used to add image processing capabilities.  

* [Summernote](https://summernote.org/) 
    * Summernote has been used as WYSIWYG editor.
  

### Database Management

* [SQLite](https://www.sqlite.com/index.html) was used as a single-file database during development.

* [Elephant Postgres](https://www.elephantsql.com/)   
    * Elephant PostgreSQL database was used in production, as a service based on PostgreSQL provided by Elephant.


### Payment Service

   * [Stripe](https://stripe.com/en-gb-nl) was used to process all online payments transactions.


### Cloud Storage

* [Amazon Web Service S3](https://aws.amazon.com/s3/) was used to store all static and media files in production. 


### Tools and Programs

* [Git](https://git-scm.com)  
    * Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub. 

* [GitPod](https://gitpod.io/)
     * GitPod was used for writing code, committing, and then pushing to GitHub.

* [GitHub](https://github.com)  
   GitHub was used to store the projects code after being pushed from Git. 

* [Heroku](https://www.heroku.com)   
    * Heroku was used to deploy the website.

* [Am I Responsive](ami.responsivedesign.is)  
    * Am I Responsive was used to preview the website across a variety of popular devices.

* [Tiny PNG](https://tinypng.com)    
    * Tiny PNG was used to reduce the file size of the images.

* [Coolors](https://coolors.co)  
    * Coolors was used to create a color scheme for the website.

* [Balsamiq](https://balsamiq.com/)
     * Balsamiq was used to create the wireframes during the design phase of the project

* [Lucid App](https://www.lucidapp.com )
     * The database model has been designed LucidApp/Lucidchart app during the design phase of the project

* [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
    * Chrome DevTools was used during development process for code review and to test responsiveness.

* [W3C Markup Validator](https://validator.w3.org/)
    * W3C Markup Validator was used to validate the HTML code.

* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
    * W3C CSS Validator was used to validate the CSS code.

* [JSHint](https://jshint.com/) 
    * The JSHints JavaScript Code Quality Tool was used to validate the site's JavaScript code.

* [Favicon.cc](https://www.favicon.cc/) 
    * Favicon.cc was used to create the site favicon.


## Testing
[Go to the top](#table-of-contents)

The testing documentation can be found [here](https://github.com/Zilvaro/adenwell-ecommerce/blob/main/TESTING.md).



## Deployment

The project was developed using[GitPod](https://gitpod.io/) workspace. The code was committed to [Git](https://git-scm.com/) and pushed to [GitHub](https://github.com/") using the terminal. The web application is deployed on Heroku as Github Pages is not able to host a Python project. Static and media files are being stored in AWS S3. The repository is hosted on Github.


### How To Use This Project
To use and further develop this project you can either fork or clone the repository.  


#### Fork GitHub Repository
By forking the GitHub repository you can make a copy of the original repository on your GitHub account to view and/or make changes without affecting the original repository, by using the following steps:  

1. Log in to GitHub.  
2. Navigate to the main page of the GitHub Repository that you want to fork.  
3. At the top right of the Repository just below your profile picture, locate the "Fork" button.  
4. You should now have a copy of the original repository in your GitHub account.  
5. Changes made to the forked repository can be merged with the original repository via a pull request.  


#### Clone Github Repository
By cloning a GitHub repository you can create a local copy on your computer of the remote repository. The developer who clones a repository can synchronize their copy of the codebase with any updates made by fellow developers with push or pull request. Cloning is done by using the following steps:  

1. Log in to GitHub.  
2. Navigate to the main page of the GitHub Repository that you want to clone.  
3. Above the list of files, click the dropdown called "Code".  
4. To clone the repository using HTTPS, under "HTTPS", copy the link.  
5. Open Git Bash.  
6. Change the current working directory to the location where you want the cloned directory to be made.  
7. Type git clone, and then paste the URL you copied in Step 4.  
```$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY```
8. Press Enter. Your local clone will be created.   
```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```  
Changes made on the local machine (cloned repository) can be pushed to the upstream repository directly if you have a write access for the repository. Otherwise, the changes made in the cloned repository are first pushed to the forked repository, and then a pull request is created.  
Click [Here](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository-from-github/cloning-a-repository) to retrieve pictures for some of the buttons and more detailed explanations of the above process.  
#### Project Set Up After Forking or Cloning  
1. Install all dependencies by typing in the CLI ```pip3 install -r requirements.txt```  
2. Create a ```.gitignore``` file and ```env.py``` file in the project's root directory. Add the ```env.py``` file to ```.gitignore```. 
3. Inside the env.py file, enter the project's environment variables:   
   ```
   import os
   os.environ.setdefault("SECRET_KEY", <your_secret_key>)
   os.environ.setdefault("DEVELOPMENT", '1')
   os.environ.setdefault("STRIPE_PUBLIC_KEY", <your_key>)
   os.environ.setdefault("STRIPE_SECRET_KEY", <your_key>)
   os.environ.setdefault("STRIPE_WH_SECRET", <your_key>)
   ```   
   You can get the keys from:
   - "SECRET_KEY" can be generated using [Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)   
   - "STRIPE_PUBLIC_KEY" and "STRIPE_SECRET_KEY" can be generated by creating a stripe account. The keys are found in 'Developers' Section, under 'API Keys'.  
   - In the Developer Section, under 'Webhooks', add a new endpoint.  "STRIPE_WH_SECRET". On Endpoint URL, enter:  
   ``` https://<your_host_url>/checkout/wh/ ```   
   Select to listen to all events, and create endpoint, and you can view your "STRIPE_WH_SECRET".   
4. Make migrations to setup the inital database operations.  
   ``` 
   python3 manage.py makemigrations 
   python3 manage.py migrate 
   ```   
5. Load data for the database or create data manually. 
   ```
   python3 manage.py loaddata <app_name>
   ``` 
6. Create a super user.
   ```
   python3 manage.py create superuser
   ```  
The project should now complete to run and can now be used for development. To run the project, type in the CLI terminal: ```python3 manage.py runserver```     
### Deployment to Heroku 
This project is deployed on Heroku for production, with all static and media files stored on AWS S3. These are steps to deploy on Heroku:
1. Navigate to Heroku.com, create a new account or login if you already have an account. On the dashboard page, click "Create New App" button. Give the app a name, the name must be unique with hypens between words. Set the region closest to you, and click "Create App".   
2. On the resources tab, provision a new Heroku Postgres database.  
3. Configure variables on Heroku by navigating to Settings, and click on Reveal Config Vars. You may not have all the values yet. Add the others as you progress through the steps.   
   Variables | Key   
   ---| ---   
   AWS_ACCESS_KEY_ID | your_access_key_id_from_AWS   
   AWS_SECRET_ACCESS_KEY | your_secret_access_key_from_AWS  
   DATABASE_URL | your_database_url   
   EMAIL_HOST_PASS | your_app_password_from_your_email   
   EMAIL_HOST_USER | your_email_address  
   SECRET_KEY | your_secret_key 
   STRIPE_PUBLIC_KEY | your_stripe_public_key  
   STRIPE_SECRET_KEY | your_stripe_secret_key  
   USE_AWS | True 
4. If you haven't install it, install dj_database_url and psycopg2.
   ```
   pip3 install dj_database_url
   pip3 install psycopg2-binary
   ```
   Note: you don't have to do this if you've installed all dependencies in the requirements.txt file.  
5. Set up a new database for the site by going to the project's settings.py and importing dj_database_url. Comment out the database's default configuration, and replace the default database with a call to dj_database_url.parse and pass it the database URL from Heroku (you can get it from your config variables in your app setting tab)
   ```
   DATABASES = {
     'default': dj_database_url.parse('YOUR_DATABASE_URL_FROM_HEROKU')
   }
   ```
6. Run migrations
   ```
   python3 manage.py migrate
   ```  
7. Import data to the database.
    - Make sure your manage.py file is connected to your sqlite3 database.
    - Use this command to backup your current database and load it into a db.json file:
    ```
    ./manage.py dumpdata --exclude auth.permission --exclude contenttypes > db.json
    ```
    - Connect your manage.py file to your postgres database
    - Then use this command to load your data from the db.json file into postgres:
    ``` 
    ./manage.py loaddata db.json
    ``` 
8. Set up a new superuser, fill out the username, email address, and password.
   ```
   python3 manage.py create superuser
   ```  
9. Remove the database config from Heroku and uncomment the original config. Add a conditional statement to define that when the app is running on Heroku. we connect to Postgres, and otherwise, we connect to Sqlite.   
   ```
   if 'DATABASE_URL' in os.environ:
      DATABASES = {
         'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
      }
   else:
      DATABASES = {
         'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
         }
      }
   ```  
10. Install gunicorn which will act as the webserver, and put it on the requirements.txt.   
   ``` 
   pip3 install gunicorn
   pip3 freeze > requirements.txt
   ```
   Note: you don't have to do this if you've installed all dependencies in the requirements.txt file.
11. Create a Procfile, to tell Heroku to create a web dyno, which will run unicorn and serve the Django app.   
   Inside the Procfile:
   ```
   web: gunicorn shoes_and_more.wsgi:application
   ```
12. Login to Heroku through CLI, using ```heroku login```. Once logged in, disable the collect static temporarily, so that Heroku won't try to collect static files when it deploys.
   ```
   heroku config:set DISABLE_COLLECTSTATIC=1 --app shoes-and-more
   ```
   And add the hostname of the Heroku app to allowed hosts in the project's settings.py, and also add localhost so that Gitpod will still work as well:  
   ```
   ALLOWED_HOSTS = ['shoes-and-more.herokuapp.com', 'localhost']
   ```   
13. Add, commit, and push to gitpod and then to Heroku. After pushing to gitpod as usual, initialize git remote first:
   ```
   heroku git:remote -a shoes-and-more
   ``` 
   Then push to Heroku:
   ```
   git push heroku main
   ```
14. Go to the app's dashboard on Heroku and go to Deploy. Connect the app to Github by clicking Github and search for the repository. Click connect. Also enable the automatic deploy by clicking Enable Automatic Deploys, so that every time we push to github, the code will automatically be deployed to Heroku as well.  
15. Go back to settings.py and replace the secret key setting with the call to get it from the environment, and use empty string as a default. 
   ```
   SECRET_KEY = os.environ.get('SECRET_KEY', '')
   ```
   Set debug to be true only if there's a variable called development in the environment.
   ```
   DEBUG = 'DEVELOPMENT' in os.environ
   ```
  
### AWS Bucket Creation   
All static and media files in this project are stored in [Amazon Web Services S3 bucket](https://aws.amazon.com/) which is a cloud based storage service. You can create your own bucket by following these steps:   
1. Go to [Amazon Web Service website](https://aws.amazon.com/) and click on Create An AWS Account, or login if you already have an account.  
2. Login to your new account, go to AWS Management Console and find service S3. Click on Create Bucket.   
   - Give it a name (I recommend naming your bucket to match the Heroku app name), and choose region closest to you.  
   - In Object Ownership section, choose ACLS enabled. and Bucket Owner Preferred.   
   - Uncheck box 'Block All Public Access'.  
   - Check box 'I acknowledge that the current settings might result in this bucket and the objects within becoming public.'  
   - Click on Create Bucket, and your bucket is created.  
3. Click on your newly created bucket, and navigate to the Properties tab. Scroll down to the bottom until you find Static Website Hosting. Click on Edit, then enable. 
   - Hosting type: choose Host a Static Website   
   - Index document: index.html  
   - Error document: error.html
   - Click on Save Changes.  
4. Navigate to the Permissions tab. Scroll down to the bottom until you find Cross-origin resource sharing (CORS). Click on Edit, and paste in this CORS Configuration below, which is going to set up the required access between the Heroku app and this S3 bucket. Click on Save Changes. 
   ```
   [
      {
         "AllowedHeaders": [
            "Authorization"
         ],
         "AllowedMethods": [
            "GET"
         ],
         "AllowedOrigins": [
            "*"
         ],
         "ExposeHeaders": []
      }
   ]
   ```   
   Still on the Permissions tab, find Bucket policy, click on Edit, and then go to Policy Generator. 
   - Select Type of Policy: choose S3 Bucket Policy   
   - Effect: choose Allow   
   - Principal: *   
   - Actions: select GetObject   
   - Fill in the Amazon Resource Name (ARN), from the Bucket ARN back in the Bucket Policy   
   - Click on the Add Statement and then Generate Policy. Copy the policy and paste in the bucket policy editor.  
   - Add a slash star on to the end of the resource key (because we want to allow access to all resources in this bucket). Click Save.
      The resource key should look like this
      ```  
      "Resource": "arn:aws:s3:::YOUR_BUCKET_NAME/*",  
      ```  
   
   Still on Permissions tab, go to Access Control List (ACL) section, click Edit and enable List for Everyone (public access), and accept the warning box.  
5. With the bucket ready, now we need to create a user to access it through another service called IAM which stands for Identity and Access Management. Go back to the service menu and open IAM.   
   a. Create a group for our user to live in.  
      Click User Groups, and then create a new group with a name you want. I gave the group the name: manage-shoes-and-more. Scroll down to the bottom and click on Create Group.     
   b. Create an access policy giving the group access to the S3 bucket that has been created.  
      - Click on Policy, and then Create Policy. Go to the JSON tab, and then select import managed policy, which will let us import one that AWS has pre-built for full access to S3. Search for S3, then import the AmazonS3FullAccess policy.   
      - Because we only want to allow full access to our new bucket and everything within it, paste the bucket ARN (from the bucket policy page in s3) in the JSON editor.
      ```
      "Resource": [
         "arn:aws:s3:::YOUR_BUCKET_NAME",
         "arn:aws:s3:::YOUR_BUCKET_NAME/*"
      ]
      ```  
      Now click on Next:Tags, then click Next:Review. 
      - Give the review policy a name and a description, then click Create Policy. The policy has now been created. 
      
   c. Finally, assign the user to the group so it can use the policy to access all our files.  
      - Go to User Groups, and select the group. Go to the Permissions tab, open the Add Permissions dropdown, and click Attach Policies.  
      - Select the policy and click Add permissions at the bottom.  
      - Create a user to put in the group, by going to the Users page, and clicking Add Users.  
      - Set a user name, give them access type: Programmatic access, and then click Next: Permissions.   
      - Check on the group that has the policy attached. Click Next: Tags, then click Next: Review, and lastly Create User.     
      - Download the csv file and save it. 
   
### Connect Django to AWS Bucket 
Note: If you've forked the repository, all of these steps are already done/ written on the files. Make sure you've installed all dependencies in the requirements.txt file, add all the AWS-related Config Vars to Heroku, and remove the DISABLE_COLLECTSTATIC variable from Heroku.   
Here are the steps I took to connect Django to AWS:  
1. Install two new packages: boto3 and django-storages. Freeze them into requirements.txt.   
   ```
   pip3 install boto3
   pip3 install django-storages 
   pip3 freeze > requirements.txt  
   ```  
2. Add storages to the Installed Apps in settings.py.
   
3. In settings.py, we need to set cache control, set bucket configurations, set static and media files location, and override static and media URLs in production. We'll only want to do this on Heroku, so add an if statement as well.
   ```
   if 'USE_AWS' in os.environ:
      # Cache control
      AWS_S3_OBJECT_PARAMETERS = {
         'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
         'CacheControl': 'max-age=94608000',
      }

      # Bucket Config
      AWS_STORAGE_BUCKET_NAME = 'YOUR_BUCKET_NAME'
      AWS_S3_REGION_NAME = 'YOUR_REGION'
      AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
      AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
      AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

      # Static and media files
      STATICFILES_STORAGE = 'custom_storages.StaticStorage'
      STATICFILES_LOCATION = 'static'
      DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
      MEDIAFILES_LOCATION = 'media' 

      # Override static and media URLs in production
      STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
      MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
   ```
   Set the Config Vars on Heroku. On your app's dashboard on Heroku, go to Settings and click Reveal Config Vars. Set this variables:
   Variables | Value
   --- | ---
   AWS_ACCESS_KEY_ID | your access key id from the csv file that you've downloaded before
   AWS_SECRET_ACCESS_KEY | your secret access key from the csv file that you've downloaded before
   USE_AWS | True    
   Also remove the COLLECTSTATIC variable from the Config Vars.

4. We then want to tell Django that in production we want to use S3 to store our static files whenever someone runs collectstatic, and that we sent any uploaded images to go there as well.  
Create a custom_storages.py file in your project's root directory, and inside it, include the Static and Media Storage locations: 
   ```
   from django.conf import settings
   from storages.backends.s3boto3 import S3Boto3Storage
 

   class StaticStorage(S3Boto3Storage):
      location = settings.STATICFILES_LOCATION


   class MediaStorage(S3Boto3Storage):
      location = settings.MEDIAFILES_LOCATION
   ```  
5. Finally, push these changes on Github.
   ```
   git add .
   git commit -m "Your commit message"
   git push
   ```



## Credits
[Go to the top](#table-of-contents)

### Content

* Website content was written by the developer.
* Example images & some quotes were taken from AdenWellness internal database as well as:
    - [Aden Wellness](https://adenwell.com/)
    - [Aden Wellness Amazon](https://www.amazon.com/stores/Enjoyeveryday/page/41E280B2-E0B0-4A0A-8FAA-65A661BC23FB?ref_=ast_bln)
* The categories images were taken from the following sources:
    - [Aromatic Oils](https://www.edenbotanicals.com/products/bestsellers.html)
    - [Diffusers](https://www.youngliving.com/en_GB/products/c/essential-oils/tools)


### Code

* [Stack Overflow](https://stackoverflow.com/) and [W3Schools](https://www.w3schools.com/) were consulted on a regular basis for inspiration and sometimes to be able to better understand the code being implement.

* The code in Code Institute's video on the Boutique Ado project was used as the main reference point to set up an e-commerce / online store project using HTML, CSS, JS, Python+Django, PostgreSQL database, Stripe, and AWS S3 as storage.


## Known Bugs

**Checkout process for unregistered users**
An issue with the checkout process for unregistered users was discovered due to the save_info check box not being present.
This issue was solved by adding a condition to the stripe_elements.js in order to check if the checkbox was present before trying to assign the saveInfo variable.

**Admin was not able to delete product in CRUD**
Relation in checkoutOrderLineItem did not exist. This issue was solved by migrating the specific application, that was not captured by fullApp migrations.

**Responsiveness in product quantity form on shopping bag**
As stated in the testing section, the appearance of the product quantity form on the shopping bag page can be improved on smaller devices. This issue has not yet been tackled due to time constrains as it does not affect the overall functionality.



## Acknowledgements

* For README.md file/Deployment section, reference of github.com/josswe26 work was considered.

* My tutor, Marcel, for his invaluable support, feedback and guidance through the whole process.

* Code Institute and its amazing Slack community for their support and providing me with the necessary knowledge to complete this project.

* FIFA for organizing WorldCup during project submission period and providing necessary pauses from coding.
  

[Go to the top](#table-of-contents)