![Aden Wellness Logo](/media/aden-logo-no-background.png)


# Welcome!


The idea is to develop a digital e-commerce solution for a real SME "Aden Wellness" where they can communicate their business ideas to their potential clients, promote products and sell directly online. 

Therefore, the app has 2 distinctive parts:
1.	Top part is the content selection of more permanent materials that are managed by the company (admin, UserAdmins)
2.	The e-commerce part where Aden Wellness can display products, collect orders and process payments  

The working version of the AdenWell e-commerce app can be found [here](https://digitalz-adenwell.herokuapp.com)


![website preview](/assets/readme_files/am-i-responsive-black.JPG)




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
  - [Features - Finished Product](#features---finished-product)
    - [General](#general)
  - [Technologies Used](#technologies-used)
    - [Languages Used](#languages-used)
    - [Libraries and Frameworks](#libraries-and-frameworks)
    - [Packages / Dependencies Installed](#packages--dependencies-installed)
    - [Database Management](#database-management)
    - [Tools and Programs](#tools-and-programs)
  - [Testing](#testing)
    - [Major Errors \& Learnings](#major-errors--learnings)
  - [Deployment](#deployment)
    - [Deploying on Heroku](#deploying-on-heroku)
  - [Finished Product](#finished-product)
  - [Credits](#credits)
    - [Content](#content)
    - [Code](#code)
  - [Acknowledgements](#acknowledgements)


***


## User Experience (UX)

### Strategy

In effect, Adenwell is a business presentation and ecommerce application with full content management functionality from the front-end, and full online-store feature (excluding the delivery follow-up).

#### Project Goals

* Responsive design to make the website accessible on different screen sizes.

* Structure is easy to understand and navigates effortlessly for an easy shopping experience.

* The website desing and colors are appealing to the customers.

* Customers are offered the opportunity to register an account.

* Easy shopping process to create a pleaseant experince for the customer.

* Flexible and clear content fiels alowing to present the company and products


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
  

**Epic 6 - Newsletter Subscription**

* As a site admin, I want shoppers to be able to provide their contact information to be able to reach out to them with information and offers.



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
Display similar products at the a product details view | 3 | 2
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

* Create, edit and delete products

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
  
* Content display & CRUD

* Rate products

* Write product reviews

* Newsletter subscription



**Third Phase**

* Car Payment

* Manage products and content in PosgreSQL

* Additional payment options


#### User Stories

GitHub projects was used as project management tool to track user stories. Using a Kanban board helped to focus on specific tasks and track the project progress. Each UserStory was given a priority label and a milestone note.


![User Stories Progress - GitHub](/media/readme_files/userstories-prioritylabels-milestones.JPG)


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
11.	As a **Site User** I want to be able **I can send a message to admin**, so that I can **Ask question or make inquiry about faulty product**

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


#### Wireframes

[Balsamiq](https://balsamiq.com/) has been used to showcase the appearance of the site and display the placement of the different elements whitin the pages.

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
* ecommerce platform for startups
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
5.	Social network links must include the <strong>rel="noopener"</strong> attribute, which tells search engines not to include these links when it looks at our search engine ranking.


These keywords later will be continualy improved and refined and over time it should utlimately assist in the site ranking higher on Google.





## Features - Finished Product
[Go to the top](#table-of-contents)

### General

* The website has been designed from a mobile first perspective.

* Responsive design across all device sizes.

* Navigation Bar
![Digitalz Aden Navigation Bar image](assets/readme_files/nav-bar.JPG)

    *  Contains the main logo, links and Welcome! with user name.


* Footer
  ![Digitalz Aden Footer image](assets/readme_files/footer-bar.JPG)

    * The footer includes a logo and link to social media channels (hidden while waiting for Aden Wellness approval to use).


Page | Desktop | Mobile |
--- | --- | --- |
| Home | ![Desktop Home Page image](assets/readme_files/home-desktop.jpg) | ![Mobile Home Page image ](assets/readme_files/home-mobile.jpg) |
| Content | ![Desktop Content Page image](assets/readme_files/content-desktop.JPG) | ![Mobile Content Page image](assets/readme_files/content-mobile.jpg) |
| Post | ![Desktop Post Page image](assets/readme_files/post-desktop.jpg) | ![Mobile Post Page image](assets/readme_files/post-mobile.jpg) |
| Contact |![Desktop Contact Page image](assets/readme_files/contact-desktop.JPG) | ![Mobile Contact Page image](assets/readme_files/contact-mobile.JPG) |
| Register |![Desktop Register Page image](assets/readme_files/register-desktop.JPG) | ![Mobile Register Page image](assets/readme_files/register-mobile.JPG) |
| Log-in |![Desktop Log-in Page image](assets/readme_files/login-desktop.JPG) | ![Mobile Log-in Page image](assets/readme_files/login-mobile.JPG) |
| Log-out | ![Desktop Log-out Page image](assets/readme_files/logout-mobile.JPG) | ![Mobile Log-out Page image](assets/readme_files/logout-mobile.JPG) |




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

* [Summernote](https://summernote.org/) 
    * Summernote has been used as WYSIWYG editor.

* [Cloudinary](https://cloudinary.com/)
    * Cloudinary has been used as image management solution

### Database Management
* [Heroku Postgres](https://www.heroku.com/postgres)   
    * Heroku Postgres database was used in production, as a service based on PostgreSQL provided by Heroku.


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

The testing documentation can be found [here](https://github.com/Zilvaro/digitalz-adenblog/blob/main/TESTING.md#digitalz-adenblog-testing).


### Major Errors & Learnings

1. Displaying 2 models on the same template. Initially I was trying to implement by creating 2 apps and the include them into index.html. However the result was the rendering the same data twice, depending which one I chose in views.py. 
After reading different materials I succesfully implemented the Context-View that worked just perfectly:

```
class PostList(generic.TemplateView):
    """View to render the list of POSTs on the home page."""
    template_name = 'index.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['blog_content'] = Post.objects.all()
        context['hero_content'] = HeroContent.objects.all()
        return context
```

2. When Content or Post was created from the frontend, I wanted the slug-field to be created automatically and to use summernote-field for content creation. But the system consistently gave errors, even things looked normal:

![Attribute Error image ](assets/readme_files/attribute-error%20message.jpg)

The solution I learning for other similar instances programming with Classes:

* I added a custom .save() method to the Post model, so that whenever it's saved, it checks to see if there's a slug and if not, generates one using slufigy on the title

```
def save(self, *args, **kwargs):
        if not self.slug:            
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
```


* Even I had the Summernote field set up correctly in forms.py, it just wasn't being accessed in the view - instead relying on manually specifying the fields to render. Adding the full form-class into the views.py did the trick:

```
class AddContentView(SuccessMessageMixin, generic.CreateView):
    """The view that renders the form to add the new Content
       from the front-end."""
    model = HeroContent
    template_name = 'add_content.html'
    
    form_class = AddContentForm
    
    success_message = "You added a new Content! Bravo!"
```




## Deployment

This project was developed using a [GitPod](https://gitpod.io/) workspace. The code was committed to [Git](https://git-scm.com/) and pushed to [GitHub](https://github.com/") using the terminal.

### Deploying on Heroku
To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Create the Heroku App:
    - Select "Create new app" in Heroku.
    - Choose a name for your app and select the location.

2. Attach the Postgres database:
    - In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

3. Prepare the environment and settings.py file:
    * In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
    * In your GitPod workspace, create an env.py file in the main directory. 
    * Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
    * Add the SECRET_KEY value to the Config Vars in Heroku.
    * Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
    * Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
    * In settings.py add the following sections:
        * Cloudinary to the INSTALLED_APPS list
        * STATICFILE_STORAGE
        * STATICFILES_DIRS
        * STATIC_ROOT
        * MEDIA_URL
        * DEFAULT_FILE_STORAGE
        * TEMPLATES_DIR
        * Update DIRS in TEMPLATES with TEMPLATES_DIR
        * Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']

4. Store Static and Media files in Cloudinary and Deploy to Heroku:
    - Create three directories in the main directory; media, storage and templates.
    - Create a file named "Procfile" in the main directory and add the following:
        - web: gunicorn project-name.wsgi
    - Go to Deploy tab on Heroku and connect to the GitHub, then to the required repository.
    Click on Deploy Branch and wait for the build to load. When the build is complete, the app can be opened through Heroku.


## Finished Product
[Go to the top](#table-of-contents)

Page | Desktop | Mobile |
--- | --- | --- |
| Home | ![Desktop Home Page image](assets/readme_files/home-desktop.jpg) | ![Mobile Home Page image ](assets/readme_files/home-mobile.jpg) |
| Content | ![Desktop Content Page image](assets/readme_files/content-desktop.JPG) | ![Mobile Content Page image](assets/readme_files/content-mobile.jpg) |
| Post | ![Desktop Post Page image](assets/readme_files/post-desktop.jpg) | ![Mobile Post Page image](assets/readme_files/post-mobile.jpg) |
| Contact |![Desktop Contact Page image](assets/readme_files/contact-desktop.JPG) | ![Mobile Contact Page image](assets/readme_files/contact-mobile.JPG) |
| Register |![Desktop Register Page image](assets/readme_files/register-desktop.JPG) | ![Mobile Register Page image](assets/readme_files/register-mobile.JPG) |
| Log-in |![Desktop Log-in Page image](assets/readme_files/login-desktop.JPG) | ![Mobile Log-in Page image](assets/readme_files/login-mobile.JPG) |
| Log-out | ![Desktop Log-out Page image](assets/readme_files/logout-mobile.JPG) | ![Mobile Log-out Page image](assets/readme_files/logout-mobile.JPG) |



## Credits
[Go to the top](#table-of-contents)

### Content

* Website content was written by the developer.
* Example images & some quotes were taken from [Aden Wellness](https://adenwell.com/).


### Code

* [Stack Overflow](https://stackoverflow.com/) and [W3Schools](https://www.w3schools.com/) were consulted on a regular basis for inspiration and sometimes to be able to better understand the code being implement.

* Message implementation an dismissal code is taken from [Code Institute](https://codeinstitute.net/)'s django-blog project.


## Acknowledgements

* For README.md file/Deployment section, reference of github.com/josswe26/code-buddy/ was considered.

* My tutor, Marcel, for his invaluable support, feedback and guidance through the whole process.

* Code Institute and its amazing Slack community for their support and providing me with the necessary knowledge to complete this project.

[Go to the top](#table-of-contents)