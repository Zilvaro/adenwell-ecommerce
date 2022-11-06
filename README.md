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
      - [Security](#security)
      - [User Stories - usage](#user-stories---usage)
      - [User Stories - creation](#user-stories---creation)
      - [Things, left "for next Iteration"](#things-left-for-next-iteration)
    - [Stages](#stages)
      - [Ideation, prioritization and planning](#ideation-prioritization-and-planning)
      - [Database Models](#database-models)
    - [Surface](#surface)
      - [Color Scheme](#color-scheme)
      - [Typography](#typography)
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




#### Security

* Site users are able to register an account in order to interact with the content.

* User can't select the author, he is author by default.

* Update/Delete content/post are not accessible via browser if you are not the author.

* Users can update/delete only the posts/content they have created.

* Users can't make a draft of the Post - to keep the system and database cleaner.


#### User Stories - usage

1.	As a **Site User** I can **register an account** so that **I can comment and like**
2.	As a **Site User** I can **view a list of posts** so that **I can select one to read**
3.	As a **Site User** I can **click on a post** so that **I can read the full text**
4.	As a **Site User** I can **leave comments on a post** so that **I can be involved in the conversation**
5.	As a **Site User** I can **like or unlike a post** so that **I can interact with the content**
6.	As a **Site User** I can **click on a content** so that **I can read more about the topic**
7.	As a **User / Admin** I can **view the number of likes on each post** so that **I can see which is the most popular or viral**
8.	As a **User / Admin** I can **view comments on an individual post** so that **I can read the conversation**


#### User Stories - creation

9.	As a **User-admin** I can **create, edit, and delete a) content & b) posts directly on app** so that **I can manage the content area without accessing admin module**
10.	As an **Admin** I can **create draft content** so that **I can publish/ update or delete later** 
11.	As an **Admin** I can **approve or disapprove comments** so that **I can filter out objectionable comments**
12.	As an **Admin** I can **set the content width** so that **I can place different number of items on one row**
13.	As a **Site Admin** I can **assign the post position number**, so **I can place posts according to importance** 
14.	As an **Admin** I can **select the card height** so that **I can create better looking design**
15.	As an **Admin** I can **select the card template** so that **I can create dynamic looking design**
16.	As a **User** I can **create a contact message** so that **I can express my opinion or ask to contact back**

  

#### Things, left "for next Iteration"

* As a **Site Admin** I can **set the publishing and validity date (&time) of the content** so that **I can manage content appearance**.

* As a **Site Admin** I can **set the end date for the post** after which it moves to 'draft' status so that **I can keep the site cleaner**.
  
* Social media sign-up


### Stages
[Go to the top](#table-of-contents)

The Planning & Execution of DigitalZ-Aden project was in 4 distinct phases: 

#### Ideation, prioritization and planning

The current webdesign of AdenWellness [here](https://adenwell.com/) was reviewed and discussed, what would be the 'wishes' for the new design:

* Responsive design

* Header, footer and navigation bar are consistent through all pages.

* Account registration

* Create, edit and delete content from front-end, not only from admin module

* Separate permanent content from the promotional materials and posts

* Ability to interact with users via comments and contact messages

* Ability to create interesting and varied content without using other tools (editors, designer tools)

* No link (at the moment) to external sources : Amazon, e-commerce, etc.


As an outcome - simple sketch of structure was drawn and defined **3 phases** of the software development. 

  **!** - content is created by the user either by upload of image or made using CRUD functionality & Summernote directly from the front-end.
![Digitalz Aden website map](assets/readme_files/digitalz_aden_wire_flow.jpg)
![Digitalz Aden balsamiq - desktop](assets/readme_files/aden-home-balsamiq-desktop.jpg)
![Digitalz Aden balsamiq - mobile](assets/readme_files/aden-home-balsamiq-mobile.png)

* 3 phases of software development were defined as projects with unique User Stories and Tasks
![Digitalz Aden projects](assets/readme_files/projects-list.JPG)


GitHub projects was used as project management tool to track user stories. Using a Kanban board helped to focus on specific tasks and track the project progress.

**Second Phase**

Second phase was to create the full CRUD functionality for 'blog-posts' that in real life would serve as promotional, informational pieces. 

* Create, read, update and delete posts as author
* Leave comment
* Like/Unlike the post

![Digitalz Aden post-project](assets/readme_files/aden-blog-userstories-project.JPG)


**Third Phase**

Third phase was to create the full CRUD functionality for 'content' pieces that in real life would serve as company's representative area. 

* Create, read, update and delete content as author
* Create variety of designs through multiple Summernote fields
* Manage drafts
* Change placement, size and template of the content 

![Digitalz Aden content-project](assets/readme_files/content-core-users-stories.JPG)


**Fourth Phase**

To make sure most relevant testing is performed, Fourth phase was to create and follow a list of testing and deployment tasks. 

* User Stories testing
* Manual testing
* W3C HTML CSS, PEP8, JSHints, Lighthouse
* TestCase automated
* Security testing
* Deployment to Heroku

![Digitalz Aden testing-project](assets/readme_files/testing-deployment-tasks-project.JPG)



#### Database Models

The database models have been designed and managed using [PostgreSQL](https://www.postgresql.org/).

1. **POST Model**

* title = models.CharField()
* slug = models.SlugField()
* author = models.ForeignKey(User)
* posted_by = models.TextField()
* order = models.IntegerField(**defines the place in relation to other posts**)
* featured_image = CloudinaryField()
* excerpt = models.TextField()
* updated_on = models.DateField()
* content = models.TextField()
* created_on = models.DateField()
* status = models.IntegerField()
* likes = models.ManyToManyField()


2. **Comment Model**

* post = models.ForeignKey(Post)
* name = models.CharField()
* email = models.EmailField()
* body = models.TextField()
* created_on = models.DateTimeField()
* approved = models.BooleanField(default=False)


3. **HeroContent Model**

* hero_title = models.CharField()
* slug = models.SlugField()
* author = models.ForeignKey(User)
* hero_featured_image = CloudinaryField()
* image_alt_text = models.CharField(**text automatically placed in html to increase accessibility**)
* hero_header = models.CharField(**summernote field that creates higher impact than title**)
* text_background = models.IntegerField(**shade of grey to increase the header text visibility on light images**)
* hero_excerpt = models.TextField()
* images_on_desktop = models.IntegerField(**number of content cards user wants to see on 1 row on larger screens**)
* image_height = models.IntegerField(**The height of image in px user wants for images on large screens**)
* image_place = models.IntegerField(**defines image vs text relationship: image as background or on the side**)
* image_order = models.IntegerField(**defines the place in relation to other Content cards**)
* updated_on = models.DateTimeField()
* hero_content = models.TextField(**another summernote field**)
* created_on = models.DateTimeField()
* status = models.IntegerField()

!Many of the model's fields have a selection option:

* STATUS = ((0, "Draft"), (1, "Published"))
* IMAGECOUNTDESKTOP = ((12, "Whole Page"), (8, "2/3 of Page"),
                     (6, "Half of Page"), (4, "1/3 of Page"),
                     (3, "1/4 of Page"))
* IMAGEHEIGHT = ((40, "400px"), (32, "320px"), (27, "270px"), (20, "220px"),
               (16, "160px"), (8, "88px"), (5, "50px"))
* IMAGEPLACE = ((1, "Image-as-background"), (2, "Image-on-side"))
* TEXTBACKGROUND = ((1, "No background"), (2, "Put background"))


4. **ContactMessage Model**

* first_name = models.CharField()
* last_name = models.CharField()
* email = models.EmailField()
* contact_message = models.TextField()
* created_on = models.DateTimeField()



### Surface
[Go to the top](#table-of-contents)

#### Color Scheme

![Color scheme image](assets/readme_files/color-pallet.jpg)

The colors used in the website respect the green-golden color-scheme of Aden Wellness, represented in the logo. 

Main colors in the application are achieved through images, so complementary slate-grey (#445261) and baby powder (#FFFFFD) were chosen just to create some contrast, improve readability and maintain consistent look. 


#### Typography

The main font being used in the site is Segoe UI with occasional introduction of Roboto, with sans-serif as a fallback in case Segoe UI doesn't get imported correctly. 

Segoe UI was chosen after refresher-research on fonts that are better for reading, however Segoe UI has proven to be font-of-choice for a few years in app development.



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