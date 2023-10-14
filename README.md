
# Your Django Project Name

This is a Django web application that allows users to share posts, follow other users, and like posts. Hosted [here](https://rishwanthvallala.pythonanywhere.com/)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Demo](#demo)
- [Contributing](#contributing)


## Installation

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

1. **Register:** Create a new user account or log in using an existing one.
2. **Home:** View and post messages on the home page.
3. **Profile:** See user profiles and follow/unfollow users.
4. **Following:** View posts from users you are following.
5. **Edit:** Edit your posts.
6. **Like:** Like and unlike posts.
7. **Logout:** Log out of your account.

## Configuration

- Ensure you've set up your database settings in the project's `settings.py` file.
- You may want to customize the HTML templates, CSS, and JavaScript to match your project's design.

## Demo

This project is hosted on [PythonAnywhere](https://rishwanthvallala.pythonanywhere.com/). You can check out the live demo [here](https://rishwanthvallala.pythonanywhere.com/).

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them thoroughly.
4. Create a pull request to the original repository.


