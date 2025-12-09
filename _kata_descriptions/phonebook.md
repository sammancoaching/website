---
title: Phonebook
kata_name: phonebook
---

# Phonebook

Given a list of phone numbers, create a Phonebook that lets you look up phone numbers by name. In addition, determine if it is consistent. In a consistent phonebook no number is a prefix of another. For example:

* Bob 91 12 54 26
* Alice 97 625 992
* Emergency 911

In this case, it is not possible to call Bob because the phone exchange would direct your call to the emergency line as soon as you dialled the first three digits of Bob's phone number. So this list would not be consistent.

## Creating a Consistent Phonebook from File
Write a function that will create a consistent Phonebook from a file of name and phone number entries. For each entry in the file, only add it to the phonebook if it does not clash with previously added entries. Return a short report about any entries from the file that were skipped.

There are files of suitable test data available in this repo: [Phone-Numbers-Kata](https://github.com/emilybache/Phone-Numbers-Kata).

## Acknowledgements
This kata is described on [cyber-dojo](https://cyber-dojo.org/) and I have tweaked it slightly.
