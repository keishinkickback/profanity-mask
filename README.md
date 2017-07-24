profanity-mask
================

Python module that masks inappropriate words with *.
This repo is based on https://github.com/jared-mess/profanity-filter.

Usage
-----
```python
cln = Cleaner()
cln.clean("Fuck bullshit apple.")
print cln.original_string   #Fuck bullshit apple.
print cln.cleaned           #F*** b***s**t apple.
```
When instanciating Cleaner, you can set optional parameter _skip_, which determines how may character you will skip between unmasked words.
```python
cln = Cleaner(skip=n)
cln.clean("Fuck bullshit apple.")
print cln.cleaned
# When n = 1, Fuck bullshit apple.
# When n = 2, F*ck b*l*s*it apple.
# When n = 3, F**k b**l**it apple.
# When n = 4, F*** b***s**t apple. (default)
```
If you want to use your own logic, change _crate_mapping_ method. To expand  vocabulary, just add words to bad_word.txt
