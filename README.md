# Chirpy Chooks

This a Django based (fictional!) e-commerce application which is the last of 5 required [Code Institute](https://codeinstitute.net/ie/) portfolio projects.

Chirpy Chooks is the online store of a small business based in the West of Ireland, specialising in live poultry. The store offers a variety of laying hens, broiler chickens and laying ducks. It also offers delivery options within a certain radius (for the sake of simplicity this is based on counties rather than actual distances) and otherwise in-store collections.
On their site, Chirpy Chooks also host a forum about all things poultry. Articles published by the business itself are posted on a regular basis, offering helpful advice about poultry keeping, interesting facts about different breeds or the latest recommendations on feeds, bedding, pest control, etc.

## Table of Contents

- [Technologies Used](#technologies-used)
    - [Work Environments and Hosting](#work-environments-and-hosting)
    - [Python Libraries](#python-libraries)
    - [Django Libraries](#django-libraries)
    - [Payment processing](#payment-processing)
    - [Emails/Newsletter](#emailsnewsletter)

- [Testing](#testing)
    - [Test Guide](#test-guide)
    - [Validator Testing](#validator-testing)
    - [Browser Testing](#browser-testing)
    - [Fixed Bugs](#fixed-bugs)
    - [Unfixed Bugs](#unfixed-bugs)

- [Deployment](#deployment)

- [Development](#development)
    - [Fork](#fork)
    - [Clone](#clone)
    - [Download ZIP](#download-as-zip)

- [Source Credits](#source-credits)
    - [References/Documentation/Tutorials](#referencesdocumentationtutorials)
    - [Media and Styling](#media-and-styling)
    - [Content/Data](#contentdata)


## Technologies Used

### Work Environments and Hosting

- [Figma](https://www.figma.com/) (Wireframes)
- [Lucid](https://lucid.app/) (ERD diagrams)
- [GitHub](https://github.com/) (Version control)
- [GitPod](https://gitpod.io/) (IDE)
- [Heroku](https://heroku.com/) (Site hosting)
- [AWS - Amazon Web servises (S3)](https://aws.amazon.com/) (Hosting static and media files)


### Python Libraries

- [pyscopg2](https://pypi.org/project/psycopg2/) (PostgreSQL Database adapter)
- [Pillow](https://pypi.org/project/Pillow/) (Python Imaging Library)

### Django Libraries

- [django-allauth](https://django-allauth.readthedocs.io/en/latest/) (User authentication)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) (Control rendering behaviour of Django forms)
- [Bootstrap5 template pack for django-crispy-forms](https://pypi.org/project/crispy-bootstrap5/)
- [django-summernote](https://github.com/summernote/django-summernote) (WYSIWYG HTML editor)

### Payment processing

- [Stripe](https://stripe.com/) (Online payment platform)

### Emails/Newsletter

- [Gmail](https://mail.google.com/) (Real email sending)
- [Mailchimp](https://mailchimp.com/) (Automated newsletter subscription service)


## Testing

### Fixed bugs

- **Placeholder for County dropdown list in checkout form**:

    Placeholder "County *" for the dropdown menu in checkout form is not displaying in muted colour.

    **Fix**:

- **"Full Name" field in checkout not auto-filled**:

    In the checkout view, the "Full Name" field remains blank in the payment form when the rest of the form is pre-populated with the user's saved informations.

    **Fix**:

- **Payment form submits without "County" field filled in**:

    In the checkout view, the "County" field of the payment should be required. However, the form submits even without filling in the field.

    **Fix**:

- **Verbose name in "Entry" model not working**:

    In forum app, the model ``Entry`` has an added Meta class to set the verbose name in the admin interface to the correct plural "Entries". The name in the admin panel however shows "Entrys".

    **Fix**:

- **``alt`` attribute on forum post image**:

    The value for the ``alt`` attribute on images attached to forum posts needs to be descriptive to adhere to accessibility standards.

    **Fix**:

    Create ``get_img_alt_value`` helper function in ``Entry`` model of forum app.



## Deployment

This project was deployed using [Heroku](https://heroku.com/), [ElephantSQL](https://www.elephantsql.com/) and [AWS](https://aws.amazon.com/). For a full list libraries refer to [Technologies Used](#technologies-used).

## Development

The following options are available to work with this code or run in a local environment.

### Fork

Any changes made to a forked repository do not affect the original repository.

- Log into GitHub and click on repository to download ([chirpy_chooks](https://github.com/Kathrin-ddggxh/chirpy_chooks))
- Click the **Fork** buttonin the top right-hand corner
- Select a different owner if necessary
- Click **Create Fork**
- The repo is now in your chosen account and can be cloned or changed

### Clone

Changes made to a cloned repository will affect the original one.

- Navigate to the main page of the repostitory (this could be a forked instance)
- Click on the **Code** dropdown menu above the list of files
- Choose a method to copy the URL for the repository: either via **HTTPS**, by using an **SSH key**, or by using **GitHub CLI**
- In your work environment, open Git Bash and change current directory to target location for cloned repository
- Type ``git clone`` followed by the copied URL and press enter **Enter**

### Download as ZIP

- Log into GitHub and click on repository to download ([chirpy_chooks](https://github.com/Kathrin-ddggxh/chirpy_chooks))
- Select **Code** and click "Download Zip" file
- Once download is completed, extract ZIP file and use in your local environment

## Source Credits

### References/Documentation/Tutorials

**General**:

The official [Django Documentation](https://docs.djangoproject.com/en/4.1/) was used throughout creating this project.
The skeleton of this project is based on the [Code Institute](https://codeinstitute.net/ie/) tutorial ["Boutique Ado"](https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/250e2c2b8e43cccb56b4721cd8a8bd4de6686546).

**Basket tools**:

[Django Docs on creating custom template tags](https://docs.djangoproject.com/en/4.1/howto/custom-template-tags/)

**Basket items count display in navbar**:

The syntax for displaying the amount of items currently in the shopping basket was taken from this [FeelFreeToCode tutorial](https://www.youtube.com/watch?v=3xQRJqxdgK4&ab_channel=FeelFreeToCode)

**User alerts (toasts/messages)**:

The live feedback messages to alert user actions were implemented using the [Django message framework](https://docs.djangoproject.com/en/4.1/ref/contrib/messages/) and the respective [message levels](https://docs.djangoproject.com/en/4.1/ref/contrib/messages/).

The alert pop-up frames were rendered using [Bootstrap 5 toasts](https://getbootstrap.com/docs/5.0/components/toasts/).


### Media and Styling

**Images:**

*freerange-hens.jpg*: Me! (Kay Welfare)

*rhode-island-red.jpg:* https://poultrypaddock.co.uk/wp-content/uploads/2017/11/blacktail1-1.jpg

*bluebell.jpg:* https://poultrypaddock.co.uk/wp-content/uploads/2017/11/Bluebell3_1.jpg

*light-sussex.jpg:* https://poultrypaddock.co.uk/wp-content/uploads/2017/11/sussex3.jpg

*blackrock.jpg:* https://poultrypaddock.co.uk/wp-content/uploads/2017/11/blackrock4.jpg

*copper-black-maran.jpg:* https://poultrypaddock.co.uk/wp-content/uploads/2017/11/maran.jpg

*white-leghorn.jpg:* https://poultrypaddock.co.uk/wp-content/uploads/2017/11/Leghorn1_1.jpg

*broiler-chicken.png:* https://thefewellhomestead.com/broiler-chicken-breeds-16-of-the-best-meat-chickens/

*aylesbury-duck.jpg:* https://www.thehappychickencoop.com/aylesbury-duck/

*khaki-campbell.jpg:* https://livestockconservancy.org/wp-content/uploads/2022/08/Campbell-Pair.jpg

*ancona-duck.jpg:* https://www.breedslist.com/wp-content/uploads/2016/10/Ancona-Duck.jpg

*laying-hen.jpg:* https://learnpoultry.com/best-egg-laying-chickens/

*broiler.jpg:* https://vegsoc.org/info-hub/why-go-veggie/animals/broiler-chickens/

*laying-duck.jpg:* https://www.thehappychickencoop.com/raising-ducks-for-eggs/

*noimage.png:* https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/Chicken_cartoon_04.svg/300px-Chicken_cartoon_04.svg.png 

All image used in the Facebook mock-up business page are my own, taken by myself of my own chickens!

**Fonts:**

All fonts were taken from [Google Fonts](https://fonts.google.com/).

*Pacifico*: Designed by Vernon Adams, Jacques Le Bailly, Botjo Nikoltchev, Ani Petrova

*Varela Round*: Designed by Joe Prince

**Icons:**

All icons were taken from [Iconify](https://icon-sets.iconify.design/). Included in this is the animated loading spinner icon of the checkout page.


### Content/Data

All fixtures for the products app were manually compiled with data gathered from various online resources.

**All layer breeds**: https://www.freewaypoultry.ie/product-category/live-poultry/point-of-lay-pullets/

**Broiler (Cornish Cross)**: https://thefewellhomestead.com/broiler-chicken-breeds-16-of-the-best-meat-chickens/

**All duck breeds**: https://petkeen.com/best-egg-laying-duck-breeds/

