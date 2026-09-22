# Mój pierwszy agent — karta obserwacji

- Narzędzie i model: …
Antigravity / Claude Sonnet 4.6

- Moje zadanie (2–3 zdania):
Zrobienie generatora haseł z wyborem długości.

- Pierwsza wiadomość (wklejona co do znaku):

Make me a password generator that is a seperate app (not html).

It will have a space for inputting how many letters u want.
A button with the words "Generate" and a space above it that spits out the password.
Work only this current folder and create as many files as you want.
At the end of your work make a README file that contains the details as to how to run the app.



- Co agent zrobił najpierw: 
Pierwszą rzeczą, którą zrobił, było sprawdzenie zawartości folderu (list_dir), żeby zobaczyć co już jest w projekcie — zanim cokolwiek napisał.
Dopiero potem stworzył plik password_generator.py z kodem aplikacji.

- O co pytał — i co zostało zatwierdzone bez czytania: 
Pytał o zatwierdzenie tylko przy run_command — czyli przy każdym uruchomieniu komendy w terminalu (tworzenie plików, sprawdzanie Pythona itp.).
Ale już nie pytał przy przeglądaniu folderu (list_dir), czytanie plików (view_file) oraz przy przeszukiwaniu sieci (search_web).



- Pierwszy błąd i co agent z nim zrobił:
Pierwszy błąd pojawił się przy tworzeniu pliku password_generator.py.
Agent spróbował zapisać plik, ale się nie udało (błąd ścieżki) → zamienił na run_command z Set-Content i plik się zapisał.


- Stan po 25 minutach: działa / częściowo / nie działa / nie wiem
Działa

- Skąd wiem, że aplikacja działa (co zostało sprawdzone):
Uruchomiłem aplikację i kliknąłem przycisk "Generate". Aplikacja wygenerowała losowe hasło o wybranej przez mnie długości.

- Rzeczy, które agent zrobił, a których nie rozumiem: 
Głównie po prostu samo pisanie kodu w pythonie bo tak to rozumiem mniej więcej czemu resztę działań wykonał

- Jak mi się wydawało, że poszło (jedno zdanie): 
Dobrze.