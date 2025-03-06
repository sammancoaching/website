---
title: Birthday Greetings
kata_name: birthday_greetings
---

# Birthday Greetings

Since you’re a very friendly person, you would like to send a birthday note to all your friends. However, you have a lot of friends and are feeling a bit lazy. Instead of writing all the notes by hand, you plan to get a computer to do it automatically for you.

Imagine you have a flat file with all your friends' birthdays:

    last_name, first_name, date_of_birth, email
    Doe, John, 1982/10/08, john.doe@example.com
    Ann, Mary, 1975/09/11, mary.ann@example.com

You would like to send them an email on their birthday:

    Subject: Happy birthday!
    
    Happy birthday, dear <first_name>!

Try to implement it so you can easily change :

* the way you retrieve the friends data (for instance, try switching to a SQLite Db)
* the way you send the note - (for instance, imagine you want to send SMS instead of emails)

## Additional Features
Friends born on February, 29th should have their Birthday greeting sent on February, 28th

Send a Birthday Reminder note to your friends about other people's birthdays:

    Subject: Birthday Reminder

    Dear <first_name>,

    Today is <full_name_1>, <full_name_2> and <full_name_3>'s birthdays.
    Don't forget to send them each a message!

## Acknowledgements
This kata is inspired by the work of [Matteo Vaccari](http://matteo.vaccari.name/blog/archives/154) and based on the description on [condingdojo.org](https://codingdojo.org/kata/birthday-greetings/) 
