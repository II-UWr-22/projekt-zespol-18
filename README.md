## Zespół 18, Projekt: Secure backup
## Wielomiany

Reprezentacje wielomianów:

- "współczynnikowa": wielomian $f$ przechowywany jest jako lista  współczynników przy
kolejnych potęgach zmiennej $x$. Np. $[1, 2, 3]$ odpowiada wielomianowi $f(x) = x^2 + 2 x + 3$;

- "wartościowa": wielomian $f$ przechowywany jest jako zbiór par wartości wielomianu w punktach,
np. $(0, 3), (1, 6), (2, 11)$ oznacza, że: f(0) = 3, f(1) = 6, f(2) = 11$.

1. Zaimplementuj dwie reprezentacje dla wielomianów (współczynnikową i wartościową)
nad $Z_p$, gdzie $p$ jest dużą liczbą pierwszą.

2. Stwórz funkcję $transform(f, [x_1, ..., x_n])$, która dla reprezentacji współczynnikowej zwraca
reprezentację wartościową $f$ w punktach $x_1, ..., x_n$.

3. Stwórz funkcję $eval(f, x)$, która dla reprezentacji współczynnikowej i punktu $x$
oblicza wartość wielomianu w tym punkcie.

4. Stwórz funkcję $lagrange(f, x)$, która dla reprezentacji wartościowej i punktu $x$
oblicza wartość wielomianu w tym punkcie.


## Szyfrowanie 

Parametry wejściowe \[s, k, n\]:
- $s$ - poziom bezpieczeństwa w bitach (np. 128),
- $k$ - liczba udziałów konieczna do zdeszyfrowania wiadomości,
- $n$ - liczba wszystkich udziałów.

1. Generowanie wielomianu (dla $s, k, n$):

- $p$ - liczba pierwsza taka, że $p > 2^s$.
- $f$ - wielomian stopnia $k-1$ ($n \geq k$) (wyjściem jest $n$ par punktów $(x_i, f(x_i))$

2. Generowanie udziałów/sekretu:

- sekretem (kluczem szyfrującym) jest $f(0)$ - wartość wielomianu $f$ w punkcie $0$,
- udziałem jest para $(x_i, f(x_i)$.

# Uruchamianie plików i instrukcja do zinstalowania potrzebnych paczek

## Instalowanie paczek 

Do uruchomienia pliku wielomiany.py potrzebne będzie zainstalowanie biblioteki numpy poniższy link pokazuje jak to zrobic: https://numpy.org/install/

## Uruchamianie plików 

Aby uruchomić plik wielomiany.py należy w terminalu wpisać: python wielomiany.py albo python3 wielomiany.py zależnie od zainstalowanej wersji pythona.

Aby uruchomić plik samir-secret.py należy w terminalu wpisać: python samir-secret.py albo python3 samir-secret.py zależnie od zainstalowanej wersji pythona.

