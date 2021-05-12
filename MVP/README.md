# CountDown v2

## At MVP release:
At launch, the minimum viable product for CountDown v2 should be able to:
* Allow a user to log-in using unique credentials for the app.
* Allow a user to log-in using a third-party API (such as Google, Facebook, etc).
* Allow a user to create a list of media of interest.
* See a countdown to the release date of their media of interest.

## Tech Stack
TBD.

## Structure
### Front-End
TBD
### Back-End
TBD
### Database
Tables listed below will have the proposed bulleted fields. Please note, all names are just current placeholders and are not yet representative of a complete team review.

The image below was drafted using Microsoft Access to provide some a basic level of visualization for the relationships between tables (assuming a relational/SQL DBMS is chosen).
<img src="https://github.com/gh-mrmoore/countdownV2/blob/main/MVP/resources/db_design_proposal_v1.jpg" alt="Visualization of potential database structure." />
#### users
* ID - a unique identifier assigned to each user (automatically numbered as the primary key)
    * Could be replaced by email, but how would that impact performance???
* email - could replace ID. Should be unique to each user.
* password - user-created password that would be stored hashed and salted (if at all)
* token - may be necessary to store depending on any third-party authentication used.
* first_name - store to make greetings more friendly
* last_name - store to make any formal communications more professional
* For consideration:
    * pronouns
    * title (Dr., Ms., Mr., etc.)

#### user_media_list
* ID - unique identifier for each record in the table.
* mediaName - the name of the title/event/etc. (i.e. *The Count of Monte Cristo* or *Iron Man*)
* mediaReleaseDate - the date (and hopefully) time the movie/book/etc will be released.
* mediaGenre - a numerical foreign key to (hopefullly) identify the media's genre
* mediaCategory - a numerical foreign key to (hopefully) identify the media's category (book, movie, etc.)

#### media_categories
* ID - unique identifier for each record in the table.
* media_description - book, movie, music, etc.
* media_genre - the general or main genre category the media would fall under.

#### genre_categories
* ID - unique identifier for each record in the table.
* genre_description - horror, science fiction, biography, non-fiction, etc.
    * For consideration:
    * Would multiple genre tables be needed? One for user interests, another for media?
    * Could genre be gather from any data we get from an API?
    * What if users are entering their own?
    * Should multiples be allowed (historical fiction, apocalyptic sci-fi)? Not really accounting for that at the moment.

#### multiple tables
Multiple tables will be needed to bridge relationships between various tables. Those that were easily anticipated are shown, but some deeper or more complex possible relationships may need to be explored.

#### ORM and DBMS disclaimer
This section is focused purely on the possible database structure as it relates to the project and may not reflect any transformations handled programmatically by any front-end or back-end software or related ORM. Additionally, the notes and diagram provided assume a relational database structure, which has yet to be confirmed.