## Manual Testing for Bridal Union 

The manual testing undertaken was used against the user stories defined in the [project board](https://github.com/Esteph27/Bridal-Union/projects/1)

Back to [README](/README.md)

***

## Epic 1 - Core website functionality 

### User stories:

### 1.[Site Navigation](https://github.com/Esteph27/Bridal-Union/issues/71):
- As a Site User I easily can browse through the app to get inspiration for my wedding dress by viewing posts/images from different designers

- As a Site User I can find relevant contact information easily

- As a Site User I can easily and intuitively navigate my way through the site to find the relevant information I'm looking for with little amount of clicks

- As a Site User I can use the navigation bar to easily navigate throughout the different pages to view the desired content


A user can browser/scroll through all posts posted by different designers in one location (discover designers page)

![screenshot of discover designer page](/assets/images/discover_designers_page.png)


The footer contains any extra key company information such as contact details. This type of information is normally always requested by the user so having it available throughout the site makes it easy for the user to obtain.

![footer](/assets/images/footer.png)


Throughout the site there are call-to-actions buttons and links to take the user to the desired page without having to rely solely on the navigation bar.

![call to action btn](/assets/images/about-us-btn.png) ![call to action link](/assets/images/cta-link-1.png) ![discover designer button](/assets/images/discover-designer-btn.png)


The nav bar contains all the relevant and important links a user will be looking for which are easy to access at any time throughout the site. The nav bar is also responsive across all screen sizes allowing the user to navigate easily no matter what device they might be using.

### 2. Informative Landing and About page (link)

- As a Site user I can get key information about the company from the landing page so that I can spend less time having to search for information.

- As a Site User I can find out more about the company if I am interested in finding out about who they are.

As mentioned above, the footer contains the websites contact details so that this information is readily available for the user at any time.

The About page provides information about the company including: who they are, how they work, who their designers are in order to satisfy the user’s interests:

![about page](/assets/images/aboutpage.png)

***

## Epic 2 - Admin functionality

### User stories:

### 1. Admin Login (link):
- As an admin site user I can log in so that I can access the site’s backend 

- Using a specified login the site owner can access the admin backend

![admin panel](/assets/images/admin-panel.png)

### 2. Manage Posts CRUD (link):
- As a Site Admin I can create, read, update and delete all posts so that I can manage the content being posted. 

- As a Site Admin I can add an Image description to provide context for the use

- As a Site Admin user I can post images of my work so that I can share and promote my work to a wider audience.

In the site’s back end panel, the admin user can access the ImagePost model where they can view and edit post information, as well as create and delete a post. 

The user gets an overview of all the posts organised by image name, date posted and designers allowing the admin to get a clear overview of all the posts. Using the filter table  on the left, the admin user is also able to filter the posts by ‘published’ or ‘draft’ and ‘date posted’ making it easy for the admin to locate a specific post.

![image post model](/assets/images/imagepostmodel.png)

The Image description field in the ImagePost models allows the user to add a nice description for each post, this information can also be updated to suite admin user’s needs. 

![add image post](/assets/images/add-imagepost-1.png)


### 3. Uploading Images (link):
- As a Site User I don’t have to worry about resizing any images prior to uploading posts so that I don’t have to spend time resizing images myself. 

The ImagePosts model handles image re resizing so the Admin user can upload any sized images and the model will handle this for them, this is done automatically via Cloudinary's CloudianryImage field. 


### 4. Designer Profile CRUD (link):

- As a Site Admin User I can update a Designer's profile information to ensure their profiles are always up-to-date.

- As a Site User, I can add a new designer or delete an existing designer to manage the designers being promoted on the site.

In the site’s back end panel, the admin user can access the Designer model where they can add, edit, view and delete a Designer’s profile information. 

![edit designer](/assets/images/edit-designer.png)

![delete designer](/assets/images/delete-designer.png)


### 5. Create Draft Posts (link):
- As a Site Admin I can create draft posts so that I can finish writing the content later

In the site’s back end, the user can access the ImagePost model where they can edit their post as needed. In the model, the site admin user can select 'draft' when they are creating a post. Any post with the status of 'draft' will not be visible on the front end until the user selects ‘posted'.

![post status](/assets/images/status-draft-posted.png)

### 6. Approve comments (link):
- As a Site Admin User I can approve or disapprove comments made by user so that I can filter out objectionable comments

Via the ImageComments model, the site admin can select manage the status of a comment by clicking on the ‘approve’ check box. If a comment has been approved then it will be visible in the front end, if this check box has been left unticked then the user’s comment will not be visible. 

(Screenshot of approved checkbox)
![checkbox](/assets/images/approve-checkbox.png)

***

## Epic 3 - Booking functionality 

### User stories:

### 1. Manage bookings CRUD 
- As a Site User I can manage my existing bookings as needed so that I can make changes as required online 

A logged in user can view their account where their booking information is displayed. There is a booking count feature displaying the number of bookings the user has, as well as booking cards containing a ‘reschedule’ and ‘delete’ link allowing the user to mange their booking/s as needed. 

![booking card](/assets/images/booking-card-1.png)

The reschedule link takes the user to view their initial booking form which is pre-populated with their previous booking information, the user can then review and edit the necessary information. On submission, the user is redirected  back to their account where their booking card information will show the updated details 

![edit booking form](/assets/images/edit-designer.png)

The delete link automatically deletes the User’s booking and their profile page is then updated. However there is no functionality included to for the user to confirm if they want to delete  their booking, or if it was an accident. 


### 2. Confirm Booking Status
- As a Site Admin I can confirm or decline bookings to help me manage the designer's booking efficiently.

Via the admin panel, the site admin user can view the Booking Model. Here the admin can select the status of a booking by selecting either 'confirm booking' or 'decline booking’. 

![booking status](/assets/images/booking-status.png)


### 3. Manage Booking (site admin user) 
- As a Site Admin I can view booking information so that I can help manage all designer's booking efficiently.

Via the admin panel, the site admin user can view the Booking Model where they can review all bookings made by different users. They are able to review and update the information as well as delete any bookings as needed.

![adming panel booking](/assets/images/admin-panel-booking.png)

*** 

## Epic 4 - User Actions

### User stories

### 1. Interaction - Comment and Like/Unlike
- As a Site User I can interact with as many designers as I like by liking and commenting on their posts so that I can gain a connection with them.

- As a Site User I can comment on a post so that I can share my thoughts on a specified post 

- As a User I can like or unlike a post that I can interact with the content

For logged in users, they are able to leave comments on a designer's post by filling out the comment form displayed in the image post detail page. On submission the user is notified that their comment has been received and will be waiting approval.

![comment form](/assets/images/comment-form.png)

![comment form waiting for approval](/assets/images/comment-waiting-approval.png)

A logged in user can like a post by clicking on the heart icon found on the bottom right corns of the image post. Once clicked the number will update to reflect the like gained by the user, the heart icon will also update to a solid heart. Alternatively, if the user decides to unlike the image then they can click the heart icon again and the like count will decrease by one and the heart icon will revert back to an empty outline. 

![like](/assets/images/heart-solid.png) ![unlike](/assets/images/heart-outline.png)

### 2. View Likes:
- As a Site User / Admin User I can view the number of likes on each post so that I can see which is the most popular or viral

Every post has a likes count feature which shows the number of times a post has been liked

![view likes](/assets/images/view-likes.png)

### 3. View a post’ detail:
- As a Site User I can click on a post so that I can view all comments left by other users so that I can see what others have said and potentially join a conversation 

Every post has a link that shows the number of comments a post has received, the user can click on this link which takes the user to the imagepost detail page. Here, the use can view all comments left by other users. 

![view comment link](/assets/images/view-comment-link.png)

The comments show the name of the user, the date it was posted as well as their comment. The comments are displayed in descending order so that the most recent post is displayed at the top.

![comment example](/assets/images/comment-example.png)

### 4. View a Designer’s Detail:
- As a Site User, I can view a designer's information to get information about a specific designer. I can find out who they are and how they work in order to help me decide if they are the designer to make my wedding dress or not.

The designer profile page includes the following information in order to provide the user the information they need to help them decide wether to book in the specified designer;

    - their posts
    - name
    - location
    - starting price
    - biography

Every designer has their own profile page allowing the user to compare the designers

Each designer profile page also has a ‘make booking’ button encouraging the user to make a booking with that specific designer.

![designer profile](/assets/images/designer-profile.png)

### 5. Receive notification of my actions:
- As a Site User I receive notifications to confirm actions taken on the site. 

Using Django messages, the user is sent alert / info / success messages when the user has logged in/out, created, edited or deleted a booking and posted a comment:

![messages confirm booking](/assets/images/messages1.png) ![messages delete booking](/assets/images/messages2.png) ![messages signed in](/assets/images//messages4.png)

***

## Epic 5 - User Authentication and Registration 

### User stories:

- As a Site User I can easily see if I'm logged in or not so that I can choose to log in or log out depending on what I'm doing.

If a user is logged in the nav bar links will update accordingly to the user’s status; once a user is logged in the ‘create account’ and ‘log in’ links will be visible. When a user is logged in the links will change to ‘log out’ and ‘view account’

![nav bar link](/assets/images/nav-bar-link.png)


When a user logs in or logs out alert messages appear on the screen to notify the user of their actions 

![messages signed in](/assets/images//messages4.png) ![messages siged out](/assets/images/messages3.png)

- As a Site User I can register an account so that I can comment and like on posts, make a booking with a designer and manage my existing bookings:

A user can create an account via the allauth registration forms.

A new user will be assigned a profile page where they can view their existing bookings.

Their profile will display bootstrap cards with the booking information including reschedule and delete links to allow the user to manage their bookings

The number of bookings a user has is also displayed in their profile so it's clear and instant for the user to see how many bookings they have. If the user has 0 bookings then they are encouraged to make a booking by displaying a button to take them to the discover designers page.

![user profile](/assets/images/user-profile-nobooking.png)

![user profile](/assets/images/user-profile-booking.png) 

The comment and like features are available for logged in users. For unregistered users, these features are disabled

![comment sign up](/assets/images/comment-signup.png)

*** 

### JavaScript Testing 

Currently, the only JS included in this release handles the display time for the Django messages. This JS code has been taken from Code Insitute’s ‘I Think Therefore I Blog” videos:

setTimeout() - this handles the amount of time the Django messages appear on the screen, right now the time is set to 2500 (2.5 seconds) after the stated time the message automatically disappears off the screen.

![messages siged out](/assets/images/messages3.png)