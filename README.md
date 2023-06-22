# Low budget Facebook

This repository contains a Flask-based thought-sharing application. Users can register, log in, and share their thoughts with others. The application also includes a fun section with random jokes.

## Features

### Home

- The home page displays a list of all the posted thoughts.
- Users can view thoughts posted by other users.

### User

- Users can log in or register for a new account.
- Once logged in, users can post their thoughts.
- Users can view their own thoughts on the user page.

### About Us

- The about us page provides information about the thought-sharing application.
- It includes a message from the creator.

### Fun

- The fun page displays a random joke fetched from an external API.
- Users can click a button to get a new joke.

## Database

The application uses SQLite as the database backend. The database file is `Database.db`.

## Templates

The application uses several HTML templates located in the `templates` directory:

- `base.html` - The base template containing the common layout for all pages.
- `aboutus.html` - The template for the about us page.
- `fun.html` - The template for the fun page displaying random jokes.
- `home.html` - The template for the home page displaying posted thoughts.
- `login.html` - The template for the login page.
- `register.html` - The template for the registration page.
- `user.html` - The template for the user page.

## Contributing

Contributions to this project are welcome. Feel free to open issues and submit pull requests to suggest improvements or fix any bugs.

## License

This project is licensed under the [MIT License](LICENSE).
