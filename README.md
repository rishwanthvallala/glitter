
# Glitter - A Django Web Application

Glitter is a Django-based web application that empowers users to share posts, follow other users, and appreciate the content they come across. Experience the magic of Glitter by visiting our hosted [demo](https://rishwanthvallala.pythonanywhere.com/).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Demo](#demo)
- [Contributing](#contributing)

## Installation

To get Glitter up and running on your local machine, follow these simple steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/rishwanthvallala/glitter.git
   ```

2. Install the required dependencies using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. Migrate the database:

   ```bash
   python manage.py migrate
   ```

4. Create a superuser to manage the admin panel:

   ```bash
   python manage.py createsuperuser
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

6. Access the web application at [http://localhost:8000](http://localhost:8000).

## Usage

Getting the most out of Glitter is a breeze:

1. **Register:** Sign up for a new user account or log in using your existing credentials.
2. **Home:** Explore the home page, where you can view and create posts.
3. **Profile:** Visit user profiles, and decide who to follow or unfollow.
4. **Following:** Discover posts from users you're following.
5. **Edit:** Make edits to your posts as needed.
6. **Like:** Show your appreciation for posts with likes, and withdraw them when necessary.
7. **Logout:** Securely log out of your account.

## Configuration

To tailor Glitter to your specific needs, consider the following:

- Make sure to configure your database settings in the project's `settings.py` file.
- Customize the HTML templates, CSS, and JavaScript to align with your project's design.

## Demo

For a hands-on experience with Glitter, visit our hosted version on [PythonAnywhere](https://rishwanthvallala.pythonanywhere.com/). Dive into the live demo [here](https://rishwanthvallala.pythonanywhere.com/).

## Contributing

We welcome contributions! If you're interested in improving Glitter, here's how you can get involved:

1. Fork the repository.
2. Create a new branch dedicated to your feature or bug fix.
3. Implement your changes and rigorously test them.
4. Initiate a pull request to the original repository.

